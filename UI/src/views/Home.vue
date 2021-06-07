<template>
    <div class="home">
       首页
    </div>
</template>
<script>
// import HelloWorld from '@/compoments/HelloWorld.vue'
import axios from 'axios'
export default {
  name: 'home',
  components: {

  },
  methods: {
    getHandle () {
      // axios.get 发起get请求
      // 参数一 表示请求地址
      // 参数二 表示配置信息
      // params 表示传递到服务器端的数据，以url参数的形式拼接在请求地址后面
      // https://api?page=16&per=3
      // headers 请求头
      axios.get('', {
        params: {
          page: 10,
          per: 3
        },
        headers: {

        }
      }).then(res => console.log(res))
    },
    postHandle () {

    }
  }
}
</script>
