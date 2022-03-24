<template>
  <div id="hotvlog">
    <div class="hotvlog_title">
      <span>热门vlog</span>
    </div>
    <div class="hotvlog_items">
      <div class="hotvlog_item" v-for="item in hotvlogs" :key="item.url">  
        <div class="hotvlog_item_img">
          <img class="hotvlog_img" :src="item.url" alt="">
          <div class="play">
            <img class="play" src="~assets/img/Vlog/播放.png" alt="">
        </div>
        </div>
        <div class="hotvlog_item_content">{{item.content}}</div>
        <div class="hotvlog_item_bottom">
          <span class="hotvlog_item_author"><img src="~assets/img/Vlog/author.png" alt="">{{item.author}} </span>
          <span class="hotvlog_item_comments">
            <img src="~assets/img/Vlog/评论.png" alt="">
            {{item.comments}} 
            浏览|{{item.browsers}}
          </span>
        </div>
      </div>
    </div>
    <div class="hotvlog_first">
      <div class="first_title">本周排名第一</div>
      <div class="first_img">
        <img src="~assets/img/TravelNote/南疆1.png" alt="">
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      hotvlogs:[
        {
          url:require('assets/img/Vlog/贵州.png'),
          content:'贵州 | 贵州有绚丽多彩的卡斯特经管，气势磅礴的黄果树瀑布...',
          author:'龙龙子',
          comments:98464,
          browsers:'54万'
        },
        {
          url:require('assets/img/Vlog/青海.png'),
          content:'青海 | 三江源头、草原雪山、鲜花与湖泊交相辉映',
          author:'昆昆子',
          comments:24634,
          browsers:'24万'
        },
        {
          url:require('assets/img/Vlog/上合峰会.png'),
          content:'海水变暖 | 上合峰会：适宜',
          author:'凌凌子',
          comments:244,
          browsers:'2.4万'
        },
        {
          url:require('assets/img/Vlog/北国风光.png'),
          content:'北国风光，千里冰封，万里雪飘，黑龙江的雪雕与冰雕是一定不能错过的绝境。',
          author:'玲玲子',
          comments:5784,
          browsers:'4.5万'
        },
        {
          url:require('assets/img/Vlog/新加坡.png'),
          content:'新加坡城市面积占总面积的绝大部分，接头到处是花圃、草坪、草茂花繁、整洁美...',
          author:'大雄',
          comments:68764,
          browsers:'47.8万'
        },
        {
          url:require('assets/img/Vlog/沙巴州.png'),
          content:'沙巴州拥有精致优美的沙滩、珊瑚群围绕的小岛、峥嵘的山峦和原始神秘的热带雨林...',
          author:'静香',
          comments:78564,
          browsers:'32.4万'
        },
      ]
    }
  }
}
</script>
<style>
  #hotvlog {
    margin: 0 auto;
    width: 65%;
    
  }
  .hotvlog_title {
    padding-top: 20px;
    padding-bottom: 3px;
    border-bottom: 1px solid white;
  }
  .hotvlog_title span {
    font-size: 20px;
    color: white;
    border-bottom: 2px solid white;
    padding-bottom: 3px;
  }
  .hotvlog_items {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;

  }
  .hotvlog_item {
    width: 28%;
    min-width: 220px;
    height: 250px;
    margin-top: 30px;
    color: white;
    position: relative;
  }
  div.play {
    position: absolute;
    top: 50px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 3;
    width: 50px;
    height: 50px;
  }
  div.play img {
    width: 100%;
    opacity: 0.6;
  }
  .hotvlog_item_content:hover {
    cursor: pointer;
    text-decoration: underline;
  }
  .hotvlog_item_img:hover > img.hotvlog_img{
    cursor: pointer;
    transform: scale(1.05);
    opacity: 0.7;
  }
  .hotvlog_item_img:hover div>img {
    opacity: 1;
    cursor: pointer;
    transform: scale(1.3);
  }
  .hotvlog_item_img {
    width: 100%;
    height: 150px;
    overflow: hidden;
    
    background-color: black;
  }
  .hotvlog_item_img img{
    display: block;
    width: 100%;
    height: 100%;
    transition: all 0.3s;
    opacity: 1;
  }
  .hotvlog_item_content {
    margin-top: 10px;
    line-height: 18px;
    font-size: 15px;
  }
  .hotvlog_item_bottom {
    position: absolute;
    bottom: 5px;
    width: 100%;
    font-size: 13px;
  }
  .hotvlog_item_author img {
    width: 15px;
    height: 15px;
    /* vertical-align: middle; */
    margin-bottom: -2px;
    margin-right: 3px;
  }
  .hotvlog_item_comments img {
    width: 15px;
    height: 15px;
    /* vertical-align: middle; */
    margin-bottom: -2px;
  }
  .hotvlog_item_comments {
    position: absolute;
    right: 0px;
    /* vertical-align: middle; */
  }
 .hotvlog_first {
  margin-top: 40px;
  text-align: center;
 }
 .first_title {
   margin: 0 auto;
   color: white;
   font-size: 25px;
   letter-spacing: 3px;
   font-family: "KaiTi";
 }
 .first_img {
   margin: 0 auto;
   margin-top: 10px;
   padding-bottom: 20px;
   width: 50%;
 }
 .first_img img {
   width: 100%;
 }
</style>