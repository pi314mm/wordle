with open("Aa.txt") as f:
    Aa = [w.strip() for w in f.readlines()]

with open("La.txt") as f:
    La = [w.strip() for w in f.readlines()]

allwords = set(Aa).union(set(La))

def synth(word,guess):
    available = dict()
    for a in word:
        available[a]=available.get(a,0)+1
    twos = []
    for w,g in zip(word,guess):
        if w==g:
            twos.append(2)
            available[w]=available[w]-1
        else:
            twos.append(0)
    result = []
    for g,v in zip(guess,twos):
        if v==2:
            result.append(2)
        else:
            if available.get(g,0)>0:
                result.append(1)
                available[g]=available[g]-1
            else:
                result.append(0)
    return result


def check(word,guess,result):
    return synth(word,guess)==result

def int2array(i):
    ans = []
    for x in range(5):
        ans.append(i%3)
        i=i//3
    return ans[::-1]

def array2int(a):
    i=0
    for x in a:
        i=i*3+x
    return i

def worstresult(guess,available):
    nextavail = dict()
    for word in available:
        r = array2int(synth(word,guess))
        s = nextavail.get(r,set())
        s.add(word)
        nextavail[r]=s
    #print(sorted([len(v) for k,v in nextavail.items()]))
    #the extra -.5 is to make sure the correct solution only happens when it's the only one left
    #return max(nextavail.items(), key=lambda i: (-.5 if i[0]==array2int([2,2,2,2,2]) else 0)+len(i[1]))
    return sorted([len(v) for k,v in nextavail.items()])

def isvalid(word):
    return word in allwords

#bestval=1000
#best='apple'
#for i,guess in zip(range(len(allwords)),allwords):
#    print(i)
#    x,possible = worstresult(guess,Aa)
#    if len(possible)<bestval:
#        bestval=len(possible)
#        best=guess
#print(best)
#worstresult('arise',Aa)
#possible = Aa
#for guess in ['arise','plunk','howdy']:
#    x,possible = worstresult(guess,possible)
#    if guess not in allwords:
#        print('not valid')
#    print(int2array(x))
#    print(len(possible))
#print(possible)


for i,a in zip(range(len(Aa)),Aa):
    print(i)
    for j,b in zip(range(len(Aa)),Aa):
        print("\t"+str(j))
        if a==b:
            pass
        for c in Aa:
            if a==c or b==c:
                pass
            avail = [worstresult(guess,[a,b,c]) for guess in [a,b,c]]
            if not any([all(y==1 for y in x) for x in avail]):
                avail = [worstresult(guess,[a,b,c]) for guess in Aa]
                if not any([all(y==1 for y in x) for x in avail]):
                    print([a,b,c])
print('done')
