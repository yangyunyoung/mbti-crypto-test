from flask import Flask, render_template, request, jsonify
import random
from mbti_data import get_crypto_by_mbti
import os

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    data= request.json
    print("Received data:", data)
    answers=data.get("answers",{})
    mbti=data.get("mbti","ISTJ")
    
    #유형 계산
    if answers:
        mbti=mbti[0]
        mbti += "E" if answers.get("EI", "I")=="E" else "I"
        mbti += "S" if answers.get("SN", "S") == "S" else "N"
        mbti += "T" if answers.get("TF", "T") == "T" else "F"
        mbti += "J" if answers.get("JP", "J") == "J" else "P"
        
    print("User mbti:", mbti)
    crypto= get_crypto_by_mbti(mbti)
    
    if mbti== "ISTJ":
        result={"mbti": mbti, "crypto": "예금/적금이 당신과 어울립니다"}
    else:
        #crypto가 딕셔너리라면 symbol을 가져와서 가격조회
        symbol= crypto.get("symbol","").lower()
        price=get_crypto_by_mbti(symbol) #코인겤코에서 가격조회
        result={
            "mbti": mbti,
            "crypto": f"{crypto['name']}({crypto['symbol'].upper()})",
            "price": f"${price} USD" if isinstance(price, (int, float)) else "가격 정보 없음"
        }
    
    return jsonify(result)

if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))  # Render에서는 PORT를 사용
   app.run(host="0.0.0.0", port=port, debug=False)  # 0.0.0.0으로 변경)
    
    