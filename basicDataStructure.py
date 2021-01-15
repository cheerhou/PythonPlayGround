# 元组
tuple_1 = (1, 2, 'test1', ['hello', 1, 2, 3])

# get the first element
print(tuple_1[0])

# 获取倒数第一个元素
print(tuple_1[-1])

# 读取第1到2个元素
print(tuple_1[0:2])


# 字典
test_dic = {}

# add
test_dic['key'] = 'hahaha'
print(test_dic)

# modify
test_dic['key'] = 'Python'
print(test_dic)

# read the value of the key
val = test_dic['key']
print(val)

# 用get获取，不存在的话可以指定默认值
invalid_val = test_dic.get('invalid', '不存在')
print(invalid_val)
