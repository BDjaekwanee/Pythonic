# 프로그래머스에서 2022 KAKAO TECH INTERNSHIP 문제가 나왔는데 아직 약150명 정도 밖에 풀지 않았어서
# 먼가 남들보다 먼저 풀어보고자 하는 욕구가 강하게 느껴져서 바로 풀어본 알고리즘.

def solution(survey, choices):
    s = ''
    for i, c in zip(survey, choices):
        mydic = {1:i[0]*3, 2:i[0]*2, 3:i[0]*1, 4:'', 5:i[1], 6:i[1]*2, 7:i[1]*3} #딕셔너리 형태로 전환해주어서 score 점수를 셀 수 있게 만들어 주었음.
        
        s += mydic[c] # 이렇게 하게 되면 RRRTTANA 뭐 이런식으로 나오는데 이걸 리스트로 바꾸고 카운트를 셀 필요가 있었음.
    s = list(s)
    
    answer =''
    
    # 이 부분의 로직은 카카오에서 성격 유형이 ENTP 이런식으로 순서가 있기 때문에 순서에 맞게 결과물을 짜야 됬고, 때문에 if문을 활용하여 
    # 문제에서 제시한 순서대로 정돈되게 구연하였음.
    # 동점인 경우 사전순이 먼저라고 해서 if 문에서 같거나 크다, 를 활용해 로직 적용.

    if s.count('R') >= s.count('T'):
        answer += 'R'
    else: answer += 'T'
    
    if s.count('C') >= s.count('F'):
        answer += 'C'
    else: answer += 'F'
    
    if s.count('J') >= s.count('M'):
        answer += 'J'
    else: answer += 'M'
    
    if s.count('A') >= s.count('N'):
        answer += 'A'
    else: answer += 'N'
    
    return answer