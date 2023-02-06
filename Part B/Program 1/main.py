l = []


class Reverse:
    def __init__(self, s):
        self.s = s

    def reverse(self):
        n = 0
        for i in self.s:
            if i in ('a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U'):
                n += 1

        r = ' '.join(reversed(self.s.split(' ')))
        tup = (n, r)
        l.append(tup)


for i in range(0, 3):
    obj = Reverse(str(input("Enter string :")))
    obj.reverse()
l.sort(reverse=True)
print(l)
for i in range(0, 3):
    print(l[i][1])
