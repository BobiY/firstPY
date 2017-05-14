#!/usr/bin/env python
# -*- coding:utf-8 -*-
   
import tornado.ioloop
import tornado.web
import uimethods as mt
import uimodle as md
   
   
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html',name="hahah",npm="123")  # 渲染文件

settings = {
    "template_path":"views", # 模板文件存放路径
    "static_path":"static", # 静态文件存放路径
    "ui_methods":mt, #自定义方法
    "ui_modules":md #自定义类
}

application = tornado.web.Application([
    (r"/index", MainHandler),
],**settings)
   
   
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()