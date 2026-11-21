"""Exercise 4: Compare failed login attempts with a threshold."""

failed_attempts = int(input("Failed login attempts: "))
threshold = 5

if failed_attempts > threshold:
    print("Threshold exceeded")
else:
    print("Threshold not exceeded")
