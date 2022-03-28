n = int(input('숫자를 입력해주세요:'))
for i in range(1, n):
    print('*'*i+' '*2*(n-i)+'*'*i) # 위쪽 부분(대칭)
for j in range(n, 0, -1):
    print('*'*j+' '*2*(n-j)+'*'*j) # 아래쪽 부분(대칭)