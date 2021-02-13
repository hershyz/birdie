import commands
import os
import sys
import store
import send

commands.add("help", "", "shows all commands")
commands.add("store", "address, name", "stores sponsors (separated by comma)")
commands.add("sendall", "", "sends email template to all recipients")
commands.add("send", "name", "sends email to a specific recipient")
commands.add("bcc", "", "sends a bcc email to all participants in the store file")

args = sys.argv
if len(args) < 2:
    commands.show()
    exit()

c = args[1].lower()

if c == "help":
    commands.show()

if c == "store":
    address = args[2]
    name = ""
    i = 3
    while i < len(args):
        name += args[i] + " "
        i+=1
    store.addSponsor(address, name)

if c == "send":
    send.sendSingle(args[2])

if c == "sendall":
    send.sendAll()

if c == "bcc":

    f = open("store.txt", "r")
    emails = []
    for x in f:
        line = x.replace("\n", "")
        email = line.split(", ")[0]
        emails.append(email)

    spliced = ""
    for x in emails:
        spliced += x + ","
    send.deliverBcc(spliced)
