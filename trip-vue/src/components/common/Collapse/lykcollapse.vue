<template>
  <div id="lykcollapse">
    <div class="lykcollapse-item" v-for="(item,index) in funcs" :key="item.title">
      <div class="lykcollapse-item-title" @click="open_collapse(index)">
        <img class="title_logo" :src="item.img" alt="">
        <span>{{item.title}}</span>
        <img v-if="item.children" class="more" src="~assets/img/Lykcollapse/up.png" alt="">
        </div>
      <div v-if="item.children" class="lykcollapse-item-hidden">
        <div class="lykcollapse-item-hidden-item" v-for="hitem in item.children" :key="hitem.title">
          {{hitem.title}}
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name:'lykcollapse',
  data() {
    return {
      funcs: [
        {
          title:'首页',
          img:require('assets/img/Lykcollapse/home.png')
        },
        {
          title:'内容管理',
          img:require('assets/img/Lykcollapse/content_manage.png'),
          isopen:false,
          children: [
            {title:'稿件管理'},
            {title:'申诉管理'},
            {title:'弹幕管理'}
          ]
        },
        {
          title:'粉丝数据',
          img:require('assets/img/Lykcollapse/fans.png')
        },
        {
          title:'互动管理',
          img:require('assets/img/Lykcollapse/interaction.png'),
          isopen:false,
          children: [
            {title:'评论管理'},
            {title:'弹幕管理'},
          ]
        },
        {
          title:'收益管理',
          img:require('assets/img/Lykcollapse/earnings.png'),
          isopen:false,
          children: [
            {title:'创作公约'},
            {title:'创作设置'},
            {title:'5U版权'}
          ]
        },
        {
          title:'数据中心',
          img:require('assets/img/Lykcollapse/data_center.png')
        }
      ]
    }
  },
  methods: {
    open_collapse(index) {
      let item = document.getElementsByClassName('lykcollapse-item')[index];
      if(this.funcs[index].children){
        let upimg = item.getElementsByClassName('more')[0];
        if(this.funcs[index].isopen == true) {
          item.style.height = '50px';
          upimg.style.transform = 'translateY(-50%) rotateZ(180deg) scale(0.7)'
          this.funcs[index].isopen = false;
        }else {
          item.style.height = 50 + 40*this.funcs[index].children.length + 'px';
          upimg.style.transform = 'translateY(-50%) rotateZ(0deg) scale(0.7)'
          this.funcs[index].isopen = true;
        }
      }
      
    }
  }
}
</script>
<style scoped>
  #lykcollapse {
    width: 75%;
    margin: 0 auto;
    margin-top: 24px;
    min-width: 160px;
  }
  .lykcollapse-item {
    transition: all 0.2s;
    overflow: hidden;
    height: 50px;
    width: 100%;
    
    /* border-bottom: 1px solid #737171; */

  }
  .lykcollapse-item:hover {
    cursor: default;
  }
  .lykcollapse-item > .lykcollapse-item-title {
    height: 50px;
    font-family: "仿宋";
    font-size: 15px;
    font-weight: 700;
    line-height: 50px;
    position: relative;
  }
  .lykcollapse-item > .lykcollapse-item-title .title_logo {
    width: 20px;
    vertical-align: middle;
    margin-top: -5px;
    margin-right: 16px;
  }
  .lykcollapse-item > .lykcollapse-item-title .more {
    position: absolute;
    height: 20px;
    right: 5px;
    top: 50%;
    transform: translateY(-50%) rotateZ(180deg) scale(0.7);
    opacity: 0.4;
    
    /* transition: all 0.2s; */
  }
  .lykcollapse-item-hidden-item {
    height: 40px;
    font-size: 14px;
    line-height: 40px;
    /* margin-top: 0px; */
    margin-left: 36px;
  }
</style>