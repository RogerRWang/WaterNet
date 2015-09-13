from firebase import Firebase
from firebase_token_generator import create_token
from threading import Thread
from math import *
import datetime
import time
import requests
import json
from urllib2 import Request, urlopen, URLError
import pyowm

def timerLoop(prevMinute):

	curr_sched = f.child('curr_sched').get() #gets which schedule is current
	profiles = f.child('profiles').get() #gets the array containing all profiles
	curr_profile_path = f.child('profiles').child(str(curr_sched))
	curr_profile = curr_profile_path.get() #the JSON object within the array of profiles that is actually the specific profile you wanted. 
	currTime = datetime.datetime.now()
	dOfWeek = datetime.datetime.now().weekday()
	currHour = datetime.datetime.now().hour
	currMinute = datetime.datetime.now().minute


	blocks_path = curr_profile_path.child('blocks')
	blocks = blocks_path.get()
	if blocks:
		for index, block in enumerate(blocks):
			if block["start_stop_posix"][1] < time.mktime(currTime.timetuple()):
				array1 = blocks[:index]
				if (len(blocks) > 1):
					array2 = blocks[index+1 :]
					blocks_path.set(array1 + array2)
				else:
					blocks_path.set(array1)

			elif dOfWeek in block["days"] and not (block["start_stop_posix"][0] > time.mktime(currTime.timetuple())):
	
	if currMinute != prevMinute:
		prevMinute = currMinute
		blocks_path = curr_profile_path.child('blocks')
		blocks = blocks_path.get()
		for index, block in enumerate(blocks):
			
			if block["start_stop_posix"][1] < time.mktime(currTime.timetuple()):
				blocks_path.child(str(index)).delete()
			elif block["days"]==dOfWeek and not (block["start_stop_posix"][0] > time.mktime(currTime.timetuple())):
				
				times = block["times"]
				
				for eachTime in times:
					hour = int(eachTime[0:2])
					minute = int(eachTime[2:4])
					if hour == currHour and minute == currMinute:
						curr_temp = f.child('curr_temp').get()
						curr_humidity = f.child('curr_humidity').get()
						duration_on = block["duration"]["time_sec"]
						#(hot, rain) = weatherGet()
					hour = eachTime[0:1]
					minute = eachTime[2:3]
					
					if hour == currHour and minute == currMinute:

						curr_temp = f.get('curr_temp')
						curr_humidity = f.get('curr_humidity')
						duration_on = block["duration"]["time_sec"]
						(hot, rain) = weatherGet()
						
>>>>>>> e7db469decb47680760a096c9ed535cf6d02957d
						if not ((hot and block["dnr-if"]["hot_days"]) or (rain and block["dnr-if"]["rain_days"])):

							if curr_temp < block["duration"]["temp_range_F"][0]:
								duration_on = duration_on * (1-block["duration"]["cold_percent"])
<<<<<<< HEAD
							elif curr_temp > block["duration"]["temp_range_F"][1]:
								duration_on = duration_on * (1+block["duration"]["hot_percent"])

							if block["frequency"] is None:
								tnof = Thread(target = oneTimeOn, args=(duration_on,))
								tnof.start()
							else:
								tf = Thread(target = freqOn, args=(duration_on, block["frequency"]["every_min"], block["frequency"]["repeat_length_min"]))
								tf.start()

	time.sleep(60)
=======
							elif curr_temp > ["duration"]["temp_range_F"][1]:
								duration_on = duration_on * (1+block["duration"]["hot_percent"])

							if block["frequency"] is None:
								t = Thread(target = oneTimeOn, args=(duration_on,))
							else:
								t = Thread(target = freqOn, args=(duration_on, block["frequency"]["every_min"], block["frequency"]["repeat_length_min"]))
>>>>>>> e7db469decb47680760a096c9ed535cf6d02957d

def oneTimeOn(duration):
	payload = "on"
	r = requests.post("https://api.particle.io/v1/devices/54ff6a066672524819361267/led?access_token=22de5c62f0253e4cabad74d98664301dabaa4859", params = payload)
	print(duration)
	time.sleep(duration)
	payload = "off"
	r = requests.post("https://api.particle.io/v1/devices/54ff6a066672524819361267/led?access_token=22de5c62f0253e4cabad74d98664301dabaa4859", params = payload)
 

def freqOn (duration, min_repeat, repeatLength_min):
	first_sec = time.clock()
	while (time.clock() < first_sec + 60* repeatLength_min):
		payload = "on"
		r = requests.post("https://api.particle.io/v1/devices/54ff6a066672524819361267/led?access_token=22de5c62f0253e4cabad74d98664301dabaa4859", params = payload)
		print(duration)
		time.sleep(duration)
		payload = "off"
		r = requests.post("https://api.particle.io/v1/devices/54ff6a066672524819361267/led?access_token=22de5c62f0253e4cabad74d98664301dabaa4859", params = payload)
 		time.sleep(min_repeat*60 - duration)

def weatherGet():
	curr_IP = f.child('curr_IP').get()
	requestURL_IP = 'http://www.telize.com/geoip/' + curr_IP
	request_IP = Request(requestURL_IP)
	response_IP = urlopen(request_IP)
	out_IP = json.loads(response_IP.read())
	lat = out_IP["latitude"]
	lon = out_IP["longitude"]

	first_sec = time.clock()
	if (time.clock() > first_sec + 24*60*60):
		first_sec = time.clock()	
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

	HI = c1 + c2*temp + c3*hum + c4*temp*hum + c5*temp**2 + c6*hum**2 + c7*temp**(2) * hum + c8*temp*hum**2 + c9*temp**(2)*hum**2
	return HI


auth_payload = { "uid": "uniqueId1", "auth_data": "foo", "other_auth_data": "bar" }
token = create_token("1yh4UVShYCta7gulWb7WZRQFgKldrPVrWny65nRk", auth_payload)


f = Firebase('https://mhacks6.firebaseio.com')
owm = pyowm.OWM('fb55216966c6d7b8a71ec1d3ad85e0c0')

while(True):
	running = Thread(target = timerLoop, args=(-1,))
	weatherT = Thread(target = weatherGet)
	running.start()
	weatherT.start()
