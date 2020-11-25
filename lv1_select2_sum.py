# 프로그래머스(programmer.co.kr) 
# level1. 두 개 뽑아서 더하기
# Q. 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
# ex) numbers = [2,1,3,4,1], result = [2,3,4,5,6,7]

# 풀이 1
def solution(numbers):                          # numbers 입력 받기
    answer = []
    for i in range(len(numbers)):               # i = 0 ~ numbers 길이 만큼 범위 순차 추출
        for j in range(i+1, len(numbers)):      # j = i+1 ~ numbers 길이 만큼 범위 순차 추출
            res = numbers[i] + numbers[j]       # i와 j를 idx 값으로 활용하여 합계 계산 결과 res 저장
            answer.append(res)                  # res 값 answer에 저장
            
    return list(sorted(set(answer)))            # set함수로 중복 제거, sorted로 정렬, list 반환



# 풀이 2
def solution(numbers):                          # numbers 입력 받기
    answer = []
    for i in range(len(numbers)):               # i = 0 ~ numbers 길이 만큼 범위 순차 추출
        for j in range(i+1, len(numbers)):      # j = i+1 ~ numbers 길이 만큼 범위 순차 추출
            res = numbers[i] + numbers[j]       # i와 j를 idx 값으로 활용하여 합계 계산 결과 res 저장
            if not res in answer:               # answer에 res 값이 없는 경우, answer에 append
                answer.append(res)              
    answer.sort()                               # answer 정렬
    return any                                  # 최종 answer 반환
