* 目标  
查找name值为top的元素
* 实现
```python
element1 = driver.find_element_by_name("top")
element2 = driver.find_element(by="name", value="top")
```
* 说明  
当前name没有重复值，所有可以直接用`find_element***`定位元素，如果`name`存在重复则在运行的时候会找不到元素，此时需要使用`find_elements***`，假设top存在重复值，则定位方式如下：
```python
element3 = driver.find_elements_by_class_name("top")
element4 = driver.find_elements(by="class name", value="top")
```