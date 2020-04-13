f=open("c:/Users/Jacob/Documents/git/creds.txt","r")
lines=f.readlines()
username=lines[0]
password=lines[1]
f.close()

print(username)
print(password)