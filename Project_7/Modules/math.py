import math

def math_menu():

    while True:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\n===== MATHEMATICAL OPERATIONS =====")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        print("\n1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometric Functions")
        print("4. Area of Geometric Shapes")
        print("5. Back")

        choice = input("Enter Choice : ")

        if choice == "1":
            import math

            num = int(input("Enter Number : "))

            N = math.factorial(num)

            print("Factorial =",N)

            print("\n----------------------------------------------------------")

        elif choice == "2":

            p = float(input("Principal Amount : "))
            r = float(input("Rate (%) : "))
            t = float(input("Time (Years) : "))

            amount = p * ((1 + r/100) ** t)

            print("Amount =", round(amount,2))

            print("\n---------------------------------------------------------------")

        elif choice == "3":

            angle = float(input("Enter Angle : "))

            print("Sin =", round(math.sin(math.radians(angle)),4))
            print("Cos =", round(math.cos(math.radians(angle)),4))
            print("Tan =", round(math.tan(math.radians(angle)),4))

            print("\n----------------------------------------------------------------")
        
        elif choice == "4":
            while True:
                print("/n Whice Shapes Area You have to Find :")
                print("1. Circle")
                print("2. Square")
                print("3. Rectengle")
                print("4. Back")
                print("\n-------------------------------------")

                option =input("Enter your choice : ")

                if opition == "1":
                    import math
                    radius = float(input("Enter radius of circle :"))

                    area = math.pi * (radius ** 2)
                    print("Area of circle :", area)

                    print("\n-----------------------------------------------------")
                
                elif opition == "2":
                    side = float(input("Enter Side of square :"))
                    area = side ** 2

                    print("Area of Square :",area)

                    print("\n------------------------------------------------------")
                
                elif opition == "3":
                    l = float(input("Enter the length of the rectangle: "))
                    w = float(input("Enter the width of the rectangle: "))

                    area = l * w
                    print("Area of Rectengle  :",area)

                    print("\n-------------------------------------------------------")
                
                elif opition == "4":
                    break

                else:
                    print("Inavlid Inpute By the user")
            
        elif choice == "5":
            print("\n---------------------------------------------------------------")
            break

        else:
            print("Invalid Choice")
