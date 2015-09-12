from firebase import Firebase
from firebase_token_generator import create_token
import threading
from math import *
import datetime

class TimerWorkerThread (threading.Thread):
	def __init__(self, arg):
		super(TimerWorkerThread, self).__init__()
		self.event_loop = TimerEventLoop(arg)

	def run(self):
		self.event_loop.start()

class TimerEventLoop():

	def __init__(self, arg):
		super(TimerEventLoop, self).__init__(arg)
		self.deployed = False

	def 

def timerLoop(prevMinute):
	curr_sched = f.get('curr_sched')
	timers = f.get('/schedules', curr_sched)
	dOfWeek = date.today().weekday()
	currHour = datetime.now().hour
	currMinute = datetime.now().minute
	if currMinute != prevMinute:
		prevMinute = currMinute
		for block in timers:
			if block["days"]==dOfWeek
				times = block["times"]
				for eachTime in times:
					hour = eachTime[0:1]
					minute = eachTime[2:3]
					if hour = currHour && minute = currMinute:
						



auth_payload = { "uid": "uniqueId1", "auth_data": "foo", "other_auth_data": "bar" }
token = create_token("1yh4UVShYCta7gulWb7WZRQFgKldrPVrWny65nRk", auth_payload)


f = Firebase('https://mhacks6.firebaseio.com')
schedules = f.get('/schedules')
for schedule in schedules:

