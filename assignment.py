def find_missing(lst):
    return [i for x,y in zip(lst,lst[1:])
            for i in range(x + 1,y) if y - x>1]
lst = [1,3,4,5,6,7,8,10]
print(find_missing(lst))

Assignment 1.1 : Calculator using if conditions 

print("Calculator")
print("1.Add")
print("2.Substract")

# input choice
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)

    print("Invalid Choice")
