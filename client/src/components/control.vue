<template>
	<div id="control" style="height: 100%">
		<div class="nav-main">
			<div class="nav-box">
				<div class="nav">
					<ul class="nav-ul">
						<li>
							<a href="#" class="home"><span>Control panel</span></a>
						</li>
						<li>
							<a href="#" class="develop"><span>Url</span></a>
						</li>
						<li>
							<a href="#" class="wechat"><span>背景色</span></a>
						</li>
						<li>
							<a href="#" class="case"><span>节点形状</span></a>
						</li>
						<li>
							<a href="#" class="news"><span>字体</span></a>
						</li>
						<!--<li><a href="#" class="contact"><span>关于我们</span></a></li>-->
					</ul>
				</div>
				<div class="nav-slide">
					<div class="nav-slide-o"></div>
					<div class="nav-slide-o">
						<ul>
							<li>
								<a href="#"><span>www.swust.edu.cn</span></a>
							</li>
							<li>
								<a href="#"><span>www.swust.edu.cn</span></a>
							</li>
							<li>
								<a href="#"><span>www.swust.edu.cn</span></a>
							</li>
						</ul>
					</div>
					<div class="nav-slide-o">
						<ul>
							<li>
								<a href="#"><span>background-color1</span></a>
							</li>
							<li>
								<a href="#"><span>background-color2</span></a>
							</li>
							<li>
								<a href="#"><span>background-color3</span></a>
							</li>
						</ul>
					</div>
					<div class="nav-slide-o">
						<ul>
							<li>
								<a href="#"><span>Rectangle</span></a>
							</li>
							<li>
								<a href="#"><span>Circle</span></a>
							</li>
							<li>
								<a href="#"><span>Rounded rectangle</span></a>
							</li>
						</ul>
					</div>
					<div class="nav-slide-o">
						<ul>
							<li>
								<a href="#"><span>宋体</span></a>
							</li>
							<li>
								<a href="#"><span>微软雅黑</span></a>
							</li>
							<li>
								<a href="#"><span>楷体</span></a>
							</li>
							<li>
								<a href="#"><span>Calibri</span></a>
							</li>
							<li>
								<a href="#"><span>Arial</span></a>
							</li>
						</ul>
					</div>
				</div>

				<div style="position: absolute; top:600px; width: 150px;  height: 100px; background-color:#111213;">
					<!--jdt-->
					<div id="box">
						<div style="color: #FFFFFF; width: 150px; height: 20px; text-align: center;">亮度调节</div>
						<div class="body">
							<div class="dragnum">
								<span style="color: #FFFFFF;">{{startNum}}</span>
							</div>
							<div class="dragnum dragbox" @mousemove="timeMove($event)" @mouseleave="timeEnd($event)" ref="dragbox">
								<div class="progress" @click="timeClick($event)">
									<div class="progressbar" :style="{width:distance+'px',transition:'width '+transTime+'s'}">
									</div>
								</div>
								<div class="bardrag" @mousedown="timeDown($event)" @mouseup="timeEnd($event)" :style="{left:distance+'px'}">
								</div>
							</div>
							<div class="dragnum">
								<span style="color: #FFFFFF;">{{endNum}}</span>
							</div>
							<div class="nowbar" style="color: #FFFFFF;width: 150px; height: 20px; text-align: center;">
								当前值：{{nowNum}}
							</div>
						</div>

					</div>
					<!--jdt-->
				</div>

			</div>

		</div>

	</div>
</template>

