# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Initialize reminder message
reminder_message = ""

# MATCH CASE implementation for priority levels
match priority.lower():
    case "high":
        # IF STATEMENT for time-bound condition
        if time_bound.lower() == "yes":
            reminder_message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder_message = f"Reminder: '{task}' is a high priority task. Please address it soon."
    
    case "medium":
        # IF STATEMENT for time-bound condition
        if time_bound.lower() == "yes":
            reminder_message = f"Reminder: '{task}' is a medium priority task that requires attention today!"
        else:
            reminder_message = f"Note: '{task}' is a medium priority task. Consider completing it this week."
    
    case "low":
        # IF STATEMENT for time-bound condition
        if time_bound.lower() == "yes":
            reminder_message = f"Note: '{task}' is a low priority task that should be done today."
        else:
            reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    
    case _:
        reminder_message = "Invalid priority level. Please use high, medium, or low."

# PRINT the customized reminder
print(reminder_message)

print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("\n🚀 Click here to tweet! 🚀")
