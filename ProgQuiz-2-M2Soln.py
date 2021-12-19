num = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

def to_integer(t):
    #['sign','number]
    #['minus','three']
    #['plus','four']
    if t[0] == 'minus':
        return -1 * num.index(t[1])
    return num.index(t[1])

# minus one plus two minus three -------- 6
# one plus two plus three ------- 5
exp = input().split(' ')

if len(exp) % 2 == 1:
    exp.insert(0, 'plus')

result = 0
for i in range(0, len(exp),2):

    result += to_integer(exp[i:i+2])
print(result)