# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv

# header
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'zip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Length': '37',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'UM_distinctid=176832b396920c-0f279559ca9f77-5a301e44-151800-176832b396a6f4; JSESSIONID=95DD76C285F5FF1ECD239AEF090F861A; CNZZDATA334452=cnzz_eid%3D617926241-1608515416-https%253A%252F%252Fzs.szu.edu.cn%252F%26ntime%3D160908154',
    'Cache-Control': 'max-age=0',
    'Host': 'zs.szu.edu.cn',

    
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
    }

# url list
"""url1 = ["http://zsb.tjut.edu.cn/info/1019/1191.htm",
       "http://zsb.tjut.edu.cn/info/1019/1192.htm",
       "http://zsb.tjut.edu.cn/info/1019/1193.htm",
       "http://zsb.tjut.edu.cn/info/1019/1194.htm",
        "http://zsb.tjut.edu.cn/info/1019/1195.htm",
        "http://zsb.tjut.edu.cn/info/1019/1196.htm",
        "http://zsb.tjut.edu.cn/info/1019/1197.htm"]"""
url="https://zs.szu.edu.cn/query/history_dtl?p=14"
# 网页值对应省份和类别
key1 = ['天津理工大学2017年-2019年在北京（理工）分专业录取情况','天津理工大学2017年-2019年在天津（理工）分专业录取情况','天津理工大学2017年-2019年在天津（文史）分专业录取情况']
key2 = ['天津理工大学2017年-2019年在辽宁（理工）分专业录取情况','天津理工大学2017年-2019年在吉林（理工）分专业录取情况','天津理工大学2017年-2019年在黑龙江（理工）分专业录取情况', '天津理工大学2017年-2019年在黑龙江（文史）分专业录取情况']
key3 = ['天津理工大学2017年-2019年在江苏（理工）分专业录取情况','天津理工大学2017年-2019年在浙江（理工）分专业录取情况','天津理工大学2017年-2019年在安徽（理工）分专业录取情况', '天津理工大学2017年-2019年在安徽（文史）分专业录取情况','天津理工大学2017年-2019年在福建（理工）分专业录取情况','天津理工大学2017年-2019年在江西（理工）分专业录取情况','天津理工大学2017年-2019年在山东（理工）分专业录取情况','天津理工大学2017年-2019年在山东（文史）分专业录取情况']
key4 = ['天津理工大学2017年-2019年在河北（理工）分专业录取情况','天津理工大学2017年-2019年在河北（文史）分专业录取情况','天津理工大学2017年-2019年在山西（理工）分专业录取情况','天津理工大学2017年-2019年在山西（文史）分专业录取情况','天津理工大学2017年-2019年在内蒙古（理工）分专业录取情况']
key5 = ['天津理工大学2017年-2019年在广东（理工）分专业录取情况','天津理工大学2017年-2019年在广西（理工）分专业录取情况','天津理工大学2017年-2019年在海南（理工）分专业录取情况','天津理工大学2017年-2019年在河南（理工）分专业录取情况','天津理工大学2017年-2019年在河南（文史）分专业录取情况','天津理工大学2017年-2019年在湖南（理工）分专业录取情况','天津理工大学2017年-2019年在湖北（理工）分专业录取情况']
key6 = ['天津理工大学2017年-2019年在重庆（理工）分专业录取情况','天津理工大学2017年-2019年在四川（理工）分专业录取情况','天津理工大学2017年-2019年在贵州（理工）分专业录取情况','天津理工大学2017年-2019年在云南（理工）分专业录取情况','天津理工大学2017年-2019年在西藏（理工）分专业录取情况']
key7 = ['天津理工大学2017年-2019年在陕西（理工）分专业录取情况','天津理工大学2017年-2019年在甘肃（理工）分专业录取情况','天津理工大学2017年-2019年在青海（理工）分专业录取情况','天津理工大学2017年-2019年在宁夏（理工）分专业录取情况','天津理工大学2017年-2019年在新疆（理工）分专业录取情况']
key = key1+key2+key3+key4+key5+key6+key7  #list合并
print(key)  # 打印

# 对应省份
provinces = ['北京', '天津','天津', '辽宁',  '吉林', '黑龙江', '黑龙江', '江苏', '浙江', '安徽', '安徽', '福建', '江西', '山东', '山东', '河北', '河北', '山西', '山西', '内蒙古', '广东', '广西', '海南', '河南', '河南', '湖南', '湖北', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆']
# 对应科别
categories = ['理工','理工','文史', '理工', '理工', '理工', '文史', '理工', '理工', '理工', '文史', '理工', '理工', '理工', '文史', '理工', '文史', '理工', '文史', '理工', '理工', '理工', '理工', '理工', '文史', '理工', '理工', '理工', '理工', '理工', '理工', '理工', '理工', '理工', '理工', '理工', '理工']

# 组成字典
# 对应省份字典
zipped1 = zip(key,provinces)
dict_1 = dict(zipped1)
# 对应科别字典
zipped2 = zip(key,categories)
dict_2 = dict(zipped2)
print(dict_1)   # 打印
print(dict_2)   # 打印

# 引用孔老师代码
def get_text(targetURL):
    """获取网页文本信息"""
    try:
         r = requests.get(targetURL, headers=headers, timeout=30)
         r.raise_for_status()  # 如果访问状态码不是200，则抛出异常
         r.encoding = 'utf-8 '
         # print(r.text)
         print("连接成功")
         return r.text
    except:
         print("无法连接")

 get_text(url);

# 引用孔老师代码并修改
def bs4_process(targetURL):
    # 解析网页，截取出本一批次的分数线，将文本转化成列表
    data = get_text(targetURL)
    data1=data.replace('&nbsp;','0')  # 存在某一年没有该专业，将字符替换成0
    soup = BeautifulSoup(data1, 'html.parser')
    texts = soup.get_text('')
    # print(texts)
    data_list = texts.split()  # 以空格为分隔符，分割文本
    Index = data_list.index('点击量：')   # 设置截取位置点击量：
    text = data_list[Index::]  # 截取数据
    resul = []  # 创建空list
    resul.extend(text)
    # print(resul)
    return resul

# bs4_process(url)

def filter(text):
    # 根据网页特征处理数据
    result = []
    year,province, category, major, score, author, college = 2019, '', '', '', '', '张致宁', '天津理工大学'
    i = 0
    while i < len(text):
        temp = text[i]
        if temp in dict_1:
            province = dict_1.get(temp)  # 读取省份字典对应值
            category = dict_2.get(temp)  # 读取科别字典对应值
            i += 15
            continue
        elif str(temp).isdigit():     # 判断是否为数字
            if str(text[i-1]).isdigit():  # 如果前一个也是数字，不符合所需
                break
            else:
                i -= 1
                j = 0
                year = 2019
                major = text[i]
                for j in range(3):  # 存入3年的最低分
                    i += 2
                    score = text[i]
                    newItem = [college , year, province, category, major, score , author]
                    print(newItem)
                    result.append(newItem)
                    year -= 1
                i += 1
        else:
            i += 1
    return result

# 爬取数据
results = []
i = 0
for i in range(len(url1)):
    results.extend(filter(bs4_process(url1[i])))

with open('天津理工大学.csv', 'a', newline='') as f:
    csv_write = csv.writer(f)
    csv_write.writerow(['学校','年份', '省份', '科别', '专业', '最低分\位次', '贡献者'])
    for item in results:
        csv_write.writerow(item)