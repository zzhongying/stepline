<template>
  <div id="force">
    <p style="color:#ccc;font-size:15px;font-family: sans-serif;font-weight: bolder;width: 15%;height:3%">对应视图
      
    </p>

<svg style="width: 100%;height:100%"></svg>
  </div>
</template>

<script>
import * as d3 from 'd3v4'
//let d3=require('../assets/d3.v3.js')
  export default {
    data() {
      return {
        myChart:{},
        option:{},
        choosed:{}
      }
    },
    computed:{
    },
    methods:{

      choose(params){
          //this.$emit('grahpselect',params);
      },
      go_back(){
      var that=this;
        d3.text('./static/resql.txt', function(root) {
          var data = new Array();
     	var datas = new Array();
     	var datass = new Array();
     	var datato = root.split(/[,]/);
     	var cc = 0;
     	for (var i = 0;i<datato.length;i=i+2) {

     		data[cc++]=datato[i].split(/[/?=]/)//使用正则表达式按/ ？ = 分割url
     	}

     	datas[0]=data[0][3]
     	var c = 0;
     	var ck= 0
     	var ifdeng =0;

     	for(var i = 1;i<data.length;i++){//统计出不同的子节点名称

     		if(data[i][3]!=data[i-1][3]){
     			for(var j=0;j<datas.length;j++){
     				if(data[i][3]===datas[j]){
     					ifdeng =1; break;
     				}
     			}
     			if(ifdeng===0){datas[c++]=data[i][3];}
     			else{ifdeng=0;}
     		}
     	}
     	for(var j=0;j<datas.length;j++)//按照子节点不同，将从属数据进行分类
     	{
     		datass[j] = new Array();
     	 for(var i = 0;i<data.length;i++)
     	  {
     		if(datas[j]===data[i][3]){
     			var x =data[i][5].split("'")//因为最初割出的值是带''的字符串，故再次分割并使用正则表达式检测结果是否为纯数字，以此来区分value的不同
     			var r = /^\+?[1-9][0-9]*$/;　　//正整数

     			if(r.test(x[0])==true){
     				x[0]=parseInt(x[0]);
     			}
     			datass[j][ck++]={name:data[i][4],value:x[0],color:0,};
     		}
     	  }
     	  ck=0;
     	}

     	var jsons = new Array();//将数据转为带有层次结构的json结构
     	    var datatojson = new Object()

     	for (var i = 0;i<datas.length;i++) {
     		jsons[i] ={

     	    	name:datas[i],
     	    	children:datass[i],
     	    }
     	}
     	datatojson ={
     	    	name:data[0][2],
     	    	children:jsons
     	    }

     	that.create("force",document.getElementById("Inf_view2").offsetWidth*0.95,document.getElementById("Inf_view2").offsetWidth*0.95,datatojson)
        })
      },
    create(divname,width,height,text,tree)  {
      var z = d3.scaleOrdinal(d3.schemeCategory20);
          var active = d3.select(null);

//  d3.select("#"+divname).select("svg").select("g").remove();
  var svg = d3.select("#"+divname).select("svg")
        .attr("width", width)
        .attr("height", height);
        var links = d3.hierarchy(text,function children(d) {return d.children;})
                  .each(function(d) {
                  //if(d.parent == null) {num = d.value;};
                  if (id = d.data.name) {
                       var id
                       d.id = id;
                       d.class = id;
                       d.value = d.data.value;
                   }})

    var tree = d3.tree()

    var link = svg.selectAll("line")
           .data(tree(links).links())
           .enter().insert("line")
          .style("stroke", "#999")
          .style("stroke-width", "2px");

       var force = d3.forceSimulation()
         .force("center", d3.forceCenter(width,height))
        .force("charge", d3.forceManyBody().strength(-800))
       .force("link", d3.forceLink(link).distance(200))
       .force("x", d3.forceX())
       .force("y", d3.forceY())
       .alphaTarget(1);



        var rectdata =new Array();
       var circledata =new Array();
       var j=0;
       var k=0;
      for(var i = 0;i<tree(links).descendants().length;i++)//根据深度不同过拆分数据，分别用不同的绘图方式加载。
      {
      	if(tree(links).descendants()[i].depth==2){
      		circledata[j++]=tree(links).descendants()[i];
      	}
      	else{
      		rectdata[k++]=tree(links).descendants()[i];
      	}
      }





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



       var legends  =[];
        legends[0]="数字型";
        legends[1]="字符型";
       var g = svg.append("g").attr("transform", "translate(" + 20 + "," + 10 + ")");
      var legend = g.append("g")
      /*.attr("font-family", "sans-serif")
      .attr("font-size", 15)
      .attr("text-anchor", "end")*/
    .selectAll("g")
    .data(legends)
    .enter().append("g")
    .attr("transform", function(d, i) { return "translate(0," + (i *25) + ")"; });
  legend.append("circle")
       .attr("r", 10)

       .style("fill", function(d,i) {
          if(d =='字符型')
          	{return "#AEEEEE";}
          	else
          	{return "#FF8247";}
          });

  legend.append("text")
      .attr("x", 10)
      .attr("y", -13)
      .attr("dy", "0.1em")
      .attr("fill", "white")
      .text(function(d) { return d; });


  /*  var node = svg.selectAll("rect.node")
          .data(rectdata)
          .enter()
          .append("rect")
          .attr("x", function(d) {return d.x; })    // 顶点的 x 坐标
		  .attr("y", function(d) { return d.y; })
          .attr("width",function(d) { if(d.depth=== 0){return 150; }else{return 130}})
          .attr("height",function(d) { if(d.depth=== 0){return 30; }else{return 20}})//根据深度不同设定每个矩形的高度
          .style("fill", function(d) { return z(d.parent && d.parent.name); })
          .style("stroke", "#000")
         .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));*/
         var node = svg.selectAll("rect.node")
             .data(rectdata)
             .enter()
             .append("circle")
             .attr("r", function(d) { if(d.depth=== 0){return 30; }else{return 15}})
             .style("stroke", "rgba(147, 235, 248, 1)")
             .attr("stroke-width",2)
              .style("filter", "url(#drop-shadow)")
             .style("fill", function(d) { return z(d.parent && d.parent.name); })

            // .style("stroke", "#000")
             .call(d3.drag()
             .on("start", dragstarted)
             .on("drag", dragged)
             .on("end", dragended));
    var text = svg.append("g")
    .attr("class", "labels")
     .selectAll("text")
    .data(rectdata)
     .enter().append("text")
    .attr("dy", 2)
    .attr("text-anchor", "middle")
    .text(function(d) { return d.class})
    .attr("fill", "white");


       var nodess = svg.selectAll("circle.node")
          .data(circledata)
          .enter()
          .append("circle")
          .attr("r", 10)
          .style("stroke", "rgba(147, 235, 248, 1)")
          .attr("stroke-width",2)
          .style("filter", "url(#drop-shadow)")
          .style("fill", function(d,i) {
          if(typeof d.value=='string')
          	{return "#AEEEEE";}
          	else
          	{return "#FF8247";}
          })

        .call(d3.drag()
          .on("start", dragstarted)
          .on("drag", dragged)
          .on("end", dragended));


 var texts = svg.append("g")
    .attr("class", "labels")
     .selectAll("text")
    .data(circledata)
     .enter().append("text")
    .attr("dy", 2)
     .style("font-size","12px")
    .attr("text-anchor", "middle")
    .text(function(d) {return d.class})
    .attr("fill", "white");


        force.nodes(tree(links).descendants())
         force.force("link").links(tree(links).links());
         force.on("tick", ticked);
         force.alpha(1).restart();

    function ticked() {

        link.attr("x1", function(d) { return d.source.x*0.6; })
            .attr("y1", function(d) { return d.source.y*0.6; })
            .attr("x2", function(d) { return d.target.x*0.6; })
            .attr("y2", function(d) { return d.target.y*0.6; });

      node.attr("cx", function(d) { if(d.depth!= 2){return d.x*0.6; }})
          .attr("cy", function(d) { if(d.depth!= 2){return d.y*0.6; }});
      nodess.attr("cx", function(d) { if(d.depth=== 2){return d.x*0.6; }})
            .attr("cy", function(d) { if(d.depth=== 2){return d.y*0.6; }});
       texts
        .attr("x", function(d) { return d.x*0.6; })
      .attr("y", function(d) { return d.y*0.6; });

       text
      .attr("x", function(d) { return d.x*0.6+70; })
      .attr("y", function(d) { return d.y*0.6+10; });

      };

function printUrl(id){

		for(var i = 0;i<data.length;i++){
			var str =""
			if(id ===data[i][data[i].length-1]){
				for(var j = 0;j<data[i].length;j++){
					if(j==data[i].length-1){
						str=str+data[i][j];
					}
					else{
						str=str+data[i][j]+".";
					}
				}
				console.log(str)
			}
		}


	}


function dragstarted(d) {

  if (!d3.event.active) force.alphaTarget(1).restart();
  d.fx = d.x;
  d.fy = d.y;
}

function dragged(d) {
  d.fx = d3.event.x;
  d.fy = d3.event.y;
}

function dragended(d) {
  if (!d3.event.active) force.alphaTarget(1);
  d.fx = null;
  d.fy = null;
}
function flatten(root) { // <-A
      var nodes = [];
      function traverse(node, depth) {
        if (node.children) {
          node.children.forEach(function(child) {
            child.parent = node;
            traverse(child, depth + 1);
          });
        }
        node.depth = depth;
        nodes.push(node);
      }
      traverse(root, 1);
      return nodes;
    }
},


  change(node){}
    },
    mounted(){
    this.go_back();
    }
  }
</script>


<style scoped>
#force{
  float:right;
  width: 100%;
  height: 100%;
  padding: 5px;
}
</style>
