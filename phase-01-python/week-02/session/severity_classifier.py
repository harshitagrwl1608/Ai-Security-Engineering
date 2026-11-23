def classify_severity(failed_attempts):
    if(failed_attempts>=6):
        return "high"
    elif(failed_attempts>2):
        return "medium"
    else:
        return "low"
    

def main():
    failed_attempts=int(input("Enter number of failed attempts"))
    print(classify_severity(failed_attempts))
   
if __name__ == "__main__":
    main()