x=[345,32,355,899,892090,389.98]
#Find largest number from the above list

largest=x[0]
for i in x:
    print(i)
    if(i>largest):
        largest=i
print("Done")
print("Largest number is:", largest)

