import requests 
import time
from tqdm import tqdm
from googlesearch import search 

with open('msn.txt', 'r') as f:
    heds = [line.strip() for line in f]
urlmsn = ""
output = ""
count = 0
total = len(heds)
print total
for hed in tqdm(heds):
	#count = count + 1
	#hed = str(heds.pop(0)).strip() + " MSN"
	#print hed
	first = True
	for url in search(hed, tld="com", num=10, start=0, stop=1):
		#print url
		if first:
			#print "turd"
			first = False
			urlmsn = url
		else:
			continue
			#print urlmsn	
		
	#print urlmsn
	try:
		r = requests.get(urlmsn)
		auth = r.text.encode('utf-8').strip()
		if '<meta property="author" content="' in auth:
			auth = auth[auth.find('<meta property="author" content="')+33:]
		elif '<span class="auth">' in auth:
			auth = auth[auth.find('<span class="auth">')+22:]
			auth = auth[:auth.find("<")].strip()
		elif '"author":"' in auth:
			auth = auth[auth.find('"author":"')+10:]
			auth = auth[:auth.find('"')]
		elif '<span class="truncate" >' in auth:
			auth = auth[auth.find('<span class="truncate" >')+24:]
			auth = auth[:auth.find("<")].strip()	
		else:	
			auth = ""
	except:
		auth = ""		
	if len(auth)>200:
		auth = ""
		output = output + '"'+hed+'",'+auth+"\n"
	else:
		output = output + '"'+hed+'",'+auth+"\n"
	
outfile = "msnauthors_" + time.strftime("%Y-%m-%d-%H-%M") +".txt"
o = open(outfile,"w")
o.write(output)
o.close()
