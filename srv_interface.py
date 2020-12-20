import subprocess as sp
import time

# edit this to 
START = "java -Xmx1G -Xms256M -jar server.jar nogui"
SERVER = None

# start server process. if wait, function will block until server is done booting up.
def srv_init(wait = True):
    global SERVER
    SERVER = sp.Popen(START,
                      shell = True,
                      stdin = sp.PIPE,
                      stdout = sp.PIPE,
                      encoding = "utf-8")
   
    if wait:
        print("starting server, waiting for initialization to complete...")
        while "Done" not in (line := SERVER.stdout.readline()):
            print(line, end = "")
        print("Done initializing.")

def srv_write(msg):
    try:
        out, err = SERVER.communicate(msg, timeout = 15)
        if err:
            raise Exception("SERVER ERROR: " + err)
        return out
    except TimeoutExpired:
        return "process timed out."

def srv_quit():
    print("stopping server...")
    srv_write("/stop")
    SERVER.terminate()
    exit()

def test():
    srv_init()
    srv_quit()

if __name__ == "__main__":
    test()
