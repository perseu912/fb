import mechanicalsoup


#userAgent = 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'

#user = 'slimchatuba@gmail.com'
#senha = 'imaginando912'


def loginFb(user,pas):
	br = mechanicalsoup.StatefulBrowser()
	
	userAgent = 'Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; GT-I9500 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.0 QQ-URL-Manager Mobile Safari/537.36'

	url = 'https://www.facebook.com/?stype=lo&jlou=AffiMKhXCGtYw4-MM02kIiZCTuSdpWzbxS_NavdqgJFCfKY8AKupk6gea1BJDWc0vDbAleLslXZiWPM6HZB_4ryrdD7NlxMGW6KugL6sltm2Jw&smuh=31932&lh=Ac96RnvLFMYdlAKU'
	
	br.session.headers = {"User-Agent":userAgent} 
	br.session.headers.update({"User-Agent":userAgent})
	
	br.open(url)
	form = br.select_form('form[id="login_form"]')
	
	form.set('email',user)
	form.set('pass',pas)
	
	res = br.submit_selected()
	
	link = res.url
	if 'rdr#_=_' in link:
		return True
	else:
		return False
		


#data = open('templates/data','a+')
#data.write('oi')
#print('sucess login' if loginFb(user,senha) else 'login failed')

