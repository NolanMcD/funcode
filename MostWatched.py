fileName = input("Enter file name: ")
file = open(fileName)
MoviesWatched = []
count = 0
for x in file:
    if(count > 0):
        y = x.split("	")
        MoviesWatched.append(y[1])
    count = count + 1

topWatch = {}
for movie in MoviesWatched:
    count = MoviesWatched.count(movie)
    topWatch[movie] = count

print("Most watched Movies of 2020")
mmax = max(topWatch.values())
while mmax > 0:
    for x in topWatch:
        if topWatch[x] == mmax:
            print(x, end = ": ")
            print(mmax)
    mmax = mmax - 1
    