    
def cal(marks, subject="None"):
    if marks >= 75:
        print(subject,": A")
    elif marks >= 65:
        print(subject,": B")
    elif marks >= 45:
        print(subject,": C")
    elif marks >= 35:
        print(subject,": S")
    else:
        print(subject,": W")
        
cal(10, "Sinhala")
cal(50)
cal(90)
cal(68)