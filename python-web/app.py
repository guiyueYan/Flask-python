import pandas as pd
from flask import Flask
from flask import render_template, request, redirect
from pyecharts.charts import EffectScatter, Bar, Line, WordCloud, Map, Grid, Pie
from pyecharts.charts import Scatter
import numpy as np
from pyecharts.charts import Geo
from pyecharts import options as opts
from pyecharts.globals import ChartType, SymbolType, ThemeType
from pyecharts.charts import Bar, Tab, Line, Map, Timeline, Funnel
from pyecharts.faker import Faker

app = Flask(__name__)


@app.route('/map')
def index_bar_every_1_tp():
    df = pd.read_csv(r'./static/data/divorce.csv', index_col="province")
    c = (
        Map()
            .add("离婚年均增长率（%）", list(zip(list(df.index), list(df.dir))), "china")
            .set_global_opts(
            title_opts=opts.TitleOpts(title="中国离婚年均增长率（取近5年数据计算所得）"),
            visualmap_opts=opts.VisualMapOpts(max_=16, min_=-14, is_piecewise=True),
        )
    )
    return render_template('index.html',
                           myechart=c.render_embed(),
                           text1='''
                           西藏、贵州、陕西及其附近的省份【集中在地图中心区域的省份】的离婚年均增长率是相对较高的；
                           ''')


@app.route('/map1')
def index_bar_every():
    df1 = pd.read_csv("./static/data/dependency_ratio.csv", index_col="地区")
    tl = Timeline()
    for i in range(2014, 2019):
        map0 = (
            Map()
                .add(
                "抚养比", list(zip(list(df1.index), list(df1["{}年".format(i)]))), "china", is_map_symbol_show=False
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="{}抚养比".format(i), subtitle="",
                                          subtitle_textstyle_opts=opts.TextStyleOpts(color="red", font_size=18,
                                                                                     font_style="italic")),
                visualmap_opts=opts.VisualMapOpts(min_=23, max_=51),

            )
        )
        tl.add(map0, "{}年".format(i))
    return render_template('index.html',
                           myechart=tl.render_embed(),
                           text1='''
                            其实，从中国整体来看，抚养比基本都是在逐年上升的；
                            根据最新一年（2018年）的分省抚养比数据来看：
                            贵州、山东、及其附近的省份【集中在地图中心区域的省份】的抚养比也是相对较高的；
                            结合上一个图表，我们可以得出结论：中国分省离婚率的上涨和抚养比是有一定关系的【抚养比：劳动力的抚养负担】
                           ''')


@app.route('/')
def index_bar_every_4():
    df2 = pd.read_csv(r'./static/data/house_price.csv')
    df = pd.read_csv(r'./static/data/divorce.csv')
    bar = (
        Bar()
            .add_xaxis(df.province.values.tolist())
            .add_yaxis("离婚年均增长率", df.dir.values.tolist())
            .set_global_opts(title_opts=opts.TitleOpts(title="中国分省离婚年均增长率情况"),
                             xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45}))

    )
    line = (
        Line()
            .add_xaxis(df2.province.values.tolist())
            .add_yaxis("房价年均增长率", df2.increase.values.tolist())
            .set_global_opts(
            title_opts=opts.TitleOpts(title="中国分省住宅商品房价格年均增长率情况", pos_top="48%"),
            legend_opts=opts.LegendOpts(pos_top="48%"),
            xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45})
        )
    )

    grid = (
        Grid()
            .add(bar, grid_opts=opts.GridOpts(pos_bottom="60%"))
            .add(line, grid_opts=opts.GridOpts(pos_top="60%"))
    )
    return render_template('index.html',
                           myechart=grid.render_embed(),
                           text1='''离婚年均增长率相对较低的省份：北京、上海、新疆、黑龙江、吉林、内蒙古；
                                但其实，北京、上海的房价年均增长率是非常高的，且新疆、黑龙江这些省份的房价年均增长率也是处于中游水平；
                            可以很明显地从整个图中看出，离婚年均增长率和房价年均增长率之间的关联性不大。''')


@app.route('/divorce')
def index_bar_every_2():
    prevention = request.args.get("city", 2014)
    df = pd.read_csv(r'./static/data/divorce.csv')
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(
            df.province.values.tolist()
        )
            .add_yaxis("离婚登记数/万",
                       df["{}年".format(prevention)].values.tolist()
                       )
            .set_global_opts(title_opts=opts.TitleOpts(title="{}年中国分省离婚登记数".format(prevention), subtitle=""),
                             xaxis_opts=opts.AxisOpts(name_rotate=60, name="省份", axislabel_opts={"rotate": 45}))
    )
    province_x = df.province.values.tolist()
    tim = df["{}年".format(prevention)].values.tolist()
    dir = df.dir.values.tolist()

    return render_template('index.html',
                           myechart=bar.render_embed(),
                           data=[[i, j, k] for i, j, k in zip(province_x, tim, dir)],
                           col=["province", "{}年".format(prevention), "dir"],
                           text1='''西藏、青海、海南、宁夏这些地区的离婚登记数都是比较少的；
                四川、河南、江苏、山东这些地区的离婚登记数都是比较多的；''')


if __name__ == '__main__':
    app.run(debug=True)
