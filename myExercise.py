import sys
dict_students={}
f=open(sys.argv[1],"r",encoding="utf-8")
for line in f:
    l1=line.split(":")
    dict_students[l1[0]]=[l1[1].strip("\n")]
student_names=sys.argv[2].split(",")
for student in student_names:
    try:
        print("Name: "+student+", University: "+dict_students[student][0])
    except KeyError:
        print("No record of "+"'"+student+"'"+" was found!")