x="pyTHoN sTriNG meThoDS"

print(x.lower())
print(x.upper())
print(x.capitalize())
print(x.title())
print(x.swapcase())


x="python"
print(x.islower())
x="Python"
print(x.islower())
x='PYTHON'
print(x.isupper())
x='PYTHoN'
print(x.isupper())
x='Python String Method'
print(x.istitle())
x='Python string Method'
print(x.istitle())



x='123'
print(x.isdigit())
x='123abc'
print(x.isdigit())
x='abc'
print(x.isalpha())
x='abc123'
print(x.isalnum())
x='abc123@*#'
print(x.isalnum())




x='_________Python________'
print(x.strip('_'))



x='_________Python________'
print(x.lstrip('_'))





x='_________Python________'
print(x.rstrip('_'))


x='Python'
print(x.startswith('P'))
print(x.startswith('p'))
print(x.endswith('n'))
print(x.endswith('N'))





x='Python String Method'
print(x.count('t'))
print(x.count('s'))
print(x.index('t'))
print(x.index('S'))

x=x.replace('S','s')
x=x.replace('M','m')
print(x)