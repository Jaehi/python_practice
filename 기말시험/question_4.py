# N, K = map(int,input().split())

N = 30
K = 5

count_1 = 1
count_2 = 1

if N % K == 0:

        while True:
            N = N - K
            # print(N)
            if N == 0:
                break
            count_1 += 1

    # while True: 이 코드는 진짜 만약 N을 K로 나누는 거일ㄷ 때
    #     N = int(N / K)
    #     print(N)
    #     if N == 0:
    #         break
    # count_1 += 1

else:
    while N >= 1:
        N = N - 1
        count_2 += 1





print(count_1, count_2)

