# EX01 Developing a Simple Webserver
## Date:
8/04/2025
## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
      from http.server import HTTPServer, BaseHTTPRequestHandler

      content = """
      <html>
      <head>
     <title>PROTOCOLS</title>
     </head>
     <body>
    <center><h1><b><u><font face="Arial"><font color= brown>LIST OF PROTOCOLS</u></b></h1></center></font></font>
     <h1>
        <center><i><small>    NAME: RUBASRI.R<br> 
         REF NO: 212224240139</center></i></small>
     </h1>
    
     <h1><u>APPLICATION LAYER</h1></u>
     <div>
         <ul>
             <li>&#8594; HTTP: Hypertext Transfer Protocol</li>
             <li>&#8594; FTP: File Transfer Protocol</li>
             <li>&#8594; SMTP: Simple Mail Transfer Protocol</li>
             <li>&#8594; DNS: Domain Name System</li>
             <li>&#8594; Telnet: Telecommunications Network</li>
             <li>&#8594; SNMP: Simple Network Management Protocol</li>
         </ul>
     </div>
     
     <h1><u>Transport Layer</h1></u>
     <div>
         <ul>
            <li>&#8594; TCP: Transmission Control Protocol</li>
            <li>&#8594; UDP: User Datagram Protocol</li>
         </ul>
     </div>
     
     <h1><u>Internet Layer</h1></u>
     <div>
         <ul>
             <li>&#8594; ICMP: Internet Control Message Protocol</li>
             <li>&#8594; IGMP: Internet Group Management Protocol</li>
             <li>&#8594; IPV4: Internet Protocol Version 4</li>
             <li>&#8594; IPV6: Internet Protocol Version 6</li>
         </ul>
     </div>
     
     <h1><u>Network Access Layer</h1></u>
     <div>
         <ul>
             <li>&#8594; MAC/Ethernet</li>
             <li>&#8594; FDDI</li>
             <li>&#8594; Frame Relay</li>
         </ul>
     </div>
  
    </body>
    </html>
    """

    class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Request received")
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

     server_address = ('', 8000)
     httpd = HTTPServer(server_address, myhandler)
      print("My webserver is running...")
     httpd.serve_forever()


         

## OUTPUT:
![alt text](<Screenshot 2025-04-08 220842.png>)

![Screenshot 2025-04-11 104210](https://github.com/user-attachments/assets/4ada84fb-8225-449b-a065-0b7ce101cecd)







## RESULT:
The program for implementing simple webserver is executed successfully.
