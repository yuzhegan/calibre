# encoding='utf-8

# @Time: 2021-12-09
# @File: %
#!/usr/bin/env
# 微信的文章是动态加载的需要点击另外一个标签，这个元素才会加载出来，所有需要用到
# selium beatifulsoup from selenium import webdriver
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import csv
url = "https://mp.weixin.qq.com/mp/homepage?__biz=MzUyMjg5MjM4Ng==&hid=3&sn=220e9aebd77902fed3d5bf44802673dd"
# 选定浏览器
path = "/home/dav/Downloads/chromedriver" 
browser = webdriver.Chrome(executable_path = path)
# 通过网页地址打开网页，此时会弹出浏览器，并加载相应的网页
browser.get(url)
# 睡眠3秒，主要是为了等待网页加载完毕后，才能执行后续操作
# Selenium本身有更好的阻塞等待方法，这里直接偷懒了
time.sleep(1)
def GetElementClick_DropLast(xpath_element, k):
    browser.find_element_by_xpath(xpath_element).click()
    time.sleep(1)
    # 需要拖动浏览器去加载更多的条目用js模拟拖拽
    js="var q=document.documentElement.scrollTop=10000"  # 滚动到最下面
    for i in range(1,10):
        browser.execute_script(js)
        time.sleep(1)
    time.sleep(3)
    articles = []
    arth_elemnt = "article_list article_list_%d jsAppmsgList"%k
    soup = BeautifulSoup(browser.page_source, "lxml")
    soup_smclass = soup.find("div",{"class":arth_elemnt})
    links = soup_smclass.findAll("a",{"class":"list_item js_post"})
    for link in links:
        url = link.get("href")
        # print(link)
        title = link.find('h2').text.strip()
        print(url)
        print(title)
        a = {"title":title,"url": url}
        articles.append(a)
    return articles
SmClass = GetElementClick_DropLast("/html/body/div/div[3]/div[1]/div/div[4]", 3)
# 解析网页，第二个参数为解析器
SmClass.reverse()
Jinxuan = GetElementClick_DropLast("/html/body/div/div[3]/div[1]/div/div[1]", 0)
Jinxuan.reverse()
Xianxia = GetElementClick_DropLast("/html/body/div/div[3]/div[1]/div/div[2]", 1)
Xianxia.reverse()
XinChen = GetElementClick_DropLast("/html/body/div/div[3]/div[1]/div/div[3]", 2)
XinChen.reverse()

All_list = SmClass + Jinxuan + XinChen + Xianxia
print (len(All_list))

with open("aopplo.csv","w", newline="") as f:
    writer = csv.writer(f)
    for line in All_list:
        writer.writerow([line])

