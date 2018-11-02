d = open('p022_names.txt').read().split('","')
d[0] = d[0][1:]
d[-1] = d[-1][:-1]
d.sort()
print(sum(sum(ord(x)-ord('A')+1 for x in d[i])*(i+1) for i in range(len(d))))