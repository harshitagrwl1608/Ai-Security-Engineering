from ip_validator import ip_validator
alerts=[]

rejected_alerts=0
while True:
    alert={}
    append_if_true=True

    alert["time"]=input("Enter alert time (DONE to finish): ")
    if(alert["time"].lower()=="done"):
        break

    ip=input("Enter source IP: ")
    alert["source_ip"]=ip
    if not(ip_validator(ip)):
        append_if_true=False
        print("Invalid IP, Use IPv4 valid nomination only.\n Alert Rejected.")    
        rejected_alerts+=1  
        continue 

    alert["event_type"]=input("Enter event type: ")

    type=input("Enter severity: ")
    if type not in ["low","medium","high"]:
        append_if_true=False
        print("Invalid severity!\nAccepted values: low, medium, high.\n Alert rejected.")    
        rejected_alerts+=1
        continue
    alert["severity"]=type

    if append_if_true: alerts.append(alert)
    
#print(alerts)
low=0
medium=0
high=0
total_alerts=len(alerts)
for i in alerts:
    if(i["severity"].lower()=="low"):
        low+=1
    elif(i["severity"].lower()=="medium"):
        medium+=1
    else:
        high+=1

print(f"Low: {low}")
print(f"Medium: {medium}")
print(f"High: {high}")
print()
print(f"Total Alerts: {total_alerts}")
print(f"Rejected Alerts: {rejected_alerts}")