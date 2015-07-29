from flask import Flask, render_template
import subprocess
import json
import pudb

app = Flask(__name__)

proc = subprocess.Popen(['/usr/local/bin/gnuchessx'],
						stdin=subprocess.PIPE,
						stdout=subprocess.PIPE)

#setup empty list to capture usr and cpu moves
cpu_moves = []
usr_moves = []

@app.route('/')
def home():
	return render_template('index.html')

#instatiate a POST route in flask to post moves from js
@app.route('/postmethod/', methods= ['POST'])
def get__post_javascript_data():
	jsdata = request.form['javascript_data']
	return jsdata

#instantiate a GET route in flask to get moves from js
@app.route('/getmethod/<jsdata>')
def get_javascript_data(jsdata):
	jsdata = jsdata[1:5]
	inp = jsdata + "\n"
	print 'sending:', repr(inp)

	#add usr move to list
	usr_moves.append(inp[:4])
	print "usr: ", repr(usr_moves)

	#send usr move to gnuchess via subprocess
	proc.stdin.write(inp)
	proc.stdin.flush()
	return jsdata

#instantiate a GET route to push python data to js
@app.route('/getpythondata')
def get_python_data():
	print "hello world"
	for i in range(0,5):
		line = proc.stdout.readline().rstrip()
		print line

	#append cpu move to list
		if i == 4:
			cpu_line = line[-4:]
			cpu_moves.append(cpu_line)
			cpu_line = list(cpu_line)
			cpu_line.insert(2, "-")
			cpu_line = "".join(cpu_line)
			pythondata = cpu_line
			print"json_move: ", repr(pythondata)
	print "cpu: ", repr(cpu_moves)

	return json.dumps(pythondata)

if __name__ == '__main__':
	app.run(debug=True)