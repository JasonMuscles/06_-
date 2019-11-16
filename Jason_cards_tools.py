
while True:

    # 显示功能菜单

    action_str = input("请输入你希望执行的数字：")
    print("你选择的操作是【 %s 】" % action_str)

    # 1，2，3针对名片的操作
    if action_str in ["1", "2", "3"]:

        # 新增名片
        if action_str == "1":
            pass

        # 显示全部
        elif action_str == "2":
            pass

        # 查询名片
        elif action_str == "3":
            pass

    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【 名片管理系统 】")

        break

    # 其它内容输入定义为输入错误，并提示用户
    else:
        print("输入有误请正确输入！")


