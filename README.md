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


