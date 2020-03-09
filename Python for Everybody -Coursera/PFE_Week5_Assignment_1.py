hrs = input("Enter Hours:")
r=input("Enter the rate:")
try:
    h = float(hrs)
    rate=float(r)
except:
    print("Enter Numerical value only.")
    quit()  #Not working here but was working in Coursera course. 
print(h,rate)
if(h<=40):
    pay=h*rate
elif(h>40):
    pay=40*rate
    pay=pay+((h-40)*(1.5*rate))
print(pay)

  
