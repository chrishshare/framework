* 目标
查找含有`highlighter-rouge`类的元素
* 实现
```python
element1 = driver.find_element_by_class_name("highlighter-rouge")
element2 = driver.find_element(by="class name", value="highlighter-rouge")
```
* 说明  
当前`class name`没有重复值，所有可以直接用`find_element***`定位元素，如果`class`存在重复则在运行的时候会找不到元素，此时需要使用`find_elements***`，假设`highlighter-rouge`存在重复值，则定位方式如下：
```python
element3 = driver.find_elements_by_class_name("highlighter-rouge")
element4 = driver.find_elements(by="class name", value="highlighter-rouge")
```
另外`class`在实际项目中经常都是以组合的方式出现，但是`find_element_by_class_name()`只能是定位单各`class name`，复合`class name`的时候需要使用`css`定位方式