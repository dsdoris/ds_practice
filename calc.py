## 연산 정의
# 덧셈 연산
def add(n1, n2):
    return n1 + n2

# 뺄셈 연산
def substract(n1, n2):
    return n1 - n2

# 곱셈 연산
def multiply(n1, n2):
    return n1 * n2

# 나눗셈 연산
def devision(n1, n2):
    return n1 / n2

## 계산기 실행
# 숫자 입력
n1 = float(input("숫자 입력:"))
op = str(input("연산 입력(+, -, *, /):"))
n2 = float(input("숫자 입력:"))

# 입력한 연산 실행 후 출력
if op == '+':
    print(n1, "+", n2, "=", add(n1, n2))
elif op == '-':
    print(n1, "-", n2, "=", substract(n1, n2))
elif op == '*':
    print(n1, "*", n2, "=", multiply(n1, n2))
elif op == '/':
    if n2 == 0:                         # 피제수가 0일 때 메시지 출력
        print("0으로 나눌 수 없습니다.")
    else:
        print(n1, "/", n2, "=", devision(n1, n2))
else:
    print("잘못 입력하셨습니다.")