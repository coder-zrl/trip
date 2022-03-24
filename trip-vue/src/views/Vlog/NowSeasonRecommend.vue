<template>
  <div id="nowseasonrecommend">
    <div class="nowseasonrecommend_title">
      当季推荐
    </div>
    <div class="month_select">
      <a class="month">1月</a>
      <a class="month">2月</a>
      <a class="month">3月</a>
      <a class="month">4月</a>
      <a class="month">5月</a>
      <a class="month">6月</a>
      <a class="month">7月</a>
      <a class="month">8月</a>
      <a class="month">9月</a>
      <a class="month">10月</a>
      <a class="month">11月</a>
      <a class="month">12月</a>
    </div>
    <div class="month_recommends">
      <div class="month_recommend"></div>
      <div class="month_recommend"></div>
      <div class="month_recommend"></div>
      <div class="month_recommend"></div>
      <div class="month_recommend"></div>
      <div class="month_recommend"></div>
      <div class="month_recommend"></div>
    </div>
  </div>
</template>
<script>
export default {
  
}
</script>

<style>
  #nowseasonrecommend {
    width: 90%;
    margin: 0 auto;
    margin-top: 150px;
    color: white;
  }
  .nowseasonrecommend_title {
    text-align: center;
    font-size: 40px;
    letter-spacing: 5px;
    margin-bottom: 20px;
  }
  .month_select {
    width: 100%;
    text-align: center;
  }
  .month_select .month {
    margin-left: 20px;
    
  }
  .month_select .month:hover {
    cursor: pointer;
    text-decoration: underline;
  }
  .month_recommends {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
  }
  .month_recommend {
    margin-top: 30px;
  }
  .month_recommend:nth-child(1) {
    width: 31%;
    height: 240px;
    background-color: rgb(120, 86, 86)
  }
  .month_recommend:nth-child(2) {
    width: 31%;
    height: 240px;
    background-color: rgb(120, 86, 86)
  }
  .month_recommend:nth-child(3) {
    width: 31%;
    height: 240px;
    background-color: rgb(120, 86, 86)
  }
  .month_recommend:nth-child(4) {
    width: 23%;
    height: 200px;
    background-color: rgb(120, 86, 86)
  }
  .month_recommend:nth-child(5) {
    width: 23%;
    height: 200px;
    background-color: rgb(120, 86, 86)
  }
  .month_recommend:nth-child(6) {
    width: 23%;
    height: 200px;
    background-color: rgb(120, 86, 86)
  }
  .month_recommend:nth-child(7) {
    width: 23%;
    height: 200px;
    background-color: rgb(120, 86, 86)
  }
</style>