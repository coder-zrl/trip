<template>
  <div id="hot_destination">
    <div class="hot_destination_title">热门目的地</div>
    <div class="hot_destination_list">
      <div class="hot_destination_item" v-for="item in hot_destination_list" :key="item.province">
        <div class="item_province">{{item.province}}</div>
        <div class="item_cities">
          <a href="" class="item_city" v-for="city in item.city" :key="city">{{city}}</a>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      hot_destination_list:[
        {
          province:'直辖市',
          city:['北京','上海','重庆','天津']
        },
        {
          province:'西藏贵州',
          city:['拉萨','林芝','阿里','黔东南','荔波','西江','镇远']
        },
        {
          province:'云南',
          city:['大理','昆明','香格里拉','双廊','西双版纳','腾冲','西崩']
        },
        {
          province:'西北',
          city:['西安','青海湖','西宁','祁连','敦煌','兰州','甘南','嘉峪关','新疆']
        },

      ]
    }
  }
}
</script>
<style>
  #hot_destination {
    width: 100%;
  }
  .hot_destination_title {
    padding-top: 50px;
    width: 100%;
    text-align: center;
    color: white;
    font-size: 40px;
    /* font-family:KaiTi_GB2312; */
    letter-spacing: 3px;
  }
  .hot_destination_list {
    width: 100%;
    display: flex;
    flex-wrap: wrap;
  }
  .hot_destination_item {
    width: 40%;
    margin: 0 auto;
    display: flex;
    padding-bottom: 8px;
    margin-top: 40px;
    border-bottom: 1px solid rgb(155, 154, 154);
  }
  .item_province {
    width: 100px;
    font-size: 19px;
    color: white;
  }
  .item_cities {
    align-content: space-around;
  }
  .item_city {
    height: 10px;
    margin-left: 15px;
    color: white;
    text-decoration: none;
  }

</style>