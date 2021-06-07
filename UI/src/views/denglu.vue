<template>
<div>
  <div class="background">
    <img :src="imgSrc" width="100%" height="100%" alt="" />
    </div>
    <div class="front">
    <el-row>
      <el-col id="waikuang">
        <el-row>
          <el-col :span="24" id="header">
            <img
              src="../assets/gonghuitubiao.png"
              alt=""
              class="gonghuitubiao"
            />
          </el-col>
        </el-row>

        <div id="input">
          <el-row id="account">
            <el-col :span="4">
              <span id="accountzi">账号：</span>
            </el-col>
            <el-col :span="20">
              <el-input v-model="account" placeholder="请输入内容"></el-input>
            </el-col>
          </el-row>

          <br />

          <el-row>
            <el-col :span="4">
              <span id="passwordzi">密码：</span>
            </el-col>
            <el-col :span="20">
              <el-input
                v-model="password"
                placeholder="请输入密码"
                show-password
              ></el-input>
            </el-col>
          </el-row>
          <el-row>
            <el-col id="zhaohui"><a href="">找回账号密码</a> </el-col>
          </el-row>
          <el-row id="button">
            <el-col :span="10">
              <el-button
                type="primary"
                native-type="submit"
                plain
                id="denglubutton"
                @click="getshuju"
                >登录</el-button
              >
            </el-col>
            <el-col :span="10">
              <router-link to="/zhuce"
                ><el-button type="primary" @click="zhuce" plain
                  >注册</el-button
                ></router-link
              >
            </el-col>
          </el-row>
        </div>
      </el-col>
    </el-row>
  </div>
</div>
</template>
<script src="https://cdn.bootcdn.net/ajax/libs/axios/0.21.1/axios.min.js"></script>

<script>
import axios from "axios";
export default {
  name: "denglu",
  data() {
    return {
      account: "",
      password: "",
      password2: "",
    };
  },
  methods: {
    getshuju() {
      axios
        .get("http://127.0.0.1:8000/axios-server", {
          params: {
            account: this.account,
            password: this.password,
          },
          headers: {},
        }).then((response) => {
          console.log(response.data)
         if(response.data==1){
          //  alert("login success");
          this.$router.push({
          name: 'Home'
        })
         }
         else
         alert("login failed")
        });
    },
  },
    data () {
    return {
      imgSrc: require('../assets/278017.jpg')
    }
  }
};
</script>

<style scoped>
html {
  height: 100%;
}
body {
  margin: 0px;
  padding: 0px;
  height: 100%;
}
.zi {
  position: absolute;
  top: 0px;
  left: 0;
  width: 400px;
  height: 100px;
}
.zizhuce {
  position: absolute;
  top: 20px;
  left: 45px;
  width: 400px;
  height: 100px;
}
.gonghuitubiao {
  height: 50px;
  width: 200px;
  margin-left: 100px;
  float: left;
}
.logo {
  height: 500px;
  width: 550px;
  position: absolute;
  top: 100px;
  left: 240px;
}
#app4456 {
  background-size: 100%;

  height: 800px;
  width: 1500px;
  position: absolute;
  top: 0;
  left: 0;
}
#zhaohui {
  margin-top: 12px;
  margin-left: 220px;
  font-size: 12px;
}
#zhaohui a {
  text-decoration: none;
  color: white;
}
#button {
  margin-top: 40px;
  margin-left: 50px;
}
.el-input {
  margin-bottom: -10px;
}
#accountzi {
  line-height: 40px;
}
#passwordzi {
  line-height: 40px;
}
#header {
  margin-left: 5px;
  margin-top: 20px;
  line-height: 50px;
}
#input {
  margin-top: 60px;
  margin-left: 50px;
  margin-right: 50px;
}
#background {
  width: 1700px;
  height: 800px;
}
#waikuang {
  width: 400px;
  height: 400px;

  position: absolute;
  top: 80px;
  left: 560px;
  background-color: rgba(255, 255, 255, 0.6);
  color: black;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
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
