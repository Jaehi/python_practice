import re

a = re.compile('^(https?://)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*')

print(a.match(input()) != ' ')