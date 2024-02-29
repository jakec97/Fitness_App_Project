from datetime import datetime, date

class user_details():
    def __init__(self,first_name,age,gender,height,weight,body_fat):
        self.first_name = first_name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.body_fat = body_fat

    # Calculating BMI (Body Mass Index)
    def bmi(self):
        bmi = float(self.weight)/(float(self.height)**2)
        return bmi

    # Classifying BMI Score against NHS Ranges
    def bmi_assessor(self):
        bmi = float(self.weight) / (float(self.height) ** 2)
        if bmi <= 18.4:
            return 'Underweight'
        elif 18.4 <= bmi <= 24.9:
            return 'Normal'
        elif 25.0 <= bmi <= 39.9:
            return 'Overweight'
        else:
            return 'Obese'

    # Classifying Body Fat % against Healthy Ranges - dependent on personal attributes (Age, Gender, etc...)
    def body_fat_score(self):
        age = int(self.age)
        body_fat = float(self.body_fat)
        if self.gender == 'M':
            if 20 <= age <= 39:
                if body_fat < 0.08:
                    return 'Too Low'
                if 0.08 <= body_fat <= 0.1999:
                    return 'Healthy'
                if 0.2 <= body_fat <= 0.25:
                    return 'Overweight'
                if body_fat > 0.25:
                    return 'Obese'
            if 40 <= age <= 59:
                if body_fat < 0.11:
                    return 'Too Low'
                if 0.11 <= body_fat <= 0.2199:
                    return 'Healthy'
                if 0.22 <= body_fat <= 0.28:
                    return 'Overweight'
                if body_fat > 0.28:
                    return 'Obese'
            if 60 <= age <= 79:
                if body_fat < 0.13:
                    return 'Too Low'
                if 0.13 <= body_fat <= 0.2499:
                    return 'Healthy'
                if 0.25 <= body_fat <= 0.30:
                    return 'Overweight'
                if body_fat > 0.30:
                    return 'Obese'
        if self.gender == 'F':
            if 20 <= age <= 39:
                if body_fat < 0.21:
                    return 'Too Low'
                if 0.21 <= body_fat <= 0.3299:
                    return 'Healthy'
                if 0.33 <= body_fat <= 0.39:
                    return 'Overweight'
                if body_fat > 0.39:
                    return 'Obese'
            if 40 <= age <= 59:
                if body_fat < 0.23:
                    return 'Too Low'
                if 0.23 <= body_fat <= 0.3499:
                    return 'Healthy'
                if 0.35 <= body_fat <= 0.40:
                    return 'Overweight'
                if body_fat > 0.40:
                    return 'Obese'
            if 60 <= age <= 79:
                if body_fat < 0.24:
                    return 'Too Low'
                if 0.24 <= body_fat <= 0.3599:
                    return 'Healthy'
                if 0.36 <= body_fat <= 0.42:
                    return 'Overweight'
                if body_fat > 0.42:
                    return 'Obese'

