# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

# Convert inputs to lowercase for consistent comparison
priority = priority.lower()
time_bound = time_bound.lower()

# Use Match Case statement to react based on priority
match priority:
    case "high":
        # Use if statement to modify reminder based on time-bound condition
        if time_bound == "yes":
            reminder_message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder_message = f"Reminder: '{task}' is a high priority task. Please address it soon."
    
    case "medium":
        # Use if statement to modify reminder based on time-bound condition
        if time_bound == "yes":
            reminder_message = f"Reminder: '{task}' is a medium priority task that requires attention today!"
        else:
            reminder_message = f"Note: '{task}' is a medium priority task. Consider completing it this week."
    
    case "low":
        # Use if statement to modify reminder based on time-bound condition
        if time_bound == "yes":
            reminder_message = f"Note: '{task}' is a low priority task that should be done today."
        else:
            reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    
    case _:
        reminder_message = "Invalid priority level. Please use high, medium, or low."

# Print the customized reminder
print(reminder_message)

# Celebration message
print("\nWell done on completing this project! Let the world hear about this milestone achieved.")
print("\n🚀 Click here to tweet! 🚀")
