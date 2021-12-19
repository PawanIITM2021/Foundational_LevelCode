dept    = input()
course  = input()
prefix  = input()
name    = input()
roll_no = input()
name = prefix + " " + name.upper() # one space
lib_id = dept[0] + course[0] + roll_no
print("Student record:")
indent = '    ' # four spaces
print(indent + "Dept:", dept)
print(indent + "Name:", name)
print(indent + "Roll No:", roll_no)
print(indent + "Library Card No:", lib_id)