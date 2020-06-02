import re

ans = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(ans)
