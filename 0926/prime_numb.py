def is_prime(numb):
    for i in range(2,numb):
        if numb % i != 0 :
            pass
        else:
            return False
        return True
 
 
f = open('result.txt', 'w') 
f.write("2\n")   
for i in range(2,250):
    prime_set = is_prime(i)
    
    if prime_set == True:
        f.write(f"{i}\n")
f.close()  
      





