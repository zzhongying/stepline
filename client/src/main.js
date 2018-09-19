// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import echarts from 'echarts'
import Vuex from 'vuex'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import './assets/global.css'

Vue.config.productionTip = false

Vue.use(Vuex)
Vue.use(ElementUI)

Vue.prototype.$echarts = echarts

let store = new Vuex.Store({
	strict:false,
	state:{//状态列表
		dataurls:"",
	  ifshan : false,
    ifcl :false,
		arr7:[],
		arr8:[],
		shuju:[],
		dir_data:[],

	},
	getters:{
		get_dataurls (state) {
			return state.dataurls
		},
		get_shuju (state) {
			return state.shuju
		},
		get_arr7 (state) {
			return state.arr7
		},
		get_arr8 (state) {
			return state.arr8
		},
		getifshan (state) {
			return state.ifshan
		},
		getifcl (state) {
			return state.ifcl
		},
		getdir_data (state) {
			return state.dir_data
		}
	},
	mutations:{//通过mutations可以改变状态，如store.commit(email_threatMutation)则会改变state.email_threat
		  dataurls_Mutation(state,aim){
		  state.dataurls = aim
		 },
	 	 shuju_Mutation(state,aim){
		  state.shuju = aim
		  },
		  arr7_Mutation(state,aim){
			state.arr7 = aim
	  	},
		   arr8_Mutation(state,aim){
			state.arr8 = aim
	   	},
			ifshanMutation(state,aim){
				state.ifshan = aim
			},
			ifclMutation(state,aim){
				state.ifcl = aim
			},
		dir_dataMutation(state,aim){
			state.dir_data = aim
		}
	},
	actions:{//Action 提交 mutation
		dataurls_Action(context,aim) {

			context.commit('dataurls_Mutation',aim)
		},
		shuju_Action(context,aim) {

			context.commit('shuju_Mutation',aim)
		},
		arr7_Action(context,aim) {

			context.commit('arr7_Mutation',aim)
		},
		arr8_Action(context,aim) {

			context.commit('arr8_Mutation',aim)
		},
		ifcl_Action(context,aim) {

			context.commit('ifclMutation',aim)
		},
		ifshan_Action(context,aim) {

			context.commit('ifshanMutation',aim)
		},
		dir_data_Action(context,aim) {

			context.commit('dir_dataMutation',aim)
		}
	}
})

Date.prototype.format = function(fmt) {
     var o = {
        "M+" : this.getMonth()+1,                 //月份
        "d+" : this.getDate(),                    //日
        "h+" : this.getHours(),                   //小时
        "m+" : this.getMinutes(),                 //分
        "s+" : this.getSeconds(),                 //秒
        "q+" : Math.floor((this.getMonth()+3)/3), //季度
        "S"  : this.getMilliseconds()             //毫秒
    };
    if(/(y+)/.test(fmt)) {
            fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
    }
     for(var k in o) {
        if(new RegExp("("+ k +")").test(fmt)){
             fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
         }
     }
    return fmt;
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
