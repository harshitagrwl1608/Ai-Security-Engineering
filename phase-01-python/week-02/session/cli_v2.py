from random_data_generator import random_generator
events = random_generator()
def report_generate(events):
    c=0
    d=0
    e=0
    f=0
    unique_ip=[]
    for i in events:
        if(i["severity"]=="high"):
            c=c+1
        elif(i["severity"]=="medium"):
            d=d+1
        elif(i["severity"]=="low"):
            e=e+1
        else: 
            print("Invalid severity")

        if(i["event"]=="Failed Login"):
            f=f+1

        if(i["source_ip"] not in unique_ip):
            unique_ip.append(i["source_ip"])
        """unique_ips = set()
            unique_ips.add(i["source_ip"])"""

    print("========== NETGUARD CLI V2 ==========")
    print()
    print("Total Events :",len(events))
    print("\n Severity Summary :")
    print("High severity:",c)
    print("medium severity:",d)
    print("low severity",e)
    print()
    print("Failed Login attempts:",f)
    print("Number of uniques IPs:",len(unique_ip))
    print("====================================")

def filter_by_severity(events, target_severity):
    list_severity=[]
    for i in events:
        if(i["severity"]==target_severity):
            list_severity.append(i)
    return list_severity

def sort_by_severity(events):
    severity_rank = {
        "high": 1,
        "medium": 2,
        "low": 3
        }
    ranked_alerts = sorted(
        events,
        key=lambda item: (severity_rank[item["severity"]])
        )
    return ranked_alerts

def group_by_ip(events):
    group_list={}
    for i in events:
        if i["source_ip"] in group_list:
            group_list[i["source_ip"]].append(i)
        else:
            group_list[i["source_ip"]] = []
            group_list[i["source_ip"]].append(i)
    return group_list

def main():
    report_generate(events)
    
    target_severity=input("Enter the severity for which event logs you want : ").strip().lower()
    list_severity=filter_by_severity(events,target_severity)
    print(f"\nThe list for {target_severity} is\n: {list_severity}")

    ranked_by_severity=sort_by_severity(events)
    print("\nSeverity Ranked\n",ranked_by_severity)

    group_by_ip_list=group_by_ip(events)
    print("\nGroup by IP list\n",group_by_ip_list)

    

if __name__=="__main__":
    main()

