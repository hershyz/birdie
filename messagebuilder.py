def read():
    f = open("settings.ini", "r")
    lines = []
    lines = []
    for x in f:
        line = x.replace("\n", "")
        lines.append(line)
    return lines

def getSubject():
    lines = read()
    for i in range(len(lines)):
        _property = lines[i].split(": ")[0]
        value = lines[i].split(": ")[1]
        if _property.lower() == "subject":
            return value

def getSenderEmail():
    lines = read()
    for i in range(len(lines)):
        _property = lines[i].split(": ")[0]
        value = lines[i].split(": ")[1]
        if _property.lower() == "email":
            return value

def getPass():
    lines = read()
    for i in range(len(lines)):
        _property = lines[i].split(": ")[0]
        value = lines[i].split(": ")[1]
        if _property == "password":
            return value

def getTag():
    lines = read()
    for i in range(len(lines)):
        _property = lines[i].split(": ")[0]
        value = lines[i].split(": ")[1]
        if _property == "tag":
            return value

def buildMessage(nameParam):
    tag = "<" + getTag() + ">"
    templateFile = open("template.txt", "r")
    raw = templateFile.read()
    body = ""
    for i in range(len(raw)):
        body += raw[i]
    body = body.replace(tag, nameParam)
    return body

def buildBCC():
    templateFile = open("template.txt", "r")
    raw = templateFile.read()
    body = ""
    for i in range(len(raw)):
        body += raw[i]
    return body
