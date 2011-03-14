import tornado.ioloop
import tornado.web
import parser
import os

global cereals

static = {
    "static_path": os.path.join(os.path.dirname(__file__), "static")
    }

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/splash.html",title="milk&cereal",cereals=carb_fat_cereals)

class CalorieHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/calorie.html",title="milk&cereal",cereals=carb_fat_cereals)

class FiberHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/fiber.html",title="milk&cereal",cerals=fiber_cereals)
        
application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/calories",CalorieHandler),
        (r"/fiber",FiberHandler),
], **static)

if __name__ == "__main__":
    retval = parser.parse()
    cereals = retval[0]
    carb_fat_cereals = retval[1]
    fiber_cereals = retval[2]
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
