 <template>
  <div>
    <div
      id="app2"
      :style="{
        backgroundImage: 'url(' + require('@/assets/278017.jpg') + ')',
      }"
    >
      <!-- <img src="./assets/zuobian.png" alt="" class="logo"> -->
      <div>
        <!-- <img src="./assets/logogonghui .png" alt="" id="logo2"> -->
      </div>
      <el-row>
        <el-col id="waikuang2">
          <el-row>
            <el-col :span="24" id="header2">
              <img
                src="../assets/gonghuitubiao.png"
                alt=""
                class="gonghuitubiao"
              />
            </el-col>
          </el-row>

          <div id="input2">
            <el-row id="username2">
              <el-col :span="6">
                <span id="accountzi2">姓名：</span>
              </el-col>
              <el-col :span="17">
                <el-input v-model="account" placeholder="请输入姓名"></el-input>
              </el-col>
            </el-row>
            <el-row id="account2">
              <el-col :span="6">
                <span id="accountzi2">学号：</span>
              </el-col>
              <el-col :span="17">
                <el-input v-model="account" placeholder="请输入学号"></el-input>
              </el-col>
            </el-row>

            <br />

            <el-row>
              <el-col :span="6">
                <span id="passwordzi2">密码：</span>
              </el-col>
              <el-col :span="17">
                <el-input
                  v-model="password"
                  placeholder="请输入密码"
                  show-password
                ></el-input>
              </el-col>
            </el-row>
            <el-row id="queren2">

            </el-row>
            <br />
            <br />
            <br />

            <el-row>
              <el-col :span="6"> 上传头像： </el-col>
              <el-col :span="17">
                <div id="upload">
                  <!--
      action              请求的路径
      show-file-list      是否显示文件列表
      on-success          成功之后的回调
      before-upload       上传前操作
      http-request        覆盖默认的上传行为，可以自定义上传的实现
更多钩子函数可查看你elementUI文档：https://element.eleme.cn/#/zh-CN/component/installation
     -->
                  <el-upload
                    class="avatar-uploader"
                    action="/api/upload/upImg"
                    :show-file-list="false"
                    :http-request="upload"
                    :before-upload="ImgBeforeAvatarUpload"
                  >
                    <img v-if="imageUrl" :src="imageUrl" class="avatar" />
                    <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                  </el-upload>
                </div>
              </el-col>
            </el-row>
            <el-row id="button2">
              <el-col :span="24">
                <!-- <a href=""><el-button type="danger" plain @click="zhuce">注册</el-button></a> -->
                <el-button type="primaey"  @click="getshuju">注册</el-button>
              </el-col>
            </el-row>
          </div>
        </el-col>
      </el-row>
    </div>
  </div>
</template>
<script src="https://cdn.bootcdn.net/ajax/libs/axios/0.21.1/axios.min.js"></script>
<script >
import axios from "axios";
export default {
  name: "denglu",
  data() {
    return {
      // imgSrc:require('./assets/images/beijing.jpg'),
      account: "",
      password: "",

      imageUrl: "",
    };
  },
  methods: {
     getshuju() {

    const pwrong=document.getElementById("pwrong")
      axios
        .get("http://127.0.0.1:3000/axios-server", {
          params: {
            account: this.account,
            password: this.password,
            imgUel:this.imageUrl

          },
          headers: {},
        }).then((response) => {
          console.log(response.data)

          alert("注册成功");
          this.$router.push({
          name: 'denglu'
        })

        });
    },
    upload(f) {
      // console.log(f)
      // 1. 获取表单数据   fromData 表单数据
      let fromData = new FormData();
      fromData.append("file", f.file);
      // 2. 发起请求
      this.$axios({
        method: "post",
        url: f.action,
        data: fromData,
      }).then((res) => {
        // 3. 请求成功之后  图片回显
        console.log(res);
        this.imageUrl = res.data.url;
      });
    },
    //上传前校验图片规则
    ImgBeforeAvatarUpload(file) {
      console.log(file);
      const isJPG = file.type === "image/jpeg" || file.type === "image/png";
      const isLt2M = file.size / 1024 / 1024 < 2;
      if (!isJPG) {
        this.$message.error("上传图片只能是 JPG 和 Png 格式!");
        return false;
      }
      if (!isLt2M) {
        this.$message.error("上传图片大小不能超过 2MB!");
        return false;
      }
    },
  },
};
</script>
<style scoped>
.avatar-uploader .el-upload {
  border: 1px solid black;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border: 1px solid black;
  border-color: #409eff;
}
.avatar-uploader-icon {
  border: 1px solid black;
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  border: 1px solid black;
  width: 178px;
  height: 178px;
  display: block;
}
html {
  height: 100%;
}
body {
  margin: 0px;
  padding: 0px;
  height: 100%;
}

.gonghuitubiao {
  height: 50px;
  width: 200px;
  margin-left: 100px;
  float: left;
}

#queren2 {
  margin-top: 20px;
}
#logo2 {
  height: 100px;
  width: 450px;
  position: absolute;
  top: 0;
  left: 0;
}
#app2 {
  /* background-image:url("..\src\assets\278017.jpg"); */
  background-size: 100%;

  /* border: 10px solid black; */
  height: 800px;
  width: 1500px;
  position: absolute;
  top: 0;
  left: 0;
}

#zhaohui2 {
  margin-left: 220px;
  font-size: 12px;
}
#zhaohui2 a {
  text-decoration: none;
  color: white;
}
#button2 {
  margin-top: 10px;
  margin-left: 0px;
  /* border:1px black solid; */
}
/* .el-input{
  margin-bottom: -10px;
} */
#accountzi2 {
  line-height: 40px;
}
#passwordzi2 {
  line-height: 40px;
}
#passwordquerenzi2 {
  line-height: 0px;
}
#header2 {
  margin-left: 5px;
  margin-top: 20px;
  line-height: 50px;
}
#input2 {
  margin-top: 40px;
  /* margin-left: 50px; */
  margin-right: 50px;
  /* border:1px black solid; */
  width: 380px;
}
#background2 {
  width: 1600px;
  height: 800px;
}
#waikuang2 {
  width: 400px;
  height: 630px;
  border-radius: 20px;
  position: absolute;
  top: 100px;
  left: 560px;
  background-color: rgba(255, 255, 255, 0.6);
  color: black;
}
#account2 {
  margin-top: 20px;
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
