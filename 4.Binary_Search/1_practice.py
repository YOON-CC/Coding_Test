##이진탐색

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid =(start+end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split())) ## 정렬된 값이 들어와야 한다.

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
    
#그러나 파이썬에서는 라이브러리를 활용한다.
#https://programming119.tistory.com/196
#코딩 테스트에서 유용하게 사용이 된다.