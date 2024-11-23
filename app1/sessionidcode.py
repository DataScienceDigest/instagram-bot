import requests, os, stdiomask
from uuid import uuid4
os.system('title  ')
os.system('cls||clear')
# write code to read username and password 
def session(username,password):
        headers = {
                "Host": "i.instagram.com",
                "X-Ig-Connection-Type": "WiFi",
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Ig-Capabilities": "36r/Fx8=",
                "User-Agent": "Instagram 159.0.0.28.123 (iPhone8,1; iOS 14_1; en_SA@calendar=gregorian; ar-SA; scale=2.00; 750x1334; 244425769) AppleWebKit/420+",
                "X-Ig-App-Locale": "en",
                "X-Mid": "Ypg64wAAAAGXLOPZjFPNikpr8nJt",
                "Content-Length": "778",
                "Accept-Encoding": "gzip, deflate"
                }
        data = {

                "username":username,
                "reg_login":"0",
                "enc_password":f"#PWD_INSTAGRAM:0:&:{password}",
                "device_id":uuid4(),
                "login_attempt_count":"0",
                "phone_id":uuid4()
                }
        url = "https://i.instagram.com/api/v1/accounts/login/"
        r = requests.post(url=url,headers=headers,data=data)
        session_id = r.cookies.get("sessionid")
        if 'The password you entered is incorrect' in r.text:
                print(f"")
                print("")
                input(f"[+] wrong pass, enter 2 exit ")
                quit()
        elif 'logged_in_user' in r.text:
                print(f"[+] Logged In Success")
        else:
                print(r.text)
                input(f"Bad Login , Try Again")
                quit()
        print(f"Session ID: {session_id}")
        return session_id



credentials = {
   
#     working ids
    'gynnnn2023': 'shiv1915',  # correct
    'deve_lopers123':'shiv1915',  # correct
    'jot1212020':'shiv1915',# correct
    'sk3354580':'shiv1915',# correct
    'dilj.ake':'shiv1915',# correct
    'himanikull':'shiv1915',# correct
    'grouppython':'shiv1915',# correct
    'losting173':'shiv1915',# correct
    'welcomeback748':'%S1h9i1v5%',
    'hynmkl':'%S1h9i1v5%',# correct
}

with open('sessions_file.txt','a') as f:

        for i in credentials.items():
                ses = session(i[0],i[1])
                f.write(f'{ses}\n')
print('all sessions saved successfully !!')



# facebook sessions
# xs 5%3AB9WLcgj-vnDutg%3A2%3A1703950332%3A-1%3A13383%3A%3AAcWXVUH3byGkKnq9nPMLkU49wBWR-OD54NxdORddtw
# c_user 100069061833988