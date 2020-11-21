<template>
  <div class="foot-wrap">
    <div class="foot-main">
      <div>
        <el-tooltip
          class="item"
          effect="dark"
          content="版权所有，请勿转载"
          placement="top"
        >
          <span>版权信息</span>
        </el-tooltip>
      </div>
      <div>
        <span>友情链接</span>
      </div>
      <div>
        <span>源码地址</span>
      </div>
      <div>
        <el-tooltip
          class="item"
          effect="dark"
          content="如果本页面涉及到您的隐私问题，请联系作者删除"
          placement="top"
        >
          <span>用户须知</span>
        </el-tooltip>
      </div>
      <div>
        <el-tooltip
          class="item"
          effect="dark"
          content="X审政字：1354678x65"
          placement="top"
        >
          <span>备案信息</span>
        </el-tooltip>
      </div>
      <div>
        <el-tooltip
          class="item"
          effect="dark"
          content="如您想了解其他行业信息或者提出建议，请联系作者"
          placement="top"
        >
          <span>提出建议</span>
        </el-tooltip>
      </div>
      <div>
        <el-tooltip
          class="item"
          effect="dark"
          content="请尽量使用谷歌浏览器访问此界面"
          placement="top"
        >
          <span>注意事项</span>
        </el-tooltip>
      </div>
      <div>
        <el-tooltip
          class="item"
          effect="dark"
          content="先选择您感兴趣的行业，然后查看各项对比数据"
          placement="top"
        >
          <span>使用说明</span>
        </el-tooltip>
      </div>
      <div class="qrwrap">
        <span class="qrspan">联系作者</span>
        <div class="qrcode">
          <img
            src="@static/img/wechat.jpg"
            alt=""
          >
          <b>添加微信</b>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {

}
</script>

<style lang="scss" scoped>
.foot-wrap {
  width: 100%;
  height: 30px;
  line-height: 30px;
  font-size: 12px;
  color: gray;
  background-color: #fff;
  .foot-main {
    width: 1206px;
    height: 100%;
    margin-left: 235px;
    // border: 1px black solid;
    div {
      float: left;
      margin: 0 10px;
      span {
        cursor: pointer;
      }
    }
  }
}
span:hover {
  color: #409eff;
}
.qrwrap {
  position: relative;
}
.qrcode {
  width: 100px;
  height: 0px;
  position: absolute;
  text-align: center;
  overflow: hidden;
  top: -120px;
  left: -37px;
  display: none;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
  background-color: #fff;
  transition: height 0.3s;
  color: #000;
  font-size: 10px;
  img {
    margin: 10% 10% 0;
    display: block;
    width: 80%;
  }
}
.qrwrap:hover .qrcode {
  display: block;
  height: 120px;
}
</style>