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

            <div class="form-group">
              <label for="confirm" class="cols-sm-2 control-label">确认密码</label>
              <div class="cols-sm-10">
                <div class="input-group">
                  <span class="input-group-addon"><i class="fa fa-lock fa-lg" aria-hidden="true"></i></span>
                  <input type="password" class="form-control" name="confirm" id="confirm"  placeholder="请确认密码" v-model="confirm"/>
                </div>
              </div>
            </div>

            <div class="form-group ">
              <button type="button" class="btn btn-primary btn-lg btn-block login-button" v-on:click="register">注册</button>
            </div>
            <div class="login-register">
                <a href="#login">登录</a>
             </div>
             <div class='blue'>
               {{register_result}}
             </div>
          </form>
        </div>
      </div>
    </div>
</template>

<script>
import $ from '../../node_modules/jquery/dist/jquery.min.js'

export default {
  name: 'register',
  data: function () {
    return {
      username: '',
      password: '',
      confirm: '',
      register_result: ''
    }
  },
  methods: {
    register: function () {
      if (this.confirm !== this.password) {
        this.register_result = '两次密码不一致'
        return
      }
      var that = this
      $.post({
        url: '/server_api/login/register',
        type: 'POST',
        data: JSON.stringify({
          'username': this.username,
          'password': this.password
        })})
        .done(function (data) {
          data = JSON.parse(data)
          if (data['result'] === 'fail') {
            that.register_result = '注册失败'
          } else if (data['result'] === 'success') {
            that.register_result = '注册成功'
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
