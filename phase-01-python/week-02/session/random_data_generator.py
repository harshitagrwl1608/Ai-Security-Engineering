import random
def random_generator():
    alert=["Failed Login", "Successful Login", "Port Scan",
    "ARP Spoof", "Suspicious Connection"]
    ip=["192.168.1.10", "192.168.1.20",
    "10.0.0.5", "172.16.0.10"]
    severity=["low", "medium", "high"]

    events=[]
    random.seed(42)
    for i in range(1000):
        """event = {
            "event": random.choice(alert),
            "source_ip": random.choice(ip),
            "severity": random.choice(severity)
        }"""

        event={}
        event["event"]=random.choice(alert)
        event["source_ip"]=random.choice(ip)
        event["severity"]=random.choice(severity)
        events.append(event)

    return events

def main():
    events=random_generator()
    print(events)

if __name__ == "__main__":
    main()