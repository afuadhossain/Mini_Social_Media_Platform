#!/usr/bin/env python

import cgi, cgitb; cgitb.enable()
import sys

print "Content-type:text/html\n\n"

form = cgi.FieldStorage()
friend = form.getvalue("friend")
username = form.getvalue("username")

print """
<html>
<head>
<link rel="stylesheet" type="text/css" href="../ass4/style.css">
<title>View Profile</title>
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

if friend == None:
    print """
    Please choose a friend before pressing the See Profile button. <br>
    <form action="./seefriends.cgi" method="post">
        <input type="hidden" name="username" value="%s">
        <input type="submit" value="Click here to return to see a friend page.">
    </form>
    </body>
    </html> """ % username
    sys.exit(0)

with open("../ass4/users.txt","r") as f:
    lines = f.readlines()
    for i in range(0,len(lines)):
        if lines[i].startswith(friend) and i%4==0:
            print "<b>Username:</b> %s<br>" % lines[i]
            print "<b>Full Name:</b> %s<br>" % lines[i+2]
            print "<b>Job Description:</b> %s<br>" % lines[i+3]
            break

print """
<form action="./seefriends.cgi" method="post">
    <input type="hidden" name="username" value="%s">
    <input type="submit" value="Click here to return to see a friend page.">
</form>
<form action="http://cs.mcgill.ca/~mrosen51/ass4/dashboard.py" method="post">
    <input type="hidden" name="username" value="%s">
    <input type="submit" value="Click here to return to the dashboard.">
</form>
</body>
</html>""" % (username,username)
