
def read ():
    try:
        fle=open('store.csv').read()
        print('file loaded ...:D')
        prodis=fle.split('\n')
        wl=list()
        for i in range(len(prodis)):
            p=prodis[i].split(',')
            d={'id':p[0],'name':p[1],'price':p[2],'count':p [3]}
            wl.append(d)
        return wl
    except Exception as e:
        print(e)
        print('file ro peyda nakard')
pr=read()
def show_menu():
    print('1-add new product')
    print('2-serch')
    print('3-edit')
    print('4-buy')
    print('5-remove')
    print('6-show all')
    print('7-show factor')
    print('8-exit')
def add():
    id=input('enter id:')
    for p in pr:
        if p['id']==id:
            print('this id is exit')
            return
    name=input('enter name:')
    prise=input('enter prise:')
    count=input('enter count:')
    pr.append({'id':id,'name':name,'price':prise,'count':count})

def search():
    word=input('enter key word:')
    for p in pr:
        if p['id']==word or p['name']==word or p['price']==word or p['count']==word:
            print(p)
            return

def write():
    fl=open('store.csv','w')
    fl=writable=True
    c=0
    for p in pr:
        id=p['id']
        name=p['name']
        price=p['price']
        count=p['count']
        fl.write(id+','+name+','+price+','+count)
        c+=1
        if c<len(pr):
            fl.write('\n')
    fl.close()

def edit():
    id=input('enter id:')
    for p in pr:
        if p['id']==id:
            p['name']=input('enter name:')
            p['price']=input('enter price:')
            p['count']=input('enter count:')
            return

def buy():
    buy_list=[]
    while True:
        s=input('enter code:')
        c=int(input('enter count:'))
        for p in pr:
            if s==p['id']:
                if c<=int(p['count']):
                    j=int(p['count'])-c
                    p['count']=str(j)
                    c=str(c)
                    buy_list.append({'id':p['id'],'name':p['name'],'price':p['price'],'count':c })
                    break
                else:
                    print('finsh..')
        else:
            print('not found ...!')
        b=input('Stop buy?(y/n)')
        if b=='y':
            break
    a=input('save buylist?(y/n)')
    if a=='n':
        buy_list=[]
        return buy_list
    elif a=='y':
        f=open('factor.csv','w')
    f.writable=True
    c=0
    ss=0
    for b in buy_list:
        id=b['id']
        name=b=['name']
        price=b['price']
        count=b['count']
        s=int(price)*int(count)
        ss+=s
        f.write('id:'+id+'name:'+name+'price:'+price+'count:'+count+'sum:'+str(s))
        c+=1
        if c<len(buy_list):
            f.write('\n')
    f.write('\nnone:'+str(ss))
    f.close
    write()

def remove():
    a=input('enter code:')
    for p in pr:
        if a==p['id']:
            pr.remove(p)

def show_all():
    for p in pr:
        print(p)


def shoe_factor():
    try:
        fl=open('factor.csv','w')
        hole=fl.read()
        print(hole)
    except Exception as e:
        print(e)

while True:
    show_menu()
    user=int(input('enter your choice:'))
    if user==1:
        add()
    elif user==2:
        search()
    elif user==3:
        edit()
    elif user==4:
        buy()
    elif user==5:
        remove()
    elif user==6:
        show_all()
    elif user==7:
        shoe_factor()
    elif user==8:
        exit



