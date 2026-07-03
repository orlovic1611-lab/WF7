

from http.server import HTTPServer,BaseHTTPRequestHandler

class App(BaseHTTPRequestHandler):


    def do_GET(self):

        html="""

<h1>WF Sentinel</h1>

<h2>Linux Security Dashboard</h2>

<p>Status: RUNNING</p>

<p>Security Engine Active</p>

<p>Database: OK</p>

<p>Plugins: ENABLED</p>

"""


        self.send_response(200)

        self.send_header(
        "Content-type",
        "text/html"
        )

        self.end_headers()

        self.wfile.write(
        html.encode()
        )



def start():

    print(
    "WF Dashboard http://localhost:9090"
    )

    HTTPServer(
    ("0.0.0.0",9090),
    App
    ).serve_forever()


