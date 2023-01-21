# Speaking with cmd using python lap
import	os
os.chdir("/")
y =os.popen("pwd") #excuite find the path of your current working directory
y =y.read()
print(y)



