import tornado.ioloop
import tornado.web
import parser
import os

global cereals, circle_viz

static = {
    "static_path": os.path.join(os.path.dirname(__file__), "static")
    }

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/home.html",title="milk&cereal",cereals=carb_fat_cereals)

class CalorieHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("templates/calorie.html",title="milk&cereal",cereals=carb_fat_cereals)

        
application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/calories",CalorieHandler),
], **static)

if __name__ == "__main__":
    retval = parser.parse()
    cereals = retval[0]
    carb_fat_cereals = retval[1]
    application.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
