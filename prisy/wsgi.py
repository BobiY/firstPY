from wsgiref.simple_server import make_server
 
 
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    # 2.x 这里不需要加 encoding ，但是 3.x 必须加。
    return [bytes('<h1>Hello, web!</h1>',encoding='utf-8'), ]
 
 
if __name__ == '__main__':
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
