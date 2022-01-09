def getresult(ans,guess):
    t = len(set(ans).intersection(set(guess)))
    f = sum([1 if a==b else 0 for a,b in zip(ans,guess)])
    t=t-f
    return (t,f)

def check(ans,guess,result):
    return result==getresult(ans,guess)

def int2array(i):
    ans = []
    for x in range(4):
        ans.append(i%10)
        i=i//10
    return ans

def array2int(a):
    i=0
    for x in a:
        i=i*10+x
    return i

#print(getresult([1,2,3,4], [5,6,7,8]))
allnumbers = []
for i in range(9877):
    x = int2array(i)
    if len(set(x))==4:
        allnumbers.append(x)



l = list(filter(lambda ans: check(ans,[4,2,7,9],(2,1)),allnumbers))
l = list(filter(lambda ans: check(ans,[4,2,1,0],(2,0)),l))
l = list(filter(lambda ans: check(ans,[2,1,7,0],(3,0)),l))
l = list(filter(lambda ans: check(ans,[1,7,2,9],(0,3)),l))
#l = list(filter(lambda ans: check(ans,[8,2,1,0],(1,1)),l))
print([array2int(i) for i in l])
print(len(l))
l2 = set(array2int(a) for a in l)

possibleans = []
for a in range(5):
    for b in range(5):
        if a+b<=4:
            possibleans.append((a,b))

best = [0,0,0,0]
bestval = 9999
for i,guess in zip(range(len(allnumbers)),allnumbers):
    #print(i)    
    guessresult = max([len(list(filter(lambda ans: check(ans,guess,result),l))) for result in possibleans])
    if guessresult < bestval:
        best = guess
        bestval = guessresult
    elif guessresult == bestval:
        if array2int(guess) in l2:
            best=guess
            bestval=guessresult

print(best)
print(bestval)
