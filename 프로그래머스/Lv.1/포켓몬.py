def solution(nums):
    length = len(nums)//2
    nums = list(set(nums))
    if length < len(nums):
        answer = length
    else:
        answer = len(nums)
    return answer

# 다른 사람 풀이
def solution(ls):
    return min(len(ls)/2, len(set(ls)))
