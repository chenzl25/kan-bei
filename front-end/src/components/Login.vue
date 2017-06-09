<template>
  <div class="wrapper">
      <div class="row main">
        <div class="panel-heading">
                 <div class="panel-title text-center">
                    <h1 class="title">看呗</h1>
                    <hr />
                  </div>
              </div> 
        <div class="main-login main-center">
          <form class="form-horizontal" method="post" action="#">

            <div class="form-group">
              <label for="username" class="cols-sm-2 control-label">用户名</label>
              <div class="cols-sm-10">
                <div class="input-group">
                  <span class="input-group-addon"><i class="fa fa-users fa" aria-hidden="true"></i></span>
                  <input type="text" class="form-control" name="username" id="username"  placeholder="请输入用户名" v-model="username"/>
                </div>
              </div>
            </div>

            <div class="form-group">
              <label for="password" class="cols-sm-2 control-label">密码</label>
              <div class="cols-sm-10">
                <div class="input-group">
                  <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
                  <input type="password" class="form-control" name="password" id="password"  placeholder="请输入密码" v-model="password"/>
                </div>
              </div>
            </div>

            <div class="form-group ">
              <button type="button" class="btn btn-primary btn-lg btn-block login-button" v-on:click="login">登录</button>
            </div>
            <div class="login-register">
                <a href="#login">注册</a>
             </div>
             <div class='blue'>
               {{login_result}}
             </div>
          </form>
        </div>
      </div>
    </div>
</template>

<script>
import $ from '../../node_modules/jquery/dist/jquery.min.js'

export default {
  name: 'login',
  data: function () {
    return {
      username: '',
      password: '',
      login_result: ''
    }
  },
  methods: {
    login: function () {
      var that = this
      $.post({
        url: '/server_api/login/in',
        type: 'POST',
        data: JSON.stringify({
          'username': this.username,
          'password': this.password
        })})
        .done(function (data) {
          data = JSON.parse(data)
          if (data['result'] === 'fail') {
            that.login_result = '登录失败'
          } else if (data['result'] === 'success') {
            that.login_result = '登录成功'
            that.$router.isLogin = true
            that.$router.useInfo = {} // TODO
            that.$router.push({name: 'Entry'})
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main{
  margin-top: 70px;
}
h1.title { 
  font-size: 50px;
  font-family: 'Passion One', cursive; 
  font-weight: 400; 
}

hr{
  width: 10%;
  color: #fff;
}

.form-group{
  margin-bottom: 15px;
}

label{
  margin-bottom: 15px;
}

input,
input::-webkit-input-placeholder {
    font-size: 11px;
    padding-top: 3px;
}

.main-login{
  background-color: #fff;
    /* shadows and rounded borders */
    -moz-border-radius: 2px;
    -webkit-border-radius: 2px;
    border-radius: 2px;
    -moz-box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
    -webkit-box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
    box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);

}

.main-center{
  margin-top: 30px;
  margin: 0 auto;
  max-width: 330px;
  padding: 40px 40px;

}

.login-button{
  margin-top: 5px;
}
.blue {
  color: blue;
}
</style>
