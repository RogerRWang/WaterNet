from firebase import Firebase

f = Firebase('https://mhacks6.firebaseio.com')
curr_sched = f.child('curr_sched').get()
print curr_sched
print f.child('profiles').child(str(curr_sched)).child('blocks').get()