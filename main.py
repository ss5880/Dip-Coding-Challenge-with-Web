# Import Libraries / Modules

# import heroku libraries
import os

# imports web stuff
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

# import MyServer class from server.py
from server import MyServer

# sets the host information
hostName = "localhost"
serverPort = 8000

# Only import Config.py if the bot is being run locally
# 'HOSTED' is a environment variable set on Heroku that equals the bot token
if os.environ.get('HOSTED') == None:
    print('Running Locally')
else:
    serverPort = int(os.environ.get('PORT', 17995))
    hostName = ''
    print('Running on Heroku')


# main function, starts the webserver
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
