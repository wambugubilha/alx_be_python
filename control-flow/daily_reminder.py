# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time-bound? (yes/no): ").strip().lower()

# Generate base reminder based on priority
match priority:
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

# Print the customized reminder
print("\n📌 Reminder:")
print(reminder)