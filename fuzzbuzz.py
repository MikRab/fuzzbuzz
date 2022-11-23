"""programu w Pythonie, który wypisze liczby od 1 do 50. Dla liczb będących 
wielokrotnością 2 program wypisze jednak zamiast danej liczby słowo „fuzz” 
a dla liczb stanowiących wielokrotność 3 program wypisze słowo „buzz”. Wreszcie,
dla liczb, które są jednocześnie wielokrotnością 2 i 3 program wyświetli komunikat:
„fuzzbuzz”."""

for x in range(1, 51):
    if x % 2 == 0 and x % 3 == 0:
        print("fuzzbuzz")
    elif x % 2 == 0:
        print("fuzz")
    elif x % 3 == 0:
        print("buzz")
    else:
        print(x)