from firebase import Firebase

f = Firebase('https://mhacks6.firebaseio.com')
print f.child('profiles').child('0').child('blocks').get()