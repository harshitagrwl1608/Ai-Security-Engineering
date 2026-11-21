alert = [
    {
    "time": "10:15",
    "source_ip": "192.168.1.10",
    "event_type": "Failed Login",
    "severity": "high"
    },
{
    "time": "10:25",
    "source_ip": "192.168.1.10",
    "event_type": "Failed Login",
    "severity": "high"
    },
{
    "time": "10:35",
    "source_ip": "192.169.1.10",
    "event_type": "Login",
    "severity": "low"
    },
{
    "time": "10:15",
    "source_ip": "192.160.1.10",
    "event_type": "ARP SPOOF",
    "severity": "medium"
    },
{
    "time": "10:15",
    "source_ip": "192.168.1.20",
    "event_type": "Successful Login",
    "severity": "low"
    },
    {
    "time": "11:00",
    "source_ip": "10.0.0.5",
    "event_type": "Suspicious Connection"
}
]

#print(f"'severity': {alert[5]["severity"]}")
#keyerror

print(f"'severity': {alert[5].get("severity")}")
print(f"'severity': {alert[5].get("severity","unknown")}")


"""
cnt=0

for i in alert:
    
    print(f"'time': {i["time"]}")
    print(f"'source_ip': {i["source_ip"]}")
    print(f"'event_type': {i["event_type"]}")
    print(f"'severity': {i["severity"]}")
    print()
    print("-------------------------------")
    print()


for j in alert:
    if(j["severity"]=="high"):
        cnt+=1
        print(f"'time': {j["time"]}")
        print(f"'source_ip': {j["source_ip"]}")
        print(f"'event_type': {j["event_type"]}")
        print(f"'severity': {j["severity"]}")
        print()
        print("-------------------------------")
        print()
print("Number of alerts",cnt)
print()
cnt=0

for j in alert:
    if(j["source_ip"]=="192.168.1.10"):
        cnt+=1
        print(f"'time': {j["time"]}")
        print(f"'source_ip': {j["source_ip"]}")
        print(f"'event_type': {j["event_type"]}")
        print(f"'severity': {j["severity"]}")
        print()
        print("-------------------------------")
        print()
print("Number of alerts",cnt)
print()
cnt=0

for j in alert:
    if(j["event_type"]=="Failed Login"):
        cnt+=1
        print(f"'time': {j["time"]}")
        print(f"'source_ip': {j["source_ip"]}")
        print(f"'event_type': {j["event_type"]}")
        print(f"'severity': {j["severity"]}")
        print()
        print("-------------------------------")
        print()
print("Number of alerts",cnt)
"""