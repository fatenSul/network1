from socket import *

serverport = 6060
serverSocket = socket(AF_INET, SOCK_DGRAM)  # create a UDP server socket
serverSocket.bind(('localhost', serverport))  # bind the server socket to a port

print("The server is ready to receive...")

while True:
    data, client_address = serverSocket.recvfrom(1024)  # receive data and client address
    print("Received:", data.decode())

    client_req_url = data.decode().split()[1]

    if client_req_url.endswith(".html"):
        with open("index.html", "rb") as file:
            content = file.read()
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n" + content.decode()
    elif client_req_url.endswith(".css"):
        with open("styles.css", "rb") as file:
            content = file.read()
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/css\r\n\r\n" + content.decode()
    elif client_req_url.endswith(".png"):
        with open("./assets/faten.png", "rb") as file:
            content = file.read()
        response = "HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n" + content.decode()
    elif client_req_url.endswith(".jpg"):
        with open("mona.jpg", "rb") as file:
            content = file.read()
        response = "HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\n\r\n" + content.decode()
    elif client_req_url == '/so':
        response = "HTTP/1.1 307 Temporary Redirect\r\nLocation: https://stackoverflow.com/\r\n\r\n"
    elif client_req_url == '/itc':
        response = "HTTP/1.1 307 Temporary Redirect\r\nLocation: https://itc.birzeit.edu/\r\n\r\n"
    else:
        response = """
            HTTP/1.1 404 Not Found\r\n
            Content-Type: text/html\r\n\r\n
            <!DOCTYPE html>
            <html>
            <head>
                <title>Error 404</title>
            </head>
            <body>
                <h1 style="color:red;">The file is not found</h1>
                <p><b>Faten Sultan - 1202750</b></p>
                <p><b>Mona Dwiekat- 1200277</b></p>
                <p><b>IP: {ip} Port: {port}</b></p>
            </body>
            </html>
        """.format(ip=client_address[0], port=client_address[1])

    serverSocket.sendto(response.encode(), client_address)  # send response to client
