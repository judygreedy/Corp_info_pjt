from django.shortcuts import render

import warnings
warnings.filterwarnings('ignore')

from .models import *

import matplotlib
matplotlib.use('Agg')  # 또는 'TkAgg'를 시도해보세요.
import matplotlib.pyplot as plt
import io
import base64 # 그래프 인코딩

from matplotlib.animation import FuncAnimation # 그래프 애니매이션
from PIL import Image

from django.http import HttpResponse
from .mbti_data import questions, mbtiTypes # mbti

from django.http import JsonResponse
import json

from django.db import connection

# ===============================================================

# Create your views here.
def index(request):
	print('====debug : client url http://127.0.0.1:8000/html.index, index() call ~~, render - index.html')
	return render(request, 'index.html')

# def test(request):
# 	print('====debug : client url http://127.0.0.1:8000/test, index() call ~~, render - blank.html')
# 	return render(request, 'blank.html')

def charts(request):
	print('====debug : client url http://127.0.0.1:8000/chart, index() call ~~, render - charts.html')
	return render(request, 'charts.html')

# ======DB 연결 확인===========================================================
def test_text(request):
    corp_info = corp_information.objects.all()
    return render(request, 'blank.html',{'corp_info': corp_info})


# =======정적인 그래프==============================================
def graph_view(request):
    # 그래프를 그리는 코드 작성
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    fig = plt.figure(figsize=(6,6))

    plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Line Graph')
    plt.grid(True)
    # plt.savefig('Corp_info_App/static/graph.png')  # 그래프 이미지 저장

    # 그래프를 바이트로 변환
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # 바이트 데이터를 base64로 인코딩
    graph_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render(request, 'blank.html', {'graph_data': graph_data})

# =======================================================================

# ====동적인 그래프(그릴려다 실패함)===========================================
# def update_graph(i):
#     # 그래프를 업데이트하는 함수 (예시)
#     x = [1, 2, 3, 4, 5]
#     y = [i, i*2, i*3, i*4, i*5]
#
#     fig = plt.figure(figsize=(6, 6))
#
#     plt.clf()
#     plt.plot(x, y)
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#     plt.title(f'Animated Graph (Frame {i})')
#     plt.grid(True)
#
# def animated_graph_view(request):
#     # 애니메이션 생성
#     fig = plt.figure()
#     anim = FuncAnimation(fig, update_graph, frames=10, interval=500, repeat=True)
#
#     # 애니메이션을 바이트로 변환하여 base64로 인코딩
#     buffer = io.BytesIO()
#     anim.save(buffer, writer='pillow', fps=2)
#     buffer.seek(0)
#     plt.close()
#
#     # 바이트 데이터를 base64로 인코딩
#     graph_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
#
#     return render(request, 'blank.html', {'graph_data': graph_data})

# =======================================================================

# mbti 예시
def mbti_main(request):
    print('====debug : client url http://127.0.0.1:8000/mbti_home, index() call ~~, render - mbti_home.html')
    return render(request, 'mbti/mbti_home.html')

def show_question(request):
    context = {}
    current_question = request.session.get('current_question', 0)
    if current_question < len(questions):
        question = questions[current_question]
        context['question'] = question['question']
        context['options'] = question['options']
        request.session['current_question'] = current_question
    else:
        request.session['current_question'] = 0
    return render(request, 'mbti/question.html', context)

def handle_answer(request):
    answer = request.POST.get('answer')
    current_question = request.session.get('current_question', 0)
    request.session['answers'] = request.session.get('answers', {})
    request.session['answers'][current_question] = answer
    request.session['current_question'] = current_question + 1
    if current_question + 1 < len(questions):
        return show_question(request)
    else:
        type_counts = {
            'I': 0, 'E': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0
        }
        for i in range(len(questions)):
            answer = request.session['answers'].get(i)
            if answer:
                type_letter = questions[i]['options'][answer]
                for letter in type_letter:
                    type_counts[letter] += 1

        mbti_type = ""
        if type_counts['I'] > type_counts['E']:
            mbti_type += "I"
        else:
            mbti_type += "E"

        if type_counts['S'] > type_counts['N']:
            mbti_type += "S"
        else:
            mbti_type += "N"

        if type_counts['T'] > type_counts['F']:
            mbti_type += "T"
        else:
            mbti_type += "F"

        if type_counts['J'] > type_counts['P']:
            mbti_type += "J"
        else:
            mbti_type += "P"

        request.session['mbti_type'] = mbti_type
        return show_result(request)

def show_result(request):
    mbti_type = request.session.get('mbti_type')
    result_data = mbtiTypes.get(mbti_type)
    context = {'mbti_type': result_data['type'], 'desc': result_data['desc'], 'job': result_data['job']}
    return render(request, 'mbti/result.html', context)

def restart_test(request):
    request.session.clear()
    return show_question(request)

def mbit_test(request):
    print('debug >>>>>> mbti test')
    return render(request, 'mbti_test_index.html')

# ===================================================================================
# chatGPT에 버튼 눌러서 검사하는 페이지 만들어달라고 함
choices = ['예', '아니오']
current_index = 0
selected_choices = []

def index3(request):
    global current_index, selected_choices
    current_index = 0
    selected_choices = []
    context = {
        'title': '심리테스트 시작',
        'choice': choices[current_index],
    }
    return render(request, 'index3.html', context)

def get_next_choice(request):
    global current_index, selected_choices
    if request.method == 'POST':
        selected_choice = request.POST.get('selected_choice')
        if selected_choice in choices:
            selected_choices.append(selected_choice)
            current_index += 1
            if current_index < len(choices):
                response_data = {
                    'next_choice': choices[current_index],
                }
                return JsonResponse(response_data)
            else:
                result = ''.join(selected_choices)
                response_data = {
                    'result': result,
                }
                return JsonResponse(response_data)
    return JsonResponse({'error': 'Invalid request.'})

# ======================================================================================================
# DB 연결 테스트용
# def
