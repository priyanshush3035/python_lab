print(1)

a = [1, 2, 3, 3, 1]
print(type(a))
print(a)

b = (10, 30, 30, 20, 20)
print(type(b))
print(b)

c = {100, 200, 300, 200, 100}
print(type(c))
print(c)


student ={"name":"Sanjeev", "rollno": 123,"marks": [{"subject": "math", "score": 90}, {"subject": "science", "score": 80}, {"subject": "english", "score": 85}]}
print(type(student["marks"]))
print(student["marks"][2]["subject"])


# num= int(input("Enter a number: "))
# num2 = input("Enter another number: ")
# num3 = num + int(num2)
# print("The sum is:", num3)


a= int(input("Enter first number: "))
b= float(input("Enter second number: "))
c= a + b
print("The sum is:", c)