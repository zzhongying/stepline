<template>
	<div id="piechart">
		<button id="return" style="right: 2%;top: 5%;">return</button>
	</div>
</template>

<script>
	import axios from 'axios'
	export default {
		data() {
			return {
				myChart: {},
				option: {},
				choosed: {}
			}
		},
		methods: {},
		mounted() {
			let me = this;

			this.$axios.get("http://127.0.0.1:5000/getMsg/").then(res => {
				var attack = res.data['5'];
				var information = res.data['4'];
				piechart(attack, information);
			})

			function piechart(attackdata, infordata) {
				var width = $("#piechart").width();
				var height = $("#piechart").height();
				var dataset = [
					["attack", 30],
					["information", 20]
				];

				var outerRadius = 100; //外半径
				var innerRadius = 65; //内半径，为0则中间没有空白
				var arc = d3.svg.arc() //弧生成器
					.innerRadius(innerRadius) //设置内半径
					.outerRadius(outerRadius); //设置外半径

				var color = d3.scale.category20()
				var nodescolor = ["#388712", "#60DD49", "#FCE639", "#FFA91A", "#FF3030"]; //构造20种颜色的序数比例尺，索引值可以是字符串或数字

				var pie = d3.layout.pie() //饼图布局
					.sort(null) //不排序，不写则会从大到小，顺时针排序。
					.value(function(d) {
						return d[1]
					}); //设置value值为上面的2二维数组中的数字
				var piedata = pie(dataset);
				var judge = 0
				//console.log(piedata)

				var svg = d3.select("#piechart") //添加一个svg并且设置宽高
					.append("svg")
					.attr("width", width)
					.attr("height", height);

				drqwMark();

				function drqwMark() {
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

				var tooltip = d3.select("#piechart")
					.append("div")
					.attr("class", "tooltip")
					.style("opacity", 0.0);

				var arcs = svg.selectAll(".arc")
					.data(piedata) //返回是pie(data0)
					.enter().append("g")
					.attr("class", "arc")
					.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")") //将圆心平移到svg的中心

					.append("path")
					.attr("id", function(d) {
						return d.data[0]
					})
					.attr("fill", function(d, i) {
						return color(i); //根据下标填充颜色
					})
					.style("filter", "url(#drop-shadow)")
					.attr("d", function(d, i) {
						return arc(d); ///调用上面的弧生成器
					})
					.on("mouseover", function(d, i) {
						arc = d3.svg.arc() //弧生成器
							.innerRadius(innerRadius) //设置内半径
							.outerRadius(outerRadius + 7); //设置外半径
						d3.select(this)
							.attr("d", function(d, i) {
								return arc(d);
							})

						/*与 桑基图交互*/
						if(d['data'][0] == 'attack') {
							me.$root.Bus.$emit("HighLigt", infordata);
						} else {
							me.$root.Bus.$emit("HighLigt", attackdata);
						}
					})
					.on("mouseout", function(d, i) {
						arc = d3.svg.arc() //弧生成器
							.innerRadius(innerRadius) //设置内半径
							.outerRadius(outerRadius); //设置外半径
						d3.select(this)
							.attr("opacity", 1)
							.attr("d", function(d, i) {
								return arc(d)
							})

						/*与 桑基图交互*/
						if(d['data'][0] == 'attack') {
							me.$root.Bus.$emit("HighOff", infordata);
						} else {
							me.$root.Bus.$emit("HighOff", attackdata);
						}
					})
					.on("click", dataChange)
					.transition()
					.delay(function(d, i) {
						return i * 200;
					})
					//.duration(1200)
					.ease("linear")
					.attrTween('d', function(d) {
						var i = d3.interpolate(d.startAngle, d.endAngle);
						return function(t) {
							d.endAngle = i(t);
							return arc(d);
						}
					})

				d3.select("#return")
					.on("click", returnHighOff)

				var text = svg.selectAll(".text")
					.data(piedata) //返回是pie(data0)
					.enter().append("g")
					.attr("class", "text")
					.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
					.append("text")
					.style('text-anchor', "middle")
					.style("fill", "#fff")
					.attr('transform', function(d, i) {
						var pos = arc.centroid(d); //将数字放在圆弧中心
						return 'translate(' + pos + ')';
					})
					.text(function(d) {
						return d.data[0];
					})
					.style("opacity", 0)
					.transition()
					.duration(1200)
					.style("opacity", 1)

				function dataChange() {

					//点击判断
					if(this.id == "attack") {
						dataset = [
							["1", 23],
							["2", 34],
							["3", 17],
							["4", 32],
							["5", 26]
						]
					}
					if(this.id == "information") {
						dataset = [
							["1", 5],
							["2", 25],
							["3", 74],
							["4", 25],
							["5", 3]
						]
					}
					if(this.id == "return") {
						judge = 1

						dataset = [
							["attack", 30],
							["information", 20]
						]
					}

					outerRadius = 100; //外半径
					innerRadius = 65; //内半径，为0则中间没有空白

					d3.selectAll(".text").remove();
					d3.selectAll(".arc").remove();

					var pie2 = pie(dataset)

					arcs = svg.selectAll(".arc")
						.data(pie2) //返回是pie(data0)
						.enter().append("g")
						.attr("class", "arc")
						.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")") //将圆心平移到svg的中心
						.on("mouseover", function(d) {
							tooltip.html(d.data[1])
								.style("left", (d3.event.pageX) + "px")
								.style("top", (d3.event.pageY + 20) + "px")
								.style("opacity", 0.85);
						})
						.on("mousemove", function(d) {
							/* 鼠标移动时，更改样式 left 和 top 来改变提示框的位置 */

							tooltip.style("left", (d3.event.pageX) + "px")
								.style("top", (d3.event.pageY + 20) + "px");
						})
						.on("mouseout", function(d) {
							/* 鼠标移出时，将透明度设定为0.0（完全透明）*/

							tooltip.style("opacity", 0.0);

						})

						.append("path")
						.attr("id", function(d) {
							return d.data[0]
						})
						.attr("fill", function(d, i) {
							return color(i); //根据下标填充颜色
						})
						.attr("d", function(d, i) {
							arc = d3.svg.arc() //弧生成器
								.innerRadius(innerRadius) //设置内半径
								.outerRadius(outerRadius); //设置外半径
							return arc(d); ///调用上面的弧生成器
						})
						.style("filter", "url(#drop-shadow)")
						.on("click", dataChange)
						.on("mouseover", function(d, i) {
							arc = d3.svg.arc() //弧生成器
								.innerRadius(innerRadius) //设置内半径
								.outerRadius(outerRadius + 7); //设置外半径
							d3.select(this)
								.attr("d", function(d, i) {
									return arc(d);
								})
						})
						.on("mouseout", function(d, i) {
							arc = d3.svg.arc() //弧生成器
								.innerRadius(innerRadius) //设置内半径
								.outerRadius(outerRadius); //设置外半径
							d3.select(this)
								.attr("d", function(d, i) {
									return arc(d);
								})
						})
						.transition()
						.delay(function(d, i) {
							return i * 200;
						})
						.duration(200)
						.ease("linear")
						.attrTween('d', function(d) {
							var i = d3.interpolate(d.startAngle, d.endAngle);
							return function(t) {
								d.endAngle = i(t);
								return arc(d);
							}
						})

					text = svg.selectAll(".text")
						.data(pie2) //返回是pie(data0)
						.enter().append("g")
						.attr("class", "text")
						.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
						.append("text")
						.style('text-anchor', "middle")
						.style("fill", "#fff")
						.attr('transform', function(d, i) {
							var pos = arc.centroid(d); //将数字放在圆弧中心
							return 'translate(' + pos + ')';
						})
						.style("opacity", 0)
						.transition()
						.duration(2000)
						.style("opacity", 1)
						.text(function(d) {
							return d.data[0];
						})

				}

				function returnHighOff() {
				me.$root.Bus.$emit("HighOff", infordata);
				me.$root.Bus.$emit("HighOff", attackdata);
					dataset = [
						["attack", 30],
						["information", 20]
					]

					outerRadius = 100; //外半径
					innerRadius = 65; //内半径，为0则中间没有空白

					d3.selectAll(".text").remove();
					d3.selectAll(".arc").remove();

					var pie2 = pie(dataset)

					arcs = svg.selectAll(".arc")
						.data(pie2) //返回是pie(data0)
						.enter().append("g")
						.attr("class", "arc")
						.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")") //将圆心平移到svg的中心
						.on("mouseover", function(d) {
							tooltip.html(d.data[1])
								.style("left", (d3.event.pageX) + "px")
								.style("top", (d3.event.pageY + 20) + "px")
								.style("opacity", 0.85);

							/*与 桑基图交互*/
							if(d['data'][0] == 'attack') {
								me.$root.Bus.$emit("HighLigt", infordata);
							} else {
								me.$root.Bus.$emit("HighLigt", attackdata);
							}
						})
						.on("mousemove", function(d) {
							/* 鼠标移动时，更改样式 left 和 top 来改变提示框的位置 */

							tooltip.style("left", (d3.event.pageX) + "px")
								.style("top", (d3.event.pageY + 20) + "px");
						})
						.on("mouseout", function(d) {
							/* 鼠标移出时，将透明度设定为0.0（完全透明）*/

							tooltip.style("opacity", 0.0);

							/*与 桑基图交互*/
							if(d['data'][0] == 'attack') {
								me.$root.Bus.$emit("HighOff", infordata);
							} else {
								me.$root.Bus.$emit("HighOff", attackdata);
							}
						})

						.append("path")
						.attr("id", function(d) {
							return d.data[0]
						})
						.attr("fill", function(d, i) {
							return color(i); //根据下标填充颜色
						})
						.attr("d", function(d, i) {
							arc = d3.svg.arc() //弧生成器
								.innerRadius(innerRadius) //设置内半径
								.outerRadius(outerRadius); //设置外半径
							return arc(d); ///调用上面的弧生成器
						})
						.style("filter", "url(#drop-shadow)")
						.on("click", dataChange)
						.on("mouseover", function(d, i) {
							arc = d3.svg.arc() //弧生成器
								.innerRadius(innerRadius) //设置内半径
								.outerRadius(outerRadius + 7); //设置外半径
							d3.select(this)
								.attr("d", function(d, i) {
									return arc(d);
								})
						})
						.on("mouseout", function(d, i) {
							arc = d3.svg.arc() //弧生成器
								.innerRadius(innerRadius) //设置内半径
								.outerRadius(outerRadius); //设置外半径
							d3.select(this)
								.attr("d", function(d, i) {
									return arc(d);
								})
						})
						.transition()
						.delay(function(d, i) {
							return i * 200;
						})
						.duration(200)
						.ease("linear")
						.attrTween('d', function(d) {
							var i = d3.interpolate(d.startAngle, d.endAngle);
							return function(t) {
								d.endAngle = i(t);
								return arc(d);
							}
						})

					text = svg.selectAll(".text")
						.data(pie2) //返回是pie(data0)
						.enter().append("g")
						.attr("class", "text")
						.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")")
						.append("text")
						.style('text-anchor', "middle")
						.style("fill", "#fff")
						.attr('transform', function(d, i) {
							var pos = arc.centroid(d); //将数字放在圆弧中心
							return 'translate(' + pos + ')';
						})
						.style("opacity", 0)
						.transition()
						.duration(2000)
						.style("opacity", 1)
						.text(function(d) {
							return d.data[0];
						})
				}

				//添加滤镜
				var defs = svg.append("defs");
				var filter = defs.append("filter")
					.attr("id", "drop-shadow")
					.attr("width", "200%")
					.attr("height", "200%");

				filter.append("feGaussianBlur")
					//  .attr("in", "SourceAlpha")
					.attr("stdDeviation", 5)

					.attr("result", "blur");

				// translate output of Gaussian blur to the right and downwards with 2px
				// store result in offsetBlur
				filter.append("feOffset")
					.attr("in", "blur")
					.attr("dx", 0)
					.attr("dy", 0)
					.attr("result", "offsetBlur");

				var feMerge = filter.append("feMerge");

				feMerge.append("feMergeNode")

					.attr("in", "offsetBlur")
				feMerge.append("feMergeNode")

					.attr("in", "SourceGraphic");
			}
		}
	}
</script>

<style type="text/css">
	button {
		position: absolute;
		margin: 10px;
		padding: 10px 15px;
		background-color: #1F77B4;
		color: #fff;
		border: none;
		display: inline-block;
		text-align: center;
	}
	
	.tooltip {
		position: absolute;
		width: auto;
		height: auto;
		padding: 10px 10px 10px 10px;
		font-family: simsun;
		font-size: 14px;
		text-align: center;
		border-style: solid;
		border-width: 0px;
		background-color: black;
		color: white;
		border-radius: 5px 5px 5px 5px;
	}
</style>