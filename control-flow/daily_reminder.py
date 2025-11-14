#!/usr/bin/env python3
"""
Daily Reminder Script
A simplified Python script that reminds users about a single priority task
based on time sensitivity using conditional statements, Match Case, and loops.
"""
def main():
    print("=== Daily Task Reminder ===")
    # Prompt for task details
    task = input("Enter your task: ")
    # Get priority with input validation loop
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ['high', 'medium', 'low']:
            break
        else:
            print("Please enter 'high', 'medium', or 'low'")
    # Get time-bound status with input validation loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ['yes', 'no']:
            break
        else:
            print("Please enter 'yes' or 'no'")
    print("\n" + "="*40)
    print("REMINDER:")
    # Process task based on priority using Match Case
    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"⚠️  '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"⚠️  '{task}' is a high priority task. Focus on completing it soon.")
        case 'medium':
            if time_bound == 'yes':
                print(f"📝 '{task}' is a medium priority task that should be completed today.")
            else:
                print(f"📝 '{task}' is a medium priority task. Schedule time for it this week.")
        case 'low':
            if time_bound == 'yes':
                print(f"📚 '{task}' is a low priority task with a time constraint. Consider completing it when possible.")
            else:
                print(f"📚 Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    print("="*40)

    # Celebration message
    print("\n🎉 Well done on completing this project! Let the world hear about this milestone achieved.")
    print("\n🚀 Click here to tweet! 🚀")
