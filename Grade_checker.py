def assign_grade(score):
    while True:
        score = int(input("Tell me what is your score:"))

        if score < 0 or score > 100:
            print("Invalid score,please try again:")
        elif score >= 90:
            print("Your grade is: A")
        elif score >= 80:
            print("Your grade is: B")
        elif score >= 70:
            print("Your grade is: C")
        elif score >= 60:
            print("Your grade is: D")
        else:
            print("Your grade is: F")
            
assign_grade(0)