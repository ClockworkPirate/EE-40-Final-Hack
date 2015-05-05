import os, cherrypy
# from galileo import *

# l = 4
# r = 2
#
# pinMode(l, OUTPUT)
# pinMode(r, OUTPUT)

class RobotControl(object):
	@cherrypy.expose
	def index(self):
		return open("index.html", "r").read()

class RobotControlAPI(object):
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	def POST(self, direction):
		print "POST"
		# digitalWrite(l, HIGH)
		# delay(1000)
		# digitalWrite(l, LOW)

	def PUT(self, direction):
		print "PUT"

if __name__ == '__main__':
	conf = {
		'/': {
			'tools.staticdir.root': os.path.abspath(os.getcwd())
		},
		'/control': {
			'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
			'tools.response_headers.on': True,
			'tools.response_headers.headers': [('Content-Type', 'text/plain')],
		},
		'/static': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': './public'
		}
	}
	page = RobotControl()
	page.control = RobotControlAPI()
	cherrypy.quickstart(page, '/', conf)
