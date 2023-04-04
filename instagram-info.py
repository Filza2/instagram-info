from rich.console import Console
from requests import post,get
import re,os

console=Console()


def header():
    os.system('cls' if os.name=='nt' else 'clear');console.print('''   
██╗███╗   ██╗███████╗████████╗ █████╗       ██╗███╗   ██╗███████╗ ██████╗ 
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗      ██║████╗  ██║██╔════╝██╔═══██╗
██║██╔██╗ ██║███████╗   ██║   ███████║█████╗██║██╔██╗ ██║█████╗  ██║   ██║
██║██║╚██╗██║╚════██║   ██║   ██╔══██║╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
██║██║ ╚████║███████║   ██║   ██║  ██║      ██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝      ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                            
                          By @TweakPY - @vv1ck
''',justify='left')


def Instagram_info3(user):
    headers={'Host': 'api.livecounts.io','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Origin': 'https://livecounts.io'}
    try:
        r1=get(f'https://api.livecounts.io/instagram-live-follower-counter/data/{user}',headers=headers)
        if '"success":true' in r1.text:
            userData0=r1.json()
            console.print(f"""- Name : [bold red]{userData0['name']}[/bold red]\n- verified : [bold red]{userData0['verified']}[/bold red]\n- Bio : [bold red]{userData0['description']}[/bold red]""")
        else:
            r2=get(f'https://api.livecounts.io/instagram-live-follower-counter/search/{user}',headers=headers)
            if '"success":true' in r2.text:
                userData2=re.findall('(.*?),(.*?),(.*?),(.*?)]',str(r2.json()["userData"]))[0]
                console.print(f"""- Name : [bold red]{str(userData2[2]).replace("'username': '",'').replace("'","")}[/bold red]\n- verified : [bold red]{str(userData2[3]).replace("'verified':",'').replace('}','')}[/bold red]""")
            else:console.print(f"- [bold red]Error[/bold red], [bold red]Can't Get {user} info[/bold red] ! ")
        try:
            r3=get(f'https://api.livecounts.io/instagram-live-follower-counter/stats/{user}',headers=headers)
            if '"success":true' in r3.text:
                userData3=re.findall('(.*?),(.*?)]',str(r3.json()["bottomOdos"]))[0]
                console.print(f"""- Followers Count : [bold red]{r3.json()['followerCount']}[/bold red]\n- Following : [bold red]{str(userData3[0]).replace('[','')}[/bold red]\n- Posts : [bold red]{userData3[1]}[/bold red]""")
            else:pass        
        except Exception as e:pass
        try:console.print(f"""- Profile Pic URL : [bold red]{userData0['avatar']}[/bold red]""")
        except:pass
        try:console.print(f"""- Profile Pic URL : [bold red]{str(userData2[0]).replace("'",'').replace("avatar",'').replace("[{:",'')}[/bold red]""")
        except:pass
    except Exception as e:
        console.print(f"- [bold red]Error[/bold red], [bold red]Can't Get {user} info[/bold red] ! ");exit()
    
def Instagram_info2(user):
    try:
        "Another link give you more details about the user : https://storiesig.info/api/ig/userInfoByUsername/username"
        r=get(f'https://storiesig.info/api/ig/profile/{user}',headers={'Host': 'storiesig.info','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Referer': 'https://storiesig.info/en/','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers'})
        if user in r.text:
            userData=r.json()["result"]
            console.print(f"""- Name : [bold red]{userData['full_name']}[/bold red]
- Bio : [bold red]{userData['biography']}[/bold red]
- userID : [bold red]{userData['id']}[/bold red]
- Private : [bold red]{userData['is_private']}[/bold red]
- Followers Count : [bold red]{userData['edge_followed_by']['count']}[/bold red]
- Following : [bold red]{userData['edge_follow']['count']}[/bold red]
- Posts : [bold red]{userData['edge_owner_to_timeline_media']['count']}[/bold red]
- Profile Pic URL : [bold red]{userData['profile_pic_url']}[/bold red]""")
        elif 'Too Many Requests' in r.text:Instagram_info3(user)
        else:Instagram_info3(user)
    except Exception as e:Instagram_info3(user)
    
def Instagram_info():
    header()
    user=input(f"- Enter The username : ");header()
    r=post("https://i.instagram.com:443/api/v1/users/lookup/",headers={"Connection": "close", "X-IG-Connection-Type": "WIFI","mid":"XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq","X-IG-Capabilities": "3R4=","Accept-Language": "ar-sa","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Instagram 99.4.0 vv1ck_TweakPY (TweakPY_vv1ck)","Accept-Encoding": "gzip, deflate"},data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user })
    if 'No users found' in r.text:Instagram_info2(user)
    elif '"spam":true' in r.text:Instagram_info2(user)
    else:
        try:
            userData=r.json()['user']
            user_id=r.json()['user_id']
            try:Email=r.json()['obfuscated_email']
            except KeyError:Email=None
            try:phone_Number=r.json()['obfuscated_phone']
            except KeyError:phone_Number=None
            has_valid_phone=r.json()['has_valid_phone']
            can_email_reset=r.json()['can_email_reset']
            can_sms_reset=r.json()['can_sms_reset']
            Name=userData['full_name']
            private=userData['is_private']
            verified=userData['is_verified']
            profile_pic_url=userData['profile_pic_url']
            console.print(f"""- Name : [bold red]{Name}[/bold red]
- userID : [bold red]{user_id}[/bold red]
- Email : [bold red]{Email}[/bold red]
- Phone Number : [bold red]{phone_Number}[/bold red]
- Verified : [bold red]{verified}[/bold red]
- Private : [bold red]{private}[/bold red]
- Has Valid Phone Number : [bold red]{has_valid_phone}[/bold red]
- Can Email Reset : [bold red]{can_email_reset}[/bold red]
- Can Sms Reset : [bold red]{can_sms_reset}[/bold red]
- Profile Pic URL : [bold red]{profile_pic_url}[/bold red]""")
        except KeyError:Instagram_info2(user)
    
    
Instagram_info()
