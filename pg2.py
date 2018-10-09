import sys

ipad=sys.argv[1];
print(ipad)
f = open("in.txt","r")
ln = f.read();
lnst = ln.split(" ")
lnst[-1] = lnst[-1].split("\n")[0]
count = 0
for ln in lnst:
    if (ln == sys.argv[1]):
    	count = count+1
if count == 0:
    print("IP IS NOT PRESENT")
    
else:
    print("IP IS FOUND")
    		
sys.exit()
   