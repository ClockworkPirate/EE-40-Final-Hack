import os, cherrypy

class RobotControl(object):
	@cherrypy.expose
	def index(self):
		return open("index.html", "r").read()

class RobotControlAPI(object):
	exposed = True

	@cherrypy.tools.accept(media='text/plain')
	def POST(self, direction):
		# move the robot
		pass

	def PUT(self, direction):
		#feedback test
		pass

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
