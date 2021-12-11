# 회문검사

# 일반적인 방법
input = "abcba"

def is_palindrome(string):
    n = len(string)
    for i in range(n):
        if string[i] != string[n - 1 - i]: #문자열 맨 앞과 뒤가 같은지 검사
            return False
    
    # 마지막까지 False가 반환이 안되었으면
    return True

print(is_palindrome(input))



# 재귀함수 방법
# 문제가 축소되는 경향일 때
input = "abcba"


def is_palindrome(string):

    # 한 글자 이하면 true
    if len(string) <= 1:
        return True

    # 앞뒤가 다르면 false
    if string[0] != string[-1]: 
        return False

    return is_palindrome(string[1:-1])


print(is_palindrome(input))