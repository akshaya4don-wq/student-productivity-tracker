def add_study_session():
    subject = input("Subject: ")
    hours = float(input("Hours studied: "))

    with open("data/study.txt", "a") as f:
        f.write(f"{subject},{hours}\n")

    print("Study session saved.")

def view_study_hours():
    total = 0
    try:
        with open("data/study.txt", "r") as f:
            for line in f:
                total += float(line.strip().split(",")[1])
        print(f"Total Study Hours: {total}")
    except FileNotFoundError:
        print("No study data found.")
