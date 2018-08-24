
def main():
    
    print("The program counts the minimum number of coins to giva a change\n")
    

    while True:
        change=input("How big is the change? :")
        
        try:
            int(change)
            break
        except ValueError:
            try:
                float(change)
                break
            except ValueError:
                print("Please enter a valid number (remember to use . not ,)\n")

              
        
        #if change.isnumeric():
         #   change=float(change)
          #  #if n >0:
           # break
    print("\nThe change is: " + str(change) + " and you will recive:\n")

    counter=0
    r_5=0
    r_2=0
    r_1=0
    r_50=0
    r_20=0
    r_10=0
    r_05=0
    r_02=0
    r_01=0
    change=float(change)
    while change>0:
        if (change >= 5):
            change = change - 5
            counter = counter + 1
            r_5 = r_5 + 1
        elif (change >= 2):
            change = change - 2
            counter = counter + 1
            r_2 = r_2 + 1
        elif (change >= 1):
            change = change - 1
            counter = counter + 1
            r_1 = r_1 + 1
        elif (change >= 0.5):
            change = change - 0.5
            counter = counter + 1
            r_50 = r_50 + 1
        elif (change >= 0.2):
            change = change - 0.2
            counter = counter + 1
            r_20 = r_20 + 1
        elif (change >= 0.1):
            change = change - 0.1
            counter = counter + 1
            r_10 = r_10 + 1
        elif (change >= 0.05):
            change = change - 0.05
            counter = counter + 1
            r_05 = r_05 + 1
        elif (change >= 0.02):
            change = change - 0.02
            counter = counter + 1
            r_02 = r_02 + 1
        elif (change >= 0.01):
            change = change - 0.01
            counter = counter + 1
            r_01 = r_01 + 1
        else:
            change = 0 #to aviod trash
            break
        
    print("Kasa: "+str(change)+ " monety: "+str(counter))
    print("Monety 5zl: "+ str(r_5))
    print("Monety 2zl: "+str(r_2))
    print("Monety 1zl: "+str(r_1))
    print("Monety 0,50zl: "+str(r_50))
    print("Monety 0,20zl: "+str(r_20))
    print("Monety 0,10zl: "+str(r_10))
    print("Monety 0,05zl: "+str(r_05))
    print("Monety 0,02zl: "+str(r_02))
    print("Monety 0,01zl: "+str(r_01))

if __name__ == "__main__":
    main()
