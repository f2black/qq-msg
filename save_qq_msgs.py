
# coding: utf-8

import codecs

#-----------------------------------------------------------------------
#-----------------------配置信息----------------------------------------

#需要整理的QQ号
vip_qq_ids = ['28505355', '448064184', '987422909', '2429246562', '3367537735', '914444602']

#QQ号和QQ昵称的对应关系
vip_qq_name_id = {'28505355':u'北京数学哥',                '448064184':u'快乐人生',                '987422909':u'妈妈爱牛牛',                '2429246562':u'青岛—小禾苗',                '3367537735':u'后知后觉已十年-上海',                '914444602':u'北京飘落的长发'}     

#指定原始QQ群消息历史记录所在位置
qq_record_file_date = "(20161127-20161204)"
qq_record_file_name = "顺势投资核心组" + qq_record_file_date + ".txt"
qq_record_file_path = "h:/08t2ff/02QQ/20161204/"
qq_record_file = qq_record_file_path + qq_record_file_name

#QQ留言时间段，暂时不从消息内容提取，直接在这里手写指定
#start_time = "20161023"
#end_time = "20161030"

#-----------------------------------------------------------------------

def get_all_qq_msgs(qq_record_file):
    file = codecs.open(qq_record_file, "r", "utf-8")
    lines = file.readlines()

    #获取所有消息记录
    msg_record = []
    msg = ''    
    
    for line in lines:
        msg = msg + line
        if '\r\n' == line:            
            msg_record.append(msg)
            msg = ''   

    file.close()
    return msg_record

def save_msg_of_qqid(in_qqid, all_msgs):
    qqid = in_qqid
    print(u"开始整理"+vip_qq_name_id[qqid] + "(" + qqid + ")" + "的留言...")

    #以utf-8格式存入txt文件
    output_file = qq_record_file_path + u"消息记录_" + vip_qq_name_id[qqid] + qq_record_file_date + ".txt"
    file=codecs.open(output_file, "w", "utf-8")
    for msg in all_msgs:
        #选取特定人的消息，以qq号为参数
        if qqid in msg:
            file.write(msg)
    file.close()
    print(u"整理完成")
    return

def save_vip_msg():

    all_msgs = get_all_qq_msgs(qq_record_file)

    for id in vip_qq_ids:
        save_msg_of_qqid(id, all_msgs)
    
    return




