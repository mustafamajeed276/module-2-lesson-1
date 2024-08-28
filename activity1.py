med_cause = input("did you have a medical cause Y or N")
atten = int(input("enter your attendance(number)"))
if med_cause == "Y":
    print("you are allowed")
else:
    if atten >= 75:
        print("allowed")
    else:
        print("not allowed")