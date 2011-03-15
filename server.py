import tornado.ioloop
import tornado.web
import parser
import os

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
        self.render("templates/fiber.html",title="milk&cereal",cereals=fiber_cereals)

class SaltHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/salt.html",title="milk&cereal",cereals=salt_cereals)

application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/calories",CalorieHandler),
        (r"/fiber",FiberHandler),
        (r"/saltvitamins",SaltHandler),
], **static)

if __name__ == "__main__":
    retval = parser.parse()
    carb_fat_cereals = retval[0]
    fiber_cereals = retval[1]
    salt_cereals = retval[2]
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
