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