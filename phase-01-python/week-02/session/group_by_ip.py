def main():
    events = [
    {"source_ip": "192.168.1.10", "event": "Failed Login"},
    {"source_ip": "192.168.1.20", "event": "Port Scan"},
    {"source_ip": "192.168.1.10", "event": "Failed Login"},
    {"source_ip": "10.0.0.5", "event": "Successful Login"},
    {"source_ip": "192.168.1.30", "event": "Failed Login"}
]
    final_group=groupby_IP(events)
    for i in final_group:
        print(i,final_group[i])

def groupby_IP(events):
    group_list={}
    for i in events:
        if i["source_ip"] in group_list:
            group_list[i["source_ip"]].append(i["event"])
        else:
            group_list[i["source_ip"]] = []
            group_list[i["source_ip"]].append(i["event"])
    return group_list

if __name__ == "__main__":
    main()