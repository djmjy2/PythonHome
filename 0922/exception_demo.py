first = int(input("Enter the Fisrt number : "))
second = int(input("Enter the Second number : "))

try : 
    print(f"{first} / {second} = {first/second}")
except Exception as err :
    print(err)
else :
    print("Program is Over")