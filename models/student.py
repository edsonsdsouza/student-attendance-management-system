class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.attendance = [] ## list to store the attendance ("Present" or "Absent")

    def view_attendance(self):
        if not self.attendance:
            print(f"{self.name} has no attendance records yet.")
        else:
            print(f"Attendance for {self.name} ({self.student_id}):")
            for i, status in enumerate(self.attendance, 1):
                print(f"Day {i}: {status}")