from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations from Lesson 1
from database_setup import Base, Category, CatalogItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create session and connect to DB
engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class webServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
        	if self.path.endswith("/categories/new"):
            if self.path.endswith("/categories"):
            	categories = session.query(Category).all()
            	output = ""
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                for category in categories:
                	output += category.name
                	output += "</br>"
                	output += "<a href = #' #' >Edit </a>"
                	output += "</br>"
                	output += "<a href = #' #' >Delete </a>"
                	output += "</br></br></br>"
                
                output += "</body></html>"
                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
    	self.send_response(301)
    	self.send_header('content-type', 'text/html')
    	self.end_headers()




def main():
    try:
        server = HTTPServer(('', 8080), webServerHandler)
        print 'Web server running...open localhost:8080/categories in your browser'
        server.serve_forever()
    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()