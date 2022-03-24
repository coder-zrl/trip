<template>
  <div class="input_box">
    <div class="input_text">
      <slot></slot>
    </div>
    <input type="text" class="input_search" :placeholder="input_text">
    <button class="submit_search">
      <img src="~assets/img/HomePage/search.png" alt="">
    </button>
  </div>
</template>
<script>
export default {
  props:[
    'input_text'
  ]
}
</script>
<style>
    .input_box {
    height: 105px;
    width: 600px;
    background-color: rgba(0, 0, 0, 0.6);
    border-radius: 20px;
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    top:63%;
  }
  .input_search {
    outline-style: none;
    width: 500px;
    height: 39px;
    border-radius: 10px;
    position: relative;
    top: 45px;
    left: 15px;
    background-color: rgb(248, 248, 248);
    opacity: 1;
    padding-left: 15px;
    font-size: 14px;
    color: rgba(5, 0, 0, 0.932);
    border: none;
    vertical-align:middle;
  }
  .submit_search {
    position: relative;
    width: 39px;
    height: 39px;
    top: 45px;
    left: 23px;
    background-color: tomato;
    border-radius: 12px;
    border-style: none;
    outline: none;
  }
  .submit_search:hover img{
    cursor: pointer;
    transform: scale(1.1);
  }
  .submit_search img {
    width: 80%;
    border-radius: 15px;
    vertical-align:middle;
    margin-left: 3px;
  }
  .input_text {
    position: absolute;
    left: 30px;
    top: 16px;
    color: rgba(255, 255, 255, 0.782);
  }
</style>