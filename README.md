# calibre
change web content to ebooks
## `Install` [Calibre](https://calibre-ebook.com/download_linux) 
```
wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin install_dir=~/calibre-bin isolated=y
```
### just creat a soft link to `/usr/bin` 
```
sudo -s /home/david/calibre-bin/calibre/calibre /usr/bin/
```



## how to use 
just get the `index` html `url` & `title` 

## if you had install the calibre and you can use the code:
```
sudo ls -n /home/david/calibre-bin/calibre/ebook-convert /usr/bin/
```

## how to convent :
```
ebook-convert xxx.recipe xxx.mobi  #or other ebook format
```
## 将微信公众号上的内容做成电子书

calibre不支持你本机的`python` 库，需要在本机python去生成一个`list` ，找出所有需要下载的链接，格式为：
```
[{dict},{dict},{dict},{...}]
```

生成的`.csv` 文件在读取到`recipe` 中列表中每个元素是`str` 格式的需要再进行转化下，转成`dict` 格式


