A = set()
B = []
n=int(input())
for i in range(n):
	new=int(input())
	if new not in A:
		A.add(new)
		B.append(new)
for k in B:
    print(k)
