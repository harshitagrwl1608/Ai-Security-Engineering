def main():
    events = [
        {"source_ip": "192.168.1.10", "event": "Failed Login"},
        {"source_ip": "192.168.1.20", "event": "Port Scan"},
        {"source_ip": "192.168.1.10", "event": "Failed Login"},
        {"source_ip": "10.0.0.5", "event": "Successful Login"},
        {"source_ip": "192.168.1.30", "event": "Failed Login"},
    ]

    print("SECURITY EVENT LOG — for loop")
    for_failed_logins = 0
    for event in events:
        print(f"{event['source_ip']} | {event['event']}")
        if event["event"].strip().lower() == "failed login":
            for_failed_logins += 1

    print("\nSECURITY EVENT LOG — while loop")
    while_failed_logins = 0
    index = 0
    while index < len(events):
        event = events[index]
        print(f"{event['source_ip']} | {event['event']}")
        if event["event"].strip().lower() == "failed login":
            while_failed_logins += 1
        index += 1

    print("\nNumber of events:", len(events))
    print("Failed logins (for loop):", for_failed_logins)
    print("Failed logins (while loop):", while_failed_logins)


if __name__ == "__main__":
    main()
