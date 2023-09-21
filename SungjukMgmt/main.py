# main.py
import student_input
import student_output
import student_calc

print("Program is Start...")

student = {}
student_input.input_(student) # Call by Reference
student_calc.calc(student)
student_output.output_(student)

print("Program is Over...")