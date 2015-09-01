import subprocess
import pudb
from threading import Thread
import time

proc = subprocess.Popen(['/usr/local/bin/gnuchessx', '--post'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE)

# setup empty list to capture usr and cpu moves
cpu_moves = []
usr_moves = []


def print_gnu_thinking():
    while True:
        line = proc.stdout.readline().rstrip()
        # receive output from gnuchess and print to console
        while ("My move is" not in line):
            print "GNU thinking: " + line
            line = proc.stdout.readline().rstrip()
        print line


def get_user_move():
    while True:
        # ask usr for move
        inp = raw_input("Whatchur moov?") + "\n"
        # add usr move to list
        usr_moves.append(inp[:4])

        # send usr move to gnuchess via subprocess
        proc.stdin.write(inp)
        proc.stdin.flush()


if __name__ == '__main__':
    t1 = Thread(target=print_gnu_thinking)
    t2 = Thread(target=get_user_move)
    t1.daemon = True
    t2.daemon = True
    t1.start()
    t2.start()
    while True:
        time.sleep(1)
