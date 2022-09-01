try:from colorama import Fore;from requests import post
except ModuleNotFoundError:exit('[!] Download The Missing Module !')
def IN1():
    user=input(f"\n[{Fore.RED}?{Fore.RESET}] username : ")
    r1=post("https://i.instagram.com:443/api/v1/users/lookup/",headers={"Connection": "close", "X-IG-Connection-Type": "WIFI","mid":"XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq","X-IG-Capabilities": "3R4=","Accept-Language": "ar-sa","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Instagram 99.4.0 vv1ck_TweakPY (TweakPY_vv1ck)","Accept-Encoding": "gzip, deflate"},data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user });inf=r1.json()
    print("-------------------------------------")
    try:print(f"[{Fore.RED}+{Fore.RESET}] Name : ",inf['user']['full_name'])
    except:print(f"[{Fore.RED}+{Fore.RESET}] Name : Null")
    try:print(f"[{Fore.RED}+{Fore.RESET}] User ID : ",inf['user_id'])
    except:print(f"[{Fore.RED}+{Fore.RESET}] User ID : Null")
    try:print(f"[{Fore.RED}+{Fore.RESET}] Email : ",inf['obfuscated_email'])
    except:print(f"[{Fore.RED}+{Fore.RESET}] Email : Null")
    try:print(f"[{Fore.RED}+{Fore.RESET}] Phone : ",inf['obfuscated_phone'])
    except:print(f"[{Fore.RED}+{Fore.RESET}] Phone : Null")
    try:print(f"[{Fore.RED}+{Fore.RESET}] Private : ",inf['user']['is_private'])
    except:print(f"[{Fore.RED}+{Fore.RESET}] Private : Null")
    try:print(f"[{Fore.RED}+{Fore.RESET}] Verified : ",inf['user']['is_verified'])
    except:print(f"[{Fore.RED}+{Fore.RESET}] Verified : Null")
    try:print(f"[{Fore.RED}+{Fore.RESET}] Valid Phone : ",inf['has_valid_phone'])
    except:print(f"[{Fore.RED}+{Fore.RESET}] Valid Phone : Null")
    try:print(f"[{Fore.RED}+{Fore.RESET}] Email Reset : ",inf['can_email_reset'])
    except:print(f"[{Fore.RED}+{Fore.RESET}] Email Reset : Null")
    try:print(f"[{Fore.RED}+{Fore.RESET}] SMS Reset : ",inf['can_sms_reset'])
    except:print(f"[{Fore.RED}+{Fore.RESET}] SMS Reset : Null")
    try:
        print("-------------------------------------")
        print(f"[{Fore.RED}+{Fore.RESET}] profile pic id :",inf['user']['profile_pic_id'])
        print(f"[{Fore.RED}+{Fore.RESET}] profile pic url:",inf['user']['profile_pic_url'])
        print("-------------------------------------")
    except:pass
print('''   
██╗ ██████╗       ███╗   ██╗███████╗
██║██╔════╝       ████╗  ██║██╔════╝
██║██║  ███╗█████╗██╔██╗ ██║█████╗  
██║██║   ██║╚════╝██║╚██╗██║██╔══╝  
██║╚██████╔╝      ██║ ╚████║██║     
╚═╝ ╚═════╝       ╚═╝  ╚═══╝╚═╝                                                                  
   By @TweakPY - @vv1ck''');IN1()
