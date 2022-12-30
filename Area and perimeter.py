ask = int(input("if you would like the Area and Perimeter of a rectangle press 1, if you would like the Area and Perimeter of a triangle press 2, for both press 3: "))



if ask==1:
    length = float(input("Enter length of the rectangle: "))
    breadth = float(input("Enter breadth of the rectangle: "))
    area = length * breadth
    perimeter = 2 * (length * breadth)
    print("Area of rectangle = ", area)
    print("Perimeter of rectangle = ", perimeter)


elif ask==2:
    print("Enter the Length of First Side of the Triangle: ")
    a = float(input())
    print("Enter the Length of Second Side of the Triangle: ")
    b = float(input())
    print("Enter the Length of Third Side of the Triangle: ")
    c = float(input())

    p = a+b+c
    print("\nPerimeter = ", p)

    print()
    print()
    print()

    d=float(input("what is the length of the triangle: "))
    h=float(input("what is the height of the triangle: "))
 
    area=0.5 * d * h
 
    print("Area of Triangle : ",area)

elif ask==3:
    length = float(input("Enter length of the rectangle: "))
    breadth = float(input("Enter breadth of the rectangle: "))
    area = length * breadth
    perimeter = 2 * (length * breadth)
    print("Area of rectangle = ", area)
    print("Perimeter of rectangle = ", perimeter)
    print()
    print()
    print()
    print("Enter the Length of First Side of the Triangle: ")
    a = float(input())
    print("Enter the Length of Second Side of the Triangle: ")
    b = float(input())
    print("Enter the Length of Third Side of the Triangle: ")
    c = float(input())

    p = a+b+c
    print("\nPerimeter = ", p)

    print()
    print()
    print()

    d=float(input("what is the length of the triangle: "))
    h=float(input("what is the height of the triangle: "))
 
    area=0.5 * d * h
 
    print("Area of Triangle : ",area)





else:
    print("please restart the program an error has occurred.")