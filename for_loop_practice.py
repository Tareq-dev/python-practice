 

#1-Square Number

'''
for i in range(1,6):
    print(i*i)
    i+=1
'''   
#2-Even Number
'''
for i in range(1,102):
    if i%2==0:
     print(i)
     i+=1
    
'''

#3-ODD Number

'''
for i in range(1,101):
    if i%2 !=0:
     print(i)
     i+=1
'''
 
#4-Sum 1-10
'''
total_num = 0
for i in range(1,101):
     total_num += i
print(total_num)
'''

#5- Reverse word


'''
word = 'Javascript'
# print(len(word)-1)
for i in range(len(word)-1,-1,-1):
    print(word[i], end=" ")
    i-=1

'''