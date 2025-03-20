from http.server import SimpleHTTPRequestHandler, HTTPServer

def main():
    HOST, PORT = 'localhost', 4000
    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    print(f"Server running on http://{HOST}:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    main()