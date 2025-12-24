# 1
a= int(input("Enter first number: "))
b= float(input("Enter second number: "))
c= a + b
print("The sum is:", c)

#2
d=int(input("Enter the number:"))
if d%2==0:
    print("The number is even.")
else:
    print("The number is odd.")

#3
num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))
if num1>num2:
    print("The greater number is:", num1)
else:
    print("The greater number is:", num2)

#4
n = int(input("Enter a number:"))
is_prime=True
if n>1:
    for i in range(2,n):
        if n%i==0:
            is_prime=False
            break
        i+=1
if is_prime:
    print("The number is prime.")
else:
    print("The number is not prime.")

#5

p=int(input("Enter the principal amount: "))
r=float(input("Enter the rate of interest: "))
t=float(input("Enter the time (in years): "))
amount = p*(1 + (r/100))**t
ci= amount-p
print("The total amount is:", amount)
print("The compound interest is:", ci)
print(type(ci))
