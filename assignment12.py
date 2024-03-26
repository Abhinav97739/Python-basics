gpa=float(input("What's the gpa of etudiant "))
inst_app=input("Is the student going to be educated at an approved institution?")

if gpa>=3.7:
    if inst_app=="yes":
        print("Eligible")
    else:
        print("Doesn't qualify")
else:
    print("Doesn't meet the criteria")
