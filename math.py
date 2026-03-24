a = float(input("請輸入第一個數字: "))
op = input("請輸入運算符 (+ - * /): ")
b = float(input("請輸入第二個數字: "))

if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    if b == 0:
        print("錯誤：不能除以 0")
        exit()
    result = a / b
else:
    print("錯誤：不支援的運算符")
    exit()

print("結果 =", result)