
class OnlineCourse():
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []

    def enroll_student(self,name):
        self.students.append(name)
        print(f"{name} has been enrolled in the {self.course} course")

    def course_details(self):
        print(f"Course Name: {self.course}")
        print(f"Instructor: {self.instructor}")
        print(f"Enrolled Students: {','.join(self.students)}")
        # join() puts them in a single string

    def complete_course(self,name):
        if name in self.students:
            self.students.remove(name)
            print(f"{name} has completed course.")
        else:
            print(f"{name} is not enrolled")


    def calculate_average_grade(self, grades):
        total = sum(grades)
        average = total / len(grades)
        print(f"Average grade is: {average}")


course_input = input("Enter a course: ").lower()
name = input("Enter a instructor: ").lower()
student = input("Enter a student name: ").lower()

course = OnlineCourse(course_input, name)
grades = [90,85,92,78,80]

course.calculate_average_grade(grades)
course.enroll_student(student)
course.course_details()
course.complete_course(name="David")
