import sys

def stdout_encode(u, default='UTF8'):
    encoding = sys.stdout.encoding or default
    if sys.version_info > (3, 0):
        return u.encode(encoding).decode(encoding)
    return u.encode(encoding)