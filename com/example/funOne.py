"""
Fundamental One :

Test if we can define and cal function anywhere? or we have to define before calling?
--- have to be defined before use... and if redefined then the one directly above is used (latest definition in order)
no overloading concept present .... eg if u repeat name with more params... it will work based on the order of definition
and crash if method call not matching the signature

@@@@@@@@@ string is pass by value - changes made to it inside the method does not reflect outside
@@@@@@@@@ list is pass by ref - like object - changes made to it inside the method are reflected outside
need to understand the internal workings - may be its just like java - and objects store their memory address
- then everything is pass my value just like java
"""

exList = [1, 2, 3, 4, 5]


def change(lol):
    # list=[6,7,8]
    for i in range(0, len(lol)):
        lol[i] += 2
        print(lol[i])
    lol = ["n", "e", "w"]  # new address reference is assigned to list var ... but exList has already been changed
    print(lol)


print(exList)
change(exList)
print("after change and outside " + str(exList))
print("-------------------------------------------------------")
str1 = "something"


def change(st):
    st = st.upper()
    st = st + "bb"
    print(st)
    st = "new"
    print(st)


print(str1)
change(str1)
print("after change and outside " + str1)

# the below is treated like a long string - not assigned to any variable - hence its not greyed as comment
# which means multi line comments cannot come in between the program ???
"""
[1, 2, 3, 4, 5]
3
4
5
6
7
['n', 'e', 'w']
after change and outside [3, 4, 5, 6, 7]
-------------------------------------------------------
something
SOMETHINGbb
new
after change and outside something
"""
