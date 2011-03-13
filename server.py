import tornado.ioloop
import tornado.web
import parser
import os

global cereals
cereals = {}

static = {
    "static_path": os.path.join(os.path.dirname(__file__), "static")
    }

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/home.html",title="protopuffs",cereals=cereals)

application = tornado.web.Application([
        (r"/", MainHandler),
], **static)

if __name__ == "__main__":
    cereals = parser.parse()
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
