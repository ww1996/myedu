
def list_type(a):
    print(a[3])
    print(a[-2])
    print(a[0:5])
    print(a[1:5])
    print(a[0:6])
    print(a[1:3])
    print(a[1:4])
def list_del():
    # alist=[1,2,3,4,5]
    alist.pop(0)
    print(alist)
def list_del():
    alist.pop()
    print(alist)
def list_add():
    alist=[1,2,3,4]
    alist.append(0)
    print(alist)
    blist=[1,2,3]
    alist.append(blist)
    print(alist)
    alist[1]=3
    print(alist)







if __name__ == '__main__':
    # list_del()
    # alist=['你好',2,'shabi','dashabi',250]
    # list_type(alist)
    # alist=[1,2,3,4,5]
    # list_del()
    list_add()

