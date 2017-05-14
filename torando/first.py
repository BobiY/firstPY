#!/usr/bin/env python
# -*- coding:utf-8 -*-
   
import tornado.ioloop
import tornado.web
   
   
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html',name="hahah")  # 渲染文件

settings = {
    "template_path":"views", # 模板文件存放路径
    "static_path":"static" # 静态文件存放路径
}

application = tornado.web.Application([
    (r"/index", MainHandler),
],**settings)
   
   
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()