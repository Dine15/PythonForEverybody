largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done" : break
        n=float(num)
        if(smallest is None):
            smallest = n
        elif smallest>n:
            smallest =n
        
        if largest is None:
            largest = n
        elif largest<n:
            largest=n
    except:
        print("Invalid Number")
print("Maximum is", largest)
print("Minimum is", smallest)

