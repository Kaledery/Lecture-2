# list of available cars and their prices
cars = { 
"Audi R8": 130000,
"Bugatti Veyron": 400000,
"Chevrolet Camaro": 500000,
"Dodge Viper": 450000,
"Excalide": 460000,
"LaFerrari": 250000,
"Honda Civic": 367000,
"Honda Accord": 567000,
"Hyundai Elantra": 350000,
"Hyundai Sonata": 67000,
"Toyata Corolla": 500000,
"Toyata RAV4": 900000,
"Porshe 917": 785000,
"BMW i8": 100000,
"Chevrolet Corvette": 4567000,
"Chrysler Aspen Hybrid": 7856000,
"Dodge Stealth": 659500,
"Ferrari FF": 900000,
"Ford Mustang": 508900,
"Lamborghini Gallardo":1402000,
"Lamborghini Urus": 200000,
"Range Rover Discovery": 1020300,
"Audi E-Tron": 1049000,
"Bentley Bentayga": 197300,
"Chevrolet Blazer": 659950,
"Dodge Hornet": 449950, 
"Honda Pilot": 520300,
"Infinity Q60": 607000,
"Kia Niro Electric": 102500,
"Toyota RAV4 Hybrid": 890700,
}
# get user input for car name
car_name = input("Enter a car_name:")
# check if car name is in the list of available cars
if car_name in cars:
    print("Yes")
    #if car name is present, get its price
    car_price= cars[car_name]
    print(f" The price of {car_name} is ${car_price}.")
else:
    #if car name is not present, inform the user
    print(f"Sorry, {car_name} is not available.")
    
    
    