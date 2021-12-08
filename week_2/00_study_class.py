class Person:
	# 클래스는 컨스트럭터 생성해 줘야 함
    def __init__(self, param_name):
        self.name = param_name

    def talk(self):
        print("hi, my name is", self.name)

person_1 = Person("Kim")
person_1.talk()
# print(person_1)
person_2 = Person("Park")
person_2.talk()
# print(person_2.name)




