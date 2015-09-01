import subprocess

proc = subprocess.Popen(['/usr/local/bin/gnuchessx'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE)

# setup empty list to capture usr and cpu moves
cpu_moves = []
usr_moves = []

while True:
    # ask usr for move
    inp = raw_input("Whatchur moov?") + "\n"

    # add usr move to list
    usr_moves.append(inp[:4])

    # send usr move to gnuchess via subprocess
    proc.stdin.write(inp)
    proc.stdin.flush()

    # receive output from gnuchess and print to console
    for i in range(0, 5):
        line = proc.stdout.readline().rstrip()

        # append cpu move to list
        if i == 4:
            cpu_moves.append(line[-4:])
    print "cpu: ", repr(cpu_moves)
