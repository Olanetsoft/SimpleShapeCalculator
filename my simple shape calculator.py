print("")
print("")
import time
print(time.asctime())
print("")
#A SIMPLE AREA CALCULATOR.... JUST CHOOSE YOUR SHAPE
print("WELCOME TO A SIMPLE AREA CALCULATOR BUILT BY OLANETSOFT")

def the_main():
    anyShape=input("PLEASE SELECT ANY SHAPE OF YOUR CHOICE? \n \n(a) TRIANGLE \n \n(b) CIRCLE \n \n(c) RECTANGLE \n \n(d) SQUARE\n \n(e) EXIT \n")

    #for triangle
    if (anyShape=="a"):
        first=float(input("ENTER A VALUE FOR SIDE A ="))
        second=float(input("ENTER A VALUE FOR SIDE B ="))
        third=float(input("ENTER A VALUE FOR SIDE C ="))
    #since area of a rectangle is A=root of (s*(s-a)*(s-b)*(s-c))
    #perimeter s=(a+b+c)/2
        S=(first + second + third)/2
        result=(S*(S-first)*(S-second)*(S-third))**0.5
        print("area of the triangle =",result)
        another=input("DO YOU WISH TO CALCULATE FOR ANOTHER SHAPE \n(a)YES \n(b)NO\n")
        if another\
           ==\
           "a":
            print("")
            return the_main()
        else:
            print("")
            print("THANK YOU FOR USING OLANETSOFT CALCULATOR")
            exit()
    #for circle
    if (anyShape=="b"):
        from math import pi
    #area of a circle is pi*R**2
        R=float(input("ENTER THE VALUE FOR RADIUS R ="))
        execution=pi*R**2
        result=round(execution,2)
        print("AREA OF THE CIRCLE =",result)
        another=input("DO YOU WISH TO CALCULATE FOR ANOTHER SHAPE \n(a)YES \n(b)NO\n")
        if another\
           ==\
           "a":
            print("")
            return the_main()
        else:
            print("")
            print("THANK YOU FOR USING OLANETSOFT CALCULATOR")
            exit()

    #for rectangle
    if (anyShape=="c"):
        l=float(input("ENTER THE VALUE FOR LENGHT L ="))
        b=float(input("ENTER THE VALUE FOR BREATH B ="))
        execution=l*b
        result=round(execution,2)
        print("AREA OF THE RECTANGLE =",result)
        another=input("DO YOU WISH TO CALCULATE FOR ANOTHER SHAPE \n(a)YES \n(b)NO\n")
        if another\
           ==\
           "a":
            print("")
            return the_main()
        else:
            print("")
            print("THANK YOU FOR USING OLANETSOFT CALCULATOR")
            exit()

    #for Square
    if (anyShape=="d"):
        sq=float(input("ENTER THE VALUE FOR L ="))
        execution=sq**2
        result=round(execution,2)
        print("AREA OF THE SQUARE =",result)
        another=input("DO YOU WISH TO CALCULATE FOR ANOTHER SHAPE \n(a)YES \n(b)NO\n")
        if another\
           ==\
           "a":
            print("")
            return the_main()
        else:
            print("")
            print("THANK YOU FOR USING OLANETSOFT CALCULATOR")
            exit()

    if (anyShape=="e"):
        print("THANK YOU FOR USING OLANETSOFT SHAPE CALCULATOR")
        quit
    else:
        print("PLEASE SELECT AN OPTION OR STUDY AT HOME, THEN RETRY LATER")
        return the_main()
print(the_main())






    




    




    
