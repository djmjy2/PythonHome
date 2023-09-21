# student_input.py

def input_(student) :
    name = input("Enter your name :")
    kor = int(input("Enter your Kor score :"))
    eng = int(input("Enter your Eng score :"))
    math = int(input("Enter your Math score :"))
    student["name"] = name
    student["kor"] = kor
    student["eng"] = eng
    student["math"] = math