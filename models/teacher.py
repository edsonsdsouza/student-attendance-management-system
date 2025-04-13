class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.students = [] ## list to store students

    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added to that class.")

    def mark_attendance(self, student, status):
        ## Ensure the status is either "Present" or "Absent"
        if status not in ["Present", "Absent"]:
            raise ValueError("Attendance must be either 'Present' or 'Absent.")
        student.attendance.append(status)
        print(f"Attendance for {student.name} marked as {status}")

    def view_student(self):
        print(f"Students in {self.name}'s class:")
        for student in self.students:
            print(f"{student.student_id}: {student.name}")