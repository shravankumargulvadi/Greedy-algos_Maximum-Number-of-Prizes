
# coding: utf-8

# In[18]:


import sys
def max_prizes (a):
    if a==1:
        return [1]
    if a==2:
        return [2]
    if a>2:
        x=[]
        for i in range(1,a):
            if (a-i)>i:
                #print(i)
                x.append(i)
                #print(x)
                a=a-i
            else:
                x.append(a)
                break
                #print(x)
        return x
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = max_prizes(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')         
            
        


# In[17]:


max_prizes(6)

