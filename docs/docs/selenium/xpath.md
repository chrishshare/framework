# 选取节点
## 精确选择节点
XPath使用路径表达式在 XML 文档中选取节点。节点是通过沿着路径或者step来选取的  
## 路径表达式
表达式 | 描述 |
:-: | :-: |
nodename | 选取此节点的所有子节点|
/ | 从根节点选取。
// | 从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。
. | 选取当前节点。
.. | 选取当前节点的父节点。
@ | 选取属性。

## 选取未知节点
XPath 通配符可用来选取未知的 XML 元素。  

通配符 | 描述|
:-: | :-: |
* | 匹配任何元素节点。|
@* | 匹配任何属性节点。|
node() | 匹配任何类型的节点。|

## 选取若干路径
通过在路径表达式中使用"|"运算符，您可以选取若干个路径。

# 绝对路径定位
绝对路径表示从html的根节点开始一层一层的往下查找元素，始于正斜杠（/）并且每层元素之间使用正斜杠（/）  

* 目标  
查找第一个a标签下的"猜猜看"
* 实现  
Xpath定位表达式
```html
/html/body/a[.="猜猜看"]
/html/body/a[text()="猜猜看"]
```
Python定位语句
```python
element1 = driver.find_element_by_xpath('/html/body/a[.="猜猜看"]')
element2 = driver.find_element_by_xpath('/html/body/a[text()="猜猜看"]')
```
* 说明  
使用绝对定位是十分不灵活的，一旦页面结构发生变化，原来的表达式就可能失效，需要重新维护，成本会增加。而且在实际项目中页面结构可能非常复杂，会造成xpath表达式非常长，不容易理解。所以不建议使用绝对定位。
# 相对路径定位
相对路径的每一步都根据当前节点集中的节点来进行计算，起始于双正斜杠（//）
* 目标    
查找第一个a标签下的"猜猜看"
*  实现  
Xpath表达式
```xpath
//a[.="猜猜看"]
//a[text()="猜猜看"]
```
Python表达式
```python
element1 = driver.find_element_by_xpath('//a[.="猜猜看"]')
element2 = driver.find_element_by_xpath('//a[text()="猜猜看"]')
```
* 说明  
相对路径xpath定位表达式简洁易读，而且不容易受页面结构变化的影响。使用时应尽量保证表达的简洁性。
# 索引定位
索引定位表示摸个被定位的页面元素在其父元素节点下的同名元素中的位置序号，起始序号为1

* 目标  
查询页面中的第二个div  
* 实现  
Xpath表达式
```xpath
//div[2]
```
Python表达式
```python
element = driver.find_element_by_xpath("//div[2]")
```
# 属性定位
## 精确属性定位
* 目标  
选择alt值等于"点我试试呀"的img元素  
* 实现  
Xpath表达式  
```xpath
//img[@alt="点我试试呀"]
```
Python表达式  
```python
element = driver.find_element_by_xpath('//img[@alt="点我试试呀"]')
```
## 模糊属性定位
模糊定位的函数有如下三个：`starts-with (str1,st2), contains (str1,str2),text()`

* 目标  
查找alt属性值包含"点我"的元素  
* 实现  
Xpath表达式  
```xpath
//img[starts-with(@alt,"点我")
//img[contains(@alt,"点我")
```
Python表达式
```python
element1 = driver.find_element_by_xpath('//img[starts-with(@alt,"点我")')
element2 = driver.find_element_by_xpath('//img[contains(@alt,"点我")')
```

# 轴定位
 
Xpath轴关键字 | 轴的定义说明 | 定位表达式实例 | 表达式解释 |
:-: | :-: | :-: | :-: |
parent | 选取当前节点的父节点 | //img[@alt='div2-img2']/parent::div | 查找到alt属性为div2-img2的img元素，并基于图片找到其上一级的div元素 |
child | 选取当前节点的子节点 | //div[@id='div1']/child::img | 查找id为div1的div标签，基于当前div查找标签为img的子节点 |
ancestor | 选取当前节点的所有上层节点 | //img[@alt='div2-img2']/ancestor::div | 查找alt属性为div2-img2的图片，基于当前图片找到其上级的div页面元素 |
descendant | 选取当前节点所有下层节点 | //div[@id='div2']/descendant::img | 查找id属性为div2的div元素，在查找其下级所有节点中的img元素 |
following | 选取当前节点之后显示的所有节点 | //div[@id='div1']/following::img | 查找到ID属性为div1的div元素，并基于div的位置找到它后面节点中的img元素 |
following-sibling | 选取当前节点所有的平级节点 | //img[@alt='div1-img1']/following-sibling::input | 查找到alt属性为div1-img1的img页面元素，并基于img的位置找到后续节点中的input元素 |
preceding | 选取当前节点前面所有的节点 | //img[@alt='div2-img2']/preceding::div | 查找到alt属性为div2-img2的图片页面元素，并基于图片的位置找到它前面节点中的div元素 |
preceding-sibling | 选取当前节点前面所有平级的节点 | //img[@alt='div2-img2']/preceding-sibling::a[1] | 查找到alt属性值为div2-img2的图片元素，基于图片位置找到它前面同级节点的第二个链接页面元素 |
ancestor-or-self | 选取当前节点的所有先辈（父、祖父等）以及当前节点本身。 | | |	　
attribute | 选取当前节点的所有属性	 | | |　
namespace | 选取当前节点的所有命名空间节点。 | | |	　
self |  选取当前节点。 | | |

# 文本定位
text()函数可以定位到元素文本包含某些关键内容的页面元素  
```
//p[text()=" openstf项目开源地址："]
//p[.=" openstf项目开源地址："]
//p[contains(text(),"openstf")]
//p[contains(.,"openstf")]
```
python表达式
```python
Driver.find_element_by_xpath('//img[contains(@alt,"点我")')
```