import { GetData,GetSecData } from "@api/getdata"
export default {
  namespaced: true,
  state: {
    data: [
      { value: 30, name: "初始数据1" },
      { value: 20, name: "初始数据2" },
      { value: 10, name: "初始数据3" },
      { value: 25, name: "初始数据4" },
      { value: 15, name: "初始数据5" },
    ],
    globalObj: {
      location: "",
      position: ""
    },
    secObj: {
      position: "",
      attr:""
    }
  },
  mutations: {
    changObj (state,obj) {
      state.globalObj.position = obj.value
      // console.log(state.globalObj);
    },
    updatePosdata (state,obj) {
      state.data = obj.data.datalist
      // console.log(obj);
    },
    updateSecObj (state,obj) {
      state.secObj = obj
      console.log(state.secObj);
    }
  },
  
  getters: {
    
  },
  actions: {
    changdata (context) {
      GetData(context.state.globalObj).then(res => {
        context.commit("updatePosdata",res)
        // state.posdata.data = res.data
      }).catch(err => {
        console.log("请求超时，请稍后再试");
        // this.$message({
        //   showClose: true,
        //   message: '请求超时，请稍后再试',
        //   type: 'error'
        // })
      })
      // console.log(context);
    },
    changSecData (context,obj) {
      GetSecData(obj).then(res => {
        context.commit("updatePosdata",res)
      }).catch(err => {
        console.log("请求超时，请稍后再试");
        // this.$message({
        //   showClose: true,
        //   message: '请求超时，请稍后再试',
        //   type: 'error'
        // })
      })
    }
  }
}