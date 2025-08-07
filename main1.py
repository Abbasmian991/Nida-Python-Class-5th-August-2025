##### Make Table in Python ======
# def table(n):
#     for i in range(1, 13):
#         print(i)
# table(1)

# def table(n):
#     for i in range(1, 13):
#         result = i * n
#         print(result)
# table(5)

# def table(n):
#     for i in range(1, 13):
#         result = i * n
#         print(f"{n} x {i} ={result}")
# table(10)

# def table(n):
#     for i in range(1, 13):
#         result = i * n
#         print(f"{n} x {i} ={result}")
# num1 = int(input("Please Enter Your Number:"))
# table(num1)

def table(n):
    for i in range(1, 13):
        result = i * n
        print(f"{n} x {i} ={result}")
# num1 = int(input("Please Enter Your Number:"))

def user_input():
    while True:
        num1 = input("Please Enter Your Number: ")
        if num1.isdigit():
            return int(num1)
        else:
            print("Error: Your input is Incorrect. Please enter a number: ")
num1 = user_input()
table(num1)            