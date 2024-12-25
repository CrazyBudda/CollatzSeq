import sys
def collatz(num):
    if num % 2 == 0:
        print (num // 2)
        return num // 2
    else:
        print (3 * num +1)
        return 3 * num +1

while True:
    val=input("Enter a positive integer number > 0 or Q to Quite: ")
    if val=='Q' or val=='q':
        sys.exit()
    else:
        try:
            k=int(val)
            if k<=0:
                raise Exception()
            count=0
            while k!=1:
                k=collatz(k)
                count+=1
            print("Number of iterations: ", count)
        except:
            print("Invalid input!")
            continue