<template>
<div>
  <div class="background">
    <img :src="imgSrc" width="100%" height="100%" alt="" />
    </div>

    <div class="front">
          <!-- <el-container>
    <el-header>Header</el-header>
    <el-main> -->
      <div class="shiyangongneng">
        <el-card class="box-card">
          <div slot="header" class="clearfix">
            <!-- <span> -->
                <el-page-header @back="goBack" content="实验功能"></el-page-header>
            <!-- </span> -->
            <el-button style="float: right;padding:3px" type="text"></el-button>
          </div>
          <div class="text item">
              <el-button :plain="true" @click="openVn" style="width: 240px; height: 140px;margin-bottom:16px;font-size:26px;">年龄分析</el-button>
              <el-button :plain="true" @click="openVn" style="width: 240px; height: 140px;margin-bottom:16px;font-size:26px;">性别分析</el-button>
              <el-button :plain="true" @click="openVn" style="width: 240px; height: 140px;margin-bottom:16px;font-size:26px;">颜值分析</el-button>
              <el-button :plain="true" @click="openVn" style="width: 240px; height: 140px;margin-bottom:16px;font-size:26px;margin-left:0px">旧图片上色</el-button>
              <el-button :plain="true" @click="openVn" style="width: 240px; height: 140px;margin-bottom:16px;font-size:26px;">情绪分析</el-button>
              <el-button :plain="true" @click="openVn" style="width: 240px; height: 140px;margin-bottom:16px;font-size:26px">卡通化</el-button>
          </div>
        </el-card>
      </div>
    <!-- </el-main>
  </el-container> -->
    </div>
</div>
</template>

//布局容器的格式
<style>
body {
  margin: 0px;
}

.el-header,
.el-footer {
  background-color: #b3c0d1;
  color: #333;
  text-align: center;
  line-height: 60px;
  padding: 0px;
}

.el-aside {
  background-color: #d3dce6;
  color: #333;
  text-align: center;
  line-height: 200px;
}

.el-main {
  background-color: #e9eef3;
  color: #333;
  text-align: center;
  line-height: 160px;
  padding: 0px;
  height: 800px;
}

body > .el-container {
  margin-bottom: 40px;
}

.el-container:nth-child(5) .el-aside,
.el-container:nth-child(6) .el-aside {
  line-height: 260px;
}

.el-container:nth-child(7) .el-aside {
  line-height: 320px;
}
</style>

//卡片格式
<style>

.el-card__header{
    height: 60px;
}

.text {
  font-size: 50px;
  color:white;
  font-family:"微软雅黑";
}

.item {
  margin-bottom: 18px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}
.clearfix:after {
  clear: both;
}

.box-card {
  width: 880px;
  height: 420px;
}

/* card所在div */
.shiyangongneng {
  margin-left: 300px;
  padding-top: 70px;
}

</style>

<style>
  .background {
    left: 0;
    top: 0;
    width:100%;
    height:100%;  /**宽高100%是为了图片铺满屏幕 */
    z-index:-1;
    position: absolute;
}

.front{
    z-index:1;
    position: absolute;
}
</style>

//弹窗方法
<script>
export default {
  methods: {
    open () {
      this.$message('这是一条消息提示')
    },

    openVn () {
      const h = this.$createElement
      this.$message({
        message: h('p', null, [
          h('span', null, '内容可以是 '),
          h('i', { style: 'color: teal' }, 'VNode')
        ])
      })
    }
  },
  data () {
    return {
      imgSrc: require('../assets/kejichengshi.png')
    }
  }
}
</script>
