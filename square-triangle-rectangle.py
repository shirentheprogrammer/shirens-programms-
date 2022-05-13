import time
time.sleep(3)
print("To calculate the value of area of following shapes, click the value corresponding to that shape: ")
a = int(input("1. Triangle \n2. Square \n3. Rectangle \n Number: "))
if a == 1:
    print("For triangle:")
    h = int(input("Please enter the value of the height: "))
    f = int(input("Please enter the value of the Base length: "))
    a1 = (h * f) / 2
    print("The area of the triangle with the height " + str(h) + " units and \nbase length " + str(
    f) + " units is " + str(a1) + " Units^2")
elif a == 2:
    print("For square:")
    e = int(input("Please enter the value of the side: "))
    a2 = e ** 2
    print("The area of the rectangle with the side " + str(e) + " units is " + str(a2) + " Units^2")
elif a == 3:
    print("For rectangle:")
    l = int(input("Please enter the value of length: "))
    b = int(input("Please enter the value of breadth: "))
    a3 = l * b
    print("The area of the rectangle with the length " + str(l) + " units and \nbreadth " + str(b) + " units is " + str(
    a3) + " Units^2")
else:
    print("Invalid input!")

