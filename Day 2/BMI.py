weight = float(input("Enter you weight in Kg: \n"))
height = float(input("Enter you height in cm: \n"))
BMI = weight/((height/100)**2)
if(BMI<18.5):
    print("Your BMI is : "+ str(BMI) + " Underweight")
if(BMI>=18.5 and BMI<=24.9):
    print("Your BMI is : "+ str(BMI) + " Not obese")
if(BMI>=25 and BMI<=29.9):
    print("Your BMI is : "+ str(BMI) + " Not obese")
if(BMI>=30 and BMI<=34.9):
    print("Your BMI is : "+ str(BMI) + " Low-risk")
if(BMI>=35 and BMI<=39.9):
    print("Your BMI is : "+ str(BMI) + " Moderate-risk")
if(BMI>=40 and BMI<=40):
    print("Your BMI is : "+ str(BMI) + " High-risk")