<script>
	require("../../static/index.css")
	export default {
		name: "content",
		data() {
			return {
				pos: {},
				startX: null,
				locked: false,
				distance: 0, //当前位置
				endDistance: 0, //上次操作结束位置
				transTime: .3, //点击拖动动画
				dragWidth: 0, //进度条宽度

				startNum: 10,
				endNum: 50,
				nowNum: 10
			}
		},
		methods: {
			mousePos: function(e) {
				var pos = {};
				pos.x = e.pageX;
				this.pos = pos;
				return pos;
			},
			timeDown: function(e) { // 当鼠标指针移动到元素上方，并按下鼠标左键时
				this.transTime = 0;
				this.mousePos(e);
				this.startX = this.pos.x;
				this.locked = true;
				this.endDistance = this.distance;
				// console.log(this.pos);
			},
			timeMove: function(e) { // 当鼠标指针移动到元素上方移动时
				if(!this.locked) return;
				var pos = this.mousePos(e);
				var moveX = pos.x - this.startX;
				if(this.distance >= this.dragWidth) {
					this.distance = this.dragWidth - 10;
				} else {
					if((this.distance <= 0 && moveX < 0) || (this.distance >= this.dragWidth && moveX > 0)) return;
					this.distance = this.endDistance + moveX;

					this.countNum(this.distance);

				}
				// console.log(moveX);
			},
			timeEnd: function(e) {
				this.transTime = .3;
				this.locked = false;
			},
			timeClick: function(e) { //点击拖动到指定位置
				var x = e.offsetX,
					moveX = x - this.distance;
				this.distance += moveX;
				this.countNum(this.distance);

			},
			countNum: function(num) {
				var len = this.endNum - this.startNum;
				var scale = Math.ceil(this.dragWidth / len);
				this.nowNum = this.startNum + Math.ceil(num / scale);
			}

		},
		mounted() {
			this.dragWidth = $('.dragbox').width();
				console.log(this.dragWidth)
			$(function() {
				var thisTime;
				$('.nav-ul li').mouseleave(function(even) {
					thisTime = setTimeout(thisMouseOut, 1000);
				})

				$('.nav-ul li').mouseenter(function() {
					clearTimeout(thisTime);
					var thisUB = $('.nav-ul li').index($(this));
					if($.trim($('.nav-slide-o').eq(thisUB).html()) != "") {
						$('.nav-slide').addClass('hover');
						$('.nav-slide-o').hide();
						$('.nav-slide-o').eq(thisUB).show();
					} else {
						$('.nav-slide').removeClass('hover');
					}

				})

				function thisMouseOut() {
					$('.nav-slide').removeClass('hover');
				}

				$('.nav-slide').mouseenter(function() {
					clearTimeout(thisTime);
					$('.nav-slide').addClass('hover');
				})
				$('.nav-slide').mouseleave(function() {
					$('.nav-slide').removeClass('hover');
				})

			})
			drqwMark();

			function drqwMark() {
				var width = $("#control").width();
				var height = $("#control").height();
				var svg = d3.select("#control")
					.append("svg")
					.attr("width", width)
					.attr("height", height);
				console.log(svg);
				var padding = {
					top: height * 0.05,
					left: width * 0.05,
					right: width * 0.95,
					bottom: height * 0.95
				}
				var lineWid = width * 0.1;
				var path1 = "M " + padding.left + " " + (padding.top + lineWid) +
					" L " + padding.left + " " + padding.top +
					" L " + (padding.left + lineWid) + " " + padding.top;

				var path2 = "M " + padding.right + " " + (padding.top + lineWid) +
					" L " + padding.right + " " + padding.top +
					" L " + (padding.right - lineWid) + " " + padding.top;

				var path3 = "M " + padding.left + " " + (padding.bottom - lineWid) +
					" L " + padding.left + " " + padding.bottom +
					" L " + (padding.left + lineWid) + " " + padding.bottom;

				var path4 = "M " + padding.right + " " + (padding.bottom - lineWid) +
					" L " + padding.right + " " + padding.bottom +
					" L " + (padding.right - lineWid) + " " + padding.bottom;

				var pathd = [path1, path2, path3, path4];
				svg.selectAll("path")
					.data(pathd)
					.enter()
					.append("path")
					.attr("d", function(d) {
						return d;
					})
					.attr("stroke", "#7394dc")
					.attr("stroke-width", 1.5);
			}
		}
	}
</script>
<style scoped>
    #box {}

    .body {
      padding: 5px;
      width: 800px;
      height: 100px;
      /*margin: 0 auto;*/
      text-align: left;
      color: #FFFFFF;
    }

    .dragbox {
      width: 100px;
      position: relative;
      height: 20px;
      background-color: #f5f5f5;
      border-radius: 4px;
      -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, .1);
      box-shadow: inset 0 1px 2px rgba(0, 0, 0, .1);
    }

    .progress {
      background: #a7a7a7;
      margin-bottom: 0px;
      height: 20px;
      margin-bottom: 20px;
      overflow: hidden;
      border-radius: 4px;
      -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, .1);
      box-shadow: inset 0 1px 2px rgba(0, 0, 0, .1);
    }

    .progressbar {
      background-color: #337ab7;
      float: left;
      width: 0;
      height: 100%;
      font-size: 12px;
      line-height: 20px;
      color: #fff;
      text-align: center;
      -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, .15);
      box-shadow: inset 0 -1px 0 rgba(0, 0, 0, .15);
      -webkit-transition: width .6s ease;
      -o-transition: width .6s ease;
      transition: width .6s ease;
    }

    .bardrag {
      position: absolute;
      top: -6px;
      left: 10px;
      display: inline-block;
      height: 28px;
      width: 10px;
      background-color: #337ab7;
      border: 1px solid #e1e0de;
      border-radius: 10px;
      cursor: e-resize;
    }

    .dragnum {
      display: inline-block;
      vertical-align: middle;
    }

    .nowbar {
      margin-top: 10px;
    }
    
</style>