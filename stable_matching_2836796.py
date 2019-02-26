import sys
import csv

def stable_matching(nMen, nWomen, prefMen, prefWomen):
    freeMen = list(range(1, nMen + 1))
    freeWomen = list(range(1, nWomen + 1))
    engaged = []
    while(len(freeMen) > 0):
        m = freeMen[0] #choose unmarried man
        if(len(prefMen[m - 1]) == 0): #proposed to everyone but failed
            break #rip
        w = prefMen[m - 1][0] #choose highest rank woman for m
        if(w in freeWomen):
            engaged.append((m,w))
            freeWomen.remove(w)
            freeMen.remove(m)
        else:
            mPrime = next(couple for couple in engaged if couple[1] == w)[0] #get w's man
            x = y = 0 #get preferences
            for i in range(nWomen):
                if m == prefWomen[w - 1][i]:
                    x = i
                if mPrime == prefWomen[w - 1][i]:
                    y = i
            if(y < x): #if current man has higher preference
                prefMen[m-1].remove(w)
            else:
                engaged.remove((mPrime, w))
                engaged.append((m, w))
                freeMen.remove(m)
                freeMen.append(mPrime)
    engaged.sort()
    print(engaged)

def main():
    prefMen = []
    prefWomen = []
    nMen = 0
    nWomen = 0
    #read in a file
    text = input("Input a file\n")
    #read in the file's contents (in this case numbers are the same across)
    with open(text, "r") as file:
        nMen = nWomen = int(file.readline())
        file.readline() #whitespace
        count = 0
        for row in csv.reader(file):
            if(count == nMen):
                break
            prefMen.append(list(map(int, row)))
            count += 1
        count = 0
        for row in csv.reader(file):
            if(count == nWomen):
                break
            prefWomen.append(list(map(int, row)))
            count += 1
    #perform a stable matching
    stable_matching(nMen, nWomen, prefMen, prefWomen)

if __name__ == "__main__":
    main()