
def main():
    
    #print("The program draws Mario's one-side pyramid\n")
    
    ccnumber=input("Enter a credit card number :")
    #"378282246310005"
    #
     
    #print(ccnumber[2])

    temp1=0
    temp2=0

    for i in range(len(ccnumber)-2,-1,-2):
        #print(ccnumber[i])

        n=int(ccnumber[i])*2
        if n>=10:
            b=(n-n%10)/10
            a=n%10
            temp1=temp1+a+b
        else:
            temp1=temp1+n
    for i in range(len(ccnumber)-1,-1,-2):
        #print(ccnumber[i])
        temp2=temp2+int(ccnumber[i])

    #print(temp1+temp2)

    if int((temp1+temp2)%10) == 0:
        print("Valid")

if __name__ == "__main__":
    main()
