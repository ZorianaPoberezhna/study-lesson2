from contextlib import contextmanager


@contextmanager
def file_opener(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with file_opener('file1.txt', 'r') as f:
    content = f.read()
    print(content)
