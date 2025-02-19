def get_crypto_by_mbti(mbti):
    crypto_mapping = {
        "INTJ": {"name": "Ethereum", "symbol": "ETH"},
        "INTP": {"name": "Chainlink", "symbol": "LINK"},
        "ENTJ": {"name": "Solana", "symbol": "SOL"},
        "ENTP": {"name": "Avalanche", "symbol": "AVAX"},
        "INFJ": {"name": "Cardano", "symbol": "ADA"},
        "INFP": {"name": "Algorand", "symbol": "ALGO"},
        "ENFJ": {"name": "Polkadot", "symbol": "DOT"},
        "ENFP": {"name": "Dogecoin", "symbol": "DOGE"},
        "ISTJ": {"name": "Bitcoin", "symbol": "BTC"},
        "ISFJ": {"name": "USD Coin", "symbol": "USDC"},
        "ESTJ": {"name": "Binance Coin", "symbol": "BNB"},
        "ESFJ": {"name": "XRP", "symbol": "XRP"},
        "ISTP": {"name": "Litecoin", "symbol": "LTC"},
        "ISFP": {"name": "Shiba Inu", "symbol": "SHIB"},
        "ESTP": {"name": "Uniswap", "symbol": "UNI"},
        "ESFP": {"name": "Gala", "symbol": "GALA"},
    }
    return crypto_mapping.get(mbti)  
