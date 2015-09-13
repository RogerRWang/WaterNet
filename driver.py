from firebase import Firebase
from firebase_token_generator import create_token
import threading
from math import *
import datetime
import time
import requests
import urllib2 import Request, urlopen, URLError
import pyowm

def timerLoop(prevMinute):
	
	curr_sched = f.get('curr_sched')
	timers = f.get('/schedules', curr_sched)
	currTime = datetime.datetime.now()
	dOfWeek = date.today().weekday()
	currHour = datetime.datetime.now().hour
	currMinute = datetime.datetime.now().minute
	
	if currMinute != prevMinute:
		prevMinute = currMinute
		for block in timers:
			
			if block["start_stop_posix"][1] < time.mktime(currTime.timetuple()):
				f.delete('block')

			elif block["start_stop_posix"][0] > time.mktime(currTime.timetuple()):
			
			elif block["days"]==dOfWeek
				
				times = block["times"]
				
				for eachTime in times:
					
					hour = eachTime[0:1]
					minute = eachTime[2:3]
					
					if hour = currHour && minute = currMinute:

						curr_temp = f.get('curr_temp')
						curr_humidity = f.get('curr_humidity')
						duration_on = block["duration"]["time_sec"]
						(hot, rain) = weatherGet()
						
						if not ((hot and block["dnr-if"]["hot_days"]) or (rain and block["dnr-if"]["rain_days"]))

							if curr_temp < block["duration"]["temp_range_F"][0]:
								duration_on = duration_on * (1-block["duration"]["cold_percent"])
							elif curr_temp > ["duration"]["temp_range_F"][1]:
								duration_on = duration_on * (1+block["duration"]["hot_percent"])

							if block["frequency"] is None:
								t = Thread(target = oneTimeOn, args=(duration_on,))
							else:
								t = Thread(target = freqOn, args=(duration_on, block["frequency"]["every_min"], block["frequency"]["repeat_length_min"]))

def oneTimeOn(duration):
	payload = "on"
	r = requests.post("https://api.particle.io/v1/devices/54ff6a066672524819361267/led?access_token=22de5c62f0253e4cabad74d98664301dabaa4859", params = payload)
	time.sleep(duration)
	payload = "off"
	r = requests.post("https://api.particle.io/v1/devices/54ff6a066672524819361267/led?access_token=22de5c62f0253e4cabad74d98664301dabaa4859", params = payload)
 

def freqOn (duration, min_repeat, repeatLength_min):
	first_sec = time.clock()
	while (time.clock() < first_sec + 60* repeatLength_min):
		payload = "on"
		r = requests.post("https://api.particle.io/v1/devices/54ff6a066672524819361267/led?access_token=22de5c62f0253e4cabad74d98664301dabaa4859", params = payload)
		time.sleep(duration)
		payload = "off"
		r = requests.post("https://api.particle.io/v1/devices/54ff6a066672524819361267/led?access_token=22de5c62f0253e4cabad74d98664301dabaa4859", params = payload)
 		time.sleep(min_repeat*60 - duration)

def weatherGet():
	curr_IP = f.get('curr_IP')
	requestURL_IP = 'http://www.telize.com/geoip' + curr_IP
	request_IP = Request(requestURL_IP)
	response_IP = urlopen(request_IP)
	out_IP = response_IP.read()
	postal_code = out_IP["postal_code"]
	lat = out_IP["latitude"]
	lon = out_IP["longitude"]

	ref = owm.weather_at_coords(lat, lon)
	weather = ref.get_weather()
	temp = weather.get_temperature('fahrenheit')['temp']
	humidity = weather.get_humidity()
	heatIndex = getHeatIndex(humidity, temp)
	hot = heatIndex > 100
	rain = weather.get_weather_code() < 623 and weather.get_weather_code() > 199
return (hot, rain)



def getHeatIndex(hum, temp):
	c1 = 42.379
	c2 = 2.04901523
	c3 = 10.14333127
	c4 = -0.22475541
	c5 = -6.83783*10**(-3)
	c6 = -5.481717*10**(-2)
	c7 = 1.22874*10**(-3)
	c8 = 8.5282*10**(-4)
	c9 = -1.99*10**(-6)

	HI = c1 + c2*temp + c3*hum + c4*temp*hum + c5*T**2 + c6*hum**2 + c7*temp**(2) * hum + c8*temp*hum**2 + c9*T**(2)*hum**2
return HI


auth_payload = { "uid": "uniqueId1", "auth_data": "foo", "other_auth_data": "bar" }
token = create_token("1yh4UVShYCta7gulWb7WZRQFgKldrPVrWny65nRk", auth_payload)


f = Firebase('https://mhacks6.firebaseio.com')
owm = pyowm.OWM('c4d5dbe30706aa6f0e2d801f34262376')

while(True):
	running = Thread(target = timerLoop, args=(-1,))
	weatherT = Thread(target = weatherGet, args = (,))