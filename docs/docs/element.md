页面元素存放在:`elements`目录下  

页面元素配置遵从[yaml规范](yamlHelp.md)

建议每个页面或每个功能独立一份`yaml`配置，公用的页面元素独立一份`yaml`配置  

# 定位方式
可选值如下：
> * class name: 类名
> * css selector: css
> * id: id
> * link text: 超链接文本
> * name: name
> * partial link text: 超链接文本（模糊）
> * tag name: 标签名称如：a,li,ul等
> * xpath: xpath表达式

# 定位值
具体的定位表达式

#示例
```
用户名:             #元素名称，中英文不限
  定位方式: xpath   # 可选择值，看[定位方式]部分
  定位值: //div     #定位值，可填写符合定位规则的表达式
```



