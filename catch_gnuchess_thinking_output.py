import subprocess
import pudb
from threading import Thread

proc = subprocess.Popen(['/usr/local/bin/gnuchessx', '--post'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE)

# setup empty list to capture usr and cpu moves
cpu_moves = []
usr_moves = []


def func1():
    while True:
        line = proc.stdout.readline().rstrip()
        # receive output from gnuchess and print to console
        while ("My move is" not in line):
            print "jeff is cool " + line
            line = proc.stdout.readline().rstrip()
        print line


def func2():
    while True:
        # ask usr for move
        inp = raw_input("Whatchur moov?") + "\n"
        # add usr move to list
        usr_moves.append(inp[:4])

        # send usr move to gnuchess via subprocess
        proc.stdin.write(inp)
        proc.stdin.flush()


if __name__ == '__main__':
    Thread(target=func1).start()
    Thread(target=func2).start()
