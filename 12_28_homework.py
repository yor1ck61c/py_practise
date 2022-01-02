"""
编写用户登陆系统
需求：
1.系统里面有多个用户，用户的信息目前保存在列表里面
 users = ['root','cjs666']
 passwd = ['123','456']
2.用户登陆(判断用户登陆是否成功）
 1).判断用户是否存在
 2).如果存在
     1).判断用户密码是否正确
     如果正确，登陆成功，退出循环
     如果密码不正确，重新登陆，总共有三次机会登陆
 3).如果用户不存在
 重新登陆，总共有三次机会
    for j in range(len(users)):
        if username == users[j]:
            for k in range(len(passwd)):
                if password == passwd[k]:
                    print("登录成功")
                    sys.exit(0)
            # 两个密码全部失配
            print("密码输入有误，您还有{0}次机会".format(2 - i))
            break
    print("用户名输入有误，您还有{0}次机会".format(2 - i))
 print("用户名输入有误，您还有{0}次机会".format(3-i))
            break
"""
import sys
users = ["root", "cjs666"]
passwd = ["123", "666"]
times = 3
for i in range(times):
    usernameFlag = False
    username = input("请输入用户名:")
    password = input("请输入密码:")
    for j in range(len(users)):
        if username == users[j]:
            usernameFlag = True
            if password == passwd[j]:
                print("登录成功")
                sys.exit(0)
            else:
                print("密码输入有误，您还有{0}次机会".format(2 - i))
                break
    else:
        print("用户名输入有误，您还有{0}次机会".format(2 - i))
