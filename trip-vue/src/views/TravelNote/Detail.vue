<template>
  <div id="detail">
    <div class="detail_mohu">
      <img src="~assets/img/TravelNote/南疆1.png" alt="">
      <div>101.20 【南疆】7月南疆人文自驾环线攻略中...走遍中国还差一个你</div>
    </div>
    <div class="detail_author">
      <div class="detail_author_touxiang"><img src="~assets/img/TravelNote/头像.jpeg" alt=""></div>
      <div class="detail_author_name">旅行鸭（武汉）</div>
      <div class="detail_author_time">2021-4-24</div>
    </div>
    <div class="detail_content">
      <detailcontent></detailcontent>
    </div>
    <footerpage></footerpage>
  </div>
</template>
<script>
export default {
  components: {
    detailcontent: () => import('views/TravelNote/DetailContent'),
    footerpage: () => import('components/content/footer/FooterPage')
  }
}
</script>
<style>
  #detail {
    width: 100%;
  }
  .detail_mohu {
    margin: 0 auto;
    width: 99%;
    height: 400px;
    position: relative;
  }
  .detail_mohu img {
    width: 100%;
    height: 100%;
    filter: blur(4px);
  }
  .detail_mohu div {
    width: 100%;
    position: absolute;
    color: white;
    bottom: 35px;
    text-align: center;
    font-size: 25px;
  }
  .detail_author {
    position: relative;
    display: flex;
    width: 60%;
    height: 100px;
    /* background-color: violet; */
    margin: 0 auto;
    margin-top: -30px;
    z-index: 3;
    padding-bottom: 10px;
    border-bottom: 1px solid #e2dfdf;
    margin-bottom: 30px;
  }
  .detail_author_touxiang {
    width: 100px;
    height: 100px;  
  }
  .detail_author_touxiang img {
    width: 100%;
    border-radius: 100px;
  }
  .detail_author_name {
    position: absolute;
    bottom: 10px;
    left: 120px;
    font-size: 18px;
    color: tomato;
    font-weight: 600;
  }
  .detail_author_time {
    position: absolute;
    bottom: 12px;
    left: 260px;
    font-size: 16px;
  }
</style>