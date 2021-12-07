def find_alphabet_occurrence_array(string):
 		alphabet_occurrence_array = [0] * 26

  # 이 부분을 채워보세요!
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue # 알파벳이 아닌 경우 다음 인덱스로 넘어감
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1
        
    return alphabet_occurrence_array

print(find_alphabet_occurrence_array("hello my name is sparta"))


