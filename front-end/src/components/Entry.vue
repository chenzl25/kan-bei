<template>
  <div class="wrapper">
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="#">
            <img id="logo-img" src="../assets/logo.png">
          </a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
          <ul class="nav navbar-nav">
          </ul>
          <form class="navbar-form navbar-left">
            <div class="form-group">
              <input type="text" class="form-control" placeholder="找电影" v-model="searchText">
            </div>
            <button type="submit" class="btn btn-default">搜索</button>
          </form>
          <ul class="nav navbar-nav navbar-right">
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false"><img id="avatar-img" src="../assets/avatar.png"> <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li v-if="!isLogin"><a href="#/register">注册</a></li>
                <li v-if="!isLogin"><a href="#/login">登录</a></li>
                <li v-if="isLogin"><a href="#">我的订单</a></li>
                <li v-if="isLogin"><a href="#" v-on:click="logout">退出</a></li>
              </ul>
            </li>
          </ul>
        </div><!-- /.navbar-collapse -->
      </div><!-- /.container-fluid -->
    </nav>
    <div class="row col-xs-1 col-md-1"></div>
    <div class="row col-xs-10 col-md-10">
      <template v-for="movie,index in filteredMovies">
        <div class="movie-item　col-xs-2 col-md-2">
          <a :href="index">
            <img class="movie-img"　:src="movie.img" >
          </a>
          <div class="movie-name">{{movie.nm}}</div>
          <div class="movie-scroe">{{movie.sc?movie.sc:'暂无'}}</div>
        </div>
      </template>
    </div>
    <div class="row col-xs-1 col-md-1"></div>
  </div>
</template>

<script>
import $ from '../../node_modules/jquery/dist/jquery.min.js'

let entryData = {}

entryData.movies = [1]

$.ajax({url: '/maoyan_api/movie/list.json?type=hot&offset=0&limit=40'})
 .done(function (data) {
   data = JSON.parse(data)
   entryData.movies = data['data']['movies']
 })

export default {
  name: 'entry',
  data: (function (entryData) {
    return function () {
      return {
        entryData: entryData,
        searchText: '',
        isLogin: this.$router.isLogin
      }
    }
  })(entryData),
  computed: {
    filteredMovies: function () {
      var self = this
      if (self.searchText === '') {
        return self.entryData.movies
      }
      return self.entryData.movies.filter(function (movie) {
        return movie.nm.indexOf(self.searchText) !== -1
      })
    }
  },
  methods: {
    logout: function () {
      var that = this
      $.post({
        url: '/server_api/login/out',
        type: 'POST'})
        .done(function (data) {
          data = JSON.parse(data)
          console.log(data)
          if (data['result'] === 'success') {
            that.isLogin = false
            that.$router.useInfo = null
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.navbar-brand {
  padding: 5px;
}
.dropdown-toggle {
  padding: 5px;
}
#avatar-img {
  width: 35px;
  height: 35px;
  padding: 0;
  margin: 0;
}
.movie-img {
  width: 165px;
  height: 230px;
  margin: 10px;
  padding: 10px;
}
.movie-item {

}
.movie-name {
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow: hidden;
  width: 165px;
  font-size: 16px;
  padding-left: 20px;
  font-family: Microsoft YaHei,Helvetica,Arial,sans-serif;
}
.movie-scroe {
  font-size: 20px;
  padding-left: 20px;
  color: orange;
}
</style>
