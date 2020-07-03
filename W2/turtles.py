import turtle as tu
x = eval(input("input a number:"))
tu.color("hotpink")
tu.pensize(3)#????
temp = 0#????

while x!=1:
    print(x)
    temp = temp+1
    if temp%2:
        tu.left(90)
    tu.forward(x)#??
    if not x%2:
        x=x/2
    else:
        x=3*x+1
tu.down()