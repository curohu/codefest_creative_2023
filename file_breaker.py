import time

stime = time.time()

file = open("peaches.mp4",'rb').read()

print(len(file))

def divide_chunks(l,n):
    for i in range(0,len(l), n):
        yield l[i:i+n]

n = int(len(file)/20)
print(int(n))
x = list(divide_chunks(file,n))

print(len(x))

count = 0
for chunk in x:
    count+=1
    file = open(f"./parts/{str(count)}.txt",'wb')
    file.write(chunk)
    file.close()


print(f"Processing Time: {time.time()-stime:.2f}")