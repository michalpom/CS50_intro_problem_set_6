
def main():
    
    print("The program draws Mario's two-side pyramid\n")
    # n=input("What is the high of the pyramid? : ")
    #print("What is the high of the pyramid?")

    while True:
        n=input("What is the high of the pyramid? :")
        #
        if n.isnumeric():
            n=int(n)
            if n > 0 and n<24:
                break
    print("\nThe high is " + str(n) + " and this is how it looks:\n")

    level=n

    for i in range(n):
        space=" " * (level-1)
        brick= "#" * (i+2)
        print(space + brick + "  " + brick + space)
        level=level-1

    print(brick)

if __name__ == "__main__":
    main()
