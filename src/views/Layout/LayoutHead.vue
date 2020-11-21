<template>
  <div class="head-wrap">
    <el-menu
      class="el-menu-demo"
      mode="horizontal"
    >
      <el-menu-item index="2">
        <el-select
          v-model="value"
          placeholder="请选择职业"
          @change="active"
        >
          <el-option
            v-for="item in positions"
            :key="item.value"
            :label="item.label"
            :value="item.value"
          >
          </el-option>
        </el-select>
      </el-menu-item>
      <el-menu-item class="menu-item3">
        <el-button
          type="primary"
          size="medium"
          plain
          @click="getData"
          :disabled="value==''"
        >查询</el-button>

        <el-button
          type="danger"
          size="medium"
          class="pull-right"
          plain
        >退出</el-button>

      </el-menu-item>
      <el-menu-item>
        <div
          plain
          class="pull-right tips el-icon-message-solid"
          @click="open"
        >

        </div>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script>
import { GetData } from "@api/getdata"
export default {
  data () {
    return {
      positions: [{
        value: 'alldata',
        label: '全部'
      }, {
        value: 'java',
        label: 'java'
      }, {
        value: 'c',
        label: 'c'
      }, {
        value: 'python',
        label: 'python'
      }, {
        value: 'golang',
        label: 'golang'
      }, {
        value: 'qianduan',
        label: '前端'
      }, {
        value: 'safe',
        label: '网络安全'
      }, {
        value: 'datas',
        label: '数据库'
      }, {
        value: 'jiagou',
        label: '架构'
      }, {
        value: 'test',
        label: '测试'
      }],
      value: ''
    };
  },
  methods: {
    getData () {
      this.$store.dispatch("posdata/changdata")
    },
    open () {
      const h = this.$createElement;

      this.$notify({
        title: '提示信息',
        message: h('b', { style: 'color: teal' }, '此项目所用数据均为智联公开招聘数据，不涉及任何个人用户隐私数据，此项目仅供个人学习使用，非商用!!!   后续将会推出其他行业、行业对比以及时间维度的详细信息，请持续关注')
      });
    },
    active (value) {
      let obj = {};
      obj = this.positions.find((item) => {//这里的selectList就是上面遍历的数据源
        return item.value === value;//筛选出匹配数据
      });
      this.$store.commit("posdata/changObj", obj)
      // console.log(this.$store.state.posdata);
    }
  }
}
</script>

<style lang="scss" scoped>
.head-wrap {
  width: 100%;
  height: 65px;
  position: fixed;
  z-index: 99;
  background-color: #fff;
}
.el-menu-demo {
  max-width: 1206px;
  margin: auto;
  display: flex;
  justify-content: space-around;
}
.el-menu-item {
  margin-top: 1px;
  height: 63px;
  border: none;
}
.menu-item3 {
  flex-grow: 1;
}
.menu-item3 :last-child {
  margin-top: 10px;
}
.el-icon-document :hover {
  color: #409eff;
}
.tips {
  width: 20px;
  height: 20px;
  color: #fff;
  border: solid 1px #409eff;
  background-color: #b3d8ff;
  display: inline-block;
  border-radius: 50%;
  margin-top: 20px;
  font-size: 20px;
}
.tips:hover {
  color: #409eff;
  background-color: #fff;
}
.el-menu.el-menu--horizontal,
.el-menu--horizontal > .el-menu-item.is-active {
  border: none;
}
</style>