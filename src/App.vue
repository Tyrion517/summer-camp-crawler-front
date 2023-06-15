<template>
  <el-menu mode="horizontal"
           router
           background-color="#545c64"
           text-color="#fff"
           active-text-color="#ffd04b"

  >
    <el-menu-item index="1" route="/ustc" @click="this.$root.$forceUpdate">中国科技大学</el-menu-item>
    <el-menu-item index="2" route="/peking" @click="this.$root.$forceUpdate">北京大学</el-menu-item>
  </el-menu>
  <div id="main">
    <router-view :key="$route.path"/>
  </div>
</template>

<script>
export default {
  name: 'App',

}
</script>

<style>

</style>
