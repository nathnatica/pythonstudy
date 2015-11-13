import sys

################## while 
f = open("foo.txt")
line = f.readline()
while line:
#    print line,         # trailing ',' omits new line character
    line = f.readline()
f.close()


################## for
for l in open("foo.txt", "r"):
#    print l,
    pass



################## file write
f = open("foo.txt", "w")
print >>f, "%3d  %0.2f" % (1, 12.999)   # 13.00 is inserted
f.close()

#text = sys.stdin.readline()    # or 
#text = raw_input("enter something :")
#f = open("foo.txt", "w")
#f.write(text)
#f.close()


################## strings
text =  "hello world"
sub = text[:4]  # "hell"

# string convert
text = "some" + str(1)
text = "some" + repr(1)
text = "some" + `1` # is same with repr(1)


################## list
list = ['a', 'b']
list.append('c')
list.insert(0, 'd')
sub = list[0:2] # ['d','a']
list = list + ['e']
list.append([['f',['g', "h"]]])
#print list[5][0][1][0]  # g

if len(sys.argv) != 1:
    pass
else:
    floats = [float(s) for s in ['1.1', '2', '3']]
#    print min(floats)   # 1.1


################## tuple
singleton = (7,)    # is 1-element tuple not an expression
t = 1,4,"string", -99   # without ()



################## set
s = set("Hello")    # set(['H','e','l','o'])    # only 1 'l'
s.add(0)
s.update("0") # add
s.remove("H")
#print(s)    # set([0, 'e', 'l', 'o', '0'])


################## dictionary
d = {"key1": "v1", "key2": "v2"}

if d.has_key("key1"):
    value = d["key1"]
else:
    value = "default"
# or 
value = d.get("key1","default")

k = d.keys()
del d["key2"]   # delete



################## iteration
for i in range (5): # [0,1,2,3,4]
#    print i
    pass
# for large ranges, use xrange() instead of range(), 
# which computes values whenever accessed

# fibonacci generator
def fibonacci(max):
    s = 1
    t = 1
    while s < max:
        yield s     # produce a value
        w = s + t
        s = t
        t = w
    return


################## function
def divide(a,b):
    q = a // b  # is truncating division
    r = a - q*b
    return q,r  # returns tuple

quotiet, remainder = divide(1000, 22)

# access global variable
a = 4
def foo():
    global a
    a = 4.1     # change the global variable


    
sys.exit()
# or use
#raise SystemExit
