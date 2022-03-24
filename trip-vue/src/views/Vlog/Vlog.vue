<template>
  <div id="vlog">
    <div id="vlog_search">
      <inputbox input_text="我想去..."><span class="vlog_ipnut_text">Dont't fear the unknow</span></inputbox>
    </div>
    <div id="vlog_content">
      <hotvlog></hotvlog>
    </div>
    <footerpage></footerpage>
  </div>
</template>
<script>
import inputbox from 'components/common/inputbox/inputbox'
import footerpage from 'components/content/footer/FooterPage'
import hotvlog from 'views/Vlog/HotVlog'
export default {
  components: {
    inputbox,
    footerpage,
    hotvlog
  }
}
</script>
<style>
  #vlog_search {
    width: 100%;
    height: calc(70vh - 70px);
    background: url('~assets/img/Vlog/header.png');
    background-size: 100% 100%;
    position: relative;
  }
  #vlog_content {
    width: 100%;
    background-color: #694545;
  }
</style>