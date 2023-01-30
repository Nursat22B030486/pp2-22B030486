''' CREATING A ARRAY '''
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
# modifing the value of the first array item:
cars[0] = "Toyota"

''' THE LENGTH OF AN ARRAY '''
x = len(cars)

''' LOOPING ARRAY ELEMENTS '''
for x in cars:
    print(x)

''' ADDING ARRAY ELEMENTS '''
cars.append("Honda")

''' REMOVING ARRAY ELEMENTS '''
cars.pop(1)
cars.remove("Volvo")