def main():
    alerts = [
        {
            "time": "10:15",
            "source_ip": "192.168.1.10",
            "event": "Failed Login",
            "severity": "high"
        },
        {
            "time": "10:20",
            "source_ip": "192.168.1.20",
            "event": "Port Scan",
            "severity": "medium"
        },
        {
            "time": "10:15",
            "source_ip": "192.168.1.10",
            "event": "Failed Login",
            "severity": "high"
        },
        {
            "time": "10:30",
            "source_ip": "10.0.0.5",
            "event": "Successful Login",
            "severity": "low"
        },
        {
            "time": "10:10",
            "source_ip": "192.168.1.30",
            "event": "ARP Spoof",
            "severity": "high"
        }
    ]
    ranked_alerts=deduplicate_rank(alerts)
    for item in ranked_alerts:
        print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]}")
    print("\n Total Unique Items: ",len(ranked_alerts))

def deduplicate_rank(alerts):
    alert_set=set()
    
    for i in alerts:
        tuple_alert=(i["time"],i["source_ip"],i["event"],i["severity"])
        alert_set.add(tuple_alert)

    severity_rank = {
    "high": 1,
    "medium": 2,
    "low": 3
    }
    ranked_alerts = sorted(
    alert_set,
    key=lambda item: (severity_rank[item[3]], item[0])
    )
    return ranked_alerts


    """for item in alert_set:
        if(item[3]=="high"):
            items=item
            print(f"{items[0]} | {items[1]} | {items[2]} | {items[3]}")
    for item in alert_set:
        if(item[3]=="medium"):
            items=item
            print(f"{items[0]} | {items[1]} | {items[2]} | {items[3]}")
    for item in alert_set:    
        if(item[3]=="low"):
            items=item
            print(f"{items[0]} | {items[1]} | {items[2]} | {items[3]}")"""
    print("\n Total Unique Items: ",len(alert_set))
    

if __name__ == "__main__":
    main()