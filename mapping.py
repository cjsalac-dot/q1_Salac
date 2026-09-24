class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id

    def display_info(self):
        return f"Student({self.name}, ID: {self.tudent_id})"


class Course:
    def __init__(self, course_name: str, course_code: str):
        self.course_name = course_name
        self.course_code = course_code
        self.students = []

    def add_student(self, student: Student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"Added {student.name} to {self.course_name}.")
        else:
            raise TypeError("Only Student objects can be added to this course.")

    def list_students(self):
        print(f"\nEnrolled students in {self.course_name}:")
        for student in self.students:
            print(f"- {student.name}")

if __name__ == "_main_":
    python_course = Course("Python Programming", "CS101")
    student1 = Student("Alice", "S001")
    student2 = Student("Bob", "S002")
    python_course.add_student(student1)
    python_course.add_student(student2)
    python_course.list_students()
