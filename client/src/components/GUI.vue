<template>
  <div id="ui">
  </div>
</template>

<script>
import * as d3 from 'd3v4'
//import dat from '../assets/dat.gui.js'
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
      go_back(){
        var Options = function() {
  this.message = 'dat.gui';
  this.speed = 0.8;
  this.displayOutline = false;
  this.button = function() {};
};

window.onload = function() {
  var options = new Options();
  var gui = new dat.GUI();

  console.log(gui)
  var myGUI = document.getElementById('ui');
  myGUI.appendChild(gui.domElement);
 gui.width = 170;
  gui.add(options, 'message');
  gui.add(options, 'speed', -5, 5);
  gui.add(options, 'displayOutline');
  gui.add(options, 'button');
};

    },
  change(node){}
    },
    mounted(){
    this.go_back();
    }
  }
</script>


<style scoped>
#ui{
  float:center;
  width: 100%;
  height: 100%;
  padding: 0px;
}
</style>
