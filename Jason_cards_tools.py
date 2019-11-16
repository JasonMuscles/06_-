# 记录所有名片字典
card_list = []


def show_menu():
    # 显示菜单界面
    print("=" * 50)
    print("欢迎使用【名片管理系统】V1.0\n")
    print("1. 新建名片\n2. 显示全部\n3. 查询名片\n0. 退出系统")
    print("=" * 50)


def new_card():
    """新增名片"""
    print('\033[1;31m新增名片\033[0m')

    # 1.提示用户依次输入名片信息
    name_str = input("请输入用户的姓名：")
    phone_str = input("请输入用户的手机号码：")
    qq_str = input("请输入用户的QQ号码：")
    email_str = input("请输入用户的邮箱地址：")

    # 2.将名片信息保存到一个字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3.将字典添加到名片列表
    card_list.append(card_dict)

    # 4.提示名片添加完成
    print("%s\n名片新增成功！" % card_dict)


def show_all():
    """显示所有名片"""
    print("\033[1;31m显示所有名片\033[0m")

    # 判断是否有名片记录,没有这提示用户并返回
    if len(card_list) == 0:
        print("当前无名片数据，请选择新增名片信息！")

        # return可以返回一个函数的执行结果
        # 下发代码不在执行，返回调用函数的位置
        return

    # 打印表头
    for name in ["姓名", "手机", "QQ", "邮箱"]:
        print(name, end="\t\t")
    print("")
    # 打印分割线
    print("- -" * 18)

    # 遍历所有名片信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s"
              % (card_dict["name"],
                 card_dict["phone"],
                 card_dict["qq"],
                 card_dict["email"]))

    print("- -" * 18)


def search_card():
    """搜索名片"""
    print("\033[1;31m搜索名片\033[0m")

    # 1. 提示要搜索的姓名
    find_name = input("请输入需要搜索的姓名：")

    # 2. 遍历字典查找搜索的姓名，如果没有找到就提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:

            print("- -" * 18)

            print("%s\t\t%s\t\t%s\t\t%s"
                  % (card_dict["name"],
                     card_dict["phone"],
                     card_dict["qq"],
                     card_dict["email"]))

            print("- -" * 18)

            deal_card(card_dict)

            break
    else:
        print("未找到名字为：%s 的信息！" % find_name)


def deal_card(find_dict):

    action_str = input("请输入需要执行的操作\n"
                       "【1】修改\n"
                       "【2】删除\n"
                       "【0】返回主菜单")

    if action_str == "1":

        find_dict["name"] = input_card_info(find_dict["name"], "请输入姓名:")
        find_dict["phone"] = input_card_info(find_dict["phone"], "请输入手机号码：")
        find_dict["qq"] = input_card_info(find_dict["qq"], "请输入QQ号码：")
        find_dict["email"] = input_card_info(find_dict["email"], "请输入邮箱地址：")

        print("成功修改为\n %s" % find_dict)

    elif action_str == "2":

        print("已删除\n%s" % find_dict)

        card_list.remove(find_dict)


def input_card_info(dict_value, tip_message):
    """

    :param dict_value: 字典原有值
    :param tip_message: 输入提示信息
    """

    # 1. 提示用户输入内容
    result_str = input(tip_message)

    # 2. 针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result_str) > 0:

        return result_str

    # 3. 如果用户没有输入内容，返回 `字典中原有的值`
    else:
        return dict_value
