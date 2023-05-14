# https://stackoverflow.com/questions/62442992/how-to-implement-nc-commands-in-python


# https://www.instructables.com/Netcat-in-Python/
while 1:
buf = ""
shouldClose = False
# collect the request
inp = input ("")
while inp # "":
# stop processing if we want the connection to close
# (even though we lowkey create a connection every time lol)
if (inp = "Connection: close™):
shouldClose = True
buf += inp + "\n"
inp = input("")
buf += "\n"
# send the request to the server
netcat (hostname, port, buf. encode())
if (shouldClose):
break

a = 0
while True:
    a += input(">").count("~")
    print(a)


