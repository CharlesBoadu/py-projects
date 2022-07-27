cgpa=float(input("Enter ypur CGPA: "))

if cgpa>=3.6:
    print("First Class")
elif cgpa>=3.0 and cgpa<=3.5:
    print("Second Class Upper")
elif cgpa>=2.5 and cgpa<=3.0:
    print("Second Class Lower")
elif cgpa>=2.0 and cgpa<=2.5:
    print("Third class")
elif cgpa<2.0:
    print("Pass")
    
