from collections import Counter
import re
words = re.findall(r'\w+', open('alice.txt').read().lower())
d = Counter(words).most_common(10)
print(d)

