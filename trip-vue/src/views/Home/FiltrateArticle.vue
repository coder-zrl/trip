<template>
  <div id="filtrateArticle">
    <div id="filtrateArticle_title">
      <div>热门游记</div>
      <div>
        <i class="el-icon-menu"></i><span>筛选</span>
      </div>
      <div>最新发表</div>
      <div id="create_vlog">
        <img src="~assets/img/HomePage/vlog.png" alt="" srcset="">
        <span>写游记</span>
      </div>
    </div>
    <div id="hotArticles">
      <div class="Article_item" v-for="(item,index) in Articles" :key="item.url">
        <div class="Article_item_img">
          <img :src="item.url" alt="">
        </div>
        <div class="Article_item_content">
          <div class="Article_item_title" @click="tolink()">{{item.title}}</div>
          <div class="Article_item_details">{{item.details}}</div>
          <div class="Article_item_bottom">
            <span class="Article_item_local">{{item.local}} /</span>
            <span class="Article_item_time">{{item.time}}</span>
            <span class="Article_item_viewNumber"> 浏览·{{item.viewsNumber}}</span>
            <div class="Article_item_islike" @click="changeLike(index)">
              <img src="~assets/img/HomePage/unlike.png" alt="" v-if="!item.islike">
              <img src="~assets/img/HomePage/like.png" alt="" v-else>
            </div>   
          </div>
        </div>
      </div>
    </div>
    <div id="filtrateArticle_more">
      更多 >>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      Articles:[
        {
          url:require('assets/img/TravelNote/南疆1.png'),
          title:'新疆 | 7月南疆人文自驾环线攻略中...走遍中国还差一个你',
          details:'新疆，一块国内游最难啃的地方，远，太远了，懒惰的我一直都未将新疆纳入计划，总找接口...',
          local:'新疆',
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
      this.Articles[index].islike = !this.Articles[index].islike;
    },
    article(msg) {
      this.Articles = [];
      this.Articles = msg;
      console.log(this.Articles);
    },
    tolink() {
      this.$router.push('/detail/nanjiang')
    }
  },
  mounted() {
    this.$bus.$on('updatearticle',function(msg) {
      this.Articles = msg
      console.log('article',msg);
    })
  }
}
</script>
<style>
  #filtrateArticle {
    width: 100%;
    margin: 0 auto;
    padding-top: 115px;
    position: relative;
  }
  #filtrateArticle_title {
    color: white;
    width: 75%;
    border-bottom: 2px solid white;
    padding-bottom: 5px;
    position: relative;
    display: flex;
    margin: 0 auto;
  }
  #filtrateArticle_title :nth-child(1) {
    position: relative;
    left: 0px;
    font-size: 20px;
    font-weight: 700;
    margin-left: 10px;

  }
  #filtrateArticle_title :nth-child(2) {
    position: relative;
    width: 70px;
    height: 20px;
    font-size: 13px;
    left: 10px;
    top: 1px;
    color: rgb(203, 199, 194);
    border: 1px solid white;
  }
  #filtrateArticle_title :nth-child(2):hover {
    cursor: pointer;
  }
  #filtrateArticle_title :nth-child(2) i {
    vertical-align: middle;
  }
  #filtrateArticle_title :nth-child(2) span {
    vertical-align: middle;
    margin-left: -4px;
    border: none;
  }
  #filtrateArticle_title :nth-child(3) {
    position: relative;
    left: 30px;
    top: 3px;
    font-size: 18px;
  }
  #filtrateArticle_title :nth-child(3):hover {
    cursor: pointer;
  }
  #filtrateArticle_title #create_vlog {
    position: absolute;
    right: 10px;
    top: -16px;
    width: 130px;
    height: 37px;
    border: 1px solid white;
    border-radius: 5px;
  }
  #filtrateArticle_title #create_vlog:hover {
     background-color: rgb(171, 168, 168);
     border: 1px solid rgb(171, 168, 168);
     cursor: pointer;
   }
  #filtrateArticle_title #create_vlog:hover span {
    color: rgb(50, 31, 31);
  }
  #filtrateArticle_title #create_vlog img {
    width: 30%;
    vertical-align: middle;
  }
  #filtrateArticle_title #create_vlog span {
    vertical-align: middle;
    font-size: 15px;
    font-weight: 600;
    border: none;
  }
  #hotArticles {
    width: 75%;
    margin: 0 auto;
  }
  .Article_item {
    margin: 0 auto;
    width: 90%;
    margin-top: 50px;
    display: flex;
    height: 160px;
    position: relative;
  }
  .Article_item_img {
    flex: 1;
    height: 100%;
    background-color: black;
    overflow: hidden;
  }
  .Article_item_img:hover img{
    transform: scale(1.2);
    opacity: 0.7;
    cursor: pointer;
  }
  .Article_item_img img {
    width: 100%;
    height: 100%;
    /* transform: scale(1); */
    transition: all 0.7s;
  }
  .Article_item_content {
    flex: 3;
    margin-left: 15px;
    position: relative;
  }
  .Article_item_title {
    width: 100%;
    margin-top: 10px;
    color: white;
    font-size: 20px;
  }
  .Article_item_details {
    width: 100%;
    margin-top: 15px;
    color: rgb(199, 196, 196);
    font-size: 14px;
  }
  .Article_item_title:hover, .Article_item_details:hover {
    text-decoration: underline;
    cursor: pointer;
  }
  .Article_item_bottom {
    position: absolute;
    width: 100%;
    bottom: 5px;
    font-size: 13px;
    color: rgb(255, 255, 255);
  }
  .Article_item_islike {
    height: 40px;
    width: 40px;
    position: absolute;
    right: 0px;
    bottom: 0px;
  }
  .Article_item_islike:hover {
    cursor: pointer;
    transform: scale(1.05);
  }
  .Article_item_bottom img {
    width: 40px;
  }
  #filtrateArticle_more {
    position: relative;
    width: 80px;
    height: 20px;
    left: 50%;
    margin-top: 30px;
    transform: translateX(-50%);
    text-align: center;
    line-height: 20px;
    font-size: 14px;
    color: rgb(206, 204, 204);
    border: 1px solid rgb(206, 204, 204);
  }
  #filtrateArticle_more:hover {
    color: rgb(229, 226, 226);
    border: 1px solid rgb(229, 226, 226);;
    cursor: pointer;
  }
</style>