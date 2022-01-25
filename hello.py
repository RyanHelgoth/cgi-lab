#!/usr/bin/env python3
import os
import json 


env = os.environ

#Plain text
#print("Content-Type: text/plain\r\n")
#print(env)

#JSON
#print("Content-Type: application/json\r\n")
#print(json.dumps(dict(env), indent=2))

#Query
#print("Content-Type: text/html\r\n")
#print("<p>QUERY_STRING={}</p>".format(env["QUERY_STRING"]))

#Browser info
print("Content-Type: text/html\r\n")
print("<p>HTTP_USER_AGENT={}".format(env["HTTP_USER_AGENT"]))