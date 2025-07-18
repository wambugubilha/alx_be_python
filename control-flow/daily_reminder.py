# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Generate base reminder based on priority
match Priority:
    case "high":
        reminder = f"🔴 High priority task: {task}."
    case "medium":
        reminder = f"🟠 Medium priority task: {task}."
    case "low":
        reminder = f"🟢 Low priority task: {task}."
    case _:
        reminder = f"⚪ Task: {task} (Unknown priority)."

# Modify reminder if time-bound
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."


# Print the customized reminder
print("\n📌 Reminder:")
print(reminder)