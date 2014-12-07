import math

a = [4,13,18,12,17,7,6,2,11,10]
b = [15,19,5,20,16,3,8,14,1,9]
c = [4,13,1,3,20,19,2,11,16,12]
d = [7,17,9,15,6,14,8,5,18,10]

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result
 
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))

def standard_dev(x):
    answer = math.sqrt(sum(x)/(len(x)-1))
    return answer

def mean(x):
    answer = sum(x)/len(x)
    return answer

answer = merge_sort(a) #Change which list here ONLY!!!

print answer
print standard_dev(answer)
print mean(answer)