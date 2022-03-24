<template>
  <div id="vip">
    <div id="vip_title">
      <div class="vip_destination">目的地 > 武汉 > 武汉景点</div>
      <div class="vip_title_names">
        <div class="chinese_name">黄鹤楼</div>
        <div class="english_name">Yellow Crane Tower</div>
      </div>
      <div id="pie"></div>
    </div>
    <div id="vip_pro">
      <div class="gaikuang">概况</div>
      <div class="comments">评价</div>
    </div>
    <div id="vip_content">
      <div class="content_img">
        <div class="content_img1">
          <img src="~assets/img/vip/黄鹤楼1.png" alt="">
        </div>
        <div class="content_img2">
          <img src="~assets/img/vip/黄鹤楼2.jpeg" alt="">
          <img src="~assets/img/vip/黄鹤楼3.jpeg" alt="">
        </div>
      </div>
      <div class="content_profile">
        <p>黄鹤楼位于武昌江畔，紧邻长江大桥，有“天下江山第一楼”的美誉，是"江南三大名楼"之一。</p>
        <p>因“昔人已乘黄鹤去，此地空余黄鹤楼”诗句而名扬天下，李白、毛泽东等都为黄鹤楼留下诗词。</p>
        <p>建于蛇山之上，登上楼顶远眺，武汉三镇和长江尽收眼底，视野开阔，是武汉的城市地标之一。</p>
        <p>景区内还有大量的石碑、石刻，都是历代名人的真迹，极具艺术价值。</p>
        <p>每天10:30, 11:30, 12:30, 14:00, 15:00, 16:00在落梅轩有楚地特色的编钟歌舞表演，30元/位。</p>
      </div>
    </div>
    <footerpage></footerpage>
  </div>
</template>
<script>
import footerpage from 'components/content/footer/FooterPage'
import * as echarts from 'echarts'
export default {
  data() {
    return {
      mychart:''
    }
  },
  components: {
    footerpage
  },
  mounted() {
    var chartDom = document.getElementById('pie')
    this.myChart = echarts.init(chartDom);
    var option;

     option = {
       color: ["#e5ee64", "#f4874b"],
      legend: {
        orient: "vertical",
        left: "left",
        data: ["差评", "好评"],
        textStyle:{
          color:'white'
        }
      },
      selectorLabel:{
        color:'#fff'
      },
      series: [{
        type: "pie",
        data: [{
          value: 4535,
          name: "差评"
        }, {
          value: 28754,
          name: "好评"
        }],
        label: {
          color: "#f7f0ec"
        }
      }],
      label: {
        width:400
      }
}

    option && this.myChart.setOption(option);
  }
}
</script>
<style>
#vip {
  width: 100%;
  background-color: #694545;
}
#vip_title {
  margin: 0 auto;
  width:70%;
  height: 160px;
  /* background-color: coral; */
  position: relative;
  border-bottom: 1px solid #dfdede;
  color: white;
}
#pie {
  width: 400px;
  height: 200px;
  position: absolute;
  right: 100px;
  bottom: -50px;
  color: white;
}
.vip_destination {
  padding-top: 20px;
  margin-left: 10px;
  font-size: 14px;
}
.vip_title_names {
  position: absolute;
  width: 300px;
  height: 70px;
  margin-left: 10px;
  bottom: 10px;
}
.chinese_name{
  font-size: 35px;
  margin-bottom: 5px;
}
#vip_pro {
  margin: 0 auto;
  width: 70%;
  height: 50px;
  display: flex;
  padding-bottom: 1px;
  border-bottom: 1px solid white;
}
#vip_pro div.gaikuang {
  height: 50px;
  width: 80px;
  text-align: center;
  font-size: 18px;
  line-height: 50px;
  color: tomato;
  border-bottom: 2px solid tomato;
}
#vip_pro div.comments {
  height: 50px;
  width: 80px;
  text-align: center;
  font-size: 18px;
  line-height: 50px;
  color: white;
}
#vip_content {
  width: 70%;
  margin: 0 auto;
  margin-top: 20px;
  height:600px;
  /* background-color: wheat; */
}
#vip_content .content_img {
  width: 100%;
  height: 350px;
  display: flex;
  padding-bottom: 20px;
  border-bottom: 1px solid #dad8d8;
}
.content_img .content_img1 {
  flex: 2;
  height: 100%;
  /* background-color: violet; */
}
.content_img1 img {
  height: 100%;
  width: 100%;
}
.content_img .content_img2 {
  flex: 1;
  height: 100%;
}
.content_img2 {
  overflow: hidden;
}
.content_img2 img{
  height: 50%;
  width: 100%;
}
.content_profile {
  margin-top: 20px;
}
.content_profile p {
  border-left: 2px solid rgb(133, 131, 131);
  padding-left: 5px;
  margin-left: 10px;
  margin-top: 10px;
  color: white;
}

</style>