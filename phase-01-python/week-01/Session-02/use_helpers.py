from helpers import clean_username
from helpers import format_event
from helpers import failed_login_threshold_exceeded

Username=clean_username(input("Enter Username "))

formatted_event=format_event(input("Enter event type "),
             input("enter source IP "),
             clean_username(input("Enter Username ")))

failed_attempt=failed_login_threshold_exceeded(int(input("Enter number of failed attempts ")),
                         int(input("Enter threshold ")))

print(Username)
print(formatted_event)
print(failed_attempt)
