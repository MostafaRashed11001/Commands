# Speaking with cmd using python lap
import	os
#os.system("echo hello terminal")
y =os.popen("sudo apt-get update") #excuite updata
y =y.read()
print(y)



