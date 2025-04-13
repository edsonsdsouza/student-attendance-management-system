from models.student import Student
from models.teacher import Teacher

def main():
    teacher = Teacher("T001", "Mr. Sharma")
    students = {}

    while True:
        print("\nWelcome to the Student Attendance Management System")
        print("1. Teacher")
        print("2. Student")
        print("3. Exit")

        choice = input("Select user type (1/2/3): ")

        if choice == "1":
            print("\n--- Teacher Menu ---")
            print("1. Add Student")
            print("2. Mark Attendance")
            print("3. View Students")
            print("4. Back")

            teacher_choice = input("Enter your choice: ")

            if teacher_choice == "1":
                try:
                    sid = input("Enter Student ID: ")
                    name = input("Enter Student Name: ")
                    if sid in students:
                        print("Student ID already exists.")
                    else:
                        student = Student(sid, name)
                        students[sid] = student
                        teacher.add_student(student)
                except Exception as e:
                    print(f"Error: {e}")

            elif teacher_choice == "2":
                try:
                    sid = input("Enter Student ID to mark attendance: ")
                    if sid in students:
                        status = input("Enter attendance status (Present/Absent): ")
                        teacher.mark_attendance(students[sid], status)
                    else:
                        print("Student not found.")
                except Exception as e:
                    print(f"Error: {e}")

            elif teacher_choice == "3":
                teacher.view_students()

            elif teacher_choice == "4":
                continue

            else:
                print("Invalid choice.")

        elif choice == "2":
            sid = input("Enter your Student ID: ")
            if sid in students:
                students[sid].view_attendance()
            else:
                print("Student not found.")

        elif choice == "3":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
