<template>
  <div id="chart">

  </div>
</template>

<script>
  import axios from 'axios';
  import $ from 'jquery'
  import {mapGetters} from 'vuex'
  import * as d3 from 'd3v4'

  //  import  d3sankey from '../assets/sankey.js'

  export default {
    name: 'chart',

      mounted() {


      }
    }

  ;
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #main_div {
    height: 100%;
    width: 100%;
  }
</style>
