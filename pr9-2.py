# 일반적인 삽입 정렬 알고리즘응 사용해서
# 리스트 [2, 4, 5, 1, 3]을 내림차순 정렬하는 과정 알고리즘

# 삽입 정렬
# 입력: 리스트 a
# 출력: 없음(입력으로 주어진 a가 정렬됨)

def ins_sort(a):
    n = len(a)
    for i in range(1, n):  # 1부터 n-1까지
        key = a[i]        # i번 위치에 있는 값을 key에 저장
        j = i - 1  # j를 i바로 왼쪽 위치로 저장

        # 리스트의 j번 위치에 있는 값과 key를 비교해 key가 삽입될 적절한 위치를 찾음
        while j >= 0 and a[j] < key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


d = [2, 4, 5, 1, 3]
ins_sort(d)
print(d)
