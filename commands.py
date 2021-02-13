commands = []
args = []
descs = []

def add(c, a, d):
    commands.append(c)
    args.append(a)
    descs.append(d)

def show():
    for i in range(len(commands)):
        print(commands[i] + " [" + args[i] + "]: " + descs[i])
