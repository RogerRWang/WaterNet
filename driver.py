from firebase import Firebase
from firebase_token_generator import create_token
import threading
from math import *
import datetime

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
						if curr_temp < block["duration"]["temp_range_F"][0]:
							duration_on = duration_on * (1-block["duration"]["cold_percent"])
						elif curr_temp > ["duration"]["temp_range_F"][1]:
							duration_on = duration_on * (1+block["duration"]["hot_percent"])
						if block["frequency"] is None:
							t = Thread(target = oneTimeOn, args=(duration_on,))
						else:
							t = Thread(target = freqOn, args=(duration_on, block["frequency"]["every_min"], block["frequency"]["repeat_length_min"]))

def oneTimeOn(duration):


def freqOn (duration, min_repeat, repeatLength_min):



auth_payload = { "uid": "uniqueId1", "auth_data": "foo", "other_auth_data": "bar" }
token = create_token("1yh4UVShYCta7gulWb7WZRQFgKldrPVrWny65nRk", auth_payload)


f = Firebase('https://mhacks6.firebaseio.com')

