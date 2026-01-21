#3.1
num1= int(input("Enter a number: "))
if num1%2==0:
    print("The number is even.")
else:
    print("The number is odd.")


#3.2
for i in range(2,11):
    print("1/",i,"=",1/i)


#4.1
my_list=[10,20,30,40,50]
my_tuple=(60,70,80,90,100)
print("List elements:")
for item in my_list:
    print(item)
print("Tuple elements:")
for item in my_tuple:
    print(item)


#4.2(a for loop)
sequence = [10,20,30,40,50]
for i in sequence:
    print(i)

#4.2(b while loop)
num = int(input("Enter a number: "))
while num >=0:
    print(num)
    num -= 1

#5.1
sum=0
max=2000000
for num in range(2, max):
    is_prime=True
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        sum += num
print("The sum of all prime numbers below", max, "is:", sum)

#5.2
a,b=1,2
sum_even=0
while a<=4000000:
    if a%2==0:
        sum_even += a
    a,b=b,a+b
print("The sum of all even Fibonacci numbers below 4 million is:", sum_even)