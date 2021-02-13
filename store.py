def addSponsor(address, name):
    f = open("sponsors.txt", "a")
    f.write(str(address) + ", " + str(name) + "\n")
    f.close()
