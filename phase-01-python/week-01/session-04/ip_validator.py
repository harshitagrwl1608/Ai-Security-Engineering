def ip_validator(ip):
    c=0
    for i in ip:
        if(i=="."):
            c=c+1
    if(c!=3):
        return False   
    a,b,c,d=ip.rsplit(".",3)
    if not(a.isdigit() and b.isdigit() and c.isdigit() and d.isdigit()):
        return False
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    if(0<=a<=255 and 0<=b<=255 and 0<=c<=255 and 0<=d<=255):
        return True
    else:
        return False

def main():
    ip=input("enter the IP address\n")
    print(ip_validator(ip))


if __name__ == "__main__":
    main()