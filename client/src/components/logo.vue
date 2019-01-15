<template>
	<div id="logo"></div>
</template>

<script>
	export default{
		name:"logo",
		mounted(){
		var nodesColor=["#388712","#60DD49","#FCE639","#FFA91A","#FF3030"];   //绿到红
      var nodetext=["威胁等级低","威胁等级较低","威胁等级中等","威胁等级较高","威胁等级高"];
		
		var svg=d3.select("#logo")
		.append("svg")
		.attr("width",$("#logo").width())
		.attr("height",$("#logo").height());
		
		//var xscale()
      //色块等级说明
        var colorsexplain=svg.append("g").selectAll(".explain")
          .data(nodesColor)
          .enter()
          .append("g")
          .attr("class","explain")

      colorsexplain.append("rect")
        .attr("x","10%")
        .attr("y",function (d){
          for (var i=0;i<nodesColor.length;i++)
          if(nodesColor[i]==d)
          {
            return (i+2)*46
          }
        })
        .attr("height",20)
        .attr("width",20)
        .style("fill",function (d) {return d})
        .style("filter", "url(#drop-shadow)") //添加阴影
	console.log(colorsexplain);
	
      colorsexplain.append("text")
        .data(nodetext)
        .attr("x","25%")
        .attr("y",function (d) {
          for(var i=0;i<nodetext.length;i++)
          {
            if(nodetext[i]==d)
            {
              return (i+2)*48
            }
          }
        })
        .attr("dy", ".35em")
        .attr("text-anchor", "start")
         .text(function (d) { return d })
        .attr("fill","#fff")
        .style("filter", "url(#drop-shadow)");

		}
	}
</script>

<style>
</style>