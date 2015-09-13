from firebase import Firebase
import urllib2, urllib
url_2 = 'https://api.particle.io/v1/devices/54ff6a066672524819361267/led?access_token=22de5c62f0253e4cabad74d98664301dabaa4859'
values = dict(args='off')
data = urllib.urlencode(values)
req = urllib2.Request(url_2, data)
rsp = urllib2.urlopen(req)
content = rsp.read()
