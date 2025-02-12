from flask import render_template
from flask_login import login_required
import requests
from . import main


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/todos')

# 이부분 수정
# 라우팅 함수 작성
# 단 dummyjson에서 requests.get()을 활용하여 데이터를 받아서 매개변수 형태로 html에 넘겨주어야 템플릿을 활용한 for문 사용가능
# 로그인 상태에서만 해당 페이지 접속할 수 있도록 구현 (힌트 flask_login 라이브러리 이용)

