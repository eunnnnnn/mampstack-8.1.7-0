#!/usr/local/bin/python3
print("Content-Type: text/html")
print()
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value
print('''<!DOCTYPE html>
<html>
<head>
    <title>WEB1 - Welcome</title>
    <meta charset="utf-8">
</head>
<body>
    <h1><a href="index.py">WEB</font></a></h1>
    <ol>
        <li><a href="index.py?id=HTML">HTML</font></a></li>
        <li><a href="index.py?id=CSS">CSS</font></a></li>
        <li><a href="index.py?id=JavaScript">JavaScript</font></a></li>
    </ol>
    <h2>{title}</h2>
    The World Wide Web (WWW), commonly known as the Web, is an information system enabling documents and other web resources to be accessed over the Internet.[1]Documents and downloadable media are made available to the network through web servers and can be accessed by programs such as web browsers. Servers and resources on the World Wide Web are identified and located through character strings called uniform resource locators (URLs). The original and still very common document type is a web page formatted in Hypertext Markup Language (HTML). This markup language supports plain text, images, embedded video and audio contents, and scripts (short programs) that implement complex user interaction. The HTML language also supports hyperlinks (embedded URLs) which provide immediate access to other web resources. Web navigation, or web surfing, is the common practice of following such hyperlinks across multiple websites. Web applications are web pages that function as application software. The information in the Web is transferred across the Internet using the Hypertext Transfer Protocol (HTTP).
</body>
</html>
'''.format(title=pageId))
