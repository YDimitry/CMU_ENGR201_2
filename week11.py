
# step 1
lst = [sum(map(int,input().split()[3:])) for _ in range(int(input()))]
print(f'{sum(lst)/len(lst):.2f}')

# step2
mu = sum(lst)/len(lst)
sig = pow(sum(map(lambda x: pow((x-mu),2), lst))/len(lst),0.5)
print(f'{sig:.2f}')

# step 3
A = mu + 1.5*sig
B = mu + 0.5*sig
C = mu - 0.5*sig
D = mu - 1.5*sig

print(*map(lambda s: ('F','D','C','B','A')[(A <= s) + (B <= s) + (C <= s) + (D <= s)], lst))