list = ['a', 'b', 'c', 'd', 'e']
def show(lst, n=0):
    if(n==len(lst)):
        return
    print(lst[n])
    show(list,n+1)
show(list)
    
