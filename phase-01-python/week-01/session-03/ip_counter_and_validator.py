from ip_counter import ip_counter
from ip_validator import ip_validator

ip_addresses = [
    "192.168.1.10",
    "192.168.1.10",
    "999.1.1.1",
    "10.0.0.5",
    "192.168.1.20",
    "192.168.1.10",
    "abc.def.1.2",
    "10.0.0.5",
    "192..1.10"
]

true_ip=[]
m=0
wrong_ip=0

for i in ip_addresses:
    if(ip_validator(str(i))):
        true_ip.append(i)
    else:
        wrong_ip+=1

ip_count=ip_counter(true_ip)

print("IP FREQUENCY REPORT")
print()
for i in ip_count:
    print(f"{i} : {ip_count[i]}")
print()
print(f"Invalid IPs Ignored = {wrong_ip}")