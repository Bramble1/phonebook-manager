import sys

class Student:
    #protected properties
    _name=None
    _age=None
    _current_class=None
    _exams=None
    
    def __init__(self,name,age,current_class,exams):
        self.name=name
        self.age=age
        self.current_class=current_class
        self.exams=exams
    def print_properties(self):
       print("name={}\tage={}\tcurret_class={}\n".format(self.name,self.age,self.current_class))

    def calculate_exam_average(self):
        return ((self.exams[0]+self.exams[1]+self.exams[2])*0.3)
        

#Main

student = Student("tess",18,"maths",(30,41,100))
student.print_properties()


exam_results={"30","24","100"}

result = student.calculate_exam_average() 
print(result)



