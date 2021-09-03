import math as m
import decimal
def beginthecalc():
    calc = input("What would you like to do?(x! for factorial, regular for basic calculations, bc for binary converter, sqrt for square roots, x^y for powers, and gl for less/greater than.) ")
    if calc.lower() == "x!":
        n = int(input("What number do you want the factorial of? "))
        print("Prossesing...(5 seconds per 100,000 although that won't fit.")
        print(m.factorial(n))
    elif calc.lower() == "regular":
        print("Type each character(Excluding spaces) in your equation on a seperate line(*for multiplication, / for division.)")
        num1 = input("")
        opr = input("")
        num2 = input("")
        def calculate():
            if opr == "+":
                ans = decimal.Decimal(num1) + decimal.Decimal(num2)
                print(ans)
            elif opr == "-":
                ans = decimal.Decimal(num1) - decimal.Decimal(num2)
                print(ans)
            elif opr == "*":
                ans = decimal.Decimal(num1) * decimal.Decimal(num2)
                print(ans)
            elif opr == "/":
                ans = decimal.Decimal(num1) / decimal.Decimal(num2)
                print(ans)
            else:
                print("Your operation doesn't exist.")
        calculate()
    elif calc.lower() == "bc":
        def decimalToBinary(n):
            int(n)
            print(bin(int(n)).replace("0b",""))
    # Driver code
        def BinaryToDecimal(binary):
            decimal = int(binary, 2)
            print(decimal)
        whichto = input("Would you like to convert binary to decimal(bd), or decimal to binary(db)? ")
        def begin():
            if whichto.lower() == "bd":
                BinaryToDecimal(input("What would you like to convert? "))
            elif whichto.lower() == "db":
                decimalToBinary(input("What number would you like to convert to binary? "))
            else:
                print("Please answer 'bd' for binary to decimal, or 'db' for decimal to binary.")
        begin()
    elif calc.lower() == "sqrt":
        num = decimal.Decimal(input("What number do you want to find the sqaure root of? "))
        sqrt = m.sqrt(num)
        print(sqrt)
    elif calc.lower() == "x^y":
        x = decimal.Decimal(input("What is your base number? "))
        y = decimal.Decimal(input("What power do you want to raise that to? "))
        ans = m.pow(x, y)
        print(ans)
    elif calc.lower() == "gl":
        num1 = decimal.Decimal(input("What is your first number? "))
        num2 = decimal.Decimal(input("What is your second number? "))
        print(max(num1, num2),"is greater than {}".format(min(num1, num2)))
    else:
        print("Your calculation request couldn't be prosesed.")
beginthecalc()