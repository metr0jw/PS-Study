import sys
import time

def eratos(minimum, maximum):
    global no_sqr
    global result

    for i in range(minimum, maximum+1):
        if i**2 > maximum:
            break
        elif i < 2:
            no_sqr[i] = 0
            continue
        
        sqr_num = i
        sqr_cnt = 0
        while sqr_num < maximum:
            sqr_num *= i
            if sqr_num < maximum:
                sqr_cnt += 1
        if not sqr_cnt:
            break
    
        for j in range(2, sqr_cnt+2):
            if not no_sqr[i**j]:
                continue
            no_sqr[i**j] = 0
    
    for i in range(minimum, maximum+1):
        if no_sqr[i]:
            result += 1
    
    return result
        


minimum, maximum = map(int, sys.stdin.readline().split())
result = 0
max_cnt = int(maximum ** (1/2))
no_sqr = [1 in range(max_cnt + 1)]
start = time.time()

result = eratos(minimum, maximum)
sys.stdout.write(str(result))
print(time.time() - start)
