'''
群聊服务：
功能：类似ＱＱ聊天群聊功能
[1]有人进入聊天室需要输入姓名(密码),姓名不能重复
[2]有人进入聊天室，其他人会收到通知(xx进入聊天室)
[3]一个人发消息其他人会收到消息(xx:msg)
[4]有人退出，则其他人会收到通知(xx离开了聊天室)
[5]扩展：服务器可以项所有群用户发送公告(管理员消息:msg)

具体实现：
1.网络连接搭建(udp)
2.进入聊天室
    1).client(input name\
        send name\
        receiver msg\
        if OK into room else Re-enter name\
        print name)
    2).server(receiver name\
        judge permission\
        if refuse send msg else save name to dict and send refuse msg\
        send others the name)
3.实现聊天功能
    1).client:
    2).server:
4.退出聊天室

5.管理员公告
'''

