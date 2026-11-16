import os, socket, http.server

host = os.environ.get("NEON_HOST", "")
results = []
for port in (5432, 443):
    try:
        socket.create_connection((host, port), timeout=10).close()
        results.append(f"PORT {port}: OK")
    except Exception as e:
        results.append(f"PORT {port}: BLOCKED ({e})")
body = "\n".join(results).encode()
print(body.decode(), flush=True)

class H(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(body)

port = int(os.environ.get("PORT", "8080"))
http.server.HTTPServer(("", port), H).serve_forever()
