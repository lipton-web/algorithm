input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!

    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue # 알파벳이 아닌 경우 다음 인덱스로 넘어감
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    # 빈도수 저장
    max_occurrence = 0
    # 가장 많이 나온 알파벳 인덱스
    max_alphabet_index = 0

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index
    print(max_alphabet_index)
    return chr(max_alphabet_index + ord("a"))

result = find_max_occurred_alphabet(input)
print(result)