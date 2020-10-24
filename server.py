from http.server import BaseHTTPRequestHandler, HTTPServer

import cgi

from fileHandler import *

# sets the HTTP status code
def set_status(server, code):
    server.send_response(code)

# sets the MIME file type to html
def set_type_html(server):
    server.send_header("Content-Type", "text/html")

# sets the MIME file type to css
def set_type_css(server):
    server.send_header("Content-Type", "text/css")

# sets the MIME file type to js
def set_type_js(server):
    server.send_header("Content-Type", "text/javascript")

# sets the MIME file type to json
def set_type_json(server):
    server.send_header("Content-Type", "text/json")

# processes get request for /test (sends back html to the client)
def get_Test(server):
    set_status(server, 200)
    set_type_html(server)
    server.end_headers()
    server.wfile.write(bytes(readFile('./webapp/html/index.html'), 'utf-8'))

# send css to the client
def get_Css(server):
    set_status(server, 200)
    set_type_css(server)
    server.end_headers()
    server.wfile.write(bytes(readFile('./webapp/css/style.css'), 'utf-8'))

# send js to the client
def get_Code(server):
    set_status(server, 200)
    set_type_js(server)
    server.end_headers()
    server.wfile.write(bytes(readFile('./webapp/js/code.js'), 'utf-8'))

# process csv from the client, and send back results
def post_Send(server):

    # gets csv from client
    form = cgi.FieldStorage(fp=server.rfile, headers=server.headers, environ={'REQUEST_METHOD': 'POST'})

    print(form.getvalue("file"))

    ### DO THINGS WITH THE CSV FILE HERE ###
    
    # parses csv
    split = split_csv(form.getvalue("file"))

    # converts csv data to json
    json = json_from_array(split)

    ### ###

    # set headers
    set_status(server, 200)
    set_type_json(server) # <- remember to change this to a text/csv filetype
    server.end_headers()

    # send final result
    server.wfile.write(bytes(json, 'utf-8'))

# MyServer class, handles all HTTP requests
class MyServer(BaseHTTPRequestHandler):

    # do_GET() is called for GET requests
    def do_GET(self):
        if self.path == '/test':
            get_Test(self)
        elif self.path == '/style':
            get_Css(self)
        elif self.path == '/code':
            get_Code(self)
        else:
            set_status(self, 404)
            set_type_html(self)
            self.end_headers()
            self.wfile.write(bytes("<html><head><meta charset='UTF-8'><title>https://pythonbasics.org</title></head><body><h1>404 Not Found</h1></body>", "utf-8"))
    
    # do_POST() is called for POST requests
    def do_POST(self):
        #self._set_headers()
        post_Send(self)