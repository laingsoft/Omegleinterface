import urllib2 as url
import urllib
import httplib as http
f = open('script.txt','r')
def fmtId( string ):
    return string[1:len( string ) - 1]

def talk(id,req,messagestr):
    print messagestr
    msgReq = url.urlopen('http://omegle.com/send', '&msg='+messagestr+'&id='+id)
    msgReq.close()

def listenserv(id,req):
    while True:
        site = url.urlopen(req)
        rec = site.read()
        if 'waiting' in rec:
            print 'waiting'
        elif 'connected' in rec: 
            print 'Got one!'
            talk(id,req,(f.read()))
        elif 'strangerDisconnected' in rec:
            print 'He left, What an *explative deleted*.'
            connect()
        elif 'typing' in rec:
            print 'he is typing..'
        elif 'gotMessage' in rec:
            user = rec[16:len( rec ) - 2]
            print(user)
            talk(id,req,(f.read()))
def connect():
    site = url.urlopen('http://omegle.com/start','')
    id = fmtId( site.read() )
    print(id)
    req = url.Request('http://omegle.com/events', urllib.urlencode( {'id':id}))
    listenserv(id,req)
connect()