<template>
  <div id="travelnote">
    <div class="travelnote_search">
      <img src="~assets/img/TravelNote/图片文字.png" alt="" class="text">
      <img src="~assets/img/TravelNote/圣托里尼名字.png" alt="" class="text">
    </div>
    <div id="travelnote_content">
      <stratety></stratety>
      <upranking></upranking>
    </div>
    <footerpage></footerpage>
  </div>
</template>
<script>
import footerpage from 'components/content/footer/FooterPage'
export default {
  components: {
    stratety: () => import('views/TravelNote/Stratety'),
    footerpage,
    upranking: () => import('views/TravelNote/UpRanking')
  }
}
</script>
<style>
  #travelnote {
    width: 100%;  
    background-color: rgb(67, 43, 43);
  }
  .travelnote_search {
    height: calc(70vh - 70px);
    background: url('~assets/img/TravelNote/圣托里尼.png') no-repeat;
    background-size: 100% 100%;
  }
  .travelnote_search img:first-child {
    display: block;
    width: 40%;
    padding-top: 100px;
    padding-left: 100px;
  }
  .travelnote_search img:nth-child(2) {
    display: block;
    width: 15%;
    padding-top: 100px;
    padding-left: 150px;
  }
</style>