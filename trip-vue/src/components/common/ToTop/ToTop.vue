<template>
  <div id="totop">
    <a href="#Navigation"><img src="~assets/img/ToTop/回到顶部.png" alt=""></a>
  </div>
</template>
<script>
export default {
  mounted() {
    var btn = document.getElementById('totop')
    window.onscroll = function(e) {
      if(document.documentElement.scrollTop >= 300) {
        btn.style.display = 'block'
      }else {
        btn.style.display = 'none'
      }
    }
  }
}
</script>
<style>
  #totop {
    position: fixed;
    width: 40px;
    right: 50px;
    bottom: 50px;
    display: none;
    opacity: 0.9;
  }
  #totop:hover {
    cursor: pointer;
  }
  #totop img {
    width: 100%;
    height: 100%;
  }
</style>