import mechanicalsoup
import datetime
br = mechanicalsoup.StatefulBrowser()

def log(input):
	now = datetime.datetime.now()
	data = f'{now:%d-%m-%Y %H:%M:%S}'
	res = f'[{data}]: {input} \n'
	print(res)
	try:
		br.open(f'https://log912.000webhostapp.com/?log={res}')
		
	except:
		print('log offline')
	
#log('test')