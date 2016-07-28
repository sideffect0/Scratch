def application(environ, start_response):
    status = '200 OK'
    body = b'Scratch Works: Hack and Learn'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(body)))]
    start_response(status, response_headers)
    return [body]
