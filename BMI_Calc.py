print("Welcome to the BMI calculator!")

#get user input for both height and weight
height = float(input("How tall are you in inches? ")) 
weight = float(input("What is your weight in pounds? "))

#multiply input to get corrected data (convert height in inches to meters and weight in pounds to kg)
height = height * 0.0254
weight = weight * 0.453592

#use bmi formula to get bmi
BMI = weight / (height * height)

print("Your Body Mass Index: ", BMI)

#compare results to weight status
if BMI <= 18.49:
    print("You are underwieght.")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are at a helthy weight.")
elif BMI >= 25 and BMI <= 29.9:
    print("You are overwight.")
elif BMI >= 30:
    print("You are obese.")
else:
    print("error, please enter correct data.")





































































