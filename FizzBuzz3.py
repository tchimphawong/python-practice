#Schreibe ein Programm das alle Zahlen von 1 bis 100 ausgibt.
#Wenn die Zahl allerdings ein Vielfaches von 3 ist, soll statt der Zahl das Wort "Fizz" ausgegeben werden.
#Wenn die Zahl ein Vielfaches von 5 ist, soll statt der Zahl das Wort "Buzz" ausgegeben werden.
#Ist die Zahl sowohl ein Vielfaches von 3 als auch von 5, soll statt der Zahl das Wort "FizzBuzz" ausgegeben werden.

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
