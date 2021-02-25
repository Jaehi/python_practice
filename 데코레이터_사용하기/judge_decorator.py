import functools
def html_tag(first):
    def decorator(func):
        @functools.wraps(func)
        def wrapper():
            return f'<{first}>{func()}</{first}>'
        return wrapper
    return decorator

a,b = input().split()

@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, World!'

print(hello())