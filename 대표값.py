'''
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세 요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높 은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.


▣ 입력설명
첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어집니다. 학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

▣ 출력설명
첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다. 평균은 소수 첫째 자리에서 반올림합니다.


▣ 입력예제 1
45 73 66 87 92 67 75 79 75 80

▣ 출력예제 1 
74 7


예제설명
평균이 74점으로 평균과 가장 가까운 점수는 73(2번), 75(7번), 75(9번)입니다. 여기서 점수가 높은 75(7번), 75(9번)이 답이 될 수 있고, 75점이 두명이므로 학생번호가 빠른 7번이 답이 됩니다.

[출처] inflearn 파이썬 알고리즘 문제풀이 (김태원)
'''

#강의 정답 풀이
a=list(map(int, input().split()))
ave=sum(a)/len(a)
ave=ave+0.5
ave=int(ave)
min=2147000000
for idx, x in enumerate(a):
    tmp=abs(x-ave)
    if tmp<min:
        min=tmp
        score=x
        res=idx+1
    elif tmp==min:
        if x>score:
            score=x
            res=idx+1
print(ave, res)


#내가 푼 풀이
scores=list(map(int, input().split()))
avg=sum(a)/len(a)
avg=round(avg) #오랜만에 파이썬에서 보는 반올림 내장함수. 소수 자리 정하기 가능. round(avg) -> 소수 첫째자리에서 반올림. round(avg, 1) -> 소수 둘째 자리에서 반올림.
min = float('inf') #파이썬에서 제일 큰 숫자.
for idx, x in enumerate(scores, start=1): #enumerate star= 으로 인덱스 숫자 어디서 부터 시작할지 줄 수 있다. 넓이 구하는 알고리즘 풀때 도움 많이 되었다.
    tmp=abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        index = idx
    elif tmp == min:
        if x > score:
            score = x
            index = idx
print(avg, index)