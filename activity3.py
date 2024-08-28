print("select your ride:")
print("\n1. bike")
print("\n2. car")
choice = int(input("enter your choice(1 for bike and 2 for car)"))
if (choice == 1):
    print("what type of bike")
    print("\nheavy bike")
    print("\nscooter")
    choice2 = int(input("enter your bike (1 for heavy bike and 2 for scooter)"))
    if choice2 == 1:
        print("ok, let's go on the heavy bike")
    else:
        print("ok, let's go on the scooter")
elif (choice == 2):
    print("what type of bike")
    print("\noffroad")
    print("\nrace car")
    choice2 = int(input("enter your car (1 for offroad and 2 for race car)"))
    if choice2 == 1:
        print("ok, let's go on the offroad")
    else:
        print("ok, let's go on the race car")
else:
    print("wrong choice")