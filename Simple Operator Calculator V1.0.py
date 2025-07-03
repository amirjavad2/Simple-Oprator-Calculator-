"""Calculator that do simple math stuff 
also have a history with date and time"""
import datetime
global his 
his = str("The history :\n")
def history(x ,y ,a ,z):
    t = datetime.datetime.now()
    match a :
        case "+"|"-"|"*"|"/": 
            global his 
            his = his + f"{x} {a} {y} = {z} {t}\n"
        case "p"|"P":
            print (his)
def action(x ,y ,a):
    match a: 
        case "+":
            z = x + y
            history(x , y , a , z)
            return x + y
        case "-":
            z = x - y
            history(x , y , a , z)
            return x - y
        case "*":
            z = x * y
            history(x , y , a , z)
            return x * y
        case "/":
            z = x / y
            history(x , y , a , z)
            return x / y
        case _:
            print("Wrong oporator Try Again")
while (1 > 0) :
    x = int(input("Enter a number :"))
    a = input("Enter a operator :")
    match a :
        case "q"|"Q":
            break
        case "h"|"H":
            history(0 , 0, "p" , 0) 
            continue
    y = int(input("Enter a number :"))
    print(action(x , y , a))
