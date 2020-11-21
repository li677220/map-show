<template>
  <div class="side-wrap">
    <el-row class="tac">
      <el-col :span="24">
        <el-menu
          class="el-menu-vertical-demo"
          background-color="#fff"
          text-color="#000"
          active-text-color="#409eff"
        >
          <el-menu-item
            v-for="item in showData"
            :index="item.index"
            :key=item.value
            @click="updateDeg(item)"
          >
            <i :class="item.icon"></i>
            <span>{{item.name}}</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data () {
    return {
      showData: [{
        icon: "el-icon-reading",
        name: "学历要求",
        value: "JobDegree",
        index: "1"
      }, {
        icon: "el-icon-menu",
        name: "工作经验",
        value: "WorkExperience",
        index: "2"
      }, {
        icon: "el-icon-document",
        name: "企业类型",
        value: "CompanyType",
        index: "3"
      }, {
        icon: "el-icon-office-building",
        name: "企业规模",
        value: "CompanyScale",
        index: "4"
      }]
    }
  },
  methods: {
    updateDeg (obj) {
      if (this.$store.state.posdata.globalObj.position == "") {
        this.$alert('请先选择一个职业', '提示', {
          confirmButtonText: '确定',
          lockScroll: false
        }).then(() => {

        }).catch();
      } else {
        let reqObj = {
          position: this.$store.state.posdata.globalObj.position,
          attr: obj.value
        }
        this.$store.dispatch("posdata/changSecData", reqObj)
      }
    }
  }
}
</script>

<style>
.side-wrap {
  position: fixed;
  top: 65px;
  width: 150px;
  height: 100vh;
  background-color: #fff;
  z-index: 99;
}
.el-menu {
  border: none;
}
/* .el-menu li {
  padding-left: 30px !important;
} */
</style>