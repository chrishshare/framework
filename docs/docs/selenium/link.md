# 超链接文本（Link text）定位
* 目标  
查找页面中的a标签
* 实现  
```python
element1 = driver. find_element_by_link_text("猜猜看")
element2 = driver. find_element(by="tag name", value="猜猜看")
```
* 说明  
当前标签没有重复值，所有可以直接用```find_element***```定位元素，如果name存在重复则在运行的时候会找不到元素，此时需要使用```find_elements***```，假设"猜猜看"存在重复值，则定位方式如下：
```python
element3 = driver.find_elements_by_class_name("猜猜看")
element4 = driver.find_elements(by="class name", value="猜猜看")
```
# 超链接模糊定位（partial link text）
* 目标  
查找页面中的a标签
* 实现  
```python
element1 = driver. find_element_by_link_text("猜猜看")
element2 = driver. find_element(by="tag name", value="猜猜看")
```
* 说明  
当前标签没有重复值，所有可以直接用```find_element***```定位元素，如果`name`存在重复则在运行的时候会找不到元素，此时需要使用```find_elements***```，假设"猜猜看"存在重复值，则定位方式如下：
```python
element3 = driver.find_elements_by_class_name("猜猜看")
element4 = driver.find_elements(by="class name", value="猜猜看")
```