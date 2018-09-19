
<template>
  <div id="main_div">
      <p style="color:#ccc;font-size:15px;font-family: sans-serif;font-weight: bolder;text-align: center">攻击流程视图</p>
  </div>
</template>

<script>
  import axios from 'axios';
  import $ from 'jquery'
  import {mapGetters} from 'vuex'
  import * as d3 from 'd3v4'
  require('../assets/smartMenu.js')
  require('../assets/smartMenu.css')
//  import  d3sankey from '../assets/sankey.js'
    export default {
      name: 'main_div',
      data () {
        return {
            email_list:[]//创建一些需要使用的对象或者数组
        }
    },
    methods:{
      choose(nodetype){
            this.$emit('nodeselect',nodetype);
        },
      daga(e){
        if(e=="run"){

          var that=this;
          var units = "Widgets";
          var ifshan = that.$store.state.ifshan;
          var margin = {top: 10, right: 10, bottom: 10, left: 10},
          width = document.getElementById("main_view").offsetWidth*0.95,
          height = document.getElementById("main_view").offsetHeight*0.95
          var shujudataS=this.$store.state.dir_data;
          console.log(shujudataS)
          var arr7=this.$store.state.arr8;
          var arr8=this.$store.state.arr7;
         function creatChart(shujudataS,arr7,arr8)
         {
         console.log(shujudataS)
           function initdelatechoice(__data){//初始化右键菜单
            		var str = 'smartMenu_chatRightControls'+__data.toString()
            		var removeObj = document.getElementById(str)
               	if(removeObj!=null){
               		 removeObj.parentNode.removeChild(removeObj);
               	}
            		var userMenuData = [
                 [{
                     text: "确认删除节点",
                     func: function () {
                      var id = $(this).on("mouseover", function(d){
                       	return d;
                      })
            	       if(id[0].__data__.sourceLinks.length==id[0].__data__.targetLinks.length){

            	        	delatechoice(id[0].__data__.sourceLinks.length,id[0].__data__,shujudataS)
            	       }
                     }
                         }]
               ];
               $("body").smartMenu(userMenuData, {
                 name: "chatRightControl",
                 container: "g.node"
               });
            	}
            	initdelatechoice(1)
            function delatechoice(__data__,__datas__,shujudataS){//重新设置右键菜单，根据经过节点路径的数量进行子菜单生成,总数，数据1，总数据
            	 	var removeObj = document.getElementById('smartMenu_chatRightControl')
               	if(removeObj!=null){ removeObj.parentNode.removeChild(removeObj);}
               	var userMenuData1 =  [{text: "选择节点路径",data:[]}]
               	userMenuData1[0].data[0]=[]
               	var userMenuData2 = []
               	var userMenuData3 = []
               	var s = 0
               	for(var i = 0;i<__data__;i++){
               	  userMenuData1[0].data[0][i]={
               	  arguments:i,
                     text: "删除路径"+(i+1).toString(),
                     func: function (d){
                     	var id = $(this).on("mouseover", function(d){
                       	return d;
                       })
                    s=parseInt(d.replace(/[^0-9]/ig,""))
                    console.log(s);
                      console.log(__data__);
                        console.log(id[0].__data__,shujudataS);
                    deletes(s,__data__,id[0].__data__,shujudataS)
                    initdelatechoice(__data__)
                     }
                   }
               	}
               	userMenuData2[0]=userMenuData1
               	userMenuData3[__data__]=userMenuData2
               	$("body").smartMenu(userMenuData3[__data__], {
                 name: "chatRightControlss"+__data__.toString(),
                 container: "g.node"
               });
             }

















           var formatNumber = d3.format(",.0f"),    // zero decimal places
               format = function(d) { return formatNumber(d) + " " + units; };
           var svg = d3.select("#main_div").append("svg")
               .attr("width", width + margin.left + margin.right)
               .attr("height", height + margin.top + margin.bottom)
               .append("g")
               .attr("transform","translate(" + margin.left + "," + margin.top + ")");
               var a = d3.rgb(175,238,238, .2);	//红色
               var b = d3.rgb(76, 165, 246);
               var defs = svg.append("defs");

                var linearGradient = defs.append("linearGradient")
                .attr("id","linearColor")
                .attr("x1","0%")
                .attr("y1","0%")
                .attr("x2","100%")
                .attr("y2","0%");

                 var stop1 = linearGradient.append("stop")
                .attr("offset","0%")
                .style("stop-color",a.toString());

                 var stop2 = linearGradient.append("stop")
                 .attr("offset","100%")
              .style("stop-color",b.toString());
           // filters go in defs element
          var defss = svg.append("defs")


// create filter with id #drop-shadow
// height=130% so that the shadow is not clipped
          var filter = defss.append("filter")

                     .attr("id", "drop-shadow")
                     .attr("width", "200%")
                     .attr("height", "200%");

// SourceAlpha refers to opacity of graphic that this filter will be applied to
// convolve that with a Gaussian with standard deviation 3 and store result
// in blur
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

// overlay original SourceGraphic over translated blurred opacity by using
// feMerge filter. Order of specifying inputs is important!
     var feMerge = filter.append("feMerge");

     feMerge.append("feMergeNode")

            .attr("in", "offsetBlur")
     feMerge.append("feMergeNode")

            .attr("in", "SourceGraphic");
           //添加marker标签及其属性
             var defsss = svg.append("defs")
           var arrowMarker = defsss.append("marker")
               .attr("id","arrow")
               .attr("markerUnits","strokeWidth")
               .attr("markerWidth",10)
               .attr("markerHeight",10)
               .attr("viewBox","0 0 12 12")
               .attr("refX",10)
               .attr("refY",6)
               .attr("orient","auto")
           var arrow_path = "M2,2 L10,6 L2,10 L6,6 L2,2";
               arrowMarker.append("path")
               .attr("d",arrow_path)
               .attr("fill","#e0f4f1");
           // Set the sankey diagram properties

           var sankey = d3.sankey()
               .nodeWidth(36)
               .nodePadding(10)
               .size([width, height]);
           var path = sankey.link();
            	if(ifshan==false)
            	{console.log("run")
                var nodeMap = {};
               shujudataS.nodes.forEach(function(x) { nodeMap[x.name] = x; });
               shujudataS.links = shujudataS.links.map(function(x) {
                 return {
                   source: nodeMap[x.source],
                   target: nodeMap[x.target],
                   urls: x.urls,
                   value: x.value
                 };
               });
           }
           var dragS =d3.drag()//节点拖拽
                 // .origin(function(d) { return d; })
                 .on("start", onDragStart)
                 .on("drag", dragmove)
                 .on("end", dragended)
             sankey
                 .nodes(shujudataS.nodes)
                 .links(shujudataS.links)
                 .layout(1,0.8)//参数1叠带次数设置，对节点纵向布局有影响
                 .overlapLinksAtSources(true)
                 .overlapLinksAtTargets(true);
           // add in the links
           var link = svg.append("g").selectAll(".link")
                 .data(shujudataS.links)
                 .enter().append("path")
                 .attr("class", "link")
                 .attr("transform", function(d,i) {return "translate(" + 0 + "," + (d.dy*0 )+ ")"; })
                  .attr("id", function(d,i){return "NO"+i})
                 .attr("d", path)
                 .attr("marker-end","url(#arrow)")

                 .style("stroke-width", function(d) { return 3; })
                 .sort(function(a, b) { return b.dy - a.dy; })


           // add the link titles
             link.append("title")
                   .text(function(d) {return d.source.name + " → " +d.target.name + "\n" + format(d.value); });

           // add in the nodes
             var node = svg.append("g").selectAll("g.node")
                 .data(shujudataS.nodes)
                 .enter().append("g")
                 .attr("class", "node")
                 .attr("id", "noderect")
                 .attr("transform", function(d,i) { return "translate(" + (d.x )+ "," + (d.y)+ ")"; })
           	  .call(dragS)
           	  .on('click', outputurl);



             node.append("rect")
                 .attr("height",30)//考虑根据节点数动态设置高度
                 .attr("width", sankey.nodeWidth()+50)
                 .attr("rx",10)
                 .attr("ry",10)
                 .style("stroke", "rgba(147, 235, 248, 1)")
                 .style("fill",  "url(#" + linearGradient.attr("id") + ")" )
                 .style("stroke-width",1.5)
                 .style("stroke-opacity",.8)
                 .style("filter", "url(#drop-shadow)")
                 .append("title")
                 .text(function(d) {return d.name + "\n" + format(d.value); });


           // add in the title for the nodes
            var textS =node.append("text")
                 .attr("x", 100)
                 .attr("y", function(d) { return (d.dy / 2); })
                 .attr("dy", ".35em")
                 .attr("text-anchor", "end")
                 .attr("transform", null)
                 .text(function(d) { return d.name; })
                 .filter(function(d) { return d.x < width / 2; })
                 .attr("x", 6 )
                 .attr("text-anchor", "start")
             link.attr("transform", function(d,i) {return "translate(" + 0 + "," + (-document.getElementById("noderect").getBBox().height+40)+ ")"; })//通过参数动态设置线段偏移
             d3.selectAll("text").attr("transform",  "translate(" + 0 + "," + (50-document.getElementById("noderect").getBBox().height+10)+ ")")



           function onDragStart() {}
// the function for moving the nodes
           function dragmove(d)
           {
           d3.select(this).attr("transform",
          "translate(" + (
            d.x = Math.max(0, Math.min(width - d.dx, d3.event.x))
            ) + "," + (
            d.y = Math.max(0, Math.min(height - d.dy, d3.event.y))
           ) + ")");
           sankey.relayout();
           link.attr("d", path);
           }
          function dragended(d, i) {}


function outputurl(d) {//输出节点文件夹对应文件路径函数
    that.choose(d.name);
    if (d3.event.defaultPrevented === false) {
     if(d.sourceLinks.length>0){
     for (var i =0;i<d.sourceLinks.length;i++) { that.$store.state.dataurls=d.sourceLinks[i].urls+"\\"+d.name.replace(/[0-9]/ig,"");}
 }else{
   for (var i =0;i<d.targetLinks.length;i++) {that.$store.state.dataurls=d.targetLinks[i].urls+"\\"+d.targetLinks[i].source.name+"\\"+d.name.replace(/[0-9]/ig,""); }
 }
 }
}
function deletes(num,sum,d,shuju) {//删除节点函数
  console.log(num,sum,d,shuju);
	var a = 0;
	var b = 0;
	var c = 0;
	var ds = 0;
	var sort =  new Array()//由于d.sourceLinks是凌乱的，无法与d.targetLinks关系对应，使得在后续的处理中发生错误
	for (var i = 0;i<shuju.links.length;i++) {//故此处根据原始数据的先后关系对d.sourceLinks顺序重排。
		for (var j = 0;j<d.sourceLinks.length;j++) {
			if(shuju.links[i].target.name==d.sourceLinks[j].target.name){

				sort[c]=d.sourceLinks[j];
				c++;
			}
		}
	}
    console.log(sort)
	d.sourceLinks=sort;
		if(d.sourceLinks.length==d.targetLinks.length){
		for(var i =0;i<shuju.links.length;i++){
		if(shuju.links[i].source.name==d.sourceLinks[num-1].source.name&&shuju.links[i].target.name==d.sourceLinks[num-1].target.name){
			a=i
			shuju.links[i].source=shuju.links[b].source;
			break;
		}
		if(shuju.links[i].source.name==d.targetLinks[num-1].source.name&&shuju.links[i].target.name==d.targetLinks[num-1].target.name){
			b=i;
		}
	}
	for(var i =0;i<shuju.links.length;i++){
		if(shuju.links[i].source.name==d.name||shuju.links[i].target.name==d.name){
			ds++;
		}
	}
	for(var i =0;i<shuju.nodes.length;i++){
		if(shuju.nodes[i].name ==d.name&&ds==1){
			shuju.nodes.splice(i,1)
		}
	}
	shuju.links.splice(b,1)
}
	d3.select("#main_div").selectAll("svg").remove()
	that.$store.state.ifshan=true;
 that.$store.state.ifcl = true;
that.$store.state.shuju =shuju;

  that.$emit('nodeselect','wtf');
 	//handlelink2(shuju,that.$store.state.ifcl);
 }


         }
         creatChart(shujudataS,arr7,arr8)

      }
    },


    },
    beforeCreate(){
    },
    created(){
    },
    beforeMount(){
    },
    mounted(){
      d3.sankey = function() {
        var sankey = {},
            nodeWidth = 24,
            nodePadding = 8,
            size = [1, 1],
            nodes = [],
            links = [],
            overlapLinksAtSources = false,
            overlapLinksAtTargets = false,
            minValue = 1;

        sankey.nodeWidth = function(_) {
          if (!arguments.length) return nodeWidth;
          nodeWidth = +_;
          return sankey;
        };

        sankey.nodePadding = function(_) {
          if (!arguments.length) return nodePadding;
          nodePadding = +_;
          return sankey;
        };

        sankey.nodes = function(_) {
          if (!arguments.length) return nodes;
          nodes = _;
          return sankey;
        };

        sankey.links = function(_) {
          if (!arguments.length) return links;
          links = _;

          return sankey;
        };

        sankey.size = function(_) {
          if (!arguments.length) return size;
          size = _;
          return sankey;
        };

        sankey.overlapLinksAtSources = function(_) {
          if (!arguments.length) return overlapLinksAtSources;
          overlapLinksAtSources = _;
          return sankey;
        };

        sankey.overlapLinksAtTargets = function(_) {
          if (!arguments.length) return overlapLinksAtTargets;
          overlapLinksAtTargets = _;
          return sankey;
        };

        sankey.minValue = function(_) {
          if (!arguments.length) return minValue;
          minValue = _;
          return sankey;
        };

        sankey.layout = function(iterations,asd) {
          computeNodeLinks();
          computeNodeValues();
          computeNodeBreadths();
          computeNodeDepths(iterations,asd);
          computeLinkDepths();
          return sankey;
        };

        sankey.relayout = function() {
          computeLinkDepths();
          return sankey;
        };

        sankey.link = function() {
          var curvature = .5;

          function link(d) {
            var x0 = d.source.x + d.source.dx,
                x1 = d.target.x,
                xi = d3.interpolateNumber(x0, x1),
                x2 = xi(curvature),
                x3 = xi(1 - curvature),
                y0 = d.source.y + (overlapLinksAtSources ? 0 : d.sy) + d.dy / 2,
                y1 = d.target.y + (overlapLinksAtTargets ? 0 : d.ty) + d.dy / 2;
            return "M" + x0 + "," + y0
                 + "C" + x2 + "," + y0
                 + " " + x3 + "," + y1
                 + " " + x1 + "," + y1;
          }

          link.curvature = function(_) {
            if (!arguments.length) return curvature;
            curvature = +_;
            return link;
          };

          return link;
        };

        // 填充每个节点的源代码链接和目标链接
        // 此外，如果源和目标不是对象，假设它们是索引。
        function computeNodeLinks() {
          nodes.forEach(function(node) {
            node.sourceLinks = [];
            node.targetLinks = [];
          });
          links.forEach(function(link) {
            var source = link.source,
                target = link.target;
            if (typeof source === "number") source = link.source = nodes[link.source];
            if (typeof target === "number") target = link.target = nodes[link.target];
            source.sourceLinks.push(link);
            target.targetLinks.push(link);
            if ("value" in link)
              link.value = Math.max(link.value, minValue);
            else
              link.value = minValue;
          });
        }

        // 通过计算相关联的链接来计算每个节点的值（大小）。
        function computeNodeValues() {
          nodes.forEach(function(node) {
            if ("value" in node)
              node.value = Math.max(node.value, minValue);
            else
              node.value = minValue;
            if (node.sourceLinks.length > 0) {
              if (overlapLinksAtSources)
               {
               	node.value = Math.max(node.value, d3.max(node.sourceLinks, value));console.log(node.value)
               		//node.value =2
               }
              else
                {
                	//node.value = Math.max(node.value, d3.sum(node.sourceLinks, value));console.log(node.value)
                		node.value =2
                	}
      //console.log(node.value)
            }
            if (node.targetLinks.length > 0) {
              if (overlapLinksAtTargets){
              	node.value = Math.max(node.value, d3.max(node.targetLinks, value));
              		//node.value =2
              }

              else
               {
               	//node.value = Math.max(node.value, d3.sum(node.targetLinks, value));  console.log(node.value)
               	node.value =2

               	}



            }
          });
        }

        // Iteratively assign the breadth (x-position) for each node.
        // Nodes are assigned the maximum breadth of incoming neighbors plus one;
        // nodes with no incoming links are assigned breadth zero, while
        // nodes with no outgoing links are assigned the maximum breadth.
        //迭代分配每个节点的广度（X位置）。

      ///节点被分配的最大邻居宽度加上一个；

      //没有传入链路的节点被分配广度为零，而

      //没有外向链路的节点被分配到最大宽度。
        function computeNodeBreadths() {
          var remainingNodes = nodes,
              nextNodes,
              x = 0;

          while (remainingNodes.length) {
            nextNodes = [];
            remainingNodes.forEach(function(node) {
              node.x = x;
              node.dx = nodeWidth;
              node.sourceLinks.forEach(function(link) {
                nextNodes.push(link.target);
              });
            });
            remainingNodes = nextNodes;
            ++x;
          }

          //
          moveSinksRight(x);
          scaleNodeBreadths((size[0] - nodeWidth) / (x - 1));
        }

        function moveSourcesRight() {
          nodes.forEach(function(node) {
            if (!node.targetLinks.length) {
              node.x = d3.min(node.sourceLinks, function(d) { return d.target.x; }) - 1;
            }
          });
        }

        function moveSinksRight(x) {
          nodes.forEach(function(node) {
            if (!node.sourceLinks.length) {
              node.x = x - 1;
            }
          });
        }

        function scaleNodeBreadths(kx) {
          nodes.forEach(function(node) {
            node.x *= kx-15;//节点间的宽度设置????
          });
        }

        function computeNodeDepths(iterations,asd) {

          var nodesByBreadth = d3.nest()//将节点分组
              .key(function(d) { return d.x; })
              .sortKeys(d3.ascending)
              .entries(nodes)
              .map(function(d) { return d.values; });

          //
          initializeNodeDepth(asd);
          resolveCollisions();
          for (var alpha = 1; iterations > 0; --iterations) {
            relaxRightToLeft(alpha *= .99);
            resolveCollisions();
            relaxLeftToRight(alpha);
            resolveCollisions();
          }

          function initializeNodeDepth(asd) {
            var ky = d3.min(nodesByBreadth, function(nodes) {
              return (size[1] - (nodes.length - 1) * nodePadding) / d3.sum(nodes, value);
            });

            nodesByBreadth.forEach(function(nodes) {
              nodes.forEach(function(node, i) {
                node.y = i;

               node.dy = node.value * ky*asd;//节点及连线y轴上的间距
               //node.dy = ky+50;//节点及连线y轴上的间距
              });
            });

            links.forEach(function(link) {
              //link.dy = link.value * ky;
              link.dy =  ky;//连接线的y轴偏移设置

            });
          }

          function relaxLeftToRight(alpha) {
            nodesByBreadth.forEach(function(nodes, breadth) {
              nodes.forEach(function(node) {
                if (node.targetLinks.length) {
                  var y = d3.sum(node.targetLinks, weightedSource) / d3.sum(node.targetLinks, value);
                  //console.log(y)
                  node.y += (y - center(node)) * alpha;

                }
              });
            });

            function weightedSource(link) {

              return center(link.source) * link.value;
            }
          }

          function relaxRightToLeft(alpha) {
            nodesByBreadth.slice().reverse().forEach(function(nodes) {
              nodes.forEach(function(node) {
                if (node.sourceLinks.length) {
                  var y = d3.sum(node.sourceLinks, weightedTarget) / d3.sum(node.sourceLinks, value);
                  node.y += (y - center(node)) * alpha;


                }
              });
            });

            function weightedTarget(link) {
              return center(link.target) * link.value;
            }
          }

          function resolveCollisions() {
            nodesByBreadth.forEach(function(nodes) {
              var node,
                  dy,
                  y0 = 0,
                  n = nodes.length,
                  i;

              // Push any overlapping nodes down.向下推任何重叠节点。
              //nodes.sort(ascendingDepth);
              for (i = 0; i < n; ++i) {
                node = nodes[i];
                dy = y0 - node.y;

                if (dy > 0) node.y += dy;
                y0 = node.y + node.dy + nodePadding;
              }

              // If the bottommost node goes outside the bounds, push it back up.如果最底部的节点超出边界，则将其推回。
              dy = y0 - nodePadding - size[1];
              if (dy > 0) {
                y0 = node.y -= dy;

                // Push any overlapping nodes back up.将任何重叠节点重新推回。
                for (i = n - 2; i >= 0; --i) {
                  node = nodes[i];
                  dy = node.y + node.dy + nodePadding - y0;
                  if (dy > 0) node.y -= dy;
                  y0 = node.y;
                }
              }
            });
          }

          function ascendingDepth(a, b) {
            return a.y - b.y;
          }
        }

        function computeLinkDepths() {
          nodes.forEach(function(node) {
            node.sourceLinks.sort(ascendingTargetDepth);
            node.targetLinks.sort(ascendingSourceDepth);
          });
          nodes.forEach(function(node) {
            var sy = 0, ty = 0;
            node.sourceLinks.forEach(function(link) {
              link.sy = sy;
              sy += link.dy;
            });
            node.targetLinks.forEach(function(link) {
              link.ty = ty;
              ty += link.dy;
            });
          });

          function ascendingSourceDepth(a, b) {
            return a.source.y - b.source.y;
          }

          function ascendingTargetDepth(a, b) {
            return a.target.y - b.target.y;
          }
        }

        function center(node) {
          return (node.y + node.dy / 2);
        }

        function value(link) {
          return link.value;
        }

        return sankey;
      };




          //consol2e.log(this.$store.state.ifcl);


}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#main_div{
    height: 100%;
    width: 100%;
}
</style>
