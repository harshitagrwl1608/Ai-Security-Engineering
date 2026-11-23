events = [
    {"source_ip": "192.168.1.10", "event": "Failed Login"},
    {"source_ip": "192.168.1.20", "event": "Port Scan"},
    {"source_ip": "192.168.1.10", "event": "Failed Login"},
    {"source_ip": "10.0.0.5", "event": "Successful Login"},
    {"source_ip": "192.168.1.30", "event": "Failed Login"}
]
print("SECURITY EVENT LOG")
print()
c=0
for i in events:
    print(f"{i["source_ip"]} | {i["event"]}")
    y=i["event"].lower().strip()
    if(y=="failed login"):
        c+=1
print()
print()
j=0
while(j<len(events)):
    k=events[j]
    print(f"{k["source_ip"]} | {k["event"]}")
    y=k["event"].lower().strip()
    if(y=="failed login"):
        c+=1
    j+=1

print()
print("Number of Events",len(events))
print("Number of failed Login Events",round(c/2))
