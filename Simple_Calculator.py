print("Dim's PyCalculator started!")

num_1 = float(input("Write a number: "))

num_2 = float(input("Write a number: "))

select = input('Select the oretion: +,-,*,/: ').lower()

if select == "+":
    print(num_1+num_2)
    print("Exiting...")
    quit()
if select == "-":
    print(num_1-num_2)
    print("Exiting")
    quit()
if select == "*":
    print(num_1*num_2)
    print("Exiting...")
    quit()
if select == "/":
    print(num_1/num_2)
    print("Exiting....")
    quit()
else:
    print("Error...")
    quit()
