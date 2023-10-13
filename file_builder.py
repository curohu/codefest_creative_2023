import time, os, sys

stime = time.time()

x = bytes()
dir = './parts/'
for count in range(1,len(os.listdir(dir))+1):
    data = open(f'./parts/{count}.txt','rb').read()
    x+=data

out = open("./parts/outfile.mp4",'wb')
out.write(x)
out.close()


print(f"Processing Time: {time.time()-stime:.2f}")