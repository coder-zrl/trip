<template>
  <div id="upranking">
    <div class="upranking_title">
      <span>up排行榜</span>
    </div>
    <div class="upranking_list">
      <div class="up_item">
        <div class="up_pic"></div>
        <div class="up_name"></div>
      </div>
      <div class="up_item">
        <div class="up_pic"></div>
        <div class="up_name"></div>
      </div>
      <div class="up_item">
        <div class="up_pic"></div>
        <div class="up_name"></div>
      </div>
      <div class="up_item">
        <div class="up_pic"></div>
        <div class="up_name"></div>
      </div>
      <div class="up_item">
        <div class="up_pic"></div>
        <div class="up_name"></div>
      </div>
      <div class="up_item">
        <div class="up_pic"></div>
        <div class="up_name"></div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  
}
</script>
<style>
  #upranking {
    width: 65%;
    margin: 0 auto;
  }
  .upranking_title {
    width: 100%;
    color: white;
    margin-top: 50px;
    height: 30px;
    font-size: 20px;
    line-height: 30px;
    border-bottom: 2px solid white;
    
  }
  .upranking_title span {
    margin-left: 10px;
    font-weight: 700;
  }
  .upranking_list {
    width: 80%;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    padding-bottom: 50px;
  }
  .up_item {
    width: 40%;
    height: 60px;
    background-color: #ececec;
    margin-top: 30px;
    position: relative;
  }
  .up_item .up_pic {
    width: 55px;
    height: 55px;
    border-radius: 55px;
    background-color: rgb(196, 194, 194);
    position: relative;
    top: 50%;
    transform: translateY(-50%);
    left: 10px;
  }
</style>