<template>
  <div id="graph">
  </div>
</template>
<script>
import * as echarts from 'echarts'
export default {
  data() {
    return {
      myChart:{},
      datas:[],
      links:[ //edges是其别名代表节点间的关系数据。
      ],
      option:{
      title:{
        text:'关系图'
      },
      tooltip: {},
      series: [
        {
          type:'graph',
          name:'关系系统',
          layout:'force',
          force: {
            repulsion:600,
            gravity:0.03,
            edgeLength:[50,100],
            layoutAnimation:true
          },
          roam:true,
          draggable:true,
          focusNodeAdjacency:true,
          data:[],
          links:[],
          categories : [ //symbol name：用于和 legend 对应以及格式化 tooltip 的内容。 label有效
                    {
                        name : '负载',
                        symbol : 'rect',
                        label : { //标签样式
                        }
                    }, {
                        name : '中间件',
                        symbol : 'rect'
                    }, {
                        name : '端口号',
                        symbol : 'roundRect'
                    }, {
                        name : '数据库',
                        symbol : 'roundRect'
                    }, {
                        name : '用户名',
                        symbol : 'roundRect'
          } ],
          lineStyle : { //==========关系边的公用线条样式。
                        normal : {
                            color : 'rgba(255,0,255,0.4)',
                            width : '3',
                            type : 'dotted', //线的类型 'solid'（实线）'dashed'（虚线）'dotted'（点线）
                            curveness : 0.3, //线条的曲线程度，从0到1
                            opacity : 1
                        // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5
                        },
                        emphasis : {//高亮状态

                        }
          },
          label : { //=============图形上的文本标签
                        normal : {
                            show : true,//是否显示标签。
                            position : 'inside',//标签的位置。['50%', '50%'] [x,y]
                            textStyle : { //标签的字体样式
                                color : '#cde6c7', //字体颜色
                                fontStyle : 'normal',//文字字体的风格 'normal'标准 'italic'斜体 'oblique' 倾斜
                                fontWeight : 'bolder',//'normal'标准'bold'粗的'bolder'更粗的'lighter'更细的或100 | 200 | 300 | 400...
                                fontFamily : 'sans-serif', //文字的字体系列
                                fontSize : 12, //字体大小
                            }
                        },
                        emphasis : {//高亮状态

                        }
          },
          itemStyle : {//===============图形样式，有 normal 和 emphasis 两个状态。normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                        normal : { //默认样式
                            label : {
                                show : true
                            },
                            borderType : 'solid', //图形描边类型，默认为实线，支持 'solid'（实线）, 'dashed'(虚线), 'dotted'（点线）。
                            borderColor : 'rgba(255,215,0,0.4)', //设置图形边框为淡金色,透明度为0.4
                            borderWidth : 2, //图形的描边线宽。为 0 时无描边。
                            opacity : 1
                        // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5

                        },
                        emphasis : {//高亮状态

                        }
          },
          edgeSymbol : [ 'none', 'none' ],//边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。默认不显示标记，常见的可以设置为箭头，如下：edgeSymbol: ['circle', 'arrow']
          edgeSymbolSize : 10,//边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
          edgeLabel : {//==============线条的边缘标签 
                        normal : {
                            show : true
                        },
                        emphasis : {//高亮状态

                        }
          },
          legend : { //=========圖表控件
                    show : true,
                    data : [ {
                        name : '负载',
                        
                        icon : 'rect'//'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
            
                    },
                    {
                        name : '中间件',
                        
                        icon : 'roundRect'
                    }, {
                        name : '端口号',
                        
                        icon : 'circle'
                    }, {
                        name : '数据库',
                        
                        icon : 'circle'
                    },{
                        name : '用户名',
                        icon : 'roundRect'
                    } ]
                },
        }
      ]
    }
    }
  },
  mounted() {
    this.myChart = echarts.init(document.getElementById('graph'));
    // this.option.data.push(...this.datas);
    // this.option.links.push(this.links);
    this.myChart.setOption({
      title:{
        text:'关系图'
      },
      tooltip: {},
      series: [
        {
          type:'graph',
          name:'关系系统',
          layout:'force',
          force: {
            repulsion:600,
            gravity:0.03,
            edgeLength:[50,100],
            layoutAnimation:true
          },
          roam:true,
          draggable:true,
          focusNodeAdjacency:true,
          data:this.datas,
          links:this.links,
          categories : [ //symbol name：用于和 legend 对应以及格式化 tooltip 的内容。 label有效
                    {
                        name : '负载',
                        symbol : 'rect',
                        label : { //标签样式
                        }
                    }, {
                        name : '中间件',
                        symbol : 'rect'
                    }, {
                        name : '端口号',
                        symbol : 'roundRect'
                    }, {
                        name : '数据库',
                        symbol : 'roundRect'
                    }, {
                        name : '用户名',
                        symbol : 'roundRect'
          } ],
          lineStyle : { //==========关系边的公用线条样式。
                        normal : {
                            color : 'rgba(255,0,255,0.4)',
                            width : '3',
                            type : 'dotted', //线的类型 'solid'（实线）'dashed'（虚线）'dotted'（点线）
                            curveness : 0.3, //线条的曲线程度，从0到1
                            opacity : 1
                        // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5
                        },
                        emphasis : {//高亮状态

                        }
          },
          label : { //=============图形上的文本标签
                        normal : {
                            show : true,//是否显示标签。
                            position : 'inside',//标签的位置。['50%', '50%'] [x,y]
                            textStyle : { //标签的字体样式
                                color : '#cde6c7', //字体颜色
                                fontStyle : 'normal',//文字字体的风格 'normal'标准 'italic'斜体 'oblique' 倾斜
                                fontWeight : 'bolder',//'normal'标准'bold'粗的'bolder'更粗的'lighter'更细的或100 | 200 | 300 | 400...
                                fontFamily : 'sans-serif', //文字的字体系列
                                fontSize : 12, //字体大小
                            }
                        },
                        emphasis : {//高亮状态

                        }
          },
          itemStyle : {//===============图形样式，有 normal 和 emphasis 两个状态。normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                        normal : { //默认样式
                            label : {
                                show : true
                            },
                            borderType : 'solid', //图形描边类型，默认为实线，支持 'solid'（实线）, 'dashed'(虚线), 'dotted'（点线）。
                            borderColor : 'rgba(255,215,0,0.4)', //设置图形边框为淡金色,透明度为0.4
                            borderWidth : 2, //图形的描边线宽。为 0 时无描边。
                            opacity : 1
                        // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5

                        },
                        emphasis : {//高亮状态

                        }
          },
          edgeSymbol : [ 'none', 'none' ],//边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。默认不显示标记，常见的可以设置为箭头，如下：edgeSymbol: ['circle', 'arrow']
          edgeSymbolSize : 10,//边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
          edgeLabel : {//==============线条的边缘标签 
                        normal : {
                            show : true
                        },
                        emphasis : {//高亮状态

                        }
          },
          legend : { //=========圖表控件
                    show : true,
                    data : [ {
                        name : '负载',
                        
                        icon : 'rect'//'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
            
                    },
                    {
                        name : '中间件',
                        
                        icon : 'roundRect'
                    }, {
                        name : '端口号',
                        
                        icon : 'circle'
                    }, {
                        name : '数据库',
                        
                        icon : 'circle'
                    },{
                        name : '用户名',
                        icon : 'roundRect'
                    } ]
                },
        }
      ]
    })
    this.datas.push({
                      id : 50,
                      category : 0,
                      name : '你好',
                      symbol : 'roundRect',
                      value : 70,
                      symbolSize : 40
    })
      this.myChart.setOption({
      title:{
        text:'关系图'
      },
      tooltip: {},
      series: [
        {
          type:'graph',
          name:'关系系统',
          layout:'force',
          force: {
            repulsion:500,
            gravity:0.03,
            edgeLength:[50,100],
            layoutAnimation:true
          },
          roam:true,
          draggable:true,
          focusNodeAdjacency:true,
          data:this.datas,
          links:this.links,
          categories : [ //symbol name：用于和 legend 对应以及格式化 tooltip 的内容。 label有效
                    {
                        name : '负载',
                        symbol : 'rect',
                        label : { //标签样式
                        }
                    }, {
                        name : '中间件',
                        symbol : 'rect'
                    }, {
                        name : '端口号',
                        symbol : 'roundRect'
                    }, {
                        name : '数据库',
                        symbol : 'roundRect'
                    }, {
                        name : '用户名',
                        symbol : 'roundRect'
          } ],
          lineStyle : { //==========关系边的公用线条样式。
                        normal : {
                            color : 'rgba(255,0,255,0.4)',
                            width : '3',
                            type : 'dotted', //线的类型 'solid'（实线）'dashed'（虚线）'dotted'（点线）
                            curveness : 0.3, //线条的曲线程度，从0到1
                            opacity : 1
                        // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5
                        },
                        emphasis : {//高亮状态

                        }
          },
          label : { //=============图形上的文本标签
                        normal : {
                            show : true,//是否显示标签。
                            position : 'inside',//标签的位置。['50%', '50%'] [x,y]
                            textStyle : { //标签的字体样式
                                color : '#cde6c7', //字体颜色
                                fontStyle : 'normal',//文字字体的风格 'normal'标准 'italic'斜体 'oblique' 倾斜
                                fontWeight : 'bolder',//'normal'标准'bold'粗的'bolder'更粗的'lighter'更细的或100 | 200 | 300 | 400...
                                fontFamily : 'sans-serif', //文字的字体系列
                                fontSize : 12, //字体大小
                            }
                        },
                        emphasis : {//高亮状态

                        }
          },
          itemStyle : {//===============图形样式，有 normal 和 emphasis 两个状态。normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                        normal : { //默认样式
                            label : {
                                show : true
                            },
                            borderType : 'solid', //图形描边类型，默认为实线，支持 'solid'（实线）, 'dashed'(虚线), 'dotted'（点线）。
                            borderColor : 'rgba(255,215,0,0.4)', //设置图形边框为淡金色,透明度为0.4
                            borderWidth : 2, //图形的描边线宽。为 0 时无描边。
                            opacity : 1
                        // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5

                        },
                        emphasis : {//高亮状态

                        }
          },
          edgeSymbol : [ 'none', 'none' ],//边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。默认不显示标记，常见的可以设置为箭头，如下：edgeSymbol: ['circle', 'arrow']
          edgeSymbolSize : 10,//边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
          edgeLabel : {//==============线条的边缘标签 
                        normal : {
                            show : true
                        },
                        emphasis : {//高亮状态

                        }
          },
          legend : { //=========圖表控件
                    show : true,
                    data : [ {
                        name : '负载',
                        
                        icon : 'rect'//'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
            
                    },
                    {
                        name : '中间件',
                        
                        icon : 'roundRect'
                    }, {
                        name : '端口号',
                        
                        icon : 'circle'
                    }, {
                        name : '数据库',
                        
                        icon : 'circle'
                    },{
                        name : '用户名',
                        icon : 'roundRect'
                    } ]
                },
        }
      ]
    })
  },
  methods: {
    update(node) {
      console.log('更新');
      this.myChart.clear();
      this.datas = []
      this.links = []
      this.datas.push(...node.nodes)
      this.links.push(...node.links)
      setTimeout(() => {
        this.myChart.setOption({
      title:{
        text:'关系图'
      },
      tooltip: {},
      series: [
        {
          type:'graph',
          name:'关系系统',
          layout:'force',
          force: {
            repulsion:600,
            gravity:0.03,
            edgeLength:[50,100],
            layoutAnimation:true
          },
          roam:true,
          draggable:true,
          focusNodeAdjacency:true,
          data:this.datas,
          links:this.links,
          categories : [ //symbol name：用于和 legend 对应以及格式化 tooltip 的内容。 label有效
                    {
                        name : '负载',
                        symbol : 'rect',
                        label : { //标签样式
                        }
                    }, {
                        name : '中间件',
                        symbol : 'rect'
                    }, {
                        name : '端口号',
                        symbol : 'roundRect'
                    }, {
                        name : '数据库',
                        symbol : 'roundRect'
                    }, {
                        name : '用户名',
                        symbol : 'roundRect'
          } ],
          lineStyle : { //==========关系边的公用线条样式。
                        normal : {
                            color : 'rgba(255,0,255,0.4)',
                            width : '3',
                            type : 'dotted', //线的类型 'solid'（实线）'dashed'（虚线）'dotted'（点线）
                            curveness : 0.3, //线条的曲线程度，从0到1
                            opacity : 1
                        // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5
                        },
                        emphasis : {//高亮状态

                        }
          },
          label : { //=============图形上的文本标签
                        normal : {
                            show : true,//是否显示标签。
                            position : 'inside',//标签的位置。['50%', '50%'] [x,y]
                            textStyle : { //标签的字体样式
                                color : '#cde6c7', //字体颜色
                                fontStyle : 'normal',//文字字体的风格 'normal'标准 'italic'斜体 'oblique' 倾斜
                                fontWeight : 'bolder',//'normal'标准'bold'粗的'bolder'更粗的'lighter'更细的或100 | 200 | 300 | 400...
                                fontFamily : 'sans-serif', //文字的字体系列
                                fontSize : 12, //字体大小
                            }
                        },
                        emphasis : {//高亮状态

                        }
          },
          itemStyle : {//===============图形样式，有 normal 和 emphasis 两个状态。normal 是图形在默认状态下的样式；emphasis 是图形在高亮状态下的样式，比如在鼠标悬浮或者图例联动高亮时。
                        normal : { //默认样式
                            label : {
                                show : true
                            },
                            borderType : 'solid', //图形描边类型，默认为实线，支持 'solid'（实线）, 'dashed'(虚线), 'dotted'（点线）。
                            borderColor : 'rgba(255,215,0,0.4)', //设置图形边框为淡金色,透明度为0.4
                            borderWidth : 2, //图形的描边线宽。为 0 时无描边。
                            opacity : 1
                        // 图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。默认0.5

                        },
                        emphasis : {//高亮状态

                        }
          },
          edgeSymbol : [ 'none', 'none' ],//边两端的标记类型，可以是一个数组分别指定两端，也可以是单个统一指定。默认不显示标记，常见的可以设置为箭头，如下：edgeSymbol: ['circle', 'arrow']
          edgeSymbolSize : 10,//边两端的标记大小，可以是一个数组分别指定两端，也可以是单个统一指定。
          edgeLabel : {//==============线条的边缘标签 
                        normal : {
                            show : true
                        },
                        emphasis : {//高亮状态

                        }
          },
          legend : { //=========圖表控件
                    show : true,
                    data : [ {
                        name : '负载',
                        
                        icon : 'rect'//'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow'
            
                    },
                    {
                        name : '中间件',
                        
                        icon : 'roundRect'
                    }, {
                        name : '端口号',
                        
                        icon : 'circle'
                    }, {
                        name : '数据库',
                        
                        icon : 'circle'
                    },{
                        name : '用户名',
                        icon : 'roundRect'
                    } ]
                },
        }
      ]
      })
      }, 500);
      
    }
  }
}
</script>
<style>
  #graph {
    height: 100%;
    background-color: rgb(16,12,42);
  }
</style>