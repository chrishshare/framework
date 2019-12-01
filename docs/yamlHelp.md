#yaml教程
##认识YAML

YAML是一个类似 XML、JSON 的标记性语言。YAML 强调以数据为中心，并不是以标识语言为重点。因而 YAML 本身的定义比较简单，号称“一种人性化的数据格式语言”

YAML语法特色如下：  
* 大小写敏感  
* 使用缩进表示层级关系
* 缩进时不允许使用TAB键，只允许使用空格  
* 缩进的空格不重要，只要同层级的元素左对齐即可


##YAML结构  

YAML文件可以由一个或多个文档组成，文档间使用“---”作为文档的开始，使用“...”作为文档的结束  
如果只是单个文档，分隔符“---”可以省略  
每个文档并不需要使用“...”来表示结束，但是建议使用  

##YAML编写规范    
* 文档使用 Unicode 编码作为字符标准编码，例如：UTF-8  
* 使用#表示注释内容  
* 使用空格作为嵌套缩进工具。通常建议使用两个空格缩进，不建议使用tab

###对象  
1. 使用冒号代表，格式为key：value，且冒号后面要加一个空格  
key: value  
2. 使用缩进表示层级关系  
key:
    child-key1: value1  
    child-key2: value2   
YAML中还支持流式（flow）语法表示对象  
key: {child-key1: value1, child-key2: value2}   
 
3. 较为复杂的对象格式，可以使用问号加一个空格代表一个复杂的key，配合一个冒号加一个空格代表一个value：  

   ?  
         - complexkey1  
        - complexkey2  
   :  
        - complexvalue1  
        - complexvalue2  
  
意思即对象的属性是一个数组[complexkey1,complexkey2]，对应的值也是一个数组[complexvalue1,complexvalue2]  
###数组  
使用一个短横线加一个空格代表一个数组项：  
   hobby:  
        - Java  
        - LOL  
一个相对复杂的例子：
companies:  
        -  
        id: 1  
        name: company1  
        price: 200W  
        -  
        id: 2  
        name: company2  
        price: 500W  
* 意思是companies属性是一个数组，每一个数组元素又是由id,name,price三个属性构成；  
数组也可以使用流式(flow)的方式表示：  
companies: [{id: 1,name: company1,price: 200W},{id: 2,name: company2,price: 500W}]  

###常量
YAML中提供了多种常量结构，包括：整数，浮点数，字符串，NULL，日期，布尔，时间。下面使用一个例子来快速了解常量的基本使用：  
        boolean:   
            - TRUE    #true,True都可以  
            - FALSE  #false，False都可以  
        float:  
            - 3.14  
            - 6.8523015e+5  #可以使用科学计数法  
        int:  
            - 123  
            - 0b1010_0111_0100_1010_1110    #二进制表示  
        null:  
            nodeName: 'node'  
            parent: ~  #使用~表示null  
        string:  
            - 哈哈  
            - 'Hello world'  #可以使用双引号或者单引号包裹特殊字符  
            - newline  
            newline2    #字符串可以拆成多行，每一行会被转化成一个空格  
        date:  
            - 2018-02-17    #日期必须使用ISO 8601格式，即yyyy-MM-dd  
        datetime:   
             -  2018-02-17T15:02:31+08:00    #时间使用ISO 8601格式，时间和日期之间使用T连接，最后使用+代表时区  
###一些特殊符号
* !! YAML中使用!!做类型强行转换：
        