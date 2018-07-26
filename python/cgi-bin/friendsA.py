#!/usr/bin/env python
import cgi
reshtml = '''Content-Type: text/html\n
<HTML><HEAD><TITLE>
Friends CGI Demo(dynamic screen)
</TITLE></HEAD>
<BODY><H3>Frieds list for:<I>%s</I></H3>
Your name is : <B>%s</B><P>
You have <B>%s</B> fridens.
</BODY></HTML>'''

form = cgi.FieldStorage()
who = form['person'].value
howmany = form['howmany'].value
print reshtml % (who,who,howmany)
