<template>
<el-container>
  <el-header></el-header>
  <el-main>Main
      <el-card class="box-card">
  <div slot="header" class="clearfix">
    <span>人脸识别</span>
    <el-row>
  <el-button type="primary">考勤</el-button>
  <el-button type="success">人脸登记</el-button>
  <el-button type="info">考勤记录</el-button>
  <el-button type="warning">人脸管理</el-button>
  <el-button type="danger">实验功能</el-button>
</el-row>
  </div>
</el-card>
  </el-main>
</el-container>

</template>

<style>
  .text {
    font-size: 14px;
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
    clear: both
  }

  .box-card {
    width: 480px;
  }

  .el-header, .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 160px;
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
