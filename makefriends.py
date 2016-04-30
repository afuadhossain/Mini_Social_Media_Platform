#!/usr/bin/env python

import cgi, cgitb

form = cgi.FieldStorage()
username = form.getvalue('username')

print "Content-type:text/html\n\n"
print "<html><head><title>Adding friends</title>"
print """
<link rel="stylesheet" type="text/css" href="../ass4/style.css">
<title> Add Friends </title>
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
print '<form action="newfriends.py" method="post">'
print """
<table cellspacing="15">
<tr>
    <td></td>
    <td><b>USERNAME</b></td>
    <td><b>NAME</b></td>
</tr>
<tr> """
with open('../ass4/users.txt','r') as f:
    count = 0
    for line in f:
        temp = line.rstrip('\n')
        count+=1
        if count%4 == 1:
            print '<td><input type="checkbox" name="addfriend" value="'+temp+'"></td>'
        if count%2 == 1:
            print '<td>'+temp+'</td>'
        if count%4 == 3:
            print "</tr><tr>"
print '</tr></table>'
print '<input type="hidden" name="username" value="%s">' % username
print '<input type="submit" value="Submit">'
print "</form>"
print "</body>"
print "</html>"
