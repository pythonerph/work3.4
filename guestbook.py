# coding : utf-8
import shelve

DATA_FILE = 'guestbook.dat'

def save_data(name,comment,create_at):
    #'''保存提交的数据'''
    #通过shelve模块打开数据库文件
    datebase = shelve.open(DATA_FILE)
    #如果数据库中没有greeting_list,就新建一个表
    if 'greeting_list' not in datebase:
        greeting_list = []
    else:
        #从数据库获取数据
        greeting_list = datebase['greeting_list']
    #将提交的数据添到表头
    greeting_list.insert(0,{
        'name':name,
        'comment':comment,
        'create_at':create_at,
        })
    #更新数据库
    datebase['greeting_list'] = greeting_list
    #关闭数据库
    datebase.close()
