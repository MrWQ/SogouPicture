import download

# 关键字
# word = '炮姐'
# page1 = 4
# page2 = 5
word  = input("输入关键字：")
print("下面输入【开始页，结束页），每页只下载前20张，因为20张以后会有重复")
page1 = input("输入开始页：")
page2 = input("输入结束页：")
download.downloadSogouPicture(word,page1,page2)