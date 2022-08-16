'''
1. input에 6 3 과 같이 공백을 기준으로 숫자 2개가 주어진다.
2. 위와 같이 주어졌을 경우 6의 약수 중 3번째 숫자를 구하는 코드를 작성해라
'''


# ----모법 정답 풀이----
n, k = map(int, input().split())
cnt = 0

for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)



# ----내가 시도한 풀이----
n, k = map(int, input().split())

print(-1) if len([i for i in range(1, n+1) if n % i == 0]) < k else print([i for i in range(1, n+1) if n % i == 0][k-1])


'''
3항 연산자를 활용해서 구연을 해 보았다. 
하지만 리스트를 먼저 구현하고 그런다음에 k번째 인덱스를 찾게 됨으로써 n과 k의 숫자가 커지게 된다면 시간이 효율적이지 못한 알고리즘이라 생각한다.
'''