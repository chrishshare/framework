# 绝对路径定位
* 目标
查找第一个文本为"猜猜看"的a标签
* 实现
CSS表达式
```
html>body>div>a[.="猜猜看"]
```

python表达式
```python
driver.find_element_by_css_selector('html>body>div>a[.="猜猜看"]')
```


# 相对路径定位
* 目标  
查找第一个文本为"猜猜看"的a标签  
* 实现  
CSS表达式  
```
a[.="猜猜看"]
```

Python表达式
```python
driver.find_element_by_css_selector('a[.="猜猜看"]')
```
# 类名定位
* 目标
查找第一个类名为"blogpost-body"的div元素
* 实现
CSS表达式
```html
div. blogpost-body
```
python表达式
```python
driver.find_element_by_css_selector("div. blogpost-body")
```
* 说明
对于复合class，如`<input class="btn btn-lg btn-default" type="text">`，直接写上所有的class即可，即：`driver.find_element_by_css_selector("input. btn.btn-lg.btn-default")`
标签名不是必须的

# 属性定位
> * ID属性定位
* 目标  
查找页面中第一个id为"cnblogs_post_body"div元素  
* 实现  
CSS表达式  
```html
div# cnblogs_post_body
```
Python表达式
```python
driver.find_element_by_css_selector("div# cnblogs_post_body")
```

> *  其他属性定位
其他属性是指除id、class以外的所有属性，如img的src、alt属性，input的type、placeholder等
* 目标  
查找页面中alt属性等于"点我试试呀"的img元素  
* 实现  
CSS表达式  
```css
img[alt="点我试试呀"]
```
Python表达式
```python
driver.find_element_by_css_selector('img[alt="点我试试呀"]')
```
* 说明  
如果单独依靠某个属性无法唯一定位元素，则可以写多个属性，如下：
```css
img[alt="点我试试呀"][src="/images/bg.jpg"]
```
```python
driver.find_element_by_css_selector('img[alt="点我试试呀"] [src="/images/bg.jpg"]')
```

> *  模糊属性定位
模糊属性定位经常使用的三个正则表达式`^、$、*`
* 目标  
查找链接地址是"http://www.baidu.com"的a标签  
* 实现  
CSS表达式  
```css
a[href^="http://www.baidu"]
a[href$="baidu.com"]
a[href*="baidu"]
```

python表达式
```python
find_element_by_css_selector('a[href^="http://www.baidu"]')
find_element_by_css_selector('a[href^=" a[href$="baidu.com"]')
find_element_by_css_selector('a[href*="baidu"]')
```
> * 子页面元素查找
* 目标
查找id为home的div下的class为highlighter-rouge的div
* 实现
CSS表达式
```css
div#home>div.highlighter-rouge
```
python表达式
```python
driver.find_element_by_css_selector("div#home>div.highlighter-rouge")
```
* 伪类定位
* 目标  
查找`div#home`下的第一个子元素  
* 实现
CSS表达式
```css
div#home :first-child
```
python表达式
```python
dirver.find_element_by_css_selector("div#home :first-child")
```
更多伪类见附录[CSS伪类](/addition/css/)
