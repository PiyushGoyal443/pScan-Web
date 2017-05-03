import routes
from controllers.modules import *

define("port",
  default = 8888,
  help = "Contact the One who made it Contact PIYUSH :P",
  type = int)

#overloading the Application
class ApplicationHandler(Application):

	def __init__(self):

		handlers = routes.routes
		settings = dict(debug = True,
                        template_path=os.path.join(os.path.dirname(__file__), "templates"),
                        static_path=os.path.join(os.path.dirname(__file__), "static"))
		Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    options.parse_command_line()
    http_server = HTTPServer(ApplicationHandler())
    http_server.listen(options.port)
    IOLoop.instance().start()
