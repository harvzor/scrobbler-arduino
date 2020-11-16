import env

def http_get(url):
    import socket

    print('GET', url)

    _, _, host_with_port, path = url.split('/', 3)
    host, port = host_with_port.split(':', 1)
    addr = socket.getaddrinfo(host, port)[0][-1]
    s = socket.socket()
    s.connect(addr)
    s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))

    data = ''

    while True:
        new_data = s.recv(100)

        if new_data:
            data += str(new_data, 'utf8')
        else:
            break

    s.close()

    return data

def get_health():
    return http_get(env.api + '/health')
