#项目结构

framework/  
├── actions  
├── baseconf   
│   ├── logger.json  
│   └── projectConfig.yaml  
├── docs  
│   ├── frameHelp.md  
│   ├── mdHelp.md  
│   └── yamlHelp.md  
├── drivers  
│   ├── chrome  
│   │   └── chromedriver_win32_78.exe  
│   ├── firefox  
│   │   ├── geckodriver-v0.26.0-win32.exe  
│   │   └── geckodriver-v0.26.0-win64.exe  
│   └── ie  
│       ├── IEDriverServer_Win32_3.150.1.exe  
│       └── IEDriverServer_x64_3.150.1.exe  
├── elements  
├── getrootdir.py  
├── requirements.txt  
├── testcases   
├── testdata  
└── utils  
    ├── appiumUtil.py  
    ├── dbUtil.py  
    ├── initDriverUtil.py  
    ├── logUtil.py  
    ├── seleniumUtil.py  
    └── yamlParser.py

# 目录说明
* actions 存放页面操作方法，建议每个页面或者以功能为单位每个功能一个py文件
* baseconf 存放公共配置文件
* docs 帮助文档
* drivers 浏览器驱动包
* elements 页面元素，建议一个页面或者功能一个py文件
* getrootdir.py 获取项目的绝对路径
* requirements.txt 第三方依赖包
* testcases 测试用例存放目录
* testdata 测试数据存放路径
* utils 工具类
> + initDriverUtil.py appium/selenium驱动初始化
> + logUtil.py 日志工具
> + yamlParser.py  yaml解析工具
> + appiumUtil.py  appium特有的操作
> + seleniumUtil.py selenium操作

# projectConfig.yaml配置规范说明
文件共分为6个节点：
> + 项目基础项配置
> + 项目信息配置
> + 数据库配置
> + 浏览器驱动配置
> + 移动设备信息配置
> + APPIUM配置

## 项目基础项配置
总共涉及projectType/project/browser三项配置
* projectType:项目类型配置，目前仅支持web/app/api三种配置
* project:项目名称，与【项目信息配置】中的一级节点对应一致，当前仅支持配置一个项目
* browser: 浏览器类型配置，与【浏览器驱动配置】中的一级节点对应一致

## 项目信息配置
*可以同时配置多个项目，但仅配置在【项目基础项配置】中“project”的项目生效
> 1.web项目信息配置
rewardbase:  \#项目名称，建议用英文，与【项目基础项配置】中的“project”相同
  url: https://www.baidu.com  \#项目地址
  normalUser:   \#登录用户信息，可以配置多个
    username: admin
    password: admin123
  dbinfo:  \#数据库信息
    type: sqlite3        \#数据库类型,mysql/oracle/hive/sqlite3
  timeout: 30  \#超时时间设置

  \*如果同一个项目有多个地址，建议配置多个项目

> 2.APP项目配置
appOperateInfo:  \#项目名称，建议用英文，与【项目基础项配置】中的“project”相同
  appInfo:  \#APK信息
    appName: baidu.apk  \#APK名称
    appActivity: com.baidu.searchbox.MainActivity \#APK入口类
    appPackage: com.baidu.searchbox  \#APK包名
  useDevice: device1   \#设备名称，与【移动设备信息配置】中的设备名称对应一致
  normalUser:  \#登录用户信息，可以配置多个
    username: admin
    password: admin123
  dbinfo:  \#数据库信息
    type: oracle        \#数据库类型


## 数据库配置
*当前仅实现了oracle/mysql/sqlite3三种数据库
mysql:  \#数据库类型
  jdbcClass: com.mysql.jdbc.Driver    \#jdbc驱动类名称
  jdbcurl: jdbc:mysql://127.0.0.1:3306/autoadmin   \#jdbc驱动url，autoadmin表示数据库名称
  username: autoadmin  \#数据库用户
  password: Zwx232372  \#数据库密码

oracle:  \#数据库类型
  jdbcClass: oracle.jdbc.driver.OracleDriver    \#jdbc驱动类名称
  jdbcurl: jdbc:oracle:thin:@localhost:1521:yfbceg \#jdbc驱动url
  username: autoadmin  \#数据库用户
  password: Zwx232372  \#数据库密码

sqlite:  \#数据库类型
  jdbcClass: org.sqlite.JDBC  \#jdbc驱动类名称
  jdbcurl: jdbc:sqlite:D:\01_Devspace\python\autotest\autotest\db.sqlite3  \#sqlite3数据库文件



##   浏览器驱动配置
webbrowser:  \#配置开始标识
  chrome_x86_v78: chromedriver_win32_78.exe
  \#浏览器别名，建议:浏览器名称_系统平台_架构_版本: 驱动文件名称，该驱动文件放在drivers目录下对应浏览器类别目录


## 移动设备信息配置
device1:  \#设备名称
  deviceName: 7396257f   \#设备序列号
  platformVersion: 9     \#系统版本号


## appium_config \#APPIUM配置，默认配置，不用修改

