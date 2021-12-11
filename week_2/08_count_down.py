# 재귀함수
# 재귀함수를 무한번 반복하게 만들면 에러 남
# 탈출 조건이 있어야 한다.

def count_down(number):
    if number < 0:
        return
    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)