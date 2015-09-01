class Game(object):

	def __init__(self):
		self.sub_process = subprocess.Popen(['/usr/local/bin/gnuchessx'],
											stdin=subprocess.PIPE,
											stdout=subprocess.PIPE)

		