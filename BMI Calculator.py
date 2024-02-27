height = input('Enter Height:')
weight = input('Enter Weight:')
height_as_float = float(height)
weight_as_int = int(weight)
BMI = weight_as_int / height_as_float ** 2
BMI_as_int = int(BMI)
print("Your BMI is", BMI_as_int)