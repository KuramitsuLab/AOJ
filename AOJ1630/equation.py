import sys, functools
#sys.setrecursionlimit(30000)

@functools.lru_cache(maxsize=10000)
def check_syntax(s):
    idx = 0
    for c in s:
        if c == ')':
            if idx == 0: return False
            idx -= 1
        if c == '(':
            idx += 1
    return idx == 0

'''
def find(s, c):
    p = -1
    while True:
        p = s.find(c, p+1)
        if p == -1: return -1
        if s.count('(', 0, p) == s.count(')', 0, p):
            return p
    return -1

@functools.lru_cache(maxsize=None)
def calc(s):
    #print('@', s)
    p = find(s, '+')
    if p != -1:
        l = []
        while p != -1:
            l.append(s[0:p])
            s = s[p+1:]
            p = find(s, '+')
        l.append(s)
        return sum(map(calc, l))
    p = find(s, '*')
    if p != -1:
        l = []
        while p != -1:
            l.append(s[0:p])
            s = s[p + 1:]
            p = find(s, '*')
        l.append(s)
        return functools.reduce(lambda x,y : x * y, map(calc, l))
    while s.startswith('(') and s.endswith(')'):
        return calc0(s[1:-1])
    return int(s)
'''

def rfind(s, c):
    end = len(s)+1
    p = end
    while True:
        p = s.rfind(c, 0, p-1)
        if p == -1: return -1
        if s.count('(', p, end) == s.count(')', p, end):
            return p
    return -1

@functools.lru_cache(maxsize=None)
def calc(s):
    #print('@', s)
    p = rfind(s, '+')
    if p != -1:
        return calc(s[0:p]) + calc(s[p+1:])
    p = rfind(s, '*')
    if p != -1:
        return calc(s[0:p]) * calc(s[p+1:])
    while s.startswith('(') and s.endswith(')'):
        return calc(s[1:-1])
    return int(s)

#print(calc('2*(2+1)*2'))
#print(calc('2+(2*1)+2'))

def solve(s, n):
    c = 0
    for i in range(0, len(s) + 1):
        if s.startswith('+', i) or s.startswith('*', i) or s.startswith(')', i): continue
        for w in range(1, len(s)+1-i):
            ee = i+w
            if s.startswith('+', ee-1) or s.startswith('*', ee-1) : continue
            if s.count('(', i, ee) != s.count(')', i, ee): continue
            sub = s[i:ee]
            if check_syntax(sub):
                m = calc(sub)
                if m == n:
                    #print('c', c, i, len(s))
                    c += 1
                if m > n : break
    return c

#print('count=', solve('(1+2)*3+3', 3))
#print('count=', solve('1*1*1+1*1*1', 2))

def main():
    while True:
        n = int(sys.stdin.readline()[:-1])
        if n == 0: return
        s = sys.stdin.readline()[:-1]
        print(solve(s, n))

main()
