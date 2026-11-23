alerts = [
    {"event": "Failed Login", "severity": "high"},
    {"event": "Port Scan", "severity": "medium"},
    {"event": "ARP Spoof", "severity": "high"},
    {"event": "Successful Login", "severity": "low"},
    {"event": "Suspicious Connection", "severity": "high"}
]
high_severity=[]
for i in alerts:
    if(i["severity"]=="high"):
        high_severity.append(i)

high_severity2=[alert for alert in alerts if alert["severity"]=="high"]

high_severity3=[alert["event"] for alert in alerts]

print(high_severity)
print("\n",high_severity2)
print("\n",high_severity3)