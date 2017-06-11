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
          <template v-for="(value, key,index) in cinemasInfo.data">
            <li role="presentation" :class="{active:activeIndex == index}"><a :href="'area-'+index" :aria-controls="'area-' + index" role="tab" data-toggle="tab" v-on:click="active(index)">{{key}}</a></li>
          </template>
        </ul>

        <!-- Tab panes -->
        <div class="tab-content">
          <template v-for="(value, key, index) in cinemasInfo.data">
            <div role="tabpanel" class="tab-pane in" :class="{active:activeIndex == index}" :id="'area-' + index">
              <template v-for="area,index in value">
                <div class="row col-xs-7 col-md-7 area-wrapper" >
                  <h4>{{area.nm}}</h4>
                  <p>地址：{{area.addr}}</p>
                  <p>票价：{{area.sellPrice}}</p>
                </div>
                <div class="row col-xs-2 col-md-2 btn-wrapper" >
                  <button  type="button" class="btn btn-warning buy-btn" v-on:click="select(area.id, area.sellPrice)">选座购票</button>
                </div>
              </template>
            </div>
          </template>
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

var cinemasData = {
  data: {

  }
}

export default {
  name: 'buy',
  data: function () {
    return {
      movieInfo: movieData,
      cinemasInfo: cinemasData,
      activeIndex: 0
    }
  },
  methods: {
    buy: function () {
      var movieId = this.$route.params.movieId
      this.$router.push({name: 'Buy', params: {movieId: movieId}})
    },

    active: function (index) {
      this.activeIndex = index
    },

    select: function (cinemaId, price) {
      var movieId = this.$route.params.movieId
      this.$router.push({name: 'Site', params: {movieId: movieId, cinemaId: cinemaId, price: price}})
    }
  },

  beforeMount: function () {
    $.ajax({url: '/maoyan_api/cinemas.json'})
      .done(function (data) {
        data = JSON.parse(data)
        cinemasData.data = data.data
      })
    var movieId = this.$route.params.movieId
    $.ajax({url: '/maoyan_api/movie/' + movieId + '.json'})
       .done(function (data) {
         data = JSON.parse(data)
         movieData.comment = data.data.CommentResponseModel
         movieData.detail = data.data.MovieDetailModel
       })
  }
}
</script>

<style scoped>
.down-wrapper {
  margin-top: 10px;
  margin-left: 40px;
  margin-right: 40px;
}

.area-wrapper {
  margin-top: 20px;
  border-bottom: 1px solid #ddd;
}

.btn-wrapper {
  margin-top: 30px;
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
