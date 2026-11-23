def ip_counter(ip_addresses):
    ip_count={}
    for i in ip_addresses:
        if(ip_count.get(i,0)==0):
            ip_count[i]=1
        else:
            ip_count[i]+=1

        #ip_count[i] = ip_count.get(i, 0) + 1
    return ip_count

def main():
    ip_addresses = [
        "192.168.1.10",
        "192.168.1.20",
        "192.168.1.10",
        "10.0.0.5",
        "192.168.1.20",
        "192.168.1.10",
        "10.0.0.5",
        "192.168.1.30"
    ]
    ip_count=ip_counter(ip_addresses)
    print(ip_count)



if __name__ == "__main__":
    main()