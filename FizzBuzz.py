def AI_check(i,dic,inp=None) :
    string=''
    
    if inp is not None :
        for k,v in dic.items() :
            if i % v == 0:
                string=string+k
        if len(string) > 0 :
            return string
        else :
            return int(inp)
    else:
        for k,v in dic.items() :
            if i % v == 0:
                string=string+k
        if len(string) > 0 :
            return string
        else :
            return i

dic=dict()
print("""Choose the rules (one at a time) by writing a space between them 
      (write done when finished)""")
print("e.g. 3 Fizz, 5 Buzz, 7 Tess...")
while True:
    inp = input("Rule: ")
    if inp in ("Done","done") :
        break
    else:
        words=inp.split()
        dic[words[1].capitalize()]=int(words[0])
print("The rules are:")
for v,k in dic.items() :
    print("The word {} for {}".format(v,k))
i=1
print("Let's play!")
while True :
    inp = input("Your turn: ")
    if inp in ("Done", "done") :
        break
    try :
        n=int(inp)
        if AI_check(i,dic,n) == n :
            print(AI_check(i+1,dic))
        else :
            print("You lost! the answer was:",AI_check(i,dic))
            break
    except :

        if AI_check(i,dic,inp).lower() == inp.lower() :
            print(AI_check(i+1,dic))
        else :
            print("You lost! the answer was:",AI_check(i,dic))
            break
    i=i+2
