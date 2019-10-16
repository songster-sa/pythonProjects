"""
Fundamental Two :

multiple variable creation / assignment in single line

some print fundamentals : comma separated; end has to be a str; cursor remains at EOL when using end

importing in the middle works - though not recommended ofcourse
"""

a = b = c = 2
d, e, f = 1, "abc", 3.12
print(a, b, c, d, e, f)

name = "john doe"
for char in name:
    print(char, end="@")

"""
2 2 2 1 abc 3.12
j@o@h@n@ @d@o@e@
"""

print("-----------------")
import random

print(random.randint(1, 10))
