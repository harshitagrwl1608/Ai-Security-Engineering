import time

from random_data_generator import random_generator


def main():
    events = random_generator()

    event_counts = {}
    failed_login_count = 0

    start = time.perf_counter()

    for event in events:
        event_type = event["event"]
        event_counts[event_type] = event_counts.get(event_type, 0) + 1

        if event_type == "Failed Login":
            failed_login_count += 1

    elapsed = time.perf_counter() - start

    print("Total events:", len(events))
    print("Event counts:")
    for event_type, count in sorted(event_counts.items()):
        print(f"{event_type}: {count}")
    print("Failed logins:", failed_login_count)
    print(f"Processing time: {elapsed:.6f} seconds")


if __name__ == "__main__":
    main()
