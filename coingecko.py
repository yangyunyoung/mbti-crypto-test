import requests

def get_crypto_price(symbol):
    url=f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response= requests.get(url)
    data= response.json()
    
    return data.get(symbol, {}).get("usd","가격 정보 없음음")