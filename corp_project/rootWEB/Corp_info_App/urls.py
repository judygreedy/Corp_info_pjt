from django.urls import path, include
from Corp_info_App import views

urlpatterns = [
    path('', views.index),

    path('test/', views.graph_view, name='graph'), # 정적인 그래프
    # path('test/', animated_graph_view, name='graph'), # 동적인 그래프

    path('charts/', views.charts),
    #
    path('mbti_home/', views.mbti_main),
    path('handle_answer/', views.handle_answer, name='handle_answer'),
    path('show_result/', views.show_result, name='show_result'),
    path('restart_test/', views.restart_test, name='restart_test'),

    path('mbti_test/', views.mbit_test, name='mbti_test'),

    path('index3', views.index3, name='index3'),
    path('ajax/', views.get_next_choice, name='get_next_choice'),
]

