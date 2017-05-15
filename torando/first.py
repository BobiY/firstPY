#!/usr/bin/env python
# -*- coding:utf-8 -*-
   
import tornado.ioloop
import tornado.web
import uimethods as mt
import uimodle as md
from session import Session

class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        # 防止重复创建随机字符串
        if self.get_cookie("aa",None):
            self.random_str = self.get_cookie("aa",None)
        else:
            self.random_str = ""
        self.session = Session(self)

   
class MainHandler(BaseHandler):
    def get(self):
        # print(str(self.get_secure_cookie("ok"),encoding='utf8')) #根据键值获取cookie,加密方式获得的cookie是字节类型，这里需要转字符串
        # self.set_secure_cookie('ok','aaaa') #设置cookie
        self.session['name'] = "111111"
        self.session['is_login'] = True
        self.set_cookie('aa',self.session.random_str)
        self.render('index.html',name="hahah",npm="123")  # 渲染文件

class MangeHandler(BaseHandler):
    def get(self):
        print(self.session["is_login"])

settings = {
    "template_path": "views", # 模板文件存放路径
    "static_path": "static", # 静态文件存放路径
    "ui_methods": mt, # 自定义方法
    "ui_modules": md, # 自定义类
    'cookie_secret': 'aiuasdhflashjdfoiuashdfiuh' # 加签cookie加密串
}

application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/mange", MangeHandler),
], **settings)
   
   
if __name__ == "__main__":
    application.listen(8888)
    print('go go go')
    tornado.ioloop.IOLoop.instance().start()