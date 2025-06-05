num1=float(input("enter first number"))
result=0
def sum(num1,num2):
    result =num1+num2
    return result
def sub(num1,num2):
    result=(num1-num2)
    return result
def mul(num1,num2):
    result= (num1*num2)
    return result
def div(num1,num2):
    result=(num1/num2)
    return result
while True:
    operator = input("enter operator")
    num2 = float(input("enter second number"))
    if operator == "+":
        print(sum(num1, num2))
        num1=sum(num1, num2)
    if operator == "-":
        print (sub(num1, num2))
        num1=sub(num1, num2)
    if operator == "*":
      print (mul(num1, num2))
      num1=mul(num1, num2)
    elif operator == "/":
        print(div(num1, num2))
        num1=div(num1, num2)
    again = input("do you want another operator (y / n )").lower()
    if again != "y":

        print("شكرًا لاستخدام الآلة الحاسبة 🧮")

        break


