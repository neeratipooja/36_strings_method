'''
DATE=25th NOV 2022
DAY= friday
TOPIC= strings
AUTHOR= pooja
'''
a="hey"
print(a.isalpha()) #true
u="7"
print(u.isalnum()) #true
z="hi dad"
print(z.isascii()) #true
b=chr(0)
print(b.isspace()) #false
b=chr(32)
print(b.isspace()) #true
print("hi"+chr(32)+"dad") #hi dad
print("hi"+chr(0)+"dad") #hidad
print(chr(32)+"hello") # hello
print(ord("b")) #98
print(ord("a")) #97
print(ord("A")) #65
print(ord("Z")) #90
print(ord("0")) #48
print(ord(" ")) #32
print(ord("!")) #33