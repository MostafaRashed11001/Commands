# Speaking with cmd using python lap
import	os
y =os.popen("cat ls.py") #excuite find the path of your current working directory
y =y.read()
print(y)



