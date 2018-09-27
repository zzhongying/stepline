<template>
  <div id="haddata">
    </div>
</template>

<script>
  import axios from 'axios'
export default {
  name: 'haddata',
  data () {
    return {
      map:null
    }
},

methods:{
  qwe(shuju,ifcl){
  console.log(shuju)
  this.map(shuju,ifcl);
  }
  /*choose(nodetype){
    this.$emit('nodeselect',nodetype);
  }*/
},
beforeCreate(){
},
created(){
},
beforeMount(){
},
mounted(){
 // axios.get('http://127.0.0.1:5000/getMsg')
 //  .then(function (response) {
 //    console.log(response);
 //  })
 //  .catch(function (error) {
 //    console.log(error);
 //  });

var that=this;
function  getData() {
  var arr7= new Array();//用于记录替换的link位置
  var arr8= new Array();
   	function handlenodes(arrdata){//此函数统计出不同的节点，并返回
   		var arr5  = new Array();
   		arr5[0]={
   				  	name:arrdata[0]
   				  }
   		var ifdeng = false;
   		var x = 1
   		var xx = 0
   		  for (var i =0;i<arrdata.length-1;i++) {
   		  	if(arr5[xx].name!=arrdata[i+1]){
   			for(var j = 0;j<arr5.length;j++){
   				if(arrdata[i+1]==arr5[j].name)
   					ifdeng = true;
   				}
   			if(ifdeng ===false&&i+1<arrdata.length-1){
   				if(arrdata[i+1].indexOf("result")<0&&arrdata[i+1].indexOf("chinaVis")<0){
   					arr5[x]={
   				  	name:arrdata[i+1]
   				  }
   				    x++;
   				    xx++;
   				}
   			 }
   			}
   		  	ifdeng = false;

   		}

   		return arr5;
   	}
   	//该函数设置source和target
   function handlelinks(arrdata){
   	var arr2  = new Array();
   	var arr3  = new Array();
   	var i = 0;
   	var l = 0;
   	var a = 0;
   	var k =0;
   	while(i<arrdata.length)
   	{
   		if(arrdata[i].indexOf("result")<0&&arrdata[i+1].indexOf("chinaVis")>0){
   			arr2[l++]=i;
   		}
   		i++;
   	}


   	//桑基图source和target赋值
   	for(var i = 0;i<arrdata.length;i++){
   		for (var j = 0;j<arr2.length;j++) {
   			if(arr2[j]==i){
   				var obj = {
   		              source:[],
   		              target:[],
   		              dataname:[],
   		              urls:arrdata[i+1],
   		              value:"2"
   	                }

   					if(j+1!=arr2.length){
   						if(arrdata[i+1]!=arrdata[arr2[j+1]+1]){

   							obj.source=arrdata[i]
   				            obj.target=arrdata[arr2[j+1]]
   				            arr3[a]=obj
   				            a++;
   						}else{
   							var asda = i-3*k-3;
   							//obj.source=arrdata[i]

   							 obj.source=arrdata[asda]
                 obj.target=arrdata[arr2[j+1]]
                 arr3[a]=obj
                 a++;
                 k++;
   						}

   				}

   			}
   			if(arr2[j]<i&&i<arr2[j+2]){
   				arr3[a-1].dataname.push(arrdata[i])

   			}
   			if(arr2[arr2.length-1]<i&&j==0&&arrdata[i].indexOf("result")>0){
   				arr3[a-1].dataname.push(arrdata[i])

   			}
   		}

   	}

   	return arr3;


   }
   function handlelink2(shujudata1,ifcl){


    /*存在一种情况，如一条路径A的末尾节点名称functionX的时候，
     * 若有其他路径B中也存在节点名称functionX的非末尾节点，
     * 此时把这个节点作为末尾节点的路径A没有完结反而会连接到路径B上.
     * 下面代码用于处理此类问题
     * */
   var arr6 = new Array();
   var arr9 = new Array();
   var j =0;
   var q = 0;
   var w = 0
   var g= 0
   if(ifcl==false){
    for (var i = 0;i<shujudata1.links.length;i++) {
    //统计出所有不同的末节点,以及相关的位置并存储在arr6中
    if(i+1<shujudata1.links.length&&shujudata1.links[i+1]!=undefined){
      if(shujudata1.links[i+1].source.indexOf("path")>=0){
      arr6[q]={
          a:shujudata1.links[i].target,
          b:i
        }
      q++;
    }
    }
    if(i+1===shujudata1.links.length){
        arr6[q]={
          a:shujudata1.links[i].target,
          b:i
        }
        q++;
      }
   }

   for (var i = 0;i<shujudata1.links.length;i++) {
    for (var j = 0;j<arr6.length;j++) {
      if(arr6[j].a==shujudata1.links[i].source){//当某个末端节点与某个节点的source相等，则改末端节点为问题节点，对他进行重命名。

        arr7[g]=arr6[j].b;
        arr8[g]=i-1;
        g++;
        shujudata1.links[arr6[j].b].target=shujudata1.links[arr6[j].b].target+w.toString();//如果存在问题节点，将节点重命名
        shujudata1.nodes[shujudata1.nodes.length]={//将重命名节点添加进节点数组
          name:shujudata1.links[arr6[j].b].target
        }
        w++;
      }
    }

   }
   }
   else{
    for (var i = 0;i<shujudata1.links.length;i++) {

    if(i+1<shujudata1.links.length-1&&shujudata1.links[i+1].name!=undefined){
      if(shujudata1.links[i+1].source.name.indexOf("path")>=0){
      arr6[q]={
          a:shujudata1.links[i].target,
          b:i
        }
      q++;
    }
    }
    if(i===shujudata1.links.length-1){
        arr6[q]={
          a:shujudata1.links[i].target,
          b:i
        }
        q++;
      }
   }
   for (var i = 0;i<shujudata1.links.length;i++) {
    for (var j = 0;j<arr6.length;j++) {
      if(arr6[j].a==shujudata1.links[i].source.name){

        arr7[g]=arr6[j].b;
        arr8[g]=i-1;
        g++;
        shujudata1.links[arr6[j].b].target=shujudata1.links[arr6[j].b].target+w.toString();
        shujudata1.nodes[shujudata1.nodes.length]={
          name:shujudata1.links[arr6[j].b].target
        }
        w++;
      }
    }
   }
   }

   //  that.$store.dispatch('arr7_Action',arr7);
   //that.$store.dispatch('arr8_Action',arr8);
   that.$store.state.dir_data=shujudata1,
   that.$emit('nodeselect','nodetype');
   //that.choose("params")
   //creatChart(shujudata1,arr7,arr8);

   }
   that.map = function (shujudata1,ifcl){


   	/*存在一种情况，如一条路径A的末尾节点名称functionX的时候，
   	 * 若有其他路径B中也存在节点名称functionX的非末尾节点，
   	 * 此时把这个节点作为末尾节点的路径A没有完结反而会连接到路径B上.
   	 * 下面代码用于处理此类问题
   	 * */
 var arr6 = new Array();
  var arr9 = new Array();
  var j =0;
   var q = 0;
   var w = 0
   var g= 0
   if(ifcl==false){
   	for (var i = 0;i<shujudata1.links.length;i++) {
  	//统计出所有不同的末节点,以及相关的位置并存储在arr6中
  	if(i+1<shujudata1.links.length&&shujudata1.links[i+1]!=undefined){
  		if(shujudata1.links[i+1].source.indexOf("path")>=0){
  		arr6[q]={
  				a:shujudata1.links[i].target,
  				b:i
  			}
  		q++;
  	}
  	}
  	if(i+1===shujudata1.links.length){
  			arr6[q]={
  				a:shujudata1.links[i].target,
  				b:i
  			}
  			q++;
  		}
  }

  for (var i = 0;i<shujudata1.links.length;i++) {
  	for (var j = 0;j<arr6.length;j++) {
  		if(arr6[j].a==shujudata1.links[i].source){//当某个末端节点与某个节点的source相等，则改末端节点为问题节点，对他进行重命名。
  			console.log(i)
  			arr7[g]=arr6[j].b;
  			arr8[g]=i-1;
  			g++;
  			shujudata1.links[arr6[j].b].target=shujudata1.links[arr6[j].b].target+w.toString();//如果存在问题节点，将节点重命名
  			shujudata1.nodes[shujudata1.nodes.length]={//将重命名节点添加进节点数组
  				name:shujudata1.links[arr6[j].b].target
  			}
  			w++;
  		}
  	}

  }

   }
   else{
   	for (var i = 0;i<shujudata1.links.length;i++) {

  	if(i+1<shujudata1.links.length-1&&shujudata1.links[i+1].name!=undefined){
  		if(shujudata1.links[i+1].source.name.indexOf("path")>=0){
  		arr6[q]={
  				a:shujudata1.links[i].target,
  				b:i
  			}
  		q++;
  	}
  	}
  	if(i===shujudata1.links.length-1){
  			arr6[q]={
  				a:shujudata1.links[i].target,
  				b:i
  			}
  			q++;
  		}
  }
  for (var i = 0;i<shujudata1.links.length;i++) {
  	for (var j = 0;j<arr6.length;j++) {
  		if(arr6[j].a==shujudata1.links[i].source.name){
  			console.log(arr6[j].b)
  			arr7[g]=arr6[j].b;
  			arr8[g]=i-1;
  			g++;
  			shujudata1.links[arr6[j].b].target=shujudata1.links[arr6[j].b].target+w.toString();
  			shujudata1.nodes[shujudata1.nodes.length]={
  				name:shujudata1.links[arr6[j].b].target
  			}
  			w++;
  		}
  	}
  }
   }


  that.$store.state.dir_data=shujudata1,
  console.log(that.$store.state.dir_data);
  that.$emit('nodeselect','wtfs');

  //creatChart(shujudata1,arr7,arr8);*/

   }
    // 对应 Python 提供的接口，这里的地址填写下面服务器运行的地址，
    const path = 'http://127.0.0.1:5000/getMsg';
    axios.get(path,{params:{urls:"E:\\chinaVis\\stepline\\client\\static\\dir"}}).then(res=>{

        var datato = res.data.split("\n");//按行分割字符串
        console.log(datato);
         	var arr  = new Array(),
         	      j = 0,
         	      k = 1;
         	      for(var i = 0;i<datato.length;i++){
         	      	if(datato[i].indexOf("path")===0){
         	      		datato[i]=datato[i].split("S")[0]
         	      	}
         	      }
         	for(var i = 0;i<datato.length-1;i++){//根据path的不同，将每条path分在数组里
         		if(datato[i].indexOf("path")===0){
         			arr[j] = new Array();
         			arr[j][0] = datato[i];
         			k = 1;
         			j++;
         		}else{
         			arr[j-1][k] = datato[i];
         			k++;
         		}
         	}
          console.log(arr)
         	var shujudata = {
         		links:[],
         		nodes:handlenodes(datato)//调用handlenodes，将所有不同的节点名称保存起来
         	}
            console.log(shujudata)
         for(var i = 0;i<arr.length;i++){
         		var X = handlelinks(arr[i])
         		for(var j = 0;j<X.length;j++){
         			shujudata.links.push(X[j])
         		}
         	}

         handlelink2(shujudata,that.$store.state.ifcl);

    }).catch(function (error) {
      alert('Error ' + error);
    })
      // 这里服务器返回的 response 为一个 json object，可通过如下方法需要转成 json 字符串
      // 可以直接通过 response.data 取key-value
      // 坑一：这里不能直接使用 this 指针，不然找不到对象

      // 坑二：这里直接按类型解析，若再通过 JSON.stringify(msg) 转，会得到带双引号的字串

  }
getData()


}
}
</script>
<style scoped>
#haddata{
  width: 100%;
  height: 30%;
}
</style>
