Selenium元素定位方法总共有八大类，分别是：id，name，class name，tag name，link text，partial link text，xpath，css。  
八种定位方法没有哪个是最好的，在不同的场景下需要使用不用的定位方法。

示例html文件如下：
```html
<!DOCTYPE html>
<html lang="zh-cn">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="referrer" content="origin" />
<title>centos7 部署openstf - ianduin - 博客园</title>
</head>
<body>
    <div>
    <a name="top">猜猜看</a>
	<img alt="点我试试呀" src="/images/bg.jpg">
    <div id="home">
        <div id="cnblogs_post_body" class="blogpost-body">
			<p><span style="line-height: 1.5">openstf项目开源地址：</span></p>
		</div>
		<div class="highlighter-rouge">
			<div class="newsItem">
				<h3 class="catListTitle">公告</h3>
				<div id="blog-news">
					明天也许是个好日子吧
				</div>
			</div>
		</div>
        </div>
    </div>
</body>
</html>
```