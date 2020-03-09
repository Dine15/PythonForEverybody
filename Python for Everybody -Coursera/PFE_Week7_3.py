##Finding the smallest value in the list..

x=[73,892,90,-29092.22,8.23,90,23,-928.2920]
smallest = None 
 #Thus if we are unsure about the value to be given to a number give it none.. !!

for i in x:
    if smallest == None:
        smallest = i
    else:
        if smallest>i:
            smallest=i
print("Done")
print("Smallest Number is",smallest)

