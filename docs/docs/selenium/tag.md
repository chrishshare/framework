tag name即标签名称，如：a、input、button、img等

* 目标  
查找页面中的a标签  
* 实现
```python
element1 = driver. find_element_by_tag_name("a")
element2 = driver. find_element(by="tag name", value="a")
```
* 说明  
当前标签没有重复值，所有可以直接用`find_element***`定位元素，如果name存在重复则在运行的时候会找不到元素，此时需要使用`find_elements***`，假设a存在重复值，则定位方式如下：
```python
element3 = driver.find_elements_by_class_name("a")
element4 = driver.find_elements(by="class name", value="a")
```