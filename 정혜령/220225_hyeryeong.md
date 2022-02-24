### 백준 후위 표기법

```python
import sys


def toRpn(tokens):
    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}
    Ost = []
    newtokens = ''
    
    for token in tokens:
        if token.isalpha():
            newtokens += token
        else:
            if not Ost or token == '(':
                Ost.append(token)
            elif token == ')':
                while Ost:
                    p = Ost.pop()
                    if p == '(': break
                    newtokens += p
            else:
                if isp[Ost[-1]] < icp[token]: # +, *
                    Ost.append(token)
                else: # + + or * +
                    while Ost and isp[Ost[-1]] >= icp[token]:
                        newtokens += Ost.pop()
                    Ost.append(token)
    while Ost:
        newtokens += Ost.pop()
    
    return newtokens


tokens = sys.stdin.readline().rstrip()
print(toRpn(tokens))

```

