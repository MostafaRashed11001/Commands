# Speaking with cmd using python lap
import	os
y =os.popen("df -h /home/mrashed/Commed_Scraibt/ls.py") #excuite find the path of your current working directory
y =y.read()
print(y)


