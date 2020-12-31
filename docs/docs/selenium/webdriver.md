从selenium3+开始，各浏览器驱动程序由浏览器官方提供。根据2018年的官方消息，在2019年selenium会采用标准的W3C标准，到时候将不再需要使用单独的浏览器驱动包。

浏览器驱动程序下载地址见[浏览器驱动下载](/addition/browser/)
# Chrome
使用chrome浏览器进行自动化测试前，需要从官网下载WebDriver驱动程序，浏览器版本与驱动程序版本之间的对应关系见各浏览器驱动下载地址说明。
程序实现如下：
```python
from selenium import webdriver
driver = webdriver.Chrome (executable_path=driver_path)
```

# Firefox
同样的使用Firefox浏览器进行自动化测试的时候，也需要下载驱动程序，驱动程序下载地址见各浏览器驱动下载地址，注意Firefox版本必须大于48
程序实现
```python
from selenium import webdriver
driver = webdriver.Firefox(executable_path=driver_path)
```
# IE
同样的使用IE浏览器进行自动化测试的时候，也需要下载驱动程序，驱动程序下载地址见各浏览器驱动下载地址，但是IE需要区分32位还是64位
```python
from selenium import webdriver
driver = webdriver. Ie (executable_path=driver_path)
```
# Edge
使用edge浏览器做自动化测试时，必须注意，下载的浏览器驱动版本需要与OS的realease版本对应。下载地址见各浏览器驱动下载地址
```python
from selenium import webdriver
driver = webdriver.Firefox(executable_path=driver_path)
```