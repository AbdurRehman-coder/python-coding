
# Arshad BMI
name1 = 'Arshad Ali'
height_m1 = 2
weight_kg1 = 65
# Harun BMI
name2 = 'Harun Persain'
height_m2 = 1.7
weight_kg2 = 53
# Nazim ud din BMI
name3 = 'Nazim'
height_m3 = 2
weight_kg3 = 110

# function to calculate the BMI for each person
def calculate_bmi(name, height, weight) :
    bmi = weight / (height ** 2)
    print(f'bmi: \n {bmi}')
    if bmi <= 25 :
        return name + ' is not overweight, ' 
    else : 
        return f'{name } is overweight, bmi: {bmi}'


person1 = calculate_bmi(name1, height_m1, weight_kg1)
person2 = calculate_bmi(name2, height_m2, weight_kg2)
person3 = calculate_bmi(name3, height_m3, weight_kg3)

print(person1)
print(person2)
print(person3)
