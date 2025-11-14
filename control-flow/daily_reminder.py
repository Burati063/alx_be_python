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
