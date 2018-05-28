import time

import download,threading

# 关键字
# word = '炮姐'
# page1 = 4
# page2 = 5
word  = input("输入关键字：")
print("下面输入【开始页，结束页），每页只下载前20张，因为20张以后会有重复")
page1 = input("输入开始页：")
page2 = input("输入结束页：")
download.downloadSogouPicture(word,page1,page2)
download.pringThreadNumberEverySecond()
# def startThread(word,page1,page2):
#     for page in range(int(page1),int(page2)):
#         try:
#             _thread.start_new_thread(download.downloadSogouPicture,(word,page,page))
#         except:
#             print('error 001')


# class startThread(threading.Thread):
#     def __init__(self,id,word,page1,page2):
#         threading.Thread.__init__(self)
#         self.