<template>
  <div id="creation">
    <creationfunc></creationfunc>
    <div id="creation_content">
    </div>
  </div>
</template>
<script>

export default {
  components: {
    creationfunc: () => import('views/Creation/Creationfunc'),
  }
}
</script>
<style>
  #creation {
    width: 100%;
    height: calc(100vh - 70px);
    display: flex;
    position: fixed;
  }
  
  #creation_content {
    flex: 6;
    height: 100%;
    /* background-color: burlywood; */
  }
</style>