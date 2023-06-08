def addition(param1, param2):
    return param1 + param2
print(addition(3, 2))
print(addition(-3, -6))
print(addition(7, 3))

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0: 
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)
print(fizz_buzz(3))  
print(fizz_buzz(5))  
print(fizz_buzz(15))  
print(fizz_buzz(7))  

def tri_area(base, height) :
     return (base * height) / 2
print(tri_area(3, 2))
print(tri_area(7, 4))
print(tri_area(10, 10))


def calculate_fuel(distance) :
    if distance >= 10 :
        return 100 + distance * 10
    else:
        return 100
print(calculate_fuel(10))
print(calculate_fuel(15)) 
print(calculate_fuel(23.5))
print (calculate_fuel(3))

def both(number1, number2) :
    if number1 < 0 and number2 < 0:
        return True
    elif number1 > 0 and number2 > 0:
        return True
    elif number1 == 0 and number2 == 0:
        return True
    else:
        return False
print(both(6, 2))    
print(both(0, 0))
print(both(-1, 2))
print(both(0, 2))

