#!/usr/bin/env python

import cgi, cgitb; cgitb.enable()
import sys

form = cgi.FieldStorage()
names = form.getlist("addfriend")
for name in names:
    name = name.rstrip()
username = form.getvalue('username')

print "Content-type:text/html\n\n"
print """
<html>
<head>
<link rel="stylesheet" type="text/css" href="../ass4/style.css">
<title>Making friends</title>
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

with open("../ass4/friends.txt",'r+') as f:
    lines = f.readlines()
    for i,line in enumerate(lines):
        if(line.startswith(username)):
            for friend in names:
                if friend not in line:
                    lines[i] = lines[i].rstrip()
                    lines[i] = lines[i]+' '+friend+"\n"
    f.seek(0)
    for line in lines:
        f.write(line)

print 'Friends list has been updated. Please use the menu above to navigate back to the dashboard.'
print "</body>"
print "</html>"
