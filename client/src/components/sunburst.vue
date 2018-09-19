<template>

</template>

<script>
//import * as d3 from 'd3v3'
import {mapGetters} from 'vuex'
 //require('../assets/d3.v3.js')
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
      change(params){

        if(this.$store.state.dataurls!=null){
          d3.select("#force").selectAll("svg").remove()
          var parentdiv = document.getElementById("force");
          var sonDiv = document.createElement("div");
          sonDiv.id="sequence"
          var sonDivS = document.createElement("div");
            sonDivS.id="explanation"
          var sp = document.createElement("span");
          sp.id="percentage"
          sonDivS.appendChild(sp);
          sonDiv.appendChild(sonDivS);
          parentdiv.appendChild(sonDiv);
         document.getElementById('percentage').style.color="white"


  function buildHierarchy(csv) {
  var root = {"name": "root", "children": []};
  for (var i = 0; i < csv.length; i++) {
    var sequence = csv[i][0];
    var size = +csv[i][1];
    if (isNaN(size)) {
      continue;
    }
    var parts = sequence.split("/");
    var currentNode = root;
    for (var j = 0; j < parts.length; j++) {
      var children = currentNode["children"];
      var nodeName = parts[j];
      var childNode;
      if (j + 1 < parts.length) {

 	var foundChild = false;
 	for (var k = 0; k < children.length; k++) {
 	  if (children[k]["name"] == nodeName) {
 	    childNode = children[k];
 	    foundChild = true;
 	    break;
 	  }
 	}

 	if (!foundChild) {
 	  childNode = {"name": nodeName, "children": []};
 	  children.push(childNode);
 	}
 	currentNode = childNode;
      } else {

 	childNode = {"name": nodeName, "size": size};
 	children.push(childNode);
      }
    }
  }
  return root;
};
//------------------------------------------------------------------------------------------------------
var width = document.getElementById("force").offsetWidth;
var height = document.getElementById("force").offsetHeight*0.8;
var radius = Math.min(width, height) / 2;
//  数据格式化，指示的大小， 点击事件。

var b = {
  w: 75, h: 30, s: 3, t: 10
};


var colors = ["#71edb4","#71e1b9","#73ccc4","#74b7cd","#74a7d5","#7599db","#7592de","#768ce1",];


var totalSize = 0;

var vis = d3.select("#force").append("svg:svg")
    .attr("width", width)
    .attr("height", height)
    .append("svg:g")
    .attr("id", "container")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");
    var defss = vis.append("defs")


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

var partition = d3.layout.partition()
    partition.size([2 * Math.PI, radius * radius])
    .value(function(d) { return d.size; });

var arc = d3.svg.arc()
    .startAngle(function(d) { return d.x; })
    .endAngle(function(d) { return d.x + d.dx; })
    .innerRadius(function(d) { return Math.sqrt(d.y); })
    .outerRadius(function(d) { return Math.sqrt(d.y + d.dy); });
     console.log(this.$store.state.dataurls)
            d3.csv("./static/directorycrawl.txt",function(root){
              console.log(root);
              var texts="";
            for(var i =0;i<root.length;i++){
            	texts = texts +(root[i].id+",1321\n")
            }
            var csv = d3.csv.parseRows(texts);
            var json = buildHierarchy(csv);
            console.log(json);



            createVisualization(json);



            function createVisualization(json) {


              initializeBreadcrumbTrail();



              vis.append("svg:circle")
                  .attr("r", radius)
                  .style("opacity", 0);


             var nodes = partition(json)//.nodes(json)
                 /* .filter(function(d) {
                  return (d.dx > 0.005);
                  });*/

              var path = vis.data([json]).selectAll("path")
                  .data(nodes)
                  .enter().append("svg:path")
                  .attr("display", function(d) { return d.depth ? null : "none"; })
                  .attr("d", arc)
                  .attr("fill-rule", "evenodd")
                  .style("stroke", "rgba(147, 235, 248, 1)")
                  .attr("stroke-width",2)
                  .style("fill", function(d) { return colors[d.depth]})
                  .style("filter", "url(#drop-shadow)")
                  .style("opacity", .8)
                  .on("mouseover", mouseover)
                  .on("click", function(d,i){
                  	for (var i = 0;i<d.length;i++) {
                  	}

                  });


              d3.select("#container").on("mouseleave", mouseleave);


              totalSize = path.node().__data__.value;
              console.log(totalSize)
             };


            function mouseover(d) {

              var percentage = (100 * d.value / totalSize).toPrecision(3);
              var percentageString = "层占比："+percentage + "%";
              if (percentage < 0.1) {
                percentageString = "< 0.1%";
              }

              d3.select("#percentage")
                  .text(percentageString);

              d3.select("#explanation")
                  .style("visibility", "");

              var sequenceArray = getAncestors(d);
              updateBreadcrumbs(sequenceArray, percentageString);


              d3.selectAll("path")
                  .style("opacity", 0.3);


              vis.selectAll("path")
                  .filter(function(node) {
                            return (sequenceArray.indexOf(node) >= 0);
                          })
                  .style("opacity", 1);
            }


            function mouseleave(d) {


              d3.select("#trail")
                  .style("visibility", "hidden");


              d3.selectAll("path").on("mouseover",  mouseover);


              d3.selectAll("path")
                  .transition()
                  .duration(1000)
                  .style("opacity", 1)
                  .each("end", function() {
                          d3.select(this).on("mouseover", mouseover);
                        });

              d3.select("#explanation")
                  .transition()
                  .duration(1000)
                  .style("visibility", "hidden");
            }


            function getAncestors(node) {
              var path = [];
              var current = node;
              while (current.parent) {
                path.unshift(current);
                current = current.parent;
              }
              return path;
            }

            function initializeBreadcrumbTrail() {

              var trail = d3.select("#sequence").append("svg:svg")
                  .attr("width", width)
                  .attr("height", 50)
                  .attr("id", "trail")
                  .style("fill", "white");

            }


            function breadcrumbPoints(d, i) {

              var points = [];


              if(i==0){
              	 points.push("0,0");
              points.push(b.w*2 + ",0");
              points.push(b.w *2+ b.t+ "," + (b.h / 2));
              points.push(b.w *2+ "," + b.h);
              points.push("0," + b.h);
            	}else{
            		points.push("0,0");
            		points.push(b.w + ",0");
              points.push(b.w + b.t + "," + (b.h / 2));
              points.push(b.w + "," + b.h);
              points.push("0," + b.h);
            	}

              if (i > 0) {
                points.push(b.t + "," + (b.h / 2));
              }
              return points.join(" ");
            }


            function updateBreadcrumbs(nodeArray, percentageString) {


              var g = d3.select("#trail")
                  .selectAll("g")
                  .data(nodeArray, function(d) { return d.name + d.depth; });


              var entering = g.enter().append("svg:g");

              entering.append("svg:polygon")
                  .attr("points", breadcrumbPoints)
                  .style("fill", function(d,i) { return colors[d.depth]; });

              entering.append("svg:text")
                  .attr("x", function(d,i){if(i==0){return b.w + b.t}else{return (b.w + b.t)/2}})
                  .attr("y", b.h / 2)
                  .attr("dy", "0.35em")
                  .attr("text-anchor", "middle")
                  .text(function(d) { return  d.name; });


              g.attr("transform", function(d, i) {
              	if(i==1){return "translate(" + i * (b.w + b.s)*2 + ", 0)";}
              	else{return "translate(" + i * (b.w + b.s) + ", 0)";}

              });


              g.exit().remove();


              d3.select("#trail").select("#endlabel")
                  .attr("x", (nodeArray.length + 0.5) * (b.w + b.s))
                  .attr("y", b.h / 2)
                  .attr("dy", "0.35em")
                  .attr("text-anchor", "middle")
                  .text(percentageString);


              d3.select("#trail")
                  .style("visibility", "");

            }












            })





          //console.log(this.$store.state.dataurls);
        }
      },
      },
    mounted(){

    }
  }
</script>
