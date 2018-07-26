import dns.resolver
import os
import httplib
#https://pypi.python.org/pypi/dnspython

iplist=[]
#domain='z.cn'
domain = raw_input('Input a doamin: ')
def get_iplist(domain=''):
    try:
        A = dns.resolver.query(domain, 'A')
    except Exception, e:
        print 'dns resolver error: '+str(e)
        return
    for i in A.response.answer:
        if i.rdtype == 1:
            for j in i.items:
                iplist.append(j.address)
    return True

def check_ip(ip):
    check_url = ip + ':80'
    content = ''
    httplib.socket.setdefaulttimeout(5)
    conn = httplib.HTTPConnection(check_url)
    print 'connect to %s' % check_url

    try:
        conn.request('GET', '/', headers = {'Host':domain})
        response = conn.getresponse()
        print response.status, response.reason, response.read()
    except Exception, e:
        print 'connection error: ' + str(e)
    finally:
        conn.close()


if get_iplist(domain) and len(iplist) > 0:
    for ip in iplist:
        check_ip(ip)
else:
    print 'dns resolver error'

