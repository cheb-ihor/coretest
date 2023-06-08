def int_within_bounds(number, lower_bound, upper_bound) :
  if not isinstance(number, int):
    return False
  elif number < lower_bound or number >= upper_bound:
    return False
  else:
    return True
print(int_within_bounds( 1, 1, 2))
print(int_within_bounds( 1, 3, 8))
print(int_within_bounds(4.5, 3, 8 ))
print('-------------')
def makes10(a, b) :
    if a == 10 or b == 10 or a + b == 10 :
        return True
    else:
        return False
print(makes10(9,10))
print(makes10(9,9))
print(makes10(1,9))
print('-------------')
def squares_sum(n) :
    total = 0
    for i in range(n+1):
        total += (i**2)
    return total
print(squares_sum(3))   

def sum_even_nums_in_range(start, stop):
    result = 0
    for i in range(start, stop+1): 
        if i % 2 == 0:
            result += i
    return result
print (sum_even_nums_in_range(51, 150))
print (sum_even_nums_in_range(63, 97))

def hello():
    return "Hello!"
print(hello())

def mean(number):
    string_number = str(number)
    digits = len(string_number)
    sum = 0
    for i in string_number:
        sum += int(i)
    mean = sum/digits
    return int(mean)
print (mean(42))
print (mean(12345))
print (mean(666))