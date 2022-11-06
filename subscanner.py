import requests

print(
"""
\u001b[31m
           _                                         
          | |                                        
 ___ _   _| |__  ___  ___ __ _ _ __  _ __   ___ _ __ 
/ __| | | | '_ \/ __|/ __/ _` | '_ \| '_ \ / _ \ '__|
\__ \ |_| | |_) \__ \ (_| (_| | | | | | | |  __/ |   
|___/\__,_|_.__/|___/\___\__,_|_| |_|_| |_|\___|_|   

\u001b[34m                                                  
=========================================================
"""
)
print(" this tool help to read the sub domain in ur web site")


def domain_scanner(domain_name,sub_domnames):
	for subdomain in sub_domnames:
		url = f"https://{subdomain}.{domain_name}"
		try:
			requests.get(url)
			print(f'[+] {url}')
		except requests.ConnectionError:
			pass

if __name__ == '__main__':
	dom_name = input("Enter the Domain Name:")
	with open('txt.txt','r') as file:
		name = file.read()
		sub_dom = name.splitlines()
	domain_scanner(dom_name,sub_dom)
	
