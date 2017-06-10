<template>
  <div class="wrapper">
    <div class="media detail-wrapper">
      <div class="media-left">
        <a>
        <img class="media-object" :src="movieInfo.detail.img">
        </a>
      </div>
      <div class="media-body">
        <h2 class="media-heading">{{movieInfo.detail.nm}}</h2>
        <p>{{movieInfo.detail.cat}}</p>
        <p>{{movieInfo.detail.rt}}</p>
        <p>{{movieInfo.detail.src + '/' + movieInfo.detail.dur + '分钟'}}</p>
        <p>剧情简介:</p>
        <div class="raw" v-html="movieInfo.detail.dra"></div>
      </div>
    </div>
    <div class="down-wrapper">

      <!-- Nav tabs -->
      <ul class="nav nav-tabs" role="tablist">
        <li role="presentation" class="active"><a href="#photos" aria-controls="photos" role="tab" data-toggle="tab" v-on:click="showComment = false">图集</a></li>
        <li role="presentation"><a href="#comment" aria-controls="comment" role="tab" data-toggle="tab" v-on:click="showComment = true">评论</a></li>
      </ul>

      <!-- Tab panes -->
      <div class="tab-content">
        <div role="tabpanel" class="tab-pane in active" id="photos">
          <div v-if="!showComment" class="row col-xs-10 col-md-10">
            <template v-for="photo,index in movieInfo.detail.photos">
              <div class="photo-item　col-xs-2 col-md-2">
                <img class="photo-img"　:src="photo.replace('w.h', '165.220')">
              </div>
            </template>
            </div>
          </div>
        </div>
        <div role="tabpanel" class="tab-pane" id="comment">
          <div v-if="showComment" class="media cmts-wrapper">
            <template v-for="cmt,index in movieInfo.comment.hcmts">
              <div class="row col-xs-10 col-md-10 cmt-wrapper" >
                <div class="media-left media-top">
                  <a href="#">
                    <img class="cmt-img" :src="cmt.avatarurl">
                  </a>
                </div>
                <div class="media-body cmt-body">
                  <h4 class="media-heading" >{{cmt.nickName}}</h4>
                  <p>{{cmt.time}}</p>
                  <p class="cmt-content">{{cmt.content}}</p>
                </div>
              </div>
            </template>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import $ from '../../node_modules/jquery/dist/jquery.min.js'

var movieData = {
  comment: {},
  detail: {}
}

export default {
  name: 'movie',
  data: function () {
    return {
      movieInfo: movieData,
      showComment: false
    }
  },
  methods: {
  },

  beforeMount: function () {
    var movieId = this.$route.params.movieId
    $.ajax({url: '/maoyan_api/movie/' + movieId + '.json'})
       .done(function (data) {
         data = JSON.parse(data)
         movieData.comment = data.data.CommentResponseModel
         movieData.detail = data.data.MovieDetailModel
         console.log(movieData)
       })
  }
}
</script>

<style scoped>
.photo-img {
  width: 150px;
  height: 150px;
  margin: 10px;
  padding: 10px;
  cursor: pointer;
}

.down-wrapper {
  margin-top: 10px;
  margin-left: 40px;
  margin-right: 40px;
}

.raw {
  width: 1000px;
}
.cmt-img {
  width: 50px;
  height: 50px;
  border-radius: 50%;
}
.cmts-wrapper {
  /*margin-left: 10px;*/
}

.cmt-wrapper {
  margin: 20px;
}
.cmt-body {
  border-bottom: 1px solid #ddd;
}
.cmt-content {
  margin-top: 20px;
}
.detail-wrapper {
  background: #392f59 no-repeat 50%;
  color: white;
  padding-bottom: 30px;
}

.detail-wrapper .media-body {
  padding-top: 20px;
  margin-top: 20px;
}

.detail-wrapper img {
  margin-left: 40px;
  border: 3px solid white;
  position: relative;
  top: 20px;
  z-index: 999;
}
</style>
