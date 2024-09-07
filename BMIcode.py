weight = int(input("Enter your weight"))
height = float(input("enter your height"))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")


bmi = weight/height**2
print(bmi)