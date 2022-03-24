<template>
  <div id="filtrateVlog">
    <div id="filtrateVlog_title">
      <div>热门景点</div>
      <div>
        <i class="el-icon-menu"></i><span>筛选</span>
      </div>
      <div id="create_vlog" @click="req">
        <img src="~assets/img/HomePage/vlog.png" alt="" srcset="">
        <span>创作vlog</span>
      </div>
    </div>
    <div id="filtrateVlog_img">
      <el-carousel :interval="4000" type="card" height="300px">
        <el-carousel-item v-for="(item,index) in imgdata" :key="index">
          <img @click="linkto()" :src="item.url" alt="">
        </el-carousel-item>
       </el-carousel>
    </div>
    <div id="filtrateVlog_change">
      <img src="~assets/img/HomePage/change.png" alt="">
      <span>换一换</span>
    </div>
  </div>
</template>
<script>
import Vue from 'vue'
export default {
  data() {
    return {
      imgdata:[
        {url:require('assets/img/vip/黄鹤楼3.jpeg')},
        {url:require('assets/img/HomePage/test2.png')},
        {url:require('assets/img/HomePage/test3.png')},
      ],
      message:'你好'
    }
  },
  methods: {
    linkto() {
      this.$router.push('/vip')
    },
    req() {
      this.axios.get('http://47.103.198.84:5000/login')
      .then(res => {
        console.log(res);
      })
    },
    change(msg) {
      this.imgdata = [];
      this.imgdata = msg
      this.message = msg
    },
    vlog(msg) {
      this.imgdata = [];
      this.imgdata = msg;
    }
  },
  mounted() {
    this.$bus.$on('updateVlog',function(msg,v) {
      console.log('vlog',msg,v);
      // for(let i = 0; i < 3; i++) {
      //   Vue.set(this.imgdata[i].url,msg[i].url)
      // }
      change(msg)
    })
  },
  watch: {
  }
}
</script>
<style>
  #filtrateVlog {
    margin: 0 auto;
    padding-top: 60px;
    position: relative;
  }
  #filtrateVlog_title {
    color: white;
    width: 75%;
    border-bottom: 2px solid white;
    padding-bottom: 5px;
    position: relative;
    display: flex;
    margin: 0 auto;
  }
  #filtrateVlog_title :nth-child(1) {
    position: relative;
    left: 0px;
    font-size: 20px;
    font-weight: 700;
    margin-left: 10px;

  }
  #filtrateVlog_title :nth-child(2) {
    position: relative;
    width: 70px;
    height: 20px;
    font-size: 13px;
    left: 10px;
    top: 1px;
    color: rgb(203, 199, 194);
    border: 1px solid white;
  }
  #filtrateVlog_title :nth-child(2):hover {
    cursor: pointer;
  }
  #filtrateVlog_title :nth-child(2) i {
    vertical-align: middle;
  }
  #filtrateVlog_title :nth-child(2) span {
    vertical-align: middle;
    margin-left: -4px;
    border: none;
  }
  #filtrateVlog_title #create_vlog {
    position: absolute;
    right: 10px;
    top: -16px;
    width: 130px;
    height: 37px;
    border: 1px solid white;
    border-radius: 5px;
  }
  #filtrateVlog_title #create_vlog:hover {
     background-color: rgb(171, 168, 168);
     border: 1px solid rgb(171, 168, 168);
     cursor: pointer;
   }
  #filtrateVlog_title #create_vlog:hover span {
    color: rgb(50, 31, 31);
  }
  #filtrateVlog_title #create_vlog img {
    width: 30%;
    vertical-align: middle;
  }
  #filtrateVlog_title #create_vlog span {
    vertical-align: middle;
    font-size: 15px;
    font-weight: 600;
    border: none;
  }
  #filtrateVlog_img {
    width: 75%;
    margin:0 auto;
    margin-top: 50px;
  }
  #filtrateVlog_img img {
    width: 100%;
    height: 100%;
  }
  #filtrateVlog_change {
    width: 72px;
    height: 22px;
    /* background-color: rgb(155, 26, 26); */
    border: 1px solid white;
    border-radius: 5px;
    position: absolute;
    right: 185px;
    top: 480px;
    z-index: 1;
  }
  #filtrateVlog_change img {
    width: 20px;
    vertical-align: middle;
    margin-left: 2px;
  }
  #filtrateVlog_change span {
    vertical-align: middle;
    margin-left: 3px;
    font-size: 14px;
    color: rgb(182, 180, 180);
  }
  #filtrateVlog_change:hover {
    border: 1px solid rgb(229, 226, 226);
    cursor: pointer;
  }
  #filtrateVlog_change:hover span {
    color: rgb(229, 226, 226);
  }
</style>