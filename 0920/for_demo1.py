#ASCII 

# UPPERCASE
# for i in range(65, 91) :
#     print(chr(i), end ='\t')
# print()

#LOWERCASE
# for i in range(97, 123) :
#     print(chr(i), end ='\t')
# print()

count, flag = 0, 0

for i in range(65, 91):
    if flag % 2 == 0:
        print(chr(i), end='\t')
    else:
        print(chr(i+32), end='\t')
    count += 1
           
    if count % 5 == 0:
        flag += 1
        print()
print()
