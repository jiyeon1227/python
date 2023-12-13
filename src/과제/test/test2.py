n=int(input("n 번째 피보나치 수열을 구하세요"))
a = [1,1]

for b in range(2,n):
    a.append(1)
    a[b] = a[b-2] + a[b-1]
print(n,"번째 값: ",a[n-1])