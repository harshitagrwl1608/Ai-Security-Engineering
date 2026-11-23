from random_data_generator import random_generator
import time

start = time.perf_counter()
events = random_generator()

event_count = {}
failed_login_count = 0

for event in events:
    event_type = event["event"]

    event_count[event_type] = event_count.get(event_type, 0) + 1

    if event_type == "Failed Login":
        failed_login_count += 1

print("Total events:", len(events))
print("Event counts:", event_count)
print("Failed logins:", failed_login_count)

end = time.perf_counter()

elapsed = end - start

print("Execution time:", elapsed, "seconds")