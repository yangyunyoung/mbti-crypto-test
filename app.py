from flask import Flask, render_template, request, jsonify
import random
from mbti_data import get_crypto_by_mbti

app=Flask(__name__)

# 질문 리스트
questions = [
   {"question": "새로운 사람들과 어울리는 게 편하다.", "category": "EI", "options": ["E", "I"]},
    {"question": "직관보다 사실과 데이터를 신뢰한다.", "category": "SN", "options": ["S", "N"]},
    {"question": "결정을 내릴 때 감정보다 논리를 따른다.", "category": "TF", "options": ["T", "F"]},
    {"question": "계획을 세우고 따르는 것을 선호한다.", "category": "JP", "options": ["J", "P"]},
]

@app.route("/")
def home():
    return render_template("index.html", questions=questions)

@app.route("/result", methods=["POST"])
def result():
    data= request.json
    answers=data.get("answers",{})
    
    #유형 계산
    mbti = ""
    mbti += "E" if answers.get("EI", "I")=="E" else "I"
    mbti += "S" if answers.get("SN", "S") == "S" else "N"
    mbti += "T" if answers.get("TF", "T") == "T" else "F"
    mbti += "J" if answers.get("JP", "J") == "J" else "P"
    
    crypto= get_crypto_by_mbti(mbti)
    
    if mbti== "ISFJ":
        result={"mbti": mbti, "crypto": "예금/적금이 당신과 어울립니다"}
    else:
        #crypto가 딕셔너리라면 symbol을 가져와서 가격조회
        symbol= crypto.get("symbol","").lower()
        price=get_crypto_by_mbti(symbol) #코인겤코에서 가격조회
        result={
            "mbti": mbti,
            "crypto": f"{crypto['name']}({crypto['symbol']})",
            "price":f"${price} USD"
        }
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=False)
    
    