import sys
import time

def eratos(minimum, maximum):
    global no_sqr
    global result

    max_sqr = int(maximum ** (1/2))
    print('max_sqr: '+str(max_sqr))
    sqr_list = [i**2 for i in range(2, max_sqr+1)]
    print('sqr_list: '+str(sqr_list))
    
    for i in sqr_list:
        sqr_num = i
        sqr_cnt = 0
        print('i: '+str(i))
        print(i, maximum)
        if i == maximum:
            no_sqr[i-1] = 0
            print('no_sqr n to zero(maximum): '+str(i))
            break
        
        if sqr_num < maximum:
            sqr_cnt += 1
        while sqr_num < maximum:
            sqr_num *= 2
            print('sqr_num: '+str(sqr_num))
            if sqr_num < maximum:
                sqr_cnt += 1
        
        print('sqr_cnt:' +str(sqr_cnt))
        if not sqr_cnt:
            if i > maximum:
                break
        if sqr_cnt == 1:
            no_sqr[i-1] = 0
            print('no_sqr n to zero(cnt1): '+str(i))
            break

        sqr_num = i
        for j in range(sqr_cnt):
            print('j: '+str(j))
            print(f'{sqr_num-1}')
            if not no_sqr[sqr_num-1]:
                continue
            no_sqr[sqr_num-1] = 0
            print(f'no_sqr {sqr_num-1} to zero')
            print(f'{sqr_num}, {i}')
            if sqr_num * int(i**(1/2)) <= (maximum - minimum + 1):
                sqr_num = sqr_num * int(i**(1/2))

    print('no_sqr: '+str(no_sqr))
    for i in range(0, maximum - minimum + 1):
        if no_sqr[i]:
            result += 1
    return result
        


minimum, maximum = map(int, sys.stdin.readline().split())
result = 0
no_sqr = [1 for i in range(maximum - minimum + 1)]
start = time.time()

result = eratos(minimum, maximum)
sys.stdout.write(str(result))
#print('the time taken: '+str(time.time() - start))
