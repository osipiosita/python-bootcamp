# Global variables

class Student:
   
    def __init__(self, name, student_id, gender, major, yeargroup):
        self.name = name
        self.student_id = student_id
        self.gender = gender
        self.major = major
        self.yeargroup = yeargroup
        
    def change_major(self,new):
        self.major = new
        return self.major
    def __str__(self):
        return f'Name: {self.name}\nID: {self.student_id}\nGender: {self.gender}\nMajor: {self.major}\nYear Group: {self.yeargroup}'
class Course():
    
    def __init__(self, course_code,course_name,course_instructor,intern,) -> None:
        self.course_code = course_code
        self.course_name = course_name
        self.course_instructor = course_instructor
        self.intern = intern
        self.studentsid = []
        self.names = []
        self.genders = []
        self.majors = []
        self.yeargroups = []
    def __str__(self) -> str:
        return f"Course code: {self.course_code}\nCourse Nmae: {self.course_name}\nInstructor: {self.course_instructor}\nIntern: {self.intern}\nStudents: {len(self.studentsid)}"
    
    def enrol_student(self,obj):
       
        if obj.student_id not in self.studentsid:
            self.studentsid.append(obj.student_id)
            self.names.append(obj.name)
            self.genders.append(obj.gender)
            self.majors.append(obj.major)
            self.yeargroups.append(obj.yeargroup)
            print(f'{obj.student_id} successfully added\n')
            return True
        print(f'ID {obj.student_id} is taken\n')
        return False
    def display_enrolled_students(self):
        for i in range(len(self.studentsid)):
            print(f'Name: {self.names[i]}\nID: {self.studentsid[i]}\nGender: {self.genders[i]}\
                  \nMajor: {self.majors[i]}\nYeargroup: {self.yeargroups[i]}\n')
    def check_enrolment_by_ID(self,iden):
        if iden in self.studentsid:
            return True
        return False
    def unenrol_student(self,id):
        for i in range(-(len(self.studentsid)),1):
            if str(self.studentsid[i]) == str(id):
                self.studentsid.pop(i)
                self.names.pop(i)
                self.genders.pop(i)
                self.majors.pop(i)
                self.yeargroups.pop(i)
                return True
            return False
    def display_enrolment_statistics(self):
        count_24, count_25, count_26 = 0,0,0
        cs_count, ps_count, mis_count, med_count = 0,0,0,0
        m_count = 0
        f_count = 0
        for i in range(len(self.genders)):
            if self.genders[i].lower() == 'm':
                m_count += 1
            if self.genders[i].lower() == 'f':
                f_count += 1
            if self.yeargroups[i] == 2024:
                count_24 += 1
            if self.yeargroups[i] == 2025:
                count_25 += 1
            if self.yeargroups[i] == 2026:
                count_26 += 1
            if self.majors[i].lower == 'cs':
                cs_count += 1
            if self.majors[i].lower == 'mis':
                mis_count += 1
            if self.majors[i].lower == 'political science':
                ps_count += 1
            if self.majors[i].lower == 'medicine':
                med_count += 1
        print(f'No of enrolled students: {len(self.studentsid)}\nMales : {m_count}\nFemales: {f_count}\n\
Year 24: {count_24}\nYear 25: {count_25}\nYear 26: {count_26}')
            

        

if __name__ == '__main__':     
    student_1 = Student('Joel',134,'M', 'cs', 2026)
    student_2 = Student('Cindy', 234, 'F', 'MIS', 2026)
    student_3 = Student('Chantelle',334, 'F', 'Political Science', 2024 )
    student_4 = Student('Max', 434, 'M', 'Medicine', 2025)
    course_1 = Course('CS101','python', 'Jan','casey')  
    course_2 = Course('MA101', 'Calculus', 'Mensah', 'Michael')      
    course_1.enrol_student(student_1)
    course_1.enrol_student(student_2)
    course_2.enrol_student(student_3)
    course_2.enrol_student(student_4)
    course_1.display_enrolled_students()
    course_2.display_enrolled_students()
    
    print(course_2.names)
    course_2.display_enrolment_statistics()

    