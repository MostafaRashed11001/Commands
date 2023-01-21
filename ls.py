# Speaking with cmd using python lap
import	os
while(1):

	#os.system("list")
	choose = input("ENTER FROM 0 TO 3")
	if choose == '1':
		y =os.popen("ls") #excuite ls
		y =y.read()
		print(y)
	elif choose == '2':
		y =os.popen("ls -R") #excuite ls -R
		y =y.read()
		print(y)
	elif choose == '3':
		y =os.popen("ls -a") #excuite ls -a
		y =y.read()
		print(y)
	elif choose == '4':
		y =os.popen("ls -lh") #excuite ls -lh
		y =y.read()
		print(y)
	elif choose == '0':
		break
