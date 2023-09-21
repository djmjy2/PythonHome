def calc_sum(start,end) : #parameter
    sum = 0
    for i in range (start, end + 1) :
        sum += i
        
    return sum
        
start= 5
end = 66
result = calc_sum(start,end) # argument, call by value
print("%d ~ %d 의 합은 %d 입니다." %(start, end, result))