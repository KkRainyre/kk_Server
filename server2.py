import http.server


# small server with displaying data from the request
class RequestHandler(http.server.BaseHTTPRequestHandler):

# info page template
    Page = '''\
<!DOCTYPE html>
   <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Webpage Info</title>
    <style>
      body {
        font-family: sans-serif;
        margin: 0;
        padding: 0;
      }

      header {
        background-color: #333;
        color: #fff;
        padding: 16px;
        text-align: center;
      }

      footer {
        background-color: #333;
        color: #fff;
        padding: 16px;
        text-align: center;
      }

      h1 {
        margin: 0;
        padding: 32px 16px;
        text-align: center;
      }

      table {
        border-collapse: collapse;
        margin: 0 auto;
        width: 80%;
      }

      th,
      td {
        padding: 12px 8px;
        text-align: left;
      }

      th {
        background-color: #f2f2f2;
        font-weight: bold;
      }

      tr:nth-child(even) {
        background-color: #f2f2f2;
      }

      caption {
        font-style: italic;
        margin-bottom: 16px;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <header>
      <h2>Webpage with detailed info</h2>
    </header>
    <main>
      <h1>Details about the Request</h1>
      <table>
        <caption>
          The table below shows the details of the request that was made to the server.
        </caption>
        <tbody>
          <tr>
            <th>Header</th>
            <td>Value</td>
          </tr>
          <tr>
            <th>Date and time</th>
            <td>{date_time}</td>
          </tr>
          <tr>
            <th>Client host</th>
            <td>{client_host}</td>
          </tr>
          <tr>
            <th>Client port</th>
            <td>{client_port}s</td>
          </tr>
          <tr>
            <th>Command</th>
            <td>{command}</td>
          </tr>
          <tr>
            <th>Path</th>
            <td>{path}</td>
          </tr>
        </tbody>
      </table>
    </main>
    <footer>
      <p>&copy; kk_Server 2023</p>
    </footer>
  </body>
 </html>
'''
 


    # the web page with all the detailed info
def do_GET(self):
        def do_GET(self):
         page = self.create_page()
         self.send_page(page)


    # create the webpage with dynamic request info 
def create_page(self):

    # get the values from request
        values = {
            'date_time'   : self.date_time_string(),
            'client_host' : self.client_address[0],
            'client_port' : self.client_address[1],
            'command'     : self.command,
            'path'        : self.path
        }
        page = self.Page.format(**values)
        return page


def send_page(self, page):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(page)))
        self.end_headers()
        self.wfile.write(page)
