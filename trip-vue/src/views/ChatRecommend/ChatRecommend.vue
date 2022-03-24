<template>
  <div id="chatrecommend">
    <div id="linkman">
      <graph ref="gra"></graph>
    </div>
    <div id="chat_window">
      <ul id="chat_content">
      </ul>
      <div class="chat_input">
        <textarea @keydown.enter.prevent="chatsubmit" rows="6" v-model="chat_content" class="input_chat_text"></textarea>
        <button  @click="chatsubmit" class="chat_text_submit">发送</button>
      </div>
    </div>
  </div>
</template>
<script>
import VisGraph from '@/utils/visgraph.min.js'
import LayoutFactory from '@/utils/visgraph-layout.min.js'
import graph from 'views/ChatRecommend/Graph'
export default {
  data() {
    return {
      link_names:['lyk','zrl','gxy','gzx','zzx'],
      chat_content:'',
      visGraph : null,
      graphData:  {
        nodes:[
          {id:'1',label:'刘备',type:'男',properties:{age:50}},
          {id:'2',label:'关羽',type:'男'},
          {id:'3',label:'张飞',type:'男'}
        ],
        links:[
          {source:'1',target:'2',label:'二弟',properties:{other:'other prop'}},
          {source:'1',target:'3',label:'三弟'}
        ]
      }
    }
  },
  components: {
    graph
    // VisGraph,
    // LayoutFactory
  },
  methods: {
    chatsubmit() {
      console.log(this.chat_content.length);
      var text = this.chat_content;
      var text1 = '';
      switch(text) {
        case '请问黄鹤楼在哪个城市':
          text1 = '湖北武汉';break;
        case '你知道避暑山庄在哪吗':
          text1 = '河北承德';break;
        case '可以推荐一些海边的景点吗':
          text1 = '巴厘岛、亚龙湾';break;
        case '能不能推荐一些小众一点的景点':
          text1 = `为您推荐的结果如下：龙玉雪山、镇远古城、归元禅寺`;break;
        case '武汉都有什么热门景点':
          text1 = `为您推荐的结果如下：黄鹤楼、东湖生态园区、湖北省博物馆`;break;
      }
      var pic = document.createElement('div')
      var pic1 = document.createElement('div')
      pic.className = 'user_touxiang_right'
      pic1.className = 'user_touxiang_left'
      this.chat_content = '';
      var ul = document.getElementById('chat_content');
      var li = document.createElement('li');
      var div = document.createElement('div');
      var div1 = document.createElement('div');
      div.className = "clear"
      div1.className = "clear"
      li.className = "chat_content_item_right";
      var span = document.createElement('span');
      // div.innerText="dsa"
      
      setTimeout(() => {
        var li1 = document.createElement('li');
        li1.className = "chat_content_item_left";
        var span1 = document.createElement('span');
        span1.innerText = text1;
        li1.appendChild(div1);
        li1.appendChild(pic1);
        li1.appendChild(span1);
        ul.appendChild(li1)
        document.getElementById('chat_content').scrollTop = document.getElementById('chat_content').scrollHeight;
      }, 200);   
      this.axios.get('http://47.103.198.84:5000/qa',{
        params:{
          question:text
        }
      })
      .then(res => {
        console.log(res.data);
        this.$refs.gra.update(res.data)
        text1 = res.data.ans
        span.innerText = text;
        li.appendChild(pic);
        li.appendChild(span);
        li.appendChild(div);
        ul.appendChild(li)
      }).catch((e) => {
        console.log(e);
      })
    }
  },
  mounted() {
    // this.visGraph = new VisGraph(document.getElementById('graphVis'));//初始化绘图客户端
    // this.visGraph.drawData(this.graphData);//绘制图完成
    // //定义节点的属性及样式
    // var link = {
    //   source:'2',
    //   target:'3',
    //   label:'兄弟'
    // };
    // var edge = this.visGraph.addEdge(link)
    // edge.lineWidth = 4
  }
}
</script>
<style>
  #chatrecommend {
    width: 100%;
    overflow-x: hidden;
    height: calc(100vh - 70px);
    min-height: 600px;
    background-color: rgb(29, 29, 29);
    display: flex;
    justify-content: center;
  }
  #linkman {
    flex:5;
    height: calc(100% - 20px);
    
    position: relative;
    border-top: 10px solid #c7c6c6;
    border-bottom: 10px solid #c7c6c6;
    border-left: 3px solid #c7c6c6;
    border-right: 3px solid #c7c6c6;
    border-image: -webkit-linear-gradient(#F80, #2ED) 10 10;
    /* border-image: -moz-linear-gradient(#F80, #2ED) 20 20;
    border-image: -o-linear-gradient(#F80, #2ED) 20 20;
    border-image: linear-gradient(#F80, #2ED) 20 20; */
    /* box-shadow: 2px 2px 3px #60c9f0; */
  }

  #chat_window {
    flex: 2;
    height: calc(100% - 10px);
    border-top: 10px solid #F80;
    /* background-color: rgb(8, 8, 8); */
    position: relative;
    /* border-top: 2px solid #acabab; */
  }

  ul#chat_content {
    /* margin: 0 auto; */
    width: 100%;
    height: 75%;
    background-color: rgb(240, 239, 239);
    overflow-y: scroll;
    padding-top: 20px;
  }
  ul#chat_content li {
    /* padding: 5px; */
    margin-bottom: 10px;
    width: 100%;
    /* display: flex; */
    overflow: hidden;
  }
  ul#chat_content li span {
    position: relative;
    background-color: white;
    padding: 5px;
    border-radius: 5px;
  }
  ul#chat_content .chat_content_item_right span{
    margin-left: 10px;
    max-width: 200px;
    background-color: rgb(66, 235, 86);
    float: right;
    margin-right: 10px;
  }
  ul#chat_content .chat_content_item_left span{
    margin-left: 10px;
    max-width: 200px;
    float: left;
  }
  
  .input_chat_text {
    display: block;
    position: absolute;
    border: 1px solid #c9c8c8;
    width: 100%;
    padding: 5px;
    font-size: 19px;
    bottom: 0px;
  }
  .chat_text_submit {
    width: 70px;
    height: 20px;
    line-height: 20px;
    position: absolute;
    right: 5%;
    bottom: 10px;
    /* margin-top: 5px; */
  }
  .user_touxiang_right {
    width: 30px;
    height: 30px;
    float: right;
    margin-right: 15px;
    background: url('~assets/img/ChatRecommend/my_pic.jpg') no-repeat;
    background-size: cover;
  }
  .user_touxiang_left {
    width: 30px;
    height: 30px;
    float: left;
    margin-left: 15px;
    background-color: aqua;
    background: url('~assets/img/ChatRecommend/机器人.png') no-repeat;
    background-size: 100% 100%;
  }
</style>