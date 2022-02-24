from tkinter import S
from StudentModel import Student

class StudentController():
    def __init__(self):
        self._student = {}

    def studentExists(self, code):
        if code in self._student.keys():
            return True
        else: return False

    def addStudent(self,dni,name,surname,age,city,province,email):
        if self.studentExists(dni):
            return False
        else: 
            s = Student(dni,name,surname,age,city,province,email)
            self._student[dni] = s
            return True

    def deleteStudent(self,code):
        if self.studentExists(code):
            del self._student[code]
            return True
        else: return False

    def modifyStudent(self,code,option,newValue):
        if self.studentExists(code):
            if option == "1":
                 self._student[code].setName(newValue)
                 return True
            if option == "2":
                 self._student[code].setSurname(newValue)
                 return True
            if option == "3":
                 self._student[code].setAge(newValue)
                 return True
            if option == "4":
                 self._student[code].setCity(newValue)
                 return True
            if option == "5":
                 self._student[code].setProvince(newValue)
                 return True
            if option == "6":
                 self._student[code].setEmail(newValue)
                 return True
        else: return False

    def searchStudent(self,code):
        if self.studentExists(code):
            return self._student[code]
        else: return False