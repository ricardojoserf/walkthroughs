import sys

print ("# Title")
print ("Description")

for i in range(int(sys.argv[1]),int(sys.argv[2])):
	print ""
	print "Text"
	print ""
	print "![Screenshot](images/Screenshot_"+str(i)+".png)"
