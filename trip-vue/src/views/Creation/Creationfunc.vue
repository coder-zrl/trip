<template>
  <div id="creationfunc">
    <div class="contribute">
      <img src="~assets/img/Creation/投稿.png" alt="">
      <span>投稿</span>
    </div>
    <lykcollapse></lykcollapse>
  </div>
</template>
<script>
export default {
  data() {
    return {
      activeNames: ['1']
    }
  },
  components: {
    lykcollapse: () => import('components/common/Collapse/lykcollapse')
  },
  methods: {
    handleChange(val) {
      console.log(val);
    }
  }
}
</script>
<style scoped>
  #creationfunc {
    flex: 1;
    height: calc(100vh - 70px);
    position: relative;
    border-right: 1px solid #e9e1e1;

  }
  .contribute {
    margin: 0 auto;
    width: 70%;
    height: 48px;
    background-color: rgb(13, 13, 14);
    text-align: center;
    margin-top: 10px;
    border-radius: 20px;
  }
  .contribute img {
    height: 35px;
    margin-right: 10px;
    vertical-align: middle;
  }
  .contribute span {
    line-height: 50px;
    vertical-align: middle;
    color: white;
    font-family: "宋体";
    font-size: 18px;
  }
  .funcs {
    width: 80%;
    margin: 0 auto;
    margin-top: 20px;
  }
  .funcs > .el-collapse > .el-collapse-item:first-child {
    text-align: center;
    font-size: 18px;
  }
  .funcs > .el-collapse > .el-collapse-item > .el-collapse-item_content {
    font-size: 20px;
  }
</style>