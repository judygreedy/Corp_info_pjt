const questions = [    {        question: "1. 나는 새로운 사람들과의 만남을 즐긴다.",        options: {            A: "그렇다",            B: "아니다"        }    },    {        question: "2. 나는 일을 계획적으로 처리하는 편이다.",        options: {            A: "그렇다",            B: "아니다"        }    },    {        question: "3. 나는 어려운 문제를 해결하는 것을 좋아한다.",        options: {            A: "그렇다",            B: "아니다"        }    },    {        question: "4. 나는 항상 새로운 아이디어를 생각해내는 편이다.",        options: {            A: "그렇다",            B: "아니다"        }    },    {        question: "5. 나는 규칙을 따르는 것보다 독자적인 생각을 추구하는 편이다.",        options: {            A: "그렇다",            B: "아니다"        }    }];

const mbtiTypes = {
    ISTJ: {
        type: "ISTJ",
        desc: "신중하고 규칙적인 성격으로, 집중력이 강하며 책임감이 강합니다.",
        job: "회계사, 경리직, 행정직"
    },
    ISTP: {
        type: "ISTP",
        desc: "조용하고 실용적인 성격으로, 문제 해결능력이 뛰어납니다.",
        job: "기술자, 마케팅, 연구개발"
    },
    ISFJ: {
        type: "ISFJ",
        desc: "사려 깊고 책임감이 강한 성격으로, 집단에서의 조화를 중요시합니다.",
        job: "간호사, 교사, 비서직"
    },
    ISFP: {
        type: "ISFP",
        desc: "침착하고 예술적인 감각을 가진 성격으로, 인간관계에 민감합니다.",
        job: "예술가, 디자이너, 작가"
    },
    INTJ: {
        type: "INTJ",
        desc: "독창적이고 논리적인 사고를 가진 성격으로, 목적 달성을 위해 계획적으로 움직입니다.",
        job: "개발자, CEO, 경영자"
    },
    INTP: {
        type: "INTP",
        desc: "창의적이고 비판적인 사고를 가진 성격으로, 독립적인 문제 해결 능력을 가지고 있습니다.",
        job: "연구원, 프로그래머, 작가"
    },
    INFJ: {
        type: "INFJ",
        desc: "이상적인 세상을 추구하고, 동정심이 많은 성격으로, 예술적인 재능을 가지고 있습니다.",
        job: "작가, 연예인, 심리학자"
    },
    INFP: {
        type: "INFP",
        desc: "이상적인 세상을 추구하고, 자신의 가치관에 따라 행동하는 성격으로, 예술적 재능을 가지고 있습니다.",
        job: "작가, 의사, 교육자"
    },
    ESTJ: {
        type: "ESTJ",
        desc: "현실적이고 논리적인 사고를 가진 성격으로, 높은 리더십을 가지고 있습니다.",
        job: "경영자, 군인, 변호사"
    },
    ESTP: {
        type: "ESTP",
        desc: "활동적이고 개방적인 성격으로, 즉흥적으로 문제를 해결합니다.",
        job: "스포츠 선수, 경영자, 컨설턴트"
    },
    ESFJ: {
        type: "ESFJ",
        desc: "친절하고 협조적인 성격으로, 사람들과 함께 일하는 것을 좋아합니다.",
        job: "의료직, 언론인, 간호사"
    },
    ESFP: {
        type: "ESFP",
        desc: "매력적이고 활발한 성격으로, 주변을 즐겁게 만드는 역할을 합니다.",
        job: "연예인, 세일즈맨, 디자이너"
    },
    ENTJ: {
        type: "ENTJ",
        desc: "논리적이고 지도력이 있는 성격으로, 목적을 달성하기 위해 전략을 세웁니다.",
        job: "CEO, 변호사, 정치인"
    },
    ENTP: {
        type: "ENTP",
        desc: "창의적이고 독창적인 사고를 가진 성격으로, 도전적인 상황에서 빛을 발합니다.",
        job: "기업인, 연예인, 광고 디자이너"
    },
    ENFJ: {
        type: "ENFJ",
        desc: "타인의 성장을 도모하고, 사람들의 신뢰를 받는 성격으로, 친절하고 사교적입니다.",
        job: "강사, 컨설턴트, 종교인"
    },
    ENFP: {
        type: "ENFP",
        desc: "열정적이고 독창적인 사고를 가진 성격으로, 새로운 것에 도전하는 것을 좋아합니다.",
        job: "작가, 예술가, 상담사"
    }
};

let currentQuestion = 0;
let answers = {};

const showQuestion = () => {
    const questionEl = document.querySelector("#question");
    questionEl.innerHTML = `
        <p>${questions[currentQuestion].question}</p>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="question${currentQuestion + 1}" value="A" id="question${currentQuestion + 1}A">
            <label class="form-check-label" for="question${currentQuestion + 1}A">
                ${questions[currentQuestion].options.A}
            </label>
        </div>
        <div class="form-check">
            <input class="form-check-input" type="radio" name="question${currentQuestion + 1}" value="B" id="question${currentQuestion + 1}B">
            <label class="form-check-label" for="question${currentQuestion + 1}B">
                ${questions[currentQuestion].options.B}
            </label>
        </div>
        <button id="next-btn" class="btn btn-primary mt-3">다음</button>
    `;
};

const showResult = (mbtiType) => {
    const resultEl = document.querySelector("#result");
    resultEl.classList.remove("d-none");
    const mbtiTypeEl = document.querySelector("#mbti-type");
    const recommendedJobEl = document.querySelector("#recommended-job");
    mbtiTypeEl.innerText = mbtiType.type;
    recommendedJobEl.innerText = mbtiType.job;
};

const restartTest = () => {
    currentQuestion = 0;
    answers = {};
    const resultEl = document.querySelector("#result");
    resultEl.classList.add("d-none");
    showQuestion();
};

$(document).ready(() => {
    showQuestion();

    $("#question").on("click", "#next-btn", () => {
        const answer = document.querySelector(`input[name="question${currentQuestion + 1}"]:checked`);
        if (answer) {
            answers[currentQuestion] = answer.value;
            currentQuestion++;
            if (currentQuestion < questions.length) {
                showQuestion();
            } else {
                let typeCounts = {
                    I: 0,
                    E: 0,
                    S: 0,
                    N: 0,
                    T: 0,
                    F: 0,
                    J: 0,
                    P: 0
                };
                for (let i = 0; i < questions.length; i++) {
                    const answer = answers[i];
                    const type = questions[i].options[answer];
                    type.split("").forEach((letter) => {
                        typeCounts[letter]++;
                    });
                }
                let mbtiType = "";
                    if (typeCounts.I > typeCounts.E) mbtiType += "I";
                    else mbtiType += "E";
                    if (typeCounts.S > typeCounts.N) mbtiType += "S";
                    else mbtiType += "N";
                    if (typeCounts.T > typeCounts.F) mbtiType += "T";
                    else mbtiType += "F";
                    if (typeCounts.J > typeCounts.P) mbtiType += "J";
                    else mbtiType += "P";
                    showResult(mbtiTypes[mbtiType]);
                }
            }
        });

        $("#result").on("click", "#restart-btn", () => {
            restartTest();
        });
    });

