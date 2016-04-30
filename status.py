#!/usr/bin/env python

import cgi, cgitb; cgitb.enable()
import sys

print "Content-type:text/html\n\n"

form = cgi.FieldStorage()
status = form.getvalue('status')
username = form.getvalue('username')
if status:
    status = status.rstrip()
print """
<html>
<head>
<link rel="stylesheet" type="text/css" href="http://cs.mcgill.ca/~hlee168/ass4/style.css">
<title> Status Update </title>
</head>
<body>

<div id='cssmenu'>
<ul>
  <li>
    <form action="http://cs.mcgill.ca/~mrosen51/ass4/dashboard.py" method="post">
      <a href="javascript:;" onclick="parentNode.submit();">Dashboard</a>
      <input type="hidden" name="username" value="{0}">
    </form>
  </li>
  <li>
    <form action="http://cs.mcgill.ca/~hlee168/cgi-bin/makefriends.py" method="post">
      <a href="javascript:;" onclick="parentNode.submit();">Add friends</a>
      <input type="hidden" name="username" value="{0}">
    </form>
  </li>
  <li>
    <form action="http://cs.mcgill.ca/~hlee168/cgi-bin/seefriends.cgi" method="post">
      <a href="javascript:;" onclick="parentNode.submit();">See Friends</a>
      <input type="hidden" name="username" value="{0}">
    </form>
  </li>
    <li>
      <form>
        <a href="http://cs.mcgill.ca/~ahossa6/ass4/welcome.html">Logout</a>
      </form>
    </li>
</ul>
</div>

<hr>
""".format(username)

if not status:
    print """
    Please enter a status before attempting to submit it. Empty statuses are not accepted! (This includes whitespace-only statuses.)<br>
    Please use the menu above to navigate back to your dashboard.
    </form>
    </body>
    </html> """
    sys.exit(0)

f = open('/home/2015/hlee168/public_html/ass4/status.txt','r')
text = f.read()
f.close()

f = open('/home/2015/hlee168/public_html/ass4/status.txt', 'w')
f.write(username + " " + status + "\n");
f.write(text)
f.close()

print """
<script>setTimeout(function() { document.forms[0].submit() },2000);</script>
<body>
<form action="http://cs.mcgill.ca/~mrosen51/ass4/dashboard.py" method="post">
<input type="hidden" name="username" value="%s">
</form>
Status updated! Please wait while we redirect you back to your dashboard.
</body>
</html>""" % username
