#!/usr/bin/env python

import cgi, cgitb; cgitb.enable()

print "Content-type:text/html\n\n"

form = cgi.FieldStorage()
# saving username
username = form.getvalue('username')

print """
<html>
<head>
<link rel="stylesheet" type="text/css" href="http://cs.mcgill.ca/~hlee168/ass4/style.css">
<title> {0}'s Dashboard </title>
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
<form action="http://cs.mcgill.ca/~mrosen51/ass4/status.py" method="post">
<input type="text" name="status" placeholder="Spit some fire, homie." maxlength="140">
<input type="hidden" name="username" value="{0}">
<input type="submit" value="Update status">
</form>
<p>Fellow rapper status updates</p>
""".format(username)

with open("/home/2015/hlee168/public_html/ass4/friends.txt","r") as f:
    for line in f:
        line = line.rstrip()
        if(line.startswith(username)):
            friendlist = line.split(' ')
            statuscounter = 0
            with open("/home/2015/hlee168/public_html/ass4/status.txt","r") as f2:
                for line in f2:
                    if line.split(' ')[0] in friendlist:
                        parsedline = "<b>"+line.split(' ')[0]+": </b>"+' '.join(line.split(' ')[1:]);
                        print parsedline+"<br>"
                        statuscounter+=1
                    if statuscounter==20:
                        break

print """
</body>
</html>
"""
