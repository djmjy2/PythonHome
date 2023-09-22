#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('cat test.dat')


# In[3]:


get_ipython().system('cat data.dat')


# In[60]:


fread = None
try :
    fread = open('data.dat','r')
    #result = fread.read()
    # result = fread.readline()
    # while result :
    #     print(result, end='')
    #     result = fread.readline()
    for line in fread.readlines():
        print(line, end='')
    
except:
    print('File Not Found')
finally:
    fread.close()


# In[62]:


lyric = """
해가 지기 전에 가려했지 
너와 내가 있던 그 언덕 풍경 속에 
아주 키 작은 그 마음으로 
세상을 꿈꾸고 그리며 말했던 곳 
이제 여행을 떠나야하는 소중한 내 친구여
때론다투기도 많이했지
서로알수 없는 오해에 조각들로
하지만 머쩍은 미소만으로
너는 내가되고 나도 니가 될수 있었던 수많은 기억들
내가 항상여기 서있을께
걷다가 지친니가 나를 볼수있게
저기 저 별위에 그릴꺼야
내가 널 사랑하는 마음볼수 있게
내가 항상 여기 서 있을게
"""


# In[63]:


fwrite = None
try:
    fwrite = open('서시.txt','w')
    fwrite.write(lyric)
    print("File save Successfully.")
except Exception as err :
    print(err)
finally:
    fwrite.close()


# In[68]:


with open ('서시.txt', 'rt')as fread :
    try :
        count = 1
        for line in fread.readlines() :
            print(f'{count} : {line}', end='')
            count += 1
    except :
        print('File not Found')


# In[69]:


import json


# In[71]:


list_= ['Hello',1896, 80.5, True, 'D' ]
type(list_)


# In[72]:


str_ = json.dumps(list_)
type(str_)


# In[73]:


print(str_)


# In[74]:


obj = json.loads(str_)
type(obj)


# In[76]:


obj[3]


# In[77]:


student = {
    "stu_no" : "32121888",
    "name" : "윤휘람",
    "age" : 32,
    "address" : "서울시 관악구 신림동"
}
type(student)


# In[80]:


str_=json.dumps(student, ensure_ascii=False, indent=None)
type(str_)


# In[81]:


with open('student.dat','wt') as fwrite :
    fwrite.write(str_)
    print("File Save Successfully.")


# In[83]:


with open("student.dat","rt") as fread :
    result = fread.read()
    obj = json.loads(result)
    print(f"name = {obj['name']}, age = {obj['age']}")


# In[87]:


with open('sungjuk.json','rt') as fread :
    result = json.load(fread)
    # print(type(result)) #list
    # print(len(result))
    print(result[0]['irum'])


# In[88]:


import os
print(os.name)


# In[90]:


print(os.getcwd())


# In[91]:


get_ipython().system('pwd')


# In[92]:


os.chdir('/')
print(os.getcwd())


# In[94]:


import sys


# In[97]:


print(f"Version : {sys.version}")
print(f"Version Info : {sys.version_info}")
print(f"Platform : {sys.platform}")


# In[98]:


import platform


# In[100]:


print(f"Platform Architecture : {platform.uname()}")


# In[102]:


import socket


# In[103]:


print(f"Host name : {socket.gethostname()}")


# In[105]:


hostname = socket.gethostname()
print(socket.gethostbyname(hostname))


# In[106]:


print(socket.gethostbyname('www.google.com'))


# In[108]:


os.chdir("/home/ubuntu/")


# In[110]:


import subprocess


# In[112]:


print(subprocess.run(["ls","-a"]))


# In[114]:


get_ipython().system('pip install nbconvert')


# In[118]:


get_ipython().system('jupyter nbconvert --to script Untitled.ipynb')


# In[ ]:





# In[ ]:




