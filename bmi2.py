"""
This is a BMI calculator written in Python by me (MGage Morgan). 
The design is minimal atm, but will improve as I get further. 
The BMI formula to use: weight / height^2 x 703

We use a float() wrapped around a raw_input() for 'weight' and 
'height'. We do this to prevent Python from thinking we're trying to 
use strings instead of numbers when actually we are not. 
"""
	
weight = float(raw_input('Enter your weight: '))
height = float(raw_input('Enter your height: '))

placeholder = {'bmi': 'Your BMI: ', 'diagnosis': 'Your Diagnosis: '}

"""
Square splits off a part of the formula to do first (think: PEMDAS). 
The Order of Operations from math says to do exponents before 
multiplying/dividng. So the 'square' variable holds the value of 
'height' being squared so we can conveniently use it later. 
"""
square = height ** 2

"""
'divvy' is the second piece of the problem. This variable holds 
the 'weight' divided by the pre-calculated 'height squared' to make 
the problem into just two pieces now.
"""
divvy = weight / square

"""
The 'finale' brings it all together. We take the first half ('divvy') 
and multiply it by 703, as per the CDC's Adult BMI formula. 
"""
finale = divvy * 703

"""
This is more for readability than anything. We round off the number 
given by 'finale' to the nearest hundredth. This way, it also 
matches the response given on CDC's website. 
"""
rounded_finale = round(finale, 2)

"""
Convert to Int for the PoundLife joke
"""
lbs_life = int(weight)

"""
These are variables that contain strings that will 
print depending on the number you received for rounded_finale.

Store variables in a dictionary where they can be retrieved on runtime. Call
it diagnosis_choice
"""
underweight = "You're way underweight! Danger - go eat something."
normal = "You are normal - no change required!"
overweight = "Go join Weight Watchers pronto!"
obese = "You is obeest, #My" + str(lbs_life) + "PoundLife"
inaccessible = "This shouldn't even by possible"
diagnosis_choice = {'underweight': underweight, 'normal': normal, 'overweight': overweight, 'obese': obese}

"""
The rounded_finale output also determines what gets printed. 
If it is:
Less than 18.50: Print underweight
Less than 24.99: Print normal
Less than 30.00: Print overweight
Greater than 30: Print obese, with that special hashtag that 
is generated using the weight you entered.
If anything else: Print the inaccessible variable
"""
if rounded_finale < 18.50:
	print "\n" + placeholder['bmi'] + str(rounded_finale) + "\n" + placeholder['diagnosis'] + diagnosis_choice['underweight'] 
elif rounded_finale < 24.99:
	print "\n" + placeholder['bmi'] + str(rounded_finale) + "\n" + placeholder['diagnosis'] + diagnosis_choice['normal'] 
elif rounded_finale < 30.00:
	print "\n" + placeholder['bmi'] + str(rounded_finale) + "\n" + placeholder['diagnosis'] + diagnosis_choice['overweight'] 
elif rounded_finale > 30.00:
	print "\n" + placeholder['bmi'] + str(rounded_finale) + "\n" + placeholder['diagnosis'] + diagnosis_choice['obese'] 
else:
	print inaccessible
