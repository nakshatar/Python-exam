import sys

ipad=sys.argv[1];
print(ipad)

with open("inp.txt") as f:
    for line in f:
    	if ipad in line:
    		print("IP IS PRESENT",ipad)
    		break
    else:
        print("IP NOT FOUND",ipad)
    		
sys.exit()
   