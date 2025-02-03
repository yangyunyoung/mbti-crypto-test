from flask import Flask, render_template, request, jsonify
import random
from mbti_data import get_crypto_by_mbti

app=Flask(__name__)

# 질문 리스트
questions = [
    {"question": "새로운 기술을 접하면?", "options": ["흥미롭게 탐색", "신중하게 조사"]},
    {"question": "투자할 때 중요하게 생각하는 것은?", "options": ["성장 가능성", "안정성"]},
    {"question": "결정을 내릴 때?", "options": ["논리적으로 분석", "직감적으로 판단"]},
    {"question": "위험이 큰 투자 기회가 생기면?", "options": ["과감히 시도", "안정적인 선택"]},
]

@app.route("/")
def home():
    return render_template("index.html", questions=questions)

@app.route("/result", methods=["POST"])
def result():
    data= request.json
    answers=data.get("answers",[])
    
    