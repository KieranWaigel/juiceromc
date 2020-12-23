import subprocess as sp
import time

START = "java -Xmx6G -Xms4G -jar ./server.jar nogui"

def log(*args):
    print("[INTERFACE]", *args)

# start server; blocks until server is done booting
def srv_start():
    with open("/home/ghh/mc-server/LASTLOG.txt", 'w') as f:
        f.write(time.asctime(time.localtime()))
        f.write("\n")
    
    server = sp.Popen(START,
                      shell = True,
                      stdin = sp.PIPE,
                      stdout = sp.PIPE,
                      encoding = "utf-8")
    log("starting minecraft server with command: " + START)
    line = ""
    while True:
        line = server.stdout.readline()
        if "Done" in line:
            break
        elif server.poll() != None: # checks if a returncode has been set (process ended)
            raise Exception("startup failed." )
        print(line, end = "")
    log("startup successful, script closing.")

if __name__ == "__main__":
    srv_start()
