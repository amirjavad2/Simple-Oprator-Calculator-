"""
Version Controll : 
V1.0

Calculator that do simple math stuff 
also have a history with date and time

V2.0 :

Now user can write a whole expression
The inputed expression will be Fixed and cleaned (put space between numbers and ops , removes more than 1 spaces , remove more than 1 ops (** will change to * and so others))
The expression will be devided into simpler expresions and will get the resualt
History was reworked and it works with any expression user enters """
import datetime
import re
global temphis
temphis = ""
def Sort(inp):#this function will manage and fix the input string into somthing that compiler can understand 
    global temphis 
    inp = re.sub(r"\++"," + ",inp)
    inp = re.sub(r"\-+"," - ",inp)
    inp = re.sub(r"\*+"," * ",inp)
    inp = re.sub(r"\/+"," / ",inp)
    inp = re.sub("\s* "," ",inp)
    print(f"{inp} = ")
    temphis += inp
    return re.split("\s", inp)


#****************************************************

global his
his = str("The history :\n")
def history(inp ,res):# This is the history function this guy saves and print the history 
    t = datetime.datetime.now()
    global his
    
    match inp :
        case "h"|"H":
            print (his)
        case _:
            his += f"{inp} = {res}      {t}\n"


#****************************************************


def oprate(exp):# this function does the simple oprations 
    x = float(exp[0])
    y = float(exp[2])
    match exp[1]:
        case "*":
            return x * y
        case "/":
            if y == 0 :
                print ("ERROR: cant devide by 0 (will be replaced with 0)")
                return 0
            return x / y
        case "+":
            return x + y
        case "-":
            return x - y


#****************************************************


def prsort(inp):#devid the whole expression to simple ones and after oprate them return the resualt 
    i = 0
    odd = ((2 * i) + 1)
    l = len(inp)
    while odd < l:
        i , odd , l
        if inp[odd] == "*" or inp[odd] == "/" :
            Tempexp = (f"{inp[odd-1]}",f"{inp[odd]}",f"{inp[odd+1]}")
            tempres = str(oprate(Tempexp))
            inp.pop(odd+1)
            inp.pop(odd-1)
            inp.pop(odd-1)
            inp.insert(odd-1,f"{tempres}")
            l = len(inp)
            continue
        i = 1 + i
        odd = ((2 * i) + 1)
        l = len(inp)
        # if odd > l :
        #     for x in inp :
        #         if x == "*" or x == "/":
        #             i = 0
    i = 0
    odd = ((2 * i) + 1)
    l = len(inp)
    while odd < l:
        i , odd , l
        if inp[odd] == "+" or inp[odd] == "-" :
            Tempexp = (f"{inp[odd-1]}",f"{inp[odd]}",f"{inp[odd+1]}")
            tempres = str(oprate(Tempexp))
            inp.pop(odd+1)
            inp.pop(odd-1)
            inp.pop(odd-1)
            inp.insert(odd-1,f"{tempres}")
            l = len(inp)
            continue
        i = 1 + i
        odd = ((2 * i) + 1)
        l = len(inp)
    return inp[0]


#****************************************************


while (1 > 0) :# This is the main part of the program 
    inp = input("Enter your expression :\n")
    match inp :
        case "q"|"Q":
             break
        case "h"|"H":
            history("h" , 0) 
            continue
    inp = Sort(inp)
    result = prsort(inp)
    print(f"{temphis} = {result}")
    history(temphis , result)
    temphis = ""
