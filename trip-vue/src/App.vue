<template>
  <div id="app">
    <navigation v-if="this.$route.name != 'login' "></navigation>
    <router-view/>
    <totop></totop>
  </div>
</template>

<script>
import navigation from 'components/content/HomePage/Navigation'
import Navigation from './components/content/HomePage/Navigation.vue'
import totop from 'components/common/ToTop/ToTop'

export default {
  components: {
    navigation,
    totop
  }
}
</script>

<style>

</style>
