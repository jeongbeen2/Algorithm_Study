"""- <list>.sort()를 사용하면 원본 리스트 순서를 변화시킬 수 있습니다.

- sorted(<list>)를 사용하면 정렬된 새로운 리스트를 반환 받을 수 있습니다.

- <list>.sort()는 새로운 복사본을 만들지 않기 때문에 sorted(<list>) 함수보다 빠릅니다."""

# print(sorted(map(int,input().split()))[1])

n = list(map(int, input().split()))
n.sort()
print(n[1])
