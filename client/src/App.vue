<template>
  <div id="app">
    <div id="Inf_view1">
      <!--<ui ref="ui"></ui>-->
      <control></control>
    </div>
    <div id="main_view">
      <sankey></sankey>
    </div>
    <div id="Inf_view2">
    	<piechart></piechart>
    	<whois></whois>
    </div>
  </div>
</template>
<script>
import * as d3 from 'd3v4'
//import maindiv from './components/main'
import lineS from './components/line'
import Ping from './components/Ping'
import haddata from './components/haddata'
import ui from './components/GUI'
import sankey from './components/sankey'
import control from './components/control'
import piechart from './components/piechart'
import logo from './components/logo'
import whois from './components/whois'
export default {
  name: 'App',
  data() {
    return {
    }
  },
  components: {
    //  maindiv,
    ui,
    haddata,
    Ping,
    sankey,
    control,
    piechart,
    logo,
    whois
  },
  methods: {

    Inf_select(node) {
      console.log(node);
    },
    nodeselect(node) {
      //根据传入参数的node.seriesId不同调用不同的更新图表函数，并将参数传入实现图表连动

      if (node == "nodetype") {
        this.$refs.Ping.daga("run");
      } else if (node == "wtf") {
        this.$refs.haddata.qwe(this.$store.state.shuju, this.$store.state.ifcl)
      } else if (node == "wtfs") {
        this.$refs.Ping.daga("run");
      } else if (node == "folder_scan") {
        this.$refs.sunburst.change("folder_scan");
      }
    }
  },
  beforeCreate() {},
  created() {},
  beforeMount() {
    var that = this;

  },
  mounted() {}
}

</script>
<style>
html {

  height: 100%;
  width: 100%;
}

body {
  background-color: #020D1F;
  height: 100%;
  width: 100%;
}

* {

  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
}

#app {

  width: 100%;
  height: 100%;
}

#main_view {
  width: 62%;
  height: 100%;
  float: left;
}

#Inf_view2{
  width: 28%;
  height: 100%;
  float: left;
}

#Inf_view1{
	width: 10%;
	height: 100%;
  float: left;
}

#whois{
	height: 60%;
}
#piechart{
	width: 100%;
	height: 40%;
}
/*#sys_email{
  width: 100%;
  height: 100%;
}

.Double_view{
  width: 100%;
  height: 40%;
  border: 1px solid  #9A2EFE;
  border-left: none;
}*/

</style>
