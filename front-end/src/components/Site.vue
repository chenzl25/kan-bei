<template>
  <div class="wrapper">
      <div class="media detail-wrapper">
        <div class="media-left">
          <a>
          <img class="media-object" :src="movieInfo.detail.img">
          </a>
        </div>
        <div class="media-body">
          <h2 class="media-heading">{{movieInfo.detail.nm}}<span class="addr">({{addr}})</span></h2>
          <p>{{movieInfo.detail.cat}}</p>
          <p>{{movieInfo.detail.rt}}</p>
          <p>{{movieInfo.detail.src + '/' + movieInfo.detail.dur + '分钟'}}</p>
          <p>剧情简介:</p>
          <div class="raw" v-html="movieInfo.detail.dra"></div>
        </div>
      </div>
      <div class="down-wrapper">
        <div class="row col-xs-12 col-md-12 item-wrapper" >
          <p class="row col-xs-2 col-md-2">日期</p>
          <p class="row col-xs-2 col-md-2">场次</p>
          <p class="row col-xs-2 col-md-2">语言版本</p>
          <p class="row col-xs-2 col-md-2">放映厅</p>
          <p class="row col-xs-2 col-md-2">价格</p>
        </div>
        <template v-for="(show, date, index) in cinemaInfo.data.DateShow">
          <template v-for="item,index in show">
            <div class="row col-xs-12 col-md-12 item-wrapper" >
              <p class="row col-xs-2 col-md-2">{{date}}</p>
              <p class="row col-xs-2 col-md-2">{{item.tm + '-' + item.end}}</p>
              <p class="row col-xs-2 col-md-2">{{item.lang}}</p>
              <p class="row col-xs-2 col-md-2">{{item.th}}</p>
              <p class="row col-xs-2 col-md-2">{{price}}</p>
              <div class="row col-xs-2 col-md-2">
              <button  type="button" class="btn btn-warning select-site-btn" data-toggle="modal" data-target="#siteModal" v-on:click="selectSite(item, date)">选座购票</button>
              </div>
            </div>
          </template>
        </template>
      </div>
      <!-- Modal -->
      <div class="modal fade" id="siteModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title" id="myModalLabel">选座</h4>
            </div>
            <div class="modal-body">
              <div class="demo">
                <div class="seat-map-wrapper">
                  <div class="front">屏幕</div>
                  <div class="seat-map">
                    <ul>
                      <template v-for="row,rowId in seatMap">
                        <li>
                          <template v-for="value,colId in row">
                              <span class="not-one-seat" :class="{active:value===2}" v-if="value != 1" v-on:click="selectSeat(rowId, colId)"></span><span class="one-seat" 　v-if="value === 1"></span>
                          </template>
                        </li>
                      </template>
                    </ul>
                  </div>
                </div>
                <div class="booking-details">
                    <p>影片：<span>{{movieInfo.detail.nm}}</span></p>
                    <p>时间：<span>{{date}} / {{item.tm + '-' + item.end}}</span></p>
                    <p>票数：<span id="counter">{{cnt}}</span></p>
                    <p>总计：<b>￥<span id="total">{{total}}</span></b></p> 
                </div>
              </div>
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
              <button type="button" class="btn btn-primary" data-dismiss="modal" v-on:click="submit()" data-toggle="modal" data-target="#codeModal" >提交订单</button>
            </div>
          </div>
        </div>
      </div>

      <!-- Modal -->
      <div class="modal fade" id="codeModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
          <div class="modal-content">
            <div class="modal-header">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
              <h4 class="modal-title" id="myModalLabel">扫码付款({{total}}元)</h4>
              <img class="code-img" src="../assets/mycode.jpg">
            </div>
            <div class="modal-footer">
              <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
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

var cinemaData = {
  data: {

  }
}

export default {
  name: 'site',
  data: function () {
    return {
      movieInfo: movieData,
      cinemaInfo: cinemaData,
      addr: null,
      price: null,
      isSite: false,
      item: {},
      date: null,
      seatMap: [],
      cnt: 0
    }
  },

  computed: {
    total: function () {
      return this.cnt * this.price
    }
  },

  methods: {
    selectSite: function (item, date) {
      this.item = item
      this.date = date
    },

    selectSeat: function (row, col) {
      if (this.seatMap[row][col] === 0) {
        this.$set(this.seatMap[row], col, 2)
        this.cnt += 1
      } else {
        this.$set(this.seatMap[row], col, 0)
        this.cnt -= 1
      }
    },

    submit: function () {
      return true
    }
  },

  beforeMount: function () {
    var that = this
    var movieId = this.$route.params.movieId
    var cinemaId = this.$route.params.cinemaId
    this.price = this.$route.params.price
    $.ajax({url: '/maoyan_api/movie/' + movieId + '.json'})
       .done(function (data) {
         data = JSON.parse(data)
         movieData.comment = data.data.CommentResponseModel
         movieData.detail = data.data.MovieDetailModel
       })
    $.ajax({url: 'maoyan_api/showtime/wrap.json?cinemaid=' + cinemaId + '&movieid=' + movieId})
      .done(function (data) {
        data = JSON.parse(data)
        cinemaData.data = data.data
        that.addr = cinemaData.data.cinemaDetailModel.addr
      })
    for (var i = 0; i < 10; i++) {
      var arr = []
      for (var j = 0; j < 10; j++) {
        arr.push(Math.random() > 0.5 ? 1 : 0)
      }
      this.seatMap.push(arr)
    }
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
.addr {
  font-size: 20px;
}
.item-wrapper {
  margin-top: 20px;
  border-bottom: 1px solid #ddd;
}

.select-site-btn {
  margin-top: -10px;
}

.front {
  width: 420px;margin: 5px 32px 45px 32px;
  background: #f0f0f0;
  color: #666;
  text-align: center;
  padding: 3px;
  border-radius: 5px;
}
.booking-details {
  width: 400px;
  margin-left: 50px;
  padding-top: 15px;
  border-top: 1px solid #ddd;
}
.booking-details h3  {
  margin: 5px 5px 0 0;
  font-size: 16px;
}
.booking-details p {
  line-height: 26px;
   font-size: 16px;
   color: #999
}
.booking-details p span {
  color: #666;
}

.seat-map ul {
  list-style: none;
}

.not-one-seat {
  display: inline-block;
  width: 20px;
  height: 17px;
  background: url(../assets/sp-seats.png) no-repeat;
  background-position: -27px 0;
  margin: 10px;
  cursor: pointer;
}

.not-one-seat:hover {
  background: url(../assets/sp-seats.png) no-repeat;
  background-position: -127px 0;
}

.not-one-seat.active {
  background: url(../assets/sp-seats.png) no-repeat;
  background-position: -77px 0;
}

.one-seat {
  display: inline-block;
  width: 20px;
  height: 17px;
  background: url(../assets/sp-seats.png) no-repeat;
  background-position: -52px 0;
  margin: 10px;
}

.code-img {
  margin-left: 80px;
  width: 400px;
  height: 500px;
}
</style>
