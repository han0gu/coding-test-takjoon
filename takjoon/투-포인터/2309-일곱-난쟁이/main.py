CNT = 9
TARGET_SUM = 100

dwarfs = [int(input()) for _ in range(CNT)]
dwarfs.sort()

start = 0
end = CNT - 1
total = sum(dwarfs)

while start < end:
    tmp_total = total - dwarfs[start] - dwarfs[end]

    if tmp_total == TARGET_SUM:
        for i in range(CNT):
            if i != start and i != end:
                print(dwarfs[i])
        break
    elif tmp_total < TARGET_SUM:
        end -= 1
    else:
        start += 1
