# 输入一个数字，看你猜不猜得对

import random

target_num = random.randint(1, 5)

while 1:
    input_num = int(input('请输入一个数字：'))
    if input_num == target_num:
        print('哈哈哈，你猜对了 :)')
        break
    elif input_num > target_num:
        print('大了 :(')
    else:
        print('小了 :(')
