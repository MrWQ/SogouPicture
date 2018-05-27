
import requests,os,re

# 创建文件夹 用来存放图片
def makedir(dirname):
    if os.path.lexists(dirname):
        os.chdir(dirname)
    else:
        os.makedirs(dirname)
        os.chdir(dirname)


def downloadSogouPicture(word,page1,page2):
    makedir(str(word))
    for page in range(int(page1),int(page2)):
        # 浏览器头
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"}
        # 查询网址
        # http = 'http://pic.sogou.com/pics?query='
        # http = http + str(word)
        http = 'http://pic.sogou.com/pics?query='+str(word)+'&page='+str(page)
        # 输出爬取网址
        print(http)
        text = requests.get(http, headers =headers).text
        # print(text)
        pattern  = re.compile(r'"thumbUrl":"(.*?)","smallThumbUrl',re.S)
        pictureList = re.findall(pattern,text)
        # print(pictureList)
        # 计数 命名文件
        count =0
        for eachpicture in pictureList:
            # 设置10毫秒timeout
            picture = requests.get(eachpicture,headers=headers, timeout=10)
            # 写入文件
            f = open(str(word)+'_'+str(page)+'__'+str(count) + '.jpg', 'wb')
            f.write(picture.content)
            f.close()
            count += 1
            # 每页只取前20张图片
            if(count == 20):
                break



