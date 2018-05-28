
import requests,os,re,threading,time

# 创建文件夹 用来存放图片
def makedir(dirname):
    if os.path.lexists(dirname):
        os.chdir(dirname)
    else:
        os.makedirs(dirname)
        os.chdir(dirname)

# 下载搜狗图片
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
        # for eachpicture in pictureList:#每个图片地址 picturelist 有48项
        for count in range(0,20):
            print('count:'+str(count))
            try:
                name = str(word) + '_' + str(page) + '_' + str(count)
                type = '.jpg'
                # 多线程下载
                mythread = threading.Thread(target=downloadPicture,args=(pictureList[count],name,type))
                mythread.start()
                # 打印线程名 和线程数目
                print('thread name:'+str(mythread.name))
                print(str(threading.activeCount())+'actived thread')
            except:
                print(print('当前（第' + str(count) + '）图片下载超时，正在下载下一张'))


#         每秒打印线程数目
def pringThreadNumberEverySecond():
    while(threading.activeCount()>1):
        print(str(threading.activeCount()) + 'actived thread')
        time.sleep(1)


#  图片下载
def downloadPicture(url,name,type):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"}
    # 设置10秒timeout
    picture = requests.get(url=url, headers=headers, timeout=20)
    # 写入文件
    f = open(name + type, 'wb')
    f.write(picture.content)
    f.close()


# downloadSogouPicture('炮姐',1,2)
