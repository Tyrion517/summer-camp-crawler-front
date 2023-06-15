<script>
import {defineComponent} from 'vue'
import http from "@/http";
export default defineComponent({
  name: "ListData",
  data() {
    return {
      data: '',
      name: this.$route.params.name,
      chinese_name: '',
      map: {
        ustc: '中国科技大学',
        peking: '北京大学'
      }
    }
  },
  mounted() {
    http.get(this.name).then(res => {
      this.data = res.data
      return res
    }).catch(e => {
      console.log(e)
    })
    this.chinese_name = this.map[this.name]
  }
})
</script>

<template>
  <h1 align="centrol">{{chinese_name}}夏令营</h1>
  <div v-for="item in data" :key="item.title" id="wrapper">
    <el-card id="item">
      <a :href="item.addr">{{item.title}}</a>
    </el-card>
  </div>
</template>

<style scoped>
#wrapper {
display: flex;
  justify-content: center;
}

#item{
  margin-bottom: 10px;
  width: 80%;
}
h1 {
  text-align: center;
}
</style>