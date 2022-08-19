# 2022 KAKAO TECH INTERNSHIP 문제2

# 내가 푼 코드
from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    cnt = 0
    while True: # JAVA 에서는 do while문이 있어서 유용하게 사용할 수 있었으나, 파이썬에서는 없기 때문에 위와 같이 사용함.
        if sum_q1 == sum_q2 or cnt > 4*len(queue1):
            break
        if sum_q1 > sum_q2:
            sum_q2 += q1[0]
            sum_q1 -= q1[0]
            q2.append(q1.popleft())
            cnt += 1
        else:
            sum_q1 += q2[0]
            sum_q2 -= q2[0]
            q1.append(q2.popleft())
            cnt += 1
    if cnt > 4*len(queue1):
        return -1
    return cnt



# 처음 시도 했었던 코드 (time out)
def solution(queue1, queue2):

    while sum(queue1) != sum(queue2):
        if sum(queue1) > sum(queue2):
            queue2.append(queue1.pop(0)) # 중요: 이부분에서 time out 발생. 왜냐? list에서 pop은 O(n)의 시간복잡도를 가짐.
            cnt += 1

        if sum(queue1) < sum(queue2):
            queue1.append(queue2.pop(0))
            cnt += 1

    if cnt > len(queue1)+ len(queue2):
        return -1

    return cnt

'''
초기 시도했던 방법이 타임아웃이 나온 이유는 먼저, 각 연산을 수행할때마다 list의 sum을 거쳐야 하며, 또한
list로 되어 있는 queue1과 queue2를 deque로 전환하지 않았기 때문이다.

deque는 linked list로 구현되어 있기 때문에 popleft 연산과 list의 pop(0)은 같은 결과를 나타내 주지만
popleft는 시간복잡도가 O(1)인 반면에 pop(0)은 O(n)임.

이 부분을 생각하지 않고 구현하게 되어서 시간이 좀 걸렸고, deque는 슬라이싱이 되지 않기 때문에 다른 로직으로 코드를 짬. 
'''