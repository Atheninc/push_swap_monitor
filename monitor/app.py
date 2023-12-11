import eel
import os

eel.init('web')

@eel.expose
def ExecCmd(cmd):
    print("exec : " + str(cmd))
    try:
        rep = os.popen(cmd).read()
    except Exception as e:
        rep = "Error: " + str(e)
    except OSError as e:
        rep = "Error: " + str(e)

    print(rep)
    return(rep)

@eel.expose
def GetData(val, path):
    tmps = []
    txt = ""
    for item in val:
        if (len(txt) != 0):
            txt += " "
        txt += str(item["value"])
        tmps.append(item["value"])
    #print(tmps)
    #print(txt)
    #executer le programme a ../push_swap
    if (os.path.isfile(path) == False):
        return "path Error"
    try:
        print("exec : " + str("./" + path + " " + txt))
        rep = os.popen("./" + path + " " + txt).read()
    except:
        rep = "path Error"
    print(rep)
    return(rep)


eel.start('index.html', mode="google-chrome")