def solution(data, n): 
    # Your code here
    if n == 0:
        return None
        
    ans = []
    value_to_count = {}
    
    for value in data:
        if value not in value_to_count:
            value_to_count[value] = 0
        else:
            value_to_count[value] += 1
        
    for value in data:
        if value_to_count[value] < n:
            ans.append(value)
            
    return ans

print(solution([1,2,3], 0))
print(solution([1,2,3], 6))
print(solution([1,2,2,3,3,3,4,5,5], 1))