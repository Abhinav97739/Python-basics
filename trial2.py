fruits=["Apple", "Mango", "Grapes"]
x,y,z=fruits
print(x)
print(y)
print(z)
x="awesome"
def func():
    global x
    x='Jios'
    print("I am " + x)

func()
print("Python is " + x)
animals=frozenset(["cat","Bat","Rat"])
print("sat" in animals)
