# student_output.py

def output_(student) :
    print(f"{student['name']}\t{student['kor']}\t{student['eng']}\t{student['math']}",end='\t')
    print(f"{student['total']}\t{student['avg']:.2f}\t{student['grade']}",end='\t')