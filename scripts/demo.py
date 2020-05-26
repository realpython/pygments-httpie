#!/usr/bin/env python3

"""A simple demo of the lexer's colorized result."""

import pygments
import pygments.formatters.terminal

from pygments_httpie import HttpLexer

lexer = HttpLexer()


def pprint(code: str) -> None:
    print(
        pygments.highlight(
            code, lexer, pygments.formatters.terminal.TerminalFormatter()
        )
    )


code = '''\
GET /myapp/ HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Host: localhost:8000
User-Agent: HTTPie/2.1.0

HTTP/1.1 200 OK
Content-Length: 160
Content-Type: text/html; charset=utf-8
Date: Mon, 25 May 2020 22:59:03 GMT
Server: WSGIServer/0.2 CPython/3.8.3
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

<!DOCTYPE html>
<html lang="en-US">
  <head><meta charset="utf-8"><title>My secure app</title></head>
  <body><p>Now this is some sweet HTML!</p></body>
</html>'''


if __name__ == "__main__":
    import sys

    sys.exit(pprint(code))
