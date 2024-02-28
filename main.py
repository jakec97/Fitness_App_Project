""" This file will request users' body information, then use that data to perform a fitness assessment to see if the
 user is a healthy weight or if they are under/overweight. It will then output the results to the user."""

from classes import user_details

# Function to get user information
def get_user_input():
    # first_name = input("First Name: ")
    # last_name = input("Last Name: ")
    # age = input("Age: ")
    # email_address = input("Email Address: ")
    # gender = input("Gender (M/F): ")
    # height = input("Height (Meters): ")
    # weight = input("Weight (KG): ")
    # body_fat = input("Body Fat %: ")
    first_name = 'Jake'
    last_name = 'Clegg'
    age = 27
    email_address = 'jakesclegg@gmail.com'
    gender = 'M'
    height = 1.78
    weight = 80.7
    body_fat = 0.25

    return user_details(first_name,last_name,age,email_address,gender,height,weight,body_fat)

# saving the provided user details to use for assessments
user = get_user_input()

# BMI ASSESSMENT
# using the BMI function from the imported class on the user details collected above. In this function, BMI is returned
bmi = user.bmi()
bmi_classification = user_details.bmi_assessor(bmi)


# BODY FAT ASSESSMENT
body_fat_percentage = float(user.body_fat)*100
body_fat_classification = user.body_fat_score()


# FINAL RESULTS
print('')
print(f'Hi {user.first_name}, thanks for providing your information. Here are your assessment results:')
print(f' - Your BMI is {int(bmi)}, which is classed as {bmi_classification}.')
print(f' - Your Body Fat Percentage is {body_fat_percentage}%, which is classed as {body_fat_classification}.')
if body_fat_classification == 'Healthy':
    print("As your Body Fat Percentage is Healthy, you don't need to make any changes - nice work!")
elif body_fat_classification == 'Too Low':
    print("As your Body Fat Percentage is Too Low, you may benefit from gaining some weight. However, this is not medical advice, and everyone is unique!")
elif body_fat_classification == 'Overweight':
    print("As your Body Fat Percentage is Overweight, you may benefit from losing some fat to get into the Healthy range.")
elif body_fat_classification == 'Obese':
    print("As your Body Fat Percentage is Obese, you may benefit from losing some fat, aiming to get into the Healthy range.")