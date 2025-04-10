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
     <h1 style="font-family: Arial, sans-serif; color: brown; text-align: center;"><b>LIST OF PROTOCOLS</b></h1>
     <h1 style="font-family: Arial, sans-serif; color: black; text-align: center; font-size: 18px;">
         NAME: RUBASRI.R<br> 
         REF NO: 212224240139
     </h1>
     
     <title>PROTOCOLS</title>
 </head>
 <body>
     <h1 style="font-family: Arial, sans-serif; font-style: italic; text-decoration: underline;text-align: center;">
         APPLICATION LAYER
     </h1>
     
     <div style="text-align: center;">
         <ul style="list-style-type: none; padding-left: 0; font-size: 20px;font-family: 'Open Sans', sans-serif;">
             <li>&#8594 HTTP: Hypertext Transfer Protocol</li>
             <li>&#8594; FTP: File Transfer Protocol</li>
             <li>&#8594; SMTP: Simple Mail Transfer Protocol</li>
             <li>&#8594; DNS: Domain Name System</li>
             <li>&#8594; Telnet: Telecommunications Network</li>
             <li>&#8594; SNMP: Simple Network Management Protocol</li>
         </ul>
     </div>
     <h1 style="font-family: Arial, sans-serif; font-style: italic; text-decoration: underline;text-align: center;">
        Transport layer
    </h1>
    <div style="text-align: center;">
     <ul style="list-style-type: none; padding-left: 0; font-size: 20px;font-family: 'Open Sans', sans-serif;">
        <li>&#8594; TCP:Transmission control protocol</li>
        <li>&#8594; UDP:User datagram protocol</li> 
     </div>
     <h1 style="font-family: Arial, sans-serif; font-style: italic; text-decoration: underline;text-align: center;">
        Internet layer
    </h1>
    <div style="text-align: center;">
        <ul style="list-style-type: none; padding-left: 0; font-size: 20px;font-family: 'Open Sans', sans-serif;">
            <li>&#8594; ICMP: Internet Control Message Protocol</li>
            <li>&#8594; IGMP: Internet Group Management Protocol</li>
            <li>&#8594; IPV4: Internet Protocol Version 4</li>
            <li>&#8594; IPV6: Internet Protocol Version 6</li>
        </div>
        <h1 style="font-family: Arial, sans-serif; font-style: italic; text-decoration: underline;text-align: center;">
           Network Access Layer
        </h1>
        <div style="text-align: center;">
            <ul style="list-style-type: none; padding-left: 0; font-size: 20px;font-family: 'Open Sans', sans-serif;">
                <li>&#8594; MAC/Ethernet</li>
                <li>&#8594; FDDI</li>
                <li>&#8594; Frame Relay</li>
            </div>
     
     
     
 </body>
 </html>
 """
 class myhandler(BaseHTTPRequestHandler):
     def do_GET(self):
         print("request received")
         self.send_response(200)
         self.send_header('content-type', 'text/html; charset=utf-8')
         self.end_headers()
         self.wfile.write(content.encode())
 server_address = ('',8000)
 httpd = HTTPServer(server_address,myhandler)
 print("my webserver is running...")
 httpd.serve_forever()

         from http.server import HTTPServer, BaseHTTPRequestHandler
         content = """
         <html>
         <head>
         <h1 style="font-family: Arial, sans-serif; color: brown; text-align: center;"><b>LIST OF PROTOCOLS</b></h1>
         <h1 style="font-family: Arial, sans-serif; color: black; text-align: center; font-size: 18px;">
         NAME: RUBASRI.R<br> 
         REF NO: 212224240139
         </h1>
     
        <title>TCP/IP Protocol Suite</title>
        </head>
        <body>
        <h1 style="font-family: Arial, sans-serif; font-style: italic; text-decoration: underline;text-align: center;">
         TCP/IP Protocol Suite
        </h1>
     
     <div style="text-align: center;">
         <ul style="list-style-type: none; padding-left: 0; font-size: 20px;font-family: 'Open Sans', sans-serif;">
             <li>&#8594; HTTP: Hypertext Transfer Protocol</li>
             <li>&#8594; FTP: File Transfer Protocol</li>
             <li>&#8594; SMTP: Simple Mail Transfer Protocol</li>
             <li>&#8594; DNS: Domain Name System</li>
             <li>&#8594; Telnet: Telecommunications Network</li>
             <li>&#8594; SNMP: Simple Network Management Protocol</li>
         </ul>
     </div>    
    </body>
        </html>
         """
          class myhandler(BaseHTTPRequestHandler):
          def do_GET(self):
          print("request received")
          self.send_response(200)
          self.send_header('content-type', 'text/html; charset=utf-8')
          self.end_headers()
          self.wfile.write(content.encode())
         server_address = ('',8000)
         httpd = HTTPServer(server_address,myhandler)
         print("my webserver is running...")
         httpd.serve_forever()


## OUTPUT:
![alt text](<Screenshot 2025-04-10 201123.png>)

![alt text](<Screenshot 2025-04-10 201123.png>)





## RESULT:
The program for implementing simple webserver is executed successfully.
