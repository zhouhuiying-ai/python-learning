def calculate_price(price, number):
    total = price * number
    print("total =", total)

    discount = total * 0.9
    print("discount =", discount)

    return discount

result = calculate_price(100, 2)

print("result =", result)