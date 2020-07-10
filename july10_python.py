"""
create a class Student With Following attributes
name
sub1
sub2
sub3

create calculateResult method inside the Student class .
it checks if the student scored >40 in all the individual in the all subject
then return the average of scored
if any student scores<40 in any of the subject then average is zero
average=(sub1+sub2+sub2)/3 


create a another class School with following attributes
name
studentDict

create getStudentResult method inside the School class .
using the calculateResult to calculate the average and who average is >60
then change the value "fail" to "pass" return the studentDict


create findStudentWithHighestMarks method inside the School class .
return the passed hightest avg mark oject
if there is no student is passed in school then return None

Sample input:
3
armaan
40
55
50
shivam
55
48
30
jai
60
47
44
DSP

sample output :
"No Student passed"

sample Input : 
3
armaan
40
55
60
shivam
55
78
90
jai
60
77
94
DPS

sample Output:
shivam
jai
jai
"""
#<---------------Start your Code Here----------------->

class Student:
    def __init__(self,name,sub1,sub2,sub3):
        self.name=name
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3

    def calculateResult(self):
        avg=0
        if(self.sub1>40 and self.sub2>40 and self.sub3>40):
            avg=(self.sub1+self.sub2+self.sub3)/3

        return avg


class School:
    def __init__(self,name,studentDict):
        self.name=name
        self.studentDict=studentDict

    def getStudentResult(self):
        for i in self.studentDict:
            if(i.calculateResult()>60):
                self.studentDict[i]="pass"
        return self.studentDict

    def findStudentWithHighestMarks(self):
        m=-1
        ob=None
        for i in self.studentDict:
            if(i.calculateResult()>m and self.studentDict[i]=="pass"):
                m=i.calculateResult()
                ob=i
        return ob
        



t=int(input())
d=dict()
for i in range(t):
    name=input()
    sub1=int(input())
    sub2=int(input())
    sub3=int(input())
    temp=Student(name,sub1,sub2,sub3)
    d[temp]="fail"

schoolname=input()

school=School(schoolname,d)
res1=school.getStudentResult()
res2=school.findStudentWithHighestMarks()
for i in res1:
    if res1[i]=="pass":
        print(i.name)
if(res2==None):
    print("No Student Passed")
else:
    print(res2.name)