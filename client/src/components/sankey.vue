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
    export default {
        name: "sankey",

       mounted() {
         axios.get('http://127.0.0.1:5000/getMsg')
           .then(function (response) {
             console.log(response);
           })
           .catch(function (error) {
             console.log(error);
           });
       }
    }
</script>

<style scoped>

</style>
