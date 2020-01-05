<div align="center">
  <h1>Python_flask技术文档之总结说明</h1>
  <p>Written by Yanguiyue for description of Python-webapp.</p>
</div>

### :sun_with_face:**个人信息**：
* 姓名：颜癸悦
* 班级：网新2班
* 学号：181013128  

### :link:**python项目查看**：
* [项目代码详情GitHub_URL](https://github.com/guiyueYan/python-flask/tree/master/python-web)
* [pythonanywhere个人部署URL](http://yuiane.pythonanywhere.com/)  

### :thought_balloon:项目主要URL及功能如下：  

    /  首页展示分省离婚增长率与商品住宅房价格增长  

    /map 展示离婚增长率  

    /map1 展示2014-2018抚养比  

    /divorce 展示2014-2018分省离婚登记数  

### :heavy_check_mark:**数据传递描述**：  

#### HTML档描述：

1.**布局**：首先用margin:auto让标题和数据来源等水平居中。用style="float: left"让图像向左浮动，图表大小width: 70%。  


2.**图表**：用table标签里的border="1"，让表格外边框和每个单元格都有了实线，让数据更易观看。colspan=3为了让中国分省离婚登记数通过选择年份后的3行单元格（省份，年份，dir）合并成一行。由于表格是显示在图表之下，利用clear:both可以消除上面与他同级的加了float:left 的div元素对布局产生的影响，页面布局就不会太乱。  


3.**html与python文档的交互体现**：在html页面设置一个空的图表容器{{ mychart|safe }}，通过后端py文件进行对应可视化函数传输数据给其中三个图表一个提交按钮<button type="submit">，提交时图表数据会提交到名为 "/" 的页面，也就是增长率对比图这个页面，map/map1/divorce的页面也是这种方法体现。最后一个各省份的图表通过select 元素创建多选下拉框（选择2014-2018年）。使用<select name="city"><option value="2014-2018年">用于对提交的表格数据进行识别表格中有关各省市的数据，最后前端页面只显示此年份的各省市有关数据。


4.**html与python档的交互**：利用{% if data %}和{% for i in col %}两个if语句用for循环选择app.py里最后一个函数的变量cols里面的省份，年份，dir。


5.**条件判断**：为了在图表下面加分析和结论，使用{% if %}标签，在app.py中每个函数中新建一个变量text1，然后在index.html中使用{% if %}标签进行判断。使得在每个图表的显示中都能显示出相应结论。&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;   
#### python档描述：&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; &emsp;&emsp;&emsp;1.**主要运用的模块**：pandas、flask、pyecharts、numpy  
2.**具体操作**：


首先，每一个视图函数都要用pandas模块pd.read_csv（）读取每个表对应的csv文件数据。


然后用@app.route(路由规则) 的方式绑定可视化视图函数, route() 会告诉告诉 Flask 什么样的URL 能触发我们的函数，就像项目里的@app.route('/map')一样，接着将17级提供的图表函数放入py文件中。


最后return render_template会根据后面传入的参数，对html进行修改渲染。例如第一个图表：离婚年均增长率，用render_embed()将定义c的图表存储在图表容器myechart中，利用jinjia2语法的动态数据绑定将图表数据还有text1标签的内容一并对html进行渲染返回到前端页面。&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;webapp动作描述：


1.**提交按钮**：项目启动后显示的主页面有三个提交按钮，分别对应的是中国分省离婚增长率与商品住宅房价格增长情况/离婚增长率/2014-2018抚养比这三个图表。通过点击可以跳转到相应的图表，并显示出相应的故事结论。


2.**下拉框**：通过选择查看各年份中国分省离婚登记数（2014-2018年）下拉框，Do it！实现相应各年份数据的提取，前端正确显示图和表的相应的数据交互变化。  

