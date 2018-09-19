<template>
  <div id="check_div">
    </div>
</template>

<script>
import * as d3 from 'd3v4'
  export default {
    data() {
      return {
        ifdetail:false,
        d:[],
        option:{},
        myChart:{},
        daydata:[]
      }
    },
    computed:{
    },
    methods:{
     change(node){
/*      if(department=='department1'){
        this.CreatChart(this.getDa2(),4)
        this.option.title.text=department;
        this.myChart.setOption(this.option)
      }else  if(department=='department2'){
        this.CreatChart(this.getDa2(),3);
        this.option.title.text=department;
        this.myChart.setOption(this.option)
      } else  if(department=='department3'){
        this.CreatChart(this.getDa2(),2);
        this.option.title.text=department;
        this.myChart.setOption(this.option);
      } else  if(department=='Hr'){
        this.CreatChart(this.getDa2(),0);
        this.option.title.text=department;
        this.myChart.setOption(this.option);
      } else {
        this.CreatChart(this.getDa2(),1);
        this.option.title.text=department;
        this.myChart.setOption(this.option);
      }*/
      },
      getDa2(){
        let that=this;
        let Hr =[];
        let finance = [];
        let development3 = [];
        let development2 = []
        let development1 =[];
        let str = "2017/11/"
        let xaxis=[];

        for(let i = 0;i<30;i++){//一个月每天


          Hr[i]=[0];
          finance[i]=[,0];
          development3[i]=[0];
          development2[i]=[0];
          development1[i]=[0];
        }
        for(let i = 0;i<that.d.length;i++){

          let ds = (new Date(that.d[i].time)).getDate()-1
         if(that.d[i].type=='HR'){

            Hr[ds][0]=parseInt(that.d[i].record);
           Hr[ds][1]=parseInt(that.d[i].record)-18;

          } else if(that.d[i].type=='finance'){

            finance[ds][0]=that.d[i].record;
           finance[ds][1]=parseInt(that.d[i].record)-24;
          }
           else if(that.d[i].type=='development3'){

            development3[ds][0]=that.d[i].record;
            development3[ds][1]=parseInt(that.d[i].record)-88;
          }else if(that.d[i].type=='development2'){

            development2[ds][0]=that.d[i].record;
           development2[ds][1]=parseInt(that.d[i].record)-62;
           }else if(that.d[i].type=='development1'){

            development1[ds][0]=that.d[i].record;
           development1[ds][1]=parseInt(that.d[i].record)-106;
           }
        }
        let data2s =[]
        data2s[0]=Hr;
        data2s[1]=finance;
        data2s[2]=development3;
        data2s[3]=development2;
        data2s[4]=development1;
        data2s[5]=xaxis;

        return data2s;
      },
      getDa1(day){
        let that=this;
        return that.daydata[day];
      },
      CreatChart(datass,n){
        let xAxisData = [];
        let data1 = [];
        let data2 = [];
        // var data3 = [];
        // var data4 = [];

        let that=this;
        for (let i = 0; i < 30; i++) {
          xAxisData.push('day' + i);
          data1.push( datass[n][i][0]);
          data2.push( datass[n][i][1]);
          // data3.push((Math.random() * 5).toFixed(2));
          // data4.push((Math.random() + 0.3).toFixed(2));
        }


        var itemStyle = {
          normal: {
          },
          emphasis: {
            barBorderWidth: 1,
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowOffsetY: 0,
            shadowColor: 'rgba(0,0,0,0.5)'
          }
        };

        that.option = {
          title: {
            text: '各部门出勤',
            top:"2%",
            left:"2%",
            textStyle:{
              color: '#ccc'
            },
          },
          textStyle:{
            color:"white"
          },


         /* brush: {
            toolbox: ['rect', 'polygon', 'lineX', 'lineY', 'keep', 'clear'],
            xAxisIndex: 0
          },*/
          toolbox: {
           left:'center',
            show: true,
            itemSize:20,
            feature:
              { mark:
                {
                  show: true
                },
                magicType:
                  {
                    show: true
                  },
                myTool1:
                  {
                    show: true,
                    title: 'finance',
                    icon: 'path://M617.8,264.8L719,126.3c4.6-6.3,5-14.3,1.1-21c-3.9-6.6-11.4-10.8-19.6-10.8h-126l-58.7-75.9c-4.2-5.4-11-9.2-18.3-8.6c-7.3,0-14.1,3.3-18.2,8.9l-56.7,75.6h-123c-8.3,0-15.9,4.3-19.8,11c-3.8,6.8-3.2,14.9,1.6,21.2L384,260.3C206.6,290.4,54.5,460,54.5,624.5v37.1C54.5,843,216.6,990,416.5,990h167c199.9,0,361.9-147,361.9-328.4v-37.1C945.5,467.2,789.6,305.1,617.8,264.8z M342.5,135.3h91.8c7.3,0,14.2-3.3,18.4-8.8l45.3-60.4l46.9,60.6c4.2,5.4,10.9,8.6,18.2,8.6h95.8L570,256.9c-10.6-1-21.2-1.8-31.7-1.8h-99.2c-1.5,0-2.9,0.2-4.4,0.2L342.5,135.3z M900.9,661.6c0,158.6-142.4,287.6-317.4,287.6h-167c-175,0-317.4-129-317.4-287.6v-37.1c0-162.8,171.6-328.6,340-328.6h99.2c176.2,0,362.6,168.9,362.6,328.6V661.6z M672.7,603.4c12.2,0,22.1-9,22.1-20c0-11-9.9-20-22.1-20h-91.5l66.8-108.4c5.9-9.7,2.1-21.9-8.6-27.2c-10.7-5.4-24.2-1.9-30.1,7.8l-78.8,127.9h-28.2l-78.8-127.9c-5.9-9.7-19.5-13.1-30.1-7.8c-10.7,5.4-14.5,17.6-8.6,27.2l66.8,108.4h-96.7c-12.2,0-22.1,9-22.1,20s9.9,20,22.1,20h136.7v78.7H355.1c-12.2,0-22.1,9-22.1,20s9.9,20,22.1,20h136.7v93c0,11,9.9,20,22.1,20c12.2,0,22.1-9,22.1-20v-93h136.7c12.2,0,22.1-9,22.1-20c0-11-9.9-20-22.1-20H536v-78.7H672.7z',
                    onclick: function() {
                      that.CreatChart(that.getDa2(),1)
                      that.option.title.text='finance'
                      that.myChart.setOption(that.option)
                    }

                  },
                myTool2:
                {
                  show: true,
                 title: 'department1',
                  icon: 'path://M688.9,106.7L688.9,106.7L688.9,106.7L688.9,106.7L688.9,106.7z M457.3,638.6h85.2c131.7,0,238.5-77.4,238.5-172.8V181.9c0-95.4-106.8-172.8-238.5-172.8h-85.2c-131.7,0-238.5,77.4-238.5,172.8v283.9C218.8,561.2,325.5,638.6,457.3,638.6z M786.8,547.3c-7.1,22.5-31.3,50.2-47.2,55.8c115.8,65.5,179.7,173.6,183.1,308.4c0.1,2.6,0,5.2-0.1,7.7H80.8c-0.1-2.6-0.1-5.1-0.1-7.7c0-131.6,82.3-247.3,179.9-309.4c-16.6-7.8-39.1-31.8-44.2-53.2C81.3,628.1,10,759.1,10,916c0,24.5,2.2,50.9,6.4,74.3h31.3v0.6l936.3-2.2V986c4-22.8,6.1-46.2,6.1-70.1C990,754.3,929,625.1,786.8,547.3z M711.7,412.1c5.2,94.9-73.5,157.7-164.2,157.7h-92.3c-90.7,0-175.8-70.1-165.4-157.7v-175c-9.4-106.8,74.7-157.7,165.4-157.7h92.3c90.7,0,167.2,47.5,164.2,157.7V412.1z',
                  onclick: function() {
                    that.CreatChart(that.getDa2(),2)
                    that.option.title.text='department1'
                    that.myChart.setOption(that.option)
                  }

                },
                myTool3:
                  {
                    show: true,
                    title: 'department2',
                    icon: 'path://M688.9,106.7L688.9,106.7L688.9,106.7L688.9,106.7L688.9,106.7z M457.3,638.6h85.2c131.7,0,238.5-77.4,238.5-172.8V181.9c0-95.4-106.8-172.8-238.5-172.8h-85.2c-131.7,0-238.5,77.4-238.5,172.8v283.9C218.8,561.2,325.5,638.6,457.3,638.6z M786.8,547.3c-7.1,22.5-31.3,50.2-47.2,55.8c115.8,65.5,179.7,173.6,183.1,308.4c0.1,2.6,0,5.2-0.1,7.7H80.8c-0.1-2.6-0.1-5.1-0.1-7.7c0-131.6,82.3-247.3,179.9-309.4c-16.6-7.8-39.1-31.8-44.2-53.2C81.3,628.1,10,759.1,10,916c0,24.5,2.2,50.9,6.4,74.3h31.3v0.6l936.3-2.2V986c4-22.8,6.1-46.2,6.1-70.1C990,754.3,929,625.1,786.8,547.3z M711.7,412.1c5.2,94.9-73.5,157.7-164.2,157.7h-92.3c-90.7,0-175.8-70.1-165.4-157.7v-175c-9.4-106.8,74.7-157.7,165.4-157.7h92.3c90.7,0,167.2,47.5,164.2,157.7V412.1z',
                    onclick: function() {
                      that.CreatChart(that.getDa2(),3)
                      that.option.title.text='department2'
                      that.myChart.setOption(that.option)
                    }

                  },
                myTool4:
                  {
                    show: true,
                    title: 'department3',
                    icon: 'path://M688.9,106.7L688.9,106.7L688.9,106.7L688.9,106.7L688.9,106.7z M457.3,638.6h85.2c131.7,0,238.5-77.4,238.5-172.8V181.9c0-95.4-106.8-172.8-238.5-172.8h-85.2c-131.7,0-238.5,77.4-238.5,172.8v283.9C218.8,561.2,325.5,638.6,457.3,638.6z M786.8,547.3c-7.1,22.5-31.3,50.2-47.2,55.8c115.8,65.5,179.7,173.6,183.1,308.4c0.1,2.6,0,5.2-0.1,7.7H80.8c-0.1-2.6-0.1-5.1-0.1-7.7c0-131.6,82.3-247.3,179.9-309.4c-16.6-7.8-39.1-31.8-44.2-53.2C81.3,628.1,10,759.1,10,916c0,24.5,2.2,50.9,6.4,74.3h31.3v0.6l936.3-2.2V986c4-22.8,6.1-46.2,6.1-70.1C990,754.3,929,625.1,786.8,547.3z M711.7,412.1c5.2,94.9-73.5,157.7-164.2,157.7h-92.3c-90.7,0-175.8-70.1-165.4-157.7v-175c-9.4-106.8,74.7-157.7,165.4-157.7h92.3c90.7,0,167.2,47.5,164.2,157.7V412.1z',
                    onclick: function() {
                      that.CreatChart(that.getDa2(),4)
                      that.option.title.text='department3'
                      that.myChart.setOption(that.option)
                    }

                  },
                myTool5:
                  {
                    show: true,
                    title: 'Hr',
                    icon: 'path://M489.3,3.2C331.5,3.2,203.5,161,203.5,355.7c0,120.8,49.2,227.3,124.3,290.9c18.4,15.6,38.4,28.6,59.6,38.6c31.7,14.9,66,23.1,102,23.1c36.1,0,70.5-8.2,102.3-23.3c17.3-8.2,33.8-18.4,49.3-30.3c80.6-62.3,134.3-172.9,134.3-299C775.2,161,647.2,3.2,489.3,3.2L489.3,3.2L489.3,3.2z"/><path d="M427.4,700l-73.5-33.7l-67.4,27.3L91.3,772.7C45.7,789,10,839.9,10,888.4v23c0,53,43,85.4,95.9,85.4h327.4h112.2h348.7c52.9,0,95.9-32.4,95.9-85.4v-23c0-48.5-35.7-99.4-81.3-115.8l-216.5-79.1l-65.7-28.4l0,0l-69,33',
                    onclick: function() {
                      that.CreatChart(that.getDa2(),0)
                      that.option.title.text='Hr'
                      that.myChart.setOption(that.option)
                    }

                  }
              }
          },
          tooltip: {},
          xAxis: {
            data: xAxisData,
            name: 'X Axis',
            silent: false,
            axisLine: {onZero: true},
            splitLine: {show: false},
            splitArea: {show: false}
          },
          yAxis: {
            inverse: true,
            type: 'value',
            scale:false,
            minInterval: 1,
            splitArea: {show: false}
          },
          grid: {
            top: "20%",
            right:"10%",
            left:"10%",
            bottom:"18%"
          },
          series: [
                {
                  name: 'Hr',
                  show:true,
                  type: 'bar',
                  stack: 'one',
                  itemStyle: itemStyle,
                  data:data1
                },
                {

                  name: 'finance',
                  type: 'bar',
                  stack: 'one',
                  show:false,
                  itemStyle: itemStyle,
                  data: data2
                }


           /*{

              name: 'development3',
              type: 'bar',
              show:false,
              stack: 'one',
              itemStyle: itemStyle,
              data:data1
            },
            {

              name: 'development2',
              show:false,
              type: 'bar',
              stack: 'one',
              itemStyle: itemStyle,
              data: data2
            }, {

              name: 'development1',
              show:false,
              type: 'bar',
              stack: 'one',
              itemStyle: itemStyle,
              data:data1
            }*/
          ]
        };

      }
    },
    mounted(){
     /* d3.json("../../static/filter/sys_email.json",function(da){
        that.daydata=da.data
      });*/


      let that=this;
      function Getdata()
      {
        let p=new Promise( (resolve, reject)=>{
          d3.csv("../../static/check.csv",function(da){
            that.d=da;
            resolve();
          });
        })

        return p;
      }
      function draw()
      {
        let p=new Promise( (resolve, reject)=>{

          that.ifdetail = false;

          let dom = document.getElementById("check_div");
          that.myChart = that.$echarts.init(dom);

          let app = {};
          that.getDa2()
          that.CreatChart(that.getDa2(),0)

          that.myChart.setOption(that.option)
          window.onresize =  that.myChart.resize;

          /*that.myChart.on('click', function (params) {
            if( that.ifdetail==false){
              that.CreatChart(that.getDa1(params.dataIndex+1));
              that.ifdetail=true;
              that.myChart.setOption(that.option)
            }
          })*/
          resolve()
        })

        return p;
      }
      Getdata().then(draw)
    }
  }
</script>


<style scoped>
#check_div{
  width: 100%;
  height: 30%;
}
</style>
