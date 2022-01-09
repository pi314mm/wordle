#from english_words import english_words_lower_alpha_set as english
#five = [w for w in english if len(w) == 5]

with open("Aa.txt") as f:
    Aa = [w.strip() for w in f.readlines()]

#with open("La.txt") as f:
#    La = [w.strip() for w in f.readlines()]

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


def check(guess,result):
    def check2(word):
        return synth(word,guess)==result
    return check2

def checkall(guesses, results):
    def checkall2(word):
        return all(map(lambda f: f(word),[check(a,b) for a,b in zip(guesses,results)]))
    return checkall2

def bestword(possible,english):
    bestval = len(english)
    best = ""
    for i,guess in zip(range(len(english)),english):
        guessmax = 0
        for solution in possible:
            guessmax = max(len(list(filter(check(guess,synth(solution,guess)),possible))),guessmax)
            if guessmax>bestval:
                pass
        if guessmax<bestval:
            best=guess
            bestval=guessmax
    return best

#print(bestword(Aa,Aa))
            
#print(synth('troll','ocean'))
#print(list(filter(checkall(['audio','tommy','total','comet'],[synth('boost','audio'),synth('boost','tommy'),synth('boost','total'),synth('boost','comet')]),Aa)))
print(list(filter(checkall(['ocean','spurt'],[synth('truss','ocean'),synth('truss','spurt')]),Aa)))
#print(synth('troll','stoup'))
#print(synth('troll','tooth'))
#print(synth('troll','troll'))

#from multiprocessing import cpu_count,Pool
#import tqdm
#pool=Pool(cpu_count()-1)

def run(gp):
    guess,possible = gp
    m = 0
    for solution in possible:
        m = max(len(list(filter(check(guess,synth(solution,guess)),possible))),m)
    return (guess,m)

#def bestword(possible,english):
#    a = [(w,possible) for w in english]
#    return dict([a for a in tqdm.tqdm(pool.imap_unordered(run,a),total=len(english))])

#def bestword2(possible,english):
#    counts = dict([run((a,possible)) for a in english])
#    m = min(counts.values())
#    for k,v in counts.items():
#        if v==m:
#            return k
#possible = list(filter(checkall(['ocean','sting'],[[0,0,0,0,1],[0,0,2,1,0]]),Aa))
possible = list(filter(checkall(['soare','think','named','fancy'],[[0,0,1,0,0],[0,0,0,1,0],[1,2,0,0,0],[0,2,2,0,0]]),Aa))
print(possible)
#print(bestword2(possible,possible))
#print(run(('audio',Aa)))
#print(list(filter(check('ocean',synth('troll','ocean')),Aa)))
#bestword(['aaaaa','bbbbb','ccccc','ddddd','eeeee','abcde'],['aaaaa','bbbbb','ccccc','ddddd','eeeee','abcde'])
#for counter,guess in zip(range(len(Aa)),Aa):
def at3(guess,english):
    partitions = []
    for i in range(3**5):
        result = []
        copy = i
        for a in range(5):
            result.append(copy%3)
            copy=copy//3
        ans = list(filter(check(guess,result),english))
        if len(ans)>0:
            partitions.append((i,ans))
    bests = [(bestword(possible,Aa),possible)for r,possible in partitions]
    return bests
one = at3('arise',Aa)
two = [at3(*v) for v in one]
two = [item for sublist in two for item in sublist]
three = [at3(*v) for v in two]
three = [item for sublist in three for item in sublist]
for a,b in three:
    if len(b)>1:
        print("no")
print("yes")

