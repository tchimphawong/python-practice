nb = 3
nm = 5
for i in range(1, 101):
    if i%nb == 0 and i%nm == 0:
        print("FizzBuzz")
    elif i%nm == 0:
        print("Buzz")
    elif i%nb == 0:
        print("Fizz")
    else:
        print(i)
