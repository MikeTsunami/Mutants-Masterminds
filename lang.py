from inspect import signature
import random as rand

def P(S):
    T = set()
    for i in range(1 << len(S)):
        T.add(frozenset(list(S)[s] for s in range(len(S)) if (i & (1 << s))))
    return T

class L:
    def __init__(self, M):
        self.__w = ''
        self._M = tuple()
        self.__name__ = type(self).__name__
        if type(M) in {tuple}:
            if len(M) == 4:
                if type(M[0]) in {set}:
                    if len(M[0]) > 0:
                        V = True
                        for A in M[0]:
                            if type(A) not in {str}:
                                V = False
                                break
                            elif len(A) == 0:
                                V = False
                                break
                        if V:
                            if type(M[1]) in {set}:
                                if len(M[1]) > 0:
                                    locals()['\u03a3'] = True
                                    for l in M[1]:
                                        if type(l) not in {str}:
                                            locals()['\u03a3'] = False
                                            break
                                        elif len(l) != 1:
                                            locals()['\u03a3'] = False
                                            break
                                    if locals()['\u03a3']:
                                        if len(M[0] & M[1]) == 0:
                                            if type(M[2]) in {dict}:
                                                if len(M[2]) > 0:
                                                    for A in M[0]:
                                                        if A not in M[2].keys():
                                                            V = False
                                                            break
                                                    if V:
                                                        R = True
                                                        for A in M[2]:
                                                            if A not in M[0]:
                                                                V = False
                                                                break
                                                            elif type(M[2][A]) not in {set}:
                                                                V = False
                                                                break
                                                            elif len(M[2][A]) == 0:
                                                                V = False
                                                                break
                                                            if V:
                                                                for u in M[2][A]:
                                                                    if type(u) not in {tuple}:
                                                                        R = False
                                                                        break
                                                                    if len(u) == 0:
                                                                        R = False
                                                                        break
                                                                    for l in u:
                                                                        if l not in M[0] | M[1] | {''}:
                                                                            R = False
                                                                            break
                                                        if R:
                                                            if M[3] in M[0]:
                                                                pda = dict()
                                                                q = 1
                                                                pda[q] = dict()
                                                                for a in M[1] | {''}:
                                                                    pda[q][a] = dict()
                                                                    for b in M[0] | M[1] | {'$', ''}:
                                                                        pda[q][a][b] = set()
                                                                        if a == '' and b == '':
                                                                            pda[q][a][b].add((q + 1, '$'))
                                                                q += 1
                                                                pda[q] = dict()
                                                                for a in M[1] | {''}:
                                                                    pda[q][a] = dict()
                                                                    for b in M[0] | M[1] | {'$', ''}:
                                                                        pda[q][a][b] = set()
                                                                        if a == '' and b == '':
                                                                            pda[q][a][b].add((q + 1, M[3]))
                                                                q += 1
                                                                pda[q] = dict()
                                                                for a in M[1] | {''}:
                                                                    pda[q][a] = dict()
                                                                    for b in M[0] | M[1] | {'$', ''}:
                                                                        pda[q][a][b] = set()
                                                                        if a in M[1] and b == a:
                                                                            pda[q][a][b].add((q, ''))
                                                                        if a == '' and b in M[0]:
                                                                            for u in M[2][b]:
                                                                                '''if len(u) == 0:
                                                                                    pda[q][a][b].add((q, ''))'''
                                                                                if len(u) == 1:
                                                                                    pda[q][a][b].add((q, u[0]))
                                                                                else:
                                                                                    pda[q][a][b].add((max(pda.keys()) + 1, u[-1]))
                                                                                    tmp = dict()
                                                                                    l = -2
                                                                                    while l > -len(u):
                                                                                        tmp[max(pda.keys())-l-1] = dict()
                                                                                        for x in M[1] | {''}:
                                                                                            tmp[max(pda.keys())-l-1][x] = dict()
                                                                                            for y in M[0] | M[1] | {'$', ''}:
                                                                                                tmp[max(pda.keys())-l-1][x][y] = set()
                                                                                                if x == '' and y == '':
                                                                                                    tmp[max(pda.keys())-l-1][x][y].add((max(pda.keys()) - l, u[l]))
                                                                                        l -= 1
                                                                                    tmp[max(pda.keys())-l-1] = dict()
                                                                                    for x in M[1] | {''}:
                                                                                        tmp[max(pda.keys())-l-1][x] = dict()
                                                                                        for y in M[0] | M[1] | {'$', ''}:
                                                                                            tmp[max(pda.keys())-l-1][x][y] = set()
                                                                                            if x == '' and y == '':
                                                                                                tmp[max(pda.keys())-l-1][x][y].add((q, u[l]))
                                                                                    pda.update(tmp)
                                                                pda[q]['']['$'].add((max(pda.keys()) + 1, ''))
                                                                q = max(pda.keys()) + 1
                                                                pda[q] = dict()
                                                                for a in M[1] | {''}:
                                                                    pda[q][a] = dict()
                                                                    for b in M[0] | M[1] | {'$', ''}:
                                                                        pda[q][a][b] = set()
                                                                self._M = (set(pda.keys()), M[1], M[0] | M[1] | {'$'}, lambda q, a, b: pda[q][a][b], min(pda.keys()), {max(pda.keys())})
                                                                self.__name__ = 'CFL'
            elif len(M) == 5:
                if type(M[0]) in {set}:
                    if len(M[0]) > 0:
                        if type(M[1]) in {set}:
                            if len(M[1]) > 0:
                                locals()['\u03a3'] = True
                                for l in M[1]:
                                    if type(l) not in {str}:
                                        locals()['\u03a3'] = False
                                        break
                                    elif len(l) != 1:
                                        locals()['\u03a3'] = False
                                        break
                                if locals()['\u03a3']:
                                    if M[3] in M[0]:
                                        if type(M[4]) in {set}:
                                            if M[4] <= M[0]:
                                                if callable(M[2]):
                                                    if len(signature(M[2]).parameters) == 2:
                                                        if [M[2](q, l) in M[0] for q in M[0] for l in M[1]] == [True] * (len(M[0]) * len(M[1])):
                                                            self._M = M
                                                            self.__name__ = 'REG'
                                                        elif [type(M[2](q, l)) for q in M[0] for l in M[1] | {''}] == [set] * (len(M[0]) * len(M[1] | {''})):
                                                            if [M[2](q, l) <= M[0] for q in M[0] for l in M[1] | {''}] == [True] * (len(M[0]) * len(M[1] | {''})):
                                                                dfa = dict()
                                                                for R in P(M[0]):
                                                                    dfa[R] = dict()
                                                                    if R == frozenset():
                                                                        for l in M[1]:
                                                                            dfa[R][l] = frozenset()
                                                                    else:
                                                                        for r in R:
                                                                            for l in M[1]:
                                                                                E = set()
                                                                                if l not in dfa[R].keys():
                                                                                    dfa[R][l] = frozenset()
                                                                                for q in M[2](r, l):
                                                                                    E.add(q)
                                                                                    for locals()['q\''] in M[2](q, ''):
                                                                                        E.add(locals()['q\''])
                                                                                dfa[R][l] = dfa[R][l] | frozenset(E)
                                                                self._M = (P(M[0]), M[1], lambda R, l: dfa[R][l], frozenset({M[3]} | {q for q in M[2](M[3], '')}), {R for R in P(M[0]) if set(R) & M[4] != set()})
                                                                self.__name__ = 'REG'
            elif len(M) == 6:
                if type(M[0]) in {set}:
                    if len(M[0]) > 0:
                        if type(M[1]) in {set}:
                            if len(M[1]) > 0:
                                locals()['\u03a3'] = True
                                for l in M[1]:
                                    if type(l) not in {str}:
                                        locals()['\u03a3'] = False
                                        break
                                    elif len(l) != 1:
                                        locals()['\u03a3'] = False
                                        break
                                if locals()['\u03a3']:
                                    if type(M[2]) in {set}:
                                        if len(M[2]) > 0:
                                            locals()['\u0393'] = True
                                            for l in M[2]:
                                                if type(l) not in {str}:
                                                    locals()['\u0393'] = False
                                                    break
                                                elif len(l) != 1:
                                                    locals()['\u0393'] = False
                                                    break
                                            if locals()['\u0393']:
                                                if M[4] in M[0]:
                                                    if type(M[5]) in {set}:
                                                        if M[5] <= M[0]:
                                                            if callable(M[3]):
                                                                if len(signature(M[3]).parameters) == 3:
                                                                    if [type(M[3](q, a, b)) for q in M[0] for a in M[1] | {''} for b in M[2] | {''}] == [set] * (len(M[0]) * len(M[1] | {''}) * len(M[2] | {''})):
                                                                        if [M[3](q, a, b) <= {(locals()['q\''], l) for locals()['q\''] in M[0] for l in M[2] | {''}} for q in M[0] for a in M[1] | {''} for b in M[2] | {''}] == [True] * (len(M[0]) * len(M[1] | {''}) * len(M[2] | {''})):
                                                                            self._M = M
                                                                            self.__name__ = 'CFL'
            elif len(M) == 7:
                if type(M[0]) in {set}:
                    if len(M[0]) > 0:
                        if type(M[1]) in {set}:
                            if len(M[1]) > 0:
                                locals()['\u03a3'] = True
                                for l in M[1]:
                                    if type(l) not in {str}:
                                        locals()['\u03a3'] = False
                                        break
                                    elif len(l) != 1:
                                        locals()['\u03a3'] = False
                                        break
                                if locals()['\u03a3']:
                                    if ' ' not in M[1]:
                                        if type(M[2]) in {set}:
                                            if len(M[2]) > 0:
                                                locals()['\u0393'] = True
                                                for l in M[2]:
                                                    if type(l) not in {str}:
                                                        locals()['\u0393'] = False
                                                        break
                                                    elif len(l) != 1:
                                                        locals()['\u0393'] = False
                                                        break
                                                if locals()['\u0393']:
                                                    if ' ' in M[2]:
                                                        if M[1] <= M[2]:
                                                            if {M[4], M[5], M[6]} <= M[0]:
                                                                if M[5] != M[6]:
                                                                    if callable(M[3]):
                                                                        if len(signature(M[3]).parameters) == 2:
                                                                            if [M[3](q, l) in {(locals()['q\''], locals()['l\''], locals()['\u0394']) for locals()['q\''] in M[0] for locals()['l\''] in M[2] for locals()['\u0394'] in {'L', 'R'}} for q in M[0] - {M[5], M[6]} for l in M[2]] == [True] * (len(M[0] - {M[5], M[6]}) * len(M[2])):
                                                                                self._M = M
                                                                                self.__name__ = 'TMR'
    def __contains__(self, w):
        try:
            if len(self._M) == 5:
                q = self._M[3]
                for l in w:
                    q = self._M[2](q, l)
                return q in self._M[4]
            elif len(self._M) == 6:
                queue = [(self._M[4], 0, tuple())]
                while len(queue) > 0:
                    q = queue.pop(0)
                    a = q[1]
                    stack = list(q[2])
                    b = stack.pop() if len(stack) > 0 else ''
                    q = q[0]
                    if a == len(w) and len(stack + ([b] if b != '' else list())) == 0:
                        if q in self._M[5]:
                            return True
                        else:
                            for i in range(len(self._M[3](q, '', b))):
                                queue.append((list(self._M[3](q, '', b))[i][0], a, tuple(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                            if b != '':
                                stack.append(b)
                                b = ''
                                for i in range(len(self._M[3](q, '', b))):
                                    queue.append((list(self._M[3](q, '', b))[i][0], a, tuple(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                    else:
                        if a < len(w):
                            for i in range(len(self._M[3](q, w[a], b))):
                                queue.append((list(self._M[3](q, w[a], b))[i][0], a + 1, tuple(stack + ([list(self._M[3](q, w[a], b))[i][1]] if list(self._M[3](q, w[a], b))[i][1] != '' else list()))))
                            for i in range(len(self._M[3](q, '', b))):
                                queue.append((list(self._M[3](q, '', b))[i][0], a, tuple(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                            if b != '':
                                stack.append(b)
                                b = ''
                                for i in range(len(self._M[3](q, w[a], b))):
                                    queue.append((list(self._M[3](q, w[a], b))[i][0], a + 1, tuple(stack + ([list(self._M[3](q, w[a], b))[i][1]] if list(self._M[3](q, w[a], b))[i][1] != '' else list()))))
                                for i in range(len(self._M[3](q, '', b))):
                                    queue.append((list(self._M[3](q, '', b))[i][0], a, tuple(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                        elif len(stack + ([b] if b != '' else list())) > 0:
                            for i in range(len(self._M[3](q, '', b))):
                                queue.append((list(self._M[3](q, '', b))[i][0], a, tuple(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                            if b != '':
                                stack.append(b)
                                b = ''
                                for i in range(len(self._M[3](q, '', b))):
                                    queue.append((list(self._M[3](q, '', b))[i][0], a, tuple(stack + ([list(self._M[3](q, '', b))[i][1]] if list(self._M[3](q, '', b))[i][1] != '' else list()))))
                return False
            else:
                s = list(w) if len(w) > 0 else [' ']
                l = 0
                q = self._M[4]
                while q != self._M[5] and q != self._M[6]:
                    q = self._M[3](q, s[l])
                    s[l] = q[1]
                    if q[2] == 'R':
                        l += 1
                    else:
                        l -= 1
                    if l >= len(s):
                        s += [' ']
                    elif l < 0:
                        s = [' '] + s
                        l = 0
                    q = q[0]
                return q == self._M[5]
        except KeyError:
            return False
    def __iter__(self):
        return self
    def __next__(self):
        return self.next()
    def next(self):
        while len(self.__w) <= 2 ** 8 - 1:
            w = self.__w
            locals()['\u0393'] = sorted(self._M[1] | {''})
            b = len(locals()['\u0393'])
            n = locals()['\u0393'].index(self.__w[-1]) if len(self.__w) > 0 else 0
            self.__w = list(self.__w) if len(self.__w) > 0 else ['']
            if locals()['\u0393'].index(self.__w[-1]) < b - 1:
                n += 1
                self.__w[-1] = locals()['\u0393'][n]
            else:
                n = 1
                for i in range(-1, -len(self.__w), -1):
                    if locals()['\u0393'].index(self.__w[i]) == b - 1:
                        self.__w[i] = locals()['\u0393'][n]
                    else:
                        self.__w[i] = locals()['\u0393'][locals()['\u0393'].index(self.__w[i])+1]
                        self.__w[i-1] = locals()['\u0393'][locals()['\u0393'].index(self.__w[i-1])-1]
                if locals()['\u0393'].index(self.__w[0]) == b - 1:
                    self.__w[0] = locals()['\u0393'][n]
                    self.__w = [locals()['\u0393'][n]] + self.__w
                else:
                    self.__w[0] = locals()['\u0393'][locals()['\u0393'].index(self.__w[0])+1]
            self.__w = ''.join(self.__w)
            if w in self:
                return w
        raise StopIteration()
    def __eq__(self, other):
        for w in self:
            if w not in other:
                return False
        for w in other:
            if w not in self:
                return False
        return True
    def __ne__(self, other):
        for w in self:
            if w not in other:
                return True
        for w in other:
            if w not in self:
                return True
        return False
    def __lt__(self, other):
        for w in self:
            if w not in other:
                return False
        return self != other
    def __le__(self, other):
        return self < other or self == other
    def __gt__(self, other):
        for w in other:
            if w not in self:
                return False
        return self != other
    def __ge__(self, other):
        return self > other or self == other
    def __invert__(self):
        if len(self._M) == 5:
            return L((self._M[0], self._M[1], lambda q, l: self._M[2](q, l), self._M[3], self._M[0] - self._M[4]))
    def __and__(self, other):
        if len(self._M) == 5:
            if len(other._M) == 5:
                dfa = dict()
                for x in self._M[0]:
                    for y in other._M[0]:
                        dfa[(x, y)] = dict()
                        for l in self._M[1] | other._M[1]:
                            dfa[(x, y)][l] = (self._M[2](x, l), other._M[2](y, l))
                return L(({(x, y) for x in self._M[0] for y in other._M[0]}, self._M[1] | other._M[1], lambda q, l: dfa[q][l], (self._M[3], other._M[3]), {(x, y) for x in self._M[0] for y in other._M[0] if x in self._M[4] and y in other._M[4]}))
    def __or__(self, other):
        if len(self._M) == 5:
            if len(other._M) == 5:
                dfa = dict()
                for x in self._M[0]:
                    for y in other._M[0]:
                        dfa[(x, y)] = dict()
                        for l in self._M[1] | other._M[1]:
                            dfa[(x, y)][l] = (self._M[2](x, l), other._M[2](y, l))
                return L(({(x, y) for x in self._M[0] for y in other._M[0]}, self._M[1] | other._M[1], lambda q, l: dfa[q][l], (self._M[3], other._M[3]), {(x, y) for x in self._M[0] for y in other._M[0] if x in self._M[4] or y in other._M[4]}))
            elif len(other._M) == 6:
                R = dict()
                for q in self._M[0]:
                    R[''.join(['Q', str(q)])] = set()
                    if q in self._M[4]:
                        R[''.join(['Q', str(q)])].add(('',))
                    for l in self._M[1]:
                        R[''.join(['Q', str(q)])].add((l, ''.join(['Q', str(self._M[2](q, l))])))
                return L((set(R.keys()), self._M[1], R, ''.join(['Q', str(self._M[3])]))) | L(other._M)
        elif len(self._M) == 6:
            if len(other._M) == 5:
                return other | self
            elif len(other._M) == 6:
                pda1 = dict()
                for q in self._M[0]:
                    pda1[list(self._M[0]).index(q)+1] = dict()
                    for a in self._M[1] | {''}:
                        pda1[list(self._M[0]).index(q)+1][a] = dict()
                        for b in self._M[2] | {''}:
                            pda1[list(self._M[0]).index(q)+1][a][b] = set()
                            for r in self._M[0]:
                                for l in self._M[2] | {''}:
                                    if (r, l) in self._M[3](q, a, b):
                                        if b != '' and l == '' or b == '' and l != '':
                                            pda1[list(self._M[0]).index(q)+1][a][b].add((list(self._M[0]).index(r)+1, l))
                                        elif b != '' and l != '':
                                            pda1[list(self._M[0]).index(q)+1][a][b].add((len(self._M[0])+list(self._M[0]).index(q)+1, ''))
                                            if list(self._M[0]).index(q) + 1 + len(self._M[0]) not in pda1:
                                                pda1[list(self._M[0]).index(q)+1+len(self._M[0])] = dict()
                                                for x in self._M[1] | {''}:
                                                    pda1[list(self._M[0]).index(q)+1+len(self._M[0])][x] = dict()
                                                    for y in self._M[2] | {''}:
                                                        pda1[list(self._M[0]).index(q)+1+len(self._M[0])][x][y] = set()
                                            pda1[list(self._M[0]).index(q)+1+len(self._M[0])][''][''].add((list(self._M[0]).index(r)+1, l))
                                        elif b == '' and l == '':
                                            i = rand.randint(0, len(self._M[2]) - 1)
                                            pda1[list(self._M[0]).index(q)+1][a][b].add((len(self._M[0])+list(self._M[0]).index(q)+1, list(self._M[2])[i]))
                                            if list(self._M[0]).index(q) + 1 + len(self._M[0]) not in pda1:
                                                pda1[list(self._M[0]).index(q)+1+len(self._M[0])] = dict()
                                                for x in self._M[1] | {''}:
                                                    pda1[list(self._M[0]).index(q)+1+len(self._M[0])][x] = dict()
                                                    for y in self._M[1] | {''}:
                                                        pda1[list(self._M[0]).index(q)+1+len(self._M[0])][x][y] = set()
                                            pda1[list(self._M[0]).index(q)+1+len(self._M[0])][''][list(self._M[2])[i]].add((list(self._M[0]).index(r)+1, l))
                i = rand.randint(0, len(self._M[2]) - 1)
                x = max(pda1.keys())
                for q in self._M[5]:
                    pda1[list(self._M[0]).index(q)+1][''][''].add((x + 1, list(self._M[2])[i]))
                pda1[x+1] = dict()
                for a in self._M[1] | {''}:
                    pda1[x+1][a] = dict()
                    for b in self._M[2] | {''}:
                        pda1[x+1][a][b] = set()
                        if a == '' and b == list(self._M[2])[i]:
                            pda1[x+1][a][b].add((x + 2, ''))
                pda1[x+2] = dict()
                for a in self._M[1] | {''}:
                    pda1[x+2][a] = dict()
                    for b in self._M[2] | {''}:
                        pda1[x+2][a][b] = set()
                R1 = dict()
                for p in set(pda1.keys()):
                    if 'A({}, {})'.format(p, p) not in R1:
                        R1['A({}, {})'.format(p, p)] = set()
                    R1['A({}, {})'.format(p, p)].add(('',))
                for p in set(pda1.keys()):
                    for q in set(pda1.keys()):
                        for r in set(pda1.keys()):
                            if 'A({}, {})'.format(p, q) not in R1:
                                R1['A({}, {})'.format(p, q)] = set()
                            R1['A({}, {})'.format(p, q)].add(('A({}, {})'.format(p, r), 'A({}, {})'.format(r, q)))
                for p in set(pda1.keys()):
                    for r in set(pda1.keys()):
                        for s in set(pda1.keys()):
                            for q in set(pda1.keys()):
                                for a in self._M[1] | {''}:
                                    for b in self._M[1] | {''}:
                                        for u in self._M[2]:
                                            if 'A({}, {})'.format(p, q) not in R1:
                                                R1['A({}, {})'.format(p, q)] = set()
                                            if (r, u) in pda1[p][a][''] and (q, '') in pda1[s][b][u]:
                                                R1['A({}, {})'.format(p, q)].add((a, 'A({}, {})'.format(r, s), b))
                pda2 = dict()
                for q in other._M[0]:
                    pda2[list(other._M[0]).index(q)+1] = dict()
                    for a in other._M[1] | {''}:
                        pda2[list(other._M[0]).index(q)+1][a] = dict()
                        for b in other._M[2] | {''}:
                            pda2[list(other._M[0]).index(q)+1][a][b] = set()
                            for r in other._M[0]:
                                for l in other._M[2] | {''}:
                                    if (r, l) in other._M[3](q, a, b):
                                        if b != '' and l == '' or b == '' and l != '':
                                            pda2[list(other._M[0]).index(q)+1][a][b].add((list(other._M[0]).index(r)+1, l))
                                        elif b != '' and l != '':
                                            pda2[list(other._M[0]).index(q)+1][a][b].add((len(other._M[0])+list(other._M[0]).index(q)+1, ''))
                                            if list(other._M[0]).index(q) + 1 + len(other._M[0]) not in pda2:
                                                pda2[list(other._M[0]).index(q)+1+len(other._M[0])] = dict()
                                                for x in other._M[1] | {''}:
                                                    pda2[list(other._M[0]).index(q)+1+len(other._M[0])][x] = dict()
                                                    for y in other._M[2] | {''}:
                                                        pda2[list(other._M[0]).index(q)+1+len(other._M[0])][x][y] = set()
                                            pda2[list(other._M[0]).index(q)+1+len(other._M[0])][''][''].add((list(other._M[0]).index(r)+1, l))
                                        elif b == '' and l == '':
                                            i = rand.randint(0, len(other._M[2]) - 1)
                                            pda2[list(other._M[0]).index(q)+1][a][b].add((len(other._M[0])+list(other._M[0]).index(q)+1, list(other._M[2])[i]))
                                            if list(other._M[0]).index(q) + 1 + len(other._M[0]) not in pda2:
                                                pda2[list(other._M[0]).index(q)+1+len(other._M[0])] = dict()
                                                for x in other._M[1] | {''}:
                                                    pda2[list(other._M[0]).index(q)+1+len(other._M[0])][x] = dict()
                                                    for y in other._M[2] | {''}:
                                                        pda2[list(other._M[0]).index(q)+1+len(other._M[0])][x][y] = set()
                                            pda2[list(other._M[0]).index(q)+1+len(other._M[0])][''][list(other._M[2])[i]].add((list(other._M[0]).index(r)+1, l))
                i = rand.randint(0, len(other._M[2]) - 1)
                x = max(pda2.keys())
                for q in other._M[5]:
                    pda2[list(other._M[0]).index(q)+1][''][''].add((x + 1, list(other._M[2])[i]))
                pda2[x+1] = dict()
                for a in other._M[1] | {''}:
                    pda2[x+1][a] = dict()
                    for b in other._M[2] | {''}:
                        pda2[x+1][a][b] = set()
                        if a == '' and b == list(other._M[2])[i]:
                            pda2[x+1][a][b].add((x + 2, ''))
                pda2[x+2] = dict()
                for a in other._M[1] | {''}:
                    pda2[x+2][a] = dict()
                    for b in other._M[2] | {''}:
                        pda2[x+2][a][b] = set()
                R2 = dict()
                for p in set(pda2.keys()):
                    if 'B({}, {})'.format(p, p) not in R2:
                        R2['B({}, {})'.format(p, p)] = set()
                    R2['B({}, {})'.format(p, p)].add(('',))
                for p in set(pda2.keys()):
                    for q in set(pda2.keys()):
                        for r in set(pda2.keys()):
                            if 'B({}, {})'.format(p, q) not in R2:
                                R2['B({}, {})'.format(p, q)] = set()
                            R2['B({}, {})'.format(p, q)].add(('B({}, {})'.format(p, r), 'B({}, {})'.format(r, q)))
                for p in set(pda2.keys()):
                    for r in set(pda2.keys()):
                        for s in set(pda2.keys()):
                            for q in set(pda2.keys()):
                                for a in other._M[1] | {''}:
                                    for b in other._M[1] | {''}:
                                        for u in other._M[2]:
                                            if 'B({}, {})'.format(p, q) not in R2:
                                                R2['B({}, {})'.format(p, q)] = set()
                                            if (r, u) in pda2[p][a][''] and (q, '') in pda2[s][b][u]:
                                                R2['B({}, {})'.format(p, q)].add((a, 'B({}, {})'.format(r, s), b))
                R = R1
                R.update(R2)
                R.update({'<S>': {('A({}, {})'.format(min(pda1.keys()), max(pda1.keys())),), ('B({}, {})'.format(min(pda2.keys()), max(pda2.keys())),)}})
                return L((set(R1.keys()) | set(R2.keys()) | {'<S>'}, self._M[1] | other._M[1], R, '<S>'))
    def __add__(self, other):
        if len(self._M) == 5:
            if len(other._M) == 5:
                nfa1 = dict()
                for q in self._M[0]:
                    nfa1[list(self._M[0]).index(q)+1] = dict()
                    for l in self._M[1] | {''}:
                        nfa1[list(self._M[0]).index(q)+1][l] = set()
                        if l == '':
                            nfa1[list(self._M[0]).index(q)+1][l].add(list(self._M[0]).index(q)+1)
                        else:
                            nfa1[list(self._M[0]).index(q)+1][l].add(list(self._M[0]).index(self._M[2](q, l))+1)
                nfa2 = dict()
                for q in other._M[0]:
                    nfa2[list(other._M[0]).index(q)+1+len(self._M[0])] = dict()
                    for l in other._M[1] | {''}:
                        nfa2[list(other._M[0]).index(q)+1+len(self._M[0])][l] = set()
                        if l == '':
                            nfa2[list(other._M[0]).index(q)+1+len(self._M[0])][l].add(list(other._M[0]).index(q)+1+len(self._M[0]))
                        else:
                            nfa2[list(other._M[0]).index(q)+1+len(self._M[0])][l].add(list(other._M[0]).index(other._M[2](q, l))+1+len(self._M[0]))
                nfa = dict()
                for q in set(nfa1.keys()) | set(nfa2.keys()):
                    nfa[q] = dict()
                    for l in self._M[1] | other._M[1] | {''}:
                        if q in set(nfa1.keys()) - {list(self._M[0]).index(r) + 1 for r in self._M[4]}:
                            nfa[q][l] = nfa1[q][l]
                        elif q in {list(self._M[0]).index(r) + 1 for r in self._M[4]}:
                            if l == '':
                                nfa[q][l] = nfa1[q][l] | {list(other._M[0]).index(other._M[3]) + 1 + len(self._M[0])}
                            else:
                                nfa[q][l] = nfa1[q][l]
                        elif q in set(nfa2.keys()):
                            nfa[q][l] = nfa2[q][l]
                        else:
                            nfa[q][l] = set()
                return L((set(nfa1.keys()) | set(nfa2.keys()), self._M[1] | other._M[1], lambda q, l: nfa[q][l], list(self._M[0]).index(self._M[3]) + 1, {list(other._M[0]).index(r) + 1 + len(self._M[0]) for r in other._M[4]}))
            elif len(other._M) == 6:
                R = dict()
                for q in self._M[0]:
                    R[''.join(['Q', str(q)])] = set()
                    if q in self._M[4]:
                        R[''.join(['Q', str(q)])].add(('',))
                    for l in self._M[1]:
                        R[''.join(['Q', str(q)])].add((l, ''.join(['Q', str(self._M[2](q, l))])))
                return L((set(R.keys()), self._M[1], R, ''.join(['Q', str(self._M[3])]))) + L(other._M)
        elif len(self._M) == 6:
            if len(other._M) == 5:
                R = dict()
                for q in other._M[0]:
                    R[''.join(['Q', str(q)])] = set()
                    if q in other._M[4]:
                        R[''.join(['Q', str(q)])].add(('',))
                    for l in other._M[1]:
                        R[''.join(['Q', str(q)])].add((l, ''.join(['Q', str(other._M[2](q, l))])))
                return L(self._M) + L((set(R.keys()), other._M[1], R, ''.join(['Q', str(other._M[3])])))
            elif len(other._M) == 6:
                pda1 = dict()
                for q in self._M[0]:
                    pda1[list(self._M[0]).index(q) + 1] = dict()
                    for a in self._M[1] | {''}:
                        pda1[list(self._M[0]).index(q) + 1][a] = dict()
                        for b in self._M[2] | {''}:
                            pda1[list(self._M[0]).index(q) + 1][a][b] = set()
                            for r in self._M[0]:
                                for l in self._M[2] | {''}:
                                    if (r, l) in self._M[3](q, a, b):
                                        if b != '' and l == '' or b == '' and l != '':
                                            pda1[list(self._M[0]).index(q) + 1][a][b].add((list(self._M[0]).index(r) + 1, l))
                                        elif b != '' and l != '':
                                            pda1[list(self._M[0]).index(q) + 1][a][b].add((len(self._M[0]) + list(self._M[0]).index(q) + 1, ''))
                                            if list(self._M[0]).index(q) + 1 + len(self._M[0]) not in pda1:
                                                pda1[list(self._M[0]).index(q) + 1 + len(self._M[0])] = dict()
                                                for x in self._M[1] | {''}:
                                                    pda1[list(self._M[0]).index(q) + 1 + len(self._M[0])][x] = dict()
                                                    for y in self._M[2] | {''}:
                                                        pda1[list(self._M[0]).index(q) + 1 + len(self._M[0])][x][y] = set()
                                            pda1[list(self._M[0]).index(q) + 1 + len(self._M[0])][''][''].add((list(self._M[0]).index(r) + 1, l))
                                        elif b == '' and l == '':
                                            i = rand.randint(0, len(self._M[2]) - 1)
                                            pda1[list(self._M[0]).index(q) + 1][a][b].add((len(self._M[0]) + list(self._M[0]).index(q) + 1, list(self._M[2])[i]))
                                            if list(self._M[0]).index(q) + 1 + len(self._M[0]) not in pda1:
                                                pda1[list(self._M[0]).index(q) + 1 + len(self._M[0])] = dict()
                                                for x in self._M[1] | {''}:
                                                    pda1[list(self._M[0]).index(q) + 1 + len(self._M[0])][x] = dict()
                                                    for y in self._M[1] | {''}:
                                                        pda1[list(self._M[0]).index(q) + 1 + len(self._M[0])][x][y] = set()
                                            pda1[list(self._M[0]).index(q) + 1 + len(self._M[0])][''][list(self._M[2])[i]].add((list(self._M[0]).index(r) + 1, l))
                i = rand.randint(0, len(self._M[2]) - 1)
                x = max(pda1.keys())
                for q in self._M[5]:
                    pda1[list(self._M[0]).index(q) + 1][''][''].add((x + 1, list(self._M[2])[i]))
                pda1[x + 1] = dict()
                for a in self._M[1] | {''}:
                    pda1[x + 1][a] = dict()
                    for b in self._M[2] | {''}:
                        pda1[x + 1][a][b] = set()
                        if a == '' and b == list(self._M[2])[i]:
                            pda1[x + 1][a][b].add((x + 2, ''))
                pda1[x + 2] = dict()
                for a in self._M[1] | {''}:
                    pda1[x + 2][a] = dict()
                    for b in self._M[2] | {''}:
                        pda1[x + 2][a][b] = set()
                R1 = dict()
                for p in set(pda1.keys()):
                    if 'A({}, {})'.format(p, p) not in R1:
                        R1['A({}, {})'.format(p, p)] = set()
                    R1['A({}, {})'.format(p, p)].add(('',))
                for p in set(pda1.keys()):
                    for q in set(pda1.keys()):
                        for r in set(pda1.keys()):
                            if 'A({}, {})'.format(p, q) not in R1:
                                R1['A({}, {})'.format(p, q)] = set()
                            R1['A({}, {})'.format(p, q)].add(('A({}, {})'.format(p, r), 'A({}, {})'.format(r, q)))
                for p in set(pda1.keys()):
                    for r in set(pda1.keys()):
                        for s in set(pda1.keys()):
                            for q in set(pda1.keys()):
                                for a in self._M[1] | {''}:
                                    for b in self._M[1] | {''}:
                                        for u in self._M[2]:
                                            if 'A({}, {})'.format(p, q) not in R1:
                                                R1['A({}, {})'.format(p, q)] = set()
                                            if (r, u) in pda1[p][a][''] and (q, '') in pda1[s][b][u]:
                                                R1['A({}, {})'.format(p, q)].add((a, 'A({}, {})'.format(r, s), b))
                pda2 = dict()
                for q in other._M[0]:
                    pda2[list(other._M[0]).index(q) + 1] = dict()
                    for a in other._M[1] | {''}:
                        pda2[list(other._M[0]).index(q) + 1][a] = dict()
                        for b in other._M[2] | {''}:
                            pda2[list(other._M[0]).index(q) + 1][a][b] = set()
                            for r in other._M[0]:
                                for l in other._M[2] | {''}:
                                    if (r, l) in other._M[3](q, a, b):
                                        if b != '' and l == '' or b == '' and l != '':
                                            pda2[list(other._M[0]).index(q) + 1][a][b].add((list(other._M[0]).index(r) + 1, l))
                                        elif b != '' and l != '':
                                            pda2[list(other._M[0]).index(q) + 1][a][b].add((len(other._M[0]) + list(other._M[0]).index(q) + 1, ''))
                                            if list(other._M[0]).index(q) + 1 + len(other._M[0]) not in pda2:
                                                pda2[list(other._M[0]).index(q) + 1 + len(other._M[0])] = dict()
                                                for x in other._M[1] | {''}:
                                                    pda2[list(other._M[0]).index(q) + 1 + len(other._M[0])][x] = dict()
                                                    for y in other._M[2] | {''}:
                                                        pda2[list(other._M[0]).index(q) + 1 + len(other._M[0])][x][y] = set()
                                            pda2[list(other._M[0]).index(q) + 1 + len(other._M[0])][''][''].add((list(other._M[0]).index(r) + 1, l))
                                        elif b == '' and l == '':
                                            i = rand.randint(0, len(other._M[2]) - 1)
                                            pda2[list(other._M[0]).index(q) + 1][a][b].add((len(other._M[0]) + list(other._M[0]).index(q) + 1, list(other._M[2])[i]))
                                            if list(other._M[0]).index(q) + 1 + len(other._M[0]) not in pda2:
                                                pda2[list(other._M[0]).index(q) + 1 + len(other._M[0])] = dict()
                                                for x in other._M[1] | {''}:
                                                    pda2[list(other._M[0]).index(q) + 1 + len(other._M[0])][x] = dict()
                                                    for y in other._M[2] | {''}:
                                                        pda2[list(other._M[0]).index(q) + 1 + len(other._M[0])][x][y] = set()
                                            pda2[list(other._M[0]).index(q) + 1 + len(other._M[0])][''][list(other._M[2])[i]].add((list(other._M[0]).index(r) + 1, l))
                i = rand.randint(0, len(other._M[2]) - 1)
                x = max(pda2.keys())
                for q in other._M[5]:
                    pda2[list(other._M[0]).index(q) + 1][''][''].add((x + 1, list(other._M[2])[i]))
                pda2[x + 1] = dict()
                for a in other._M[1] | {''}:
                    pda2[x + 1][a] = dict()
                    for b in other._M[2] | {''}:
                        pda2[x + 1][a][b] = set()
                        if a == '' and b == list(other._M[2])[i]:
                            pda2[x + 1][a][b].add((x + 2, ''))
                pda2[x + 2] = dict()
                for a in other._M[1] | {''}:
                    pda2[x + 2][a] = dict()
                    for b in other._M[2] | {''}:
                        pda2[x + 2][a][b] = set()
                R2 = dict()
                for p in set(pda2.keys()):
                    if 'B({}, {})'.format(p, p) not in R2:
                        R2['B({}, {})'.format(p, p)] = set()
                    R2['B({}, {})'.format(p, p)].add(('',))
                for p in set(pda2.keys()):
                    for q in set(pda2.keys()):
                        for r in set(pda2.keys()):
                            if 'B({}, {})'.format(p, q) not in R2:
                                R2['B({}, {})'.format(p, q)] = set()
                            R2['B({}, {})'.format(p, q)].add(('B({}, {})'.format(p, r), 'B({}, {})'.format(r, q)))
                for p in set(pda2.keys()):
                    for r in set(pda2.keys()):
                        for s in set(pda2.keys()):
                            for q in set(pda2.keys()):
                                for a in other._M[1] | {''}:
                                    for b in other._M[1] | {''}:
                                        for u in other._M[2]:
                                            if 'B({}, {})'.format(p, q) not in R2:
                                                R2['B({}, {})'.format(p, q)] = set()
                                            if (r, u) in pda2[p][a][''] and (q, '') in pda2[s][b][u]:
                                                R2['B({}, {})'.format(p, q)].add((a, 'B({}, {})'.format(r, s), b))
                R = R1
                R.update(R2)
                R.update({'<S>': {('A({}, {})'.format(min(pda1.keys()), max(pda1.keys())), 'B({}, {})'.format(min(pda2.keys()), max(pda2.keys())))}})
                return L((set(R1.keys()) | set(R2.keys()) | {'<S>'}, self._M[1] | other._M[1], R, '<S>'))
    def __sub__(self, other):
        return self & ~other
    def __key(self):
        if len(self._M) == 5:
            return (frozenset(self._M[0]), frozenset(self._M[1]), self._M[2], self._M[3], frozenset(self._M[4]))
        elif len(self._M) == 6:
            return (frozenset(self._M[0]), frozenset(self._M[1]), frozenset(self._M[2]), self._M[3], self._M[4], frozenset(self._M[5]))
        else:
            return (frozenset(self._M[0]), frozenset(self._M[1]), frozenset(self._M[2]), self._M[3], self._M[4], self._M[5], self._M[6])
    def __hash__(self):
        return hash(self.__key())

class Trie:
    class Node:
        def __init__(self):
            self.__children = dict()
            self.__end = False
        def children(self) -> dict:
            return self.__children
        def isLeaf(self) -> bool:
            return self.__end
        def setLeaf(self):
            self.__end = not self.__end
    def __init__(self):
        self.__root = Trie.Node()
    def insert(self, w: str):
        curr = self.__root
        for l in range(len(w)):
            if w[l] not in curr.children():
                curr.children()[w[l]] = Trie.Node()
            curr = curr.children()[w[l]]
        curr.setLeaf()
    def __contains__(self, w: str) -> bool:
        curr = self.__root
        for l in range(len(w)):
            if w[l] not in curr.children():
                return False
            curr = curr.children()[w[l]]
        return curr.isLeaf()