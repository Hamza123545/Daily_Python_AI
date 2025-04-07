# # # 0 devide concept by Sir Ali Aftab
# # # try:

# # #     result = 10 / 0

# # # except: ZeroDivisionError

# # # print("Zero can't divide by 0")

# # # print("Important line of code")

# # # result: int = int (input("Enter a Value"))
# # # print(result)


# # def divide(a, b):
# #     try:
# #         result = a / b
# #     except ZeroDivisionError:
# #         print("Error of zero division")
# #     divide("Pizza", 0)
# #     print(result)



class Namaz_Not_offered_Error(Exception):

    pass

try:
    num1 = int(input("Enter num1"))
    num2 = int(input("Enter num2"))
    result = num1/num2
except ValueError:
    print("Only number allowed")
else:
    print(f"Seccessufully chalgaya")
finally:
    print("Program should be run in every condition")



# num1 = int(input("First number"))
# num2 = input("secound number")

# print(num1/ num2)