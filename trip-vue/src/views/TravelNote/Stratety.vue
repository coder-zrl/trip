<template>
  <div id="stratety">
    <div id="stratety_title">
      <div>旅游攻略</div>
    </div>
    <div id="hotStratety">
      <div class="Stratety_item" v-for="(item,index) in Stratety" :key="item.url">
        <div class="Stratety_item_img">
          <img :src="item.url" alt="">
        </div>
        <div class="Stratety_item_content">
          <div class="Stratety_item_title" @click="todetail('/detail/nanjiang')">{{item.title}}</div>
          <div class="Stratety_item_details">{{item.details}}</div>
          <div class="Stratety_item_bottom">
            <span class="Stratety_item_local">{{item.local}} /</span>
            <span class="Stratety_item_time">{{item.time}}</span>
            <span class="Stratety_item_viewNumber"> 浏览·{{item.viewsNumber}}</span>
            <div class="Stratety_item_islike" @click="changeLike(index)">
              <img src="~assets/img/HomePage/unlike.png" alt="" v-if="!item.islike">
              <img src="~assets/img/HomePage/like.png" alt="" v-else>
            </div>   
          </div>
        </div>
      </div>
    </div>
    <div id="stratety_page">
      <div class="pages">1</div>
      <div class="pages">2</div>
      <div class="pages">3</div>
      <div class="pages">4</div>
      <div class="pages">5</div>
      <div class="next">下一页</div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      Stratety:[
        {
          url:require('assets/img/TravelNote/南疆1.png'),
          title:'万里无疆 | 7月南疆人文自驾环线攻略，走遍中国还差一个你（含私藏路线）',
          details:'说起新疆，大家对天池、喀纳斯湖、伊犁草原、赛里木湖、吐鲁番这些景区都不会陌生，他们也仿佛成了新疆的标签和名片。但其实，他们只代表了新疆一半的特色，这一半，就是北疆。而新疆的另一半——南疆，世人却知之甚少。',
          local:'新疆',
          time:'2021-4-24',
          viewsNumber:'758689',
          islike:false
        },
        {
          url:require('assets/img/HomePage/test1.png'),
          title:'超值干货 | 北京故宫必备游览手册，解锁故宫的正确打开方式（含私藏路线）',
          details:'前面也提到，故宫中轴线上的宫殿：三大殿（太和殿、中和殿和保和殿）、后三宫（乾清宫、交泰殿和坤宁宫...',
          local:'北京',
          time:'2021-4-9',
          viewsNumber:'18689',
          islike:false
        },
        {
          url:require('assets/img/HomePage/test2.png'),
          title:'武汉赏樱 | 十日樱花作意开，绕花岂惜日千回？',
          details:'行程第一天，初见武汉9点半的飞剑，免不了在机场拍拍拍。12:05我们准时到武汉...',
          local:'武汉',
          time:'2021-3-2',
          viewsNumber:'2429',
          islike:false
        },
        {
          url:require('assets/img/HomePage/test3.png'),
          title:'稻城亚丁 | 天谴神功，底蕴香醇，惊世园田。网神山三枯，观音祥善，金刚威猛，师利超然。',
          details:'本人学生党，没事喜欢到处走走，瞅准了清明假期跟同学商量了一下...',
          local:'稻城',
          time:'2020-5-24',
          viewsNumber:'5876',
          islike:false
        },
      ]
    }
  },
  methods: {
    changeLike(index) {
      this.Stratety[index].islike = !this.Stratety[index].islike;
    },
    todetail(path) {
      this.$router.push(path)
    }
  }
}
</script>
<style>
  #stratety {
    width: 100%;
    margin: 0 auto;
    padding-top: 45px;
    position: relative;
  }
  #stratety_title {
    color: white;
    width: 65%;
    border-bottom: 2px solid white;
    padding-bottom: 5px;
    position: relative;
    display: flex;
    margin: 0 auto;
  }
  #stratety_title :nth-child(1) {
    position: relative;
    left: 0px;
    font-size: 20px;
    font-weight: 700;
    margin-left: 10px;

  }

  #hotStratety {
    width: 70%;
    margin: 0 auto;
  }
  .Stratety_item {
    margin: 0 auto;
    width: 90%;
    margin-top: 50px;
    display: flex;
    height: 160px;
    position: relative;
  }
  .Stratety_item_img {
    flex: 1;
    height: 100%;
    background-color: black;
    overflow: hidden;
  }
  .Stratety_item_img:hover img{
    transform: scale(1.03);
    opacity: 0.7;
    cursor: pointer;
  }
  .Stratety_item_img img {
    width: 101%;
    height: 101%;
    transition: all 0.6s;
  }
  .Stratety_item_content {
    flex: 3;
    margin-left: 15px;
    position: relative;
  }
  .Stratety_item_title {
    width: 100%;
    margin-top: 10px;
    color: white;
    font-size: 20px;
  }
  .Stratety_item_details {
    width: 100%;
    height: 60px;
    text-overflow: ellipsis;
    margin-top: 15px;
    color: rgb(199, 196, 196);
    font-size: 14px;
  }
  .Stratety_item_details:hover,.Stratety_item_title:hover {
    cursor: pointer;
    text-decoration: underline;
  }
  .Stratety_item_bottom {
    position: absolute;
    width: 100%;
    bottom: 5px;
    font-size: 13px;
    color: rgb(255, 255, 255);
  }
  .Stratety_item_islike {
    height: 40px;
    width: 40px;
    position: absolute;
    right: 0px;
    bottom: 0px;
  }
  .Stratety_item_islike:hover {
    cursor: pointer;
    transform: scale(1.05);
  }
  .Stratety_item_bottom img {
    width: 40px;
  }
  #stratety_page {
    position: relative;
    width: 20%;
    height: 20px;
    left: 50%;
    margin-top: 30px;
    transform: translateX(-50%);
    text-align: center;
    line-height: 20px;
    font-size: 14px;
    color: rgb(206, 204, 204);
    display: flex;
  }
  .pages {
    flex: 1;
  }
  #stratety_page > div:hover {
    cursor: pointer;
    text-decoration: underline;
  }
</style>