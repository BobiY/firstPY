# -*- coding:utf-8 -*-

from wsgiref.simple_server import make_server

def index():
    return "index"

def new():
    return "new"



URLS = {
    '/index':index,
    '/new':new
}


def RunServer(req,res):
    url = req["PATH_INFO"]
    res('200 ok',[('Content-Type','text/html')])
    if url in URLS:
        ret = URLS[url]()
    else:
        ret = '404'
    return [bytes(ret), ]

if __name__ == "__main__":
    http = make_server('',3000,RunServer)
    print("go go go")
    http.serve_forever()