import json

adict = {"username":"yansl","password":"123456"}
bdict = {'5':"yansl","password":[2,5]}
cdick = '{"username":"yansl","password":"123456"}'

def dict_sel():
    print(adict['username'])
def dict_del():
    adict.pop('password')
    print(adict)
    bdict.pop(5)
    print(bdict)
    bdict.pop()
def dick_update():
    adict['username']='郑清文'
    print(adict)
def dick_add():
    adict.update(bdict)
    print(adict)
    cdict=dict(adict,**bdict)
    print(cdict)
def dict_add1():
    adict['老三']='屎真香'
    print(adict)
def dict2str():
    print(type(adict))
    adict_str=json.dumps(adict)
    print(adict_str)
    print(type(adict_str))
def dick_str():
    print(type(cdick))
    dick=json.loads(cdick)
    print(dick)
    print(type(dick))
    







if __name__ == '__main__':
    dick_str()
    # dict2str()
    # dict_sel()
    # dict_del()
    # dick_update()
    # dict_add1()