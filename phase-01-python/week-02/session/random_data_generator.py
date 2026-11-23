import random


def random_generator():
    alert_types = [
        "Failed Login",
        "Successful Login",
        "Port Scan",
        "ARP Spoof",
        "Suspicious Connection",
    ]
    ip_addresses = [
        "192.168.1.10",
        "192.168.1.20",
        "10.0.0.5",
        "172.16.0.10",
    ]
    severity_levels = ["low", "medium", "high"]

    events = []
    random.seed(42)

    for _ in range(1000):
        event = {
            "event": random.choice(alert_types),
            "source_ip": random.choice(ip_addresses),
            "severity": random.choice(severity_levels),
        }
        events.append(event)

    return events


def main():
    events = random_generator()
    print(f"Generated events: {len(events)}")
    print("First five events:")
    for event in events[:5]:
        print(event)


if __name__ == "__main__":
    main()
