def generate_report():
    total_hours = 0
    total_tasks = 0

    try:
        with open("data/study.txt", "r") as f:
            for line in f:
                total_hours += float(line.strip().split(",")[1])
    except FileNotFoundError:
        pass

    try:
        with open("data/tasks.txt", "r") as f:
            total_tasks = len(f.readlines())
    except FileNotFoundError:
        pass

    print("\n===== REPORT =====")
    print(f"Study Hours: {total_hours}")
    print(f"Tasks Added: {total_tasks}")

    if total_hours >= 10:
        print("Excellent Progress!")
    else:
        print("Keep Going!")
