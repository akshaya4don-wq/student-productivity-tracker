def calculate_attendance():
    attended = int(input("Classes attended: "))
    total = int(input("Total classes: "))

    percentage = (attended / total) * 100
    print(f"Attendance: {percentage:.2f}%")
