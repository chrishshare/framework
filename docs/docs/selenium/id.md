* 目标  
根据元素ID找到"明天也许是个好日子吧"所属的元素
* 实现
```python
element1 = driver.find_element_by_id("blog-news")
element2 = driver.find_element(by="id", value="blog-news")
```
* 说明  
当前ID没有重复值，所有可以直接用`find_element***`定位元素，如果ID存在重复则在运行的时候会找不到元素，此时需要使用`find_elements***`，假设`blog-news`存在重复值，则定位方式如下：
```python
element3 = driver.find_elements_by_id("blog-news")
element4 = driver.find_elements(by="id", value="blog-news")
```
使用`driver.find_element(by=by, value=value)`方式定位时，by传入的是定位方式，`by`在`selenium.webdriver.common.by.By`类中，各种定位方式对应关系如下：
```python
CLASS_NAME = 'class name'
CSS_SELECTOR = 'css selector'
ID = 'id'
LINK_TEXT = 'link text'
NAME = 'name'
PARTIAL_LINK_TEXT = 'partial link text'
TAG_NAME = 'tag name'
XPATH = 'xpath'
```