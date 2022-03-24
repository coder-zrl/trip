<template>
  <div id="Navigation">
    <div id="logo">
      <img src="~assets/5u.png" alt="">
    </div>
    <div id="Nav_modules">
      <div @click="jumpto('/')" :class="{active:this.$route.name == 'Home'}">首页</div>
      <div @click="jumpto('/vlog')" :class="{active:this.$route.name == 'Vlog'}">视频Vlog</div>
      <div @click="jumpto('/travelnote')" :class="{active:(this.$route.name == 'TravelNote' ||  this.$route.name == 'Detail')}">旅游攻略</div>
      <div @click="jumpto('/chatrecommend')" :class="{active:this.$route.name == 'ChatRecommend'}">问答推荐</div>
      <div @click="jumpto('/creation')" :class="{active:this.$route.name == 'Creation'}">创作中心</div>
      <div @click="jumpto('/vip')" :class="{active:this.$route.name == 'Vip'}">会员中心</div>
    </div>
    <div id="state">
      <div id="navigation_search">
        <input type="text">
        <a href="#" class="navigation_search"><img src="~assets/img/HomePage/search.png" alt=""></a>
      </div>
      <a id="qq" href="#"><img src="~assets/img/HomePage/QQ.png" alt=""></a>
      <a id="wx" href="#"><img src="~assets/img/HomePage/微信.png" alt=""></a>
      <div class="log" v-if="$store.state.username == '' ">
        <div id="log" @click="log">登陆</div>
        <span> | </span>
        <div id="register">注册</div> 
      </div>
      <div class="username" v-else>{{$store.state.username}}</div>
    </div>
  </div>
</template>
<script>
export default {
  methods: {
    jumpto(to) {
      this.$router.push(to);
    },
    log() {
      this.$router.push('/login')
    }
  },
}
</script>
<style>
  #Navigation {
    width: 100%;
    height: 70px;
    background-color: rgb(10, 0, 0);
    color: rgb(247, 247, 247);
    display: flex;
    line-height: 80px;
    text-align: center;
    box-shadow: 1px 1px 1px rgb(155, 155, 155);
  }
  #logo {
    flex: 2;
  }
  #logo img {
    display: block;
    width: 150px;
    height: 50px;
    margin: 0 auto;
    margin-top: 10px;
  }
  #Nav_modules {
    flex: 3;
    display: flex;
  }
  #Nav_modules > div {
    flex: 1;
    font-size: 15px;
  }
  .active {
    background-color: rgb(247, 247, 247);
    color:  rgb(10, 0, 0);
  }
  #Nav_modules > div:hover {
    background-color: rgb(247, 247, 247);
    color:  rgb(10, 0, 0);
    cursor: pointer;
  }
  #state {
    flex:2;
    display: flex;
    flex-direction: row;
    margin-right: 100px;
    justify-content: flex-end;
  }
  /* #state > div:hover {
    cursor: pointer;
  } */
  #navigation_search {
    margin-right: 20px;
    display: flex;
    align-items: center;
    margin-top: 3px;
  }
  #navigation_search>input {
    display: block; 
    height: 28px; 
    font-size: 16px;
    padding-left: 5px;
    padding-right: 5px;
    width: 150px;
  }
  .navigation_search {
    display: block;
    width: 30px;
    height: 30px;
    /* background-color: #ffffff; */
    border-radius: 6px;
    margin-left: 2px;
  }
  .navigation_search:hover {
    transform: scale(1.1);
  }
  .navigation_search>img {
    display: block;
    width: 100%;
  }
  .log {
    width: 80px;
    display: flex;
  }
  a#qq {
    display: block;
    width: 26px;
    height: 28px;
    margin-right: 5px;
  }
  a#wx {
    display: block;
    width: 30px;
    height: 30px;
    margin-right: 15px;
  }
  a#qq>img,a#wx>img {
    display: block;
    width: 100%;
    /* vertical-align: middle; */
    margin-top: 25px;
  }
  #log,#register {
    width: 35px;
  }
  #log:hover,#register:hover {
    cursor: pointer;
    text-decoration: underline;
  }
  .username {
    font-weight: 600;
  }

</style>