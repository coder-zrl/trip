<template>
  <div id="Home">
    <div id="search">
      <inputbox input_text="搜目的地/攻略/游记"></inputbox>
    </div>
    <div id="Home_content_bg">
      <div id="Home_content">
        <FiltrateVlog ref="vlog"></FiltrateVlog>
        <FiltrateArticle ref="article"></FiltrateArticle>
      </div>
    </div>
    <footerpage></footerpage>
  </div>
</template>
<script>

import FiltrateVlog from 'views/Home/FiltrateVlog'
import FiltrateArticle from 'views/Home/FiltrateArticle'
import footerpage from 'components/content/footer/FooterPage'
import inputbox from 'components/common/inputbox/inputbox'
export default {
  data() {
    return {
      homedata:{}
    }
  },
  components: {
    FiltrateVlog,
    FiltrateArticle,
    footerpage,
    inputbox
  },
  created() {
    console.log(this.$store.state.username);
    this.axios.get('http://47.103.198.84:5000/recommend',{
        params:{
          uid:this.$store.state.username
        }
      })
      .then(res => {
        console.log(res.data); 
        this.homedata = res.data
        this.$refs.vlog.vlog(res.data.scenery)
        this.$refs.article.article(res.data.artical)
      }).catch((e) => {
        console.log(e);
      })
  }
}
</script>
<style>
  #search {
    width: 100%;
    height: calc(70vh - 70px);
    background: url('~assets/img/HomePage/header.png');
    background-size: 100% 100%;
    position: relative;
  }
  #Home_content_bg {
    width: 100%;
    background-color: rgb(67, 43, 43);
    position: relative;
    padding-bottom: 50px;
  }
  #Home_content {
    width: 80%;
    position: relative;
    left: 50%;
    transform: translateX(-50%);
  }
</style>