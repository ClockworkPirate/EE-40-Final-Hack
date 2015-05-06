import os, random, string
import cherrypy
from galileo import *

class RobotControl(object):
	@cherrypy.expose
	def index(self):
		return file("index.html")

class RobotControlWebService(object):
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	def GET(self):
		return cherrypy.session["mystring"]
	
	def POST(self, direction=""):
		print "POST"
		digitalWrite(l, HIGH)
		delay(500)
		digitalWrite(l, LOW)
		return "POSTed"

	def PUT(self, direction):
		print "PUT"

	def DELETE(self):
		cherrypy.session.pop('mystring', None)

if __name__ == '__main__':
	l = 4
	r = 2
	
	pinMode(l, OUTPUT)
	pinMode(r, OUTPUT)
	
	conf = {
		'/': {
			'tools.sessions.on': True,
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
	page.control = RobotControlWebService()
	cherrypy.quickstart(page, '/', conf)
