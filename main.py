from study import add_study_session, view_study_hours
from tasks import add_task, view_tasks
from attendance import calculate_attendance
from report import generate_report

while True:
    print("\n=== Student Productivity Tracker ===")
    print("1. Add Study Session")
    print("2. Add Task")
    print("3. View Tasks")
    print("4. Attendance Calculator")
    print("5. View Study Hours")
    print("6. Generate Report")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_study_session()
    elif choice == "2":
        add_task()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        calculate_attendance()
    elif choice == "5":
        view_study_hours()
    elif choice == "6":
        generate_report()
    elif choice == "7":
        break
    else:
        print("Invalid choice")
