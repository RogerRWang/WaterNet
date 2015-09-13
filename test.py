from firebase import Firebase

f = Firebase('https://mhacks6.firebaseio.com')
#curr_sched = f.child('curr_sched').get()
direct = f.child('profiles').child('0').child('blocks').child('0').child('times').child('0')
direct.remove()
#print curr_sched
#print f.child('profiles').child(str(curr_sched)).child('blocks').get()