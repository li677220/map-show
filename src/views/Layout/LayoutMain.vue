<template>
  <div class="main-wrap">
    <el-carousel
      :autoplay="false"
      type="card"
      height="506px"
    >
      <el-carousel-item class="ca-item">
        <barcpm></barcpm>
      </el-carousel-item>
      <el-carousel-item class="ca-item">
        <linecpm></linecpm>
      </el-carousel-item>
      <el-carousel-item class="ca-item">
        <pie3cpm></pie3cpm>
      </el-carousel-item>
      <el-carousel-item class="ca-item">
        <piecpm></piecpm>
      </el-carousel-item>
      <el-carousel-item class="ca-item">
        <pie2cpm></pie2cpm>
      </el-carousel-item>
    </el-carousel>
    <br><br>
    <primap></primap>
  </div>
</template>
<script>
import linecpm from "@c/linecpm"
import piecpm from "@c/piecpm"
import barcpm from "@c/barcpm"
import primap from "@c/map"
import pie2cpm from "@c/pie2cpm"
import pie3cpm from "@c/pie3cpm"
export default {
  components: { linecpm, piecpm, pie2cpm, barcpm, primap, pie3cpm }
}
</script>
<style lang="scss" scoped>
.main-wrap {
  max-width: 1206px;
  margin: auto;
  margin-left: 235px;
}
.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #d3dce6;
}
.ca-item {
  width: 900px;
  // transform: translateX(-100px);
  left: -150px;
  border-radius: 8px;
}
</style>