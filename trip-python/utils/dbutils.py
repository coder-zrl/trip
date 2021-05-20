import pymysql

host = 'localhost'
user = 'root'
password = '422518'
database = '3chuang'

'''
连接数据库
'''
def connect_db():
    db = ''
    try:
        db = pymysql.connect(host=host,port=3306,user=user,password=password,database=database)
    except Exception as e:
        print('连接数据库出错')
        print(e)
    return db


'''
执行MySQL查询命令，返回结果
result格式：
[{'id':1,'username':'xx','password':'xx'}]
'''
def select_data(sql):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    db.commit()
    db.close()
    desp_list = [i[0] for i in cursor.description]  # 获取字段列表
    data = []
    for i in result:
        data.append(dict(zip(desp_list,i)))
    return data

'''
执行MySQL插入命令，返回结果
data格式
{id:'xx','username':'xxx',password:'xxxx'}
'''
def insert_data(data,table_name):
    db = connect_db()
    cursor = db.cursor()
    key_list = []
    value_list = []
    for item in data:
        key_list.append(item)
        value_list.append("'" + db.escape_string(str(data[item])) + "'")
    key = ','.join(key_list)
    value = ','.join(value_list)
    sql = 'insert into %s (%s) values (%s)'%(table_name,key,value)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
    except Exception as e:
        print(e)
        return -1

'''
删除内容,传入id属性即可
'''
def delete_data(t_id,table_name):
    assert type(t_id) is int
    db = connect_db()
    cursor = db.cursor()
    sql = 'delete from %s where id=%s'%(table_name,t_id)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
    except Exception as e:
        print(e)
        return -1

'''
更新属性，传入id和要修改的内容
data是字典格式
'''
def update_data(data,table_name):
    assert 'id' in data
    db = connect_db()
    cursor = db.cursor()
    value_list = []
    for i in list(data.items())[1:]:
        value_list.append(str(i[0])+'='+ "'" +db.escape_string(str(i[1])) +"'")
    value = ','.join(value_list)
    sql = 'update %s set %s where id=%s'%(table_name,value,data['id'])
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
    except Exception as e:
        print(e)
        return -1


if __name__ == '__main__':
    data = {'id':2,'username':'xxx'}
    update_data(data,'user')
    sql = 'select * from user'
    result = select_data(sql)
    print(result)

