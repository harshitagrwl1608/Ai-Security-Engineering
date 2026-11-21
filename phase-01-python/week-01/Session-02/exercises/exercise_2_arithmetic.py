"""Exercise 2: Calculate failed login attempts per minute."""

failed_attempts = int(input("Failed attempts: "))
duration_minutes = float(input("Duration in minutes: "))

if duration_minutes <= 0:
    print("Duration must be greater than zero.")
else:
    average_per_minute = failed_attempts / duration_minutes
    print(f"{average_per_minute:g} failed attempts per minute")
