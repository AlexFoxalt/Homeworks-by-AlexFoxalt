def second_index(text: str, symbol: str) -> [int, None]:
    return text.find(symbol, text.index(symbol) + 1) if text.count(symbol) > 1 else None


print(second_index("hi mayor", " "))
