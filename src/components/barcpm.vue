<template>
  <div class="analyzeSystem">
    <div
      :class="className"
      :id="id"
      :style="{height,width}"
      ref="myEchart"
    ></div>
  </div>
</template>

<script>
import echarts from '@/lib/util/echarts.js'
export default {
  // name: "analyzeSystem",
  props: {
    className: {
      type: String,
      default: "yourClassName"
    },
    id: {
      type: String,
      default: "yourID"
    },
    width: {
      type: String,
      default: "900px"
    },
    height: {
      type: String,
      default: "506px"
    }
  },
  data () {
    return {
      chart: null,
      optionObj: {
        option: {
          backgroundColor: "#fff",
          xAxis: {
            type: 'category',
            data: [
              this.$store.state.posdata.data[0].name,
              this.$store.state.posdata.data[1].name,
              this.$store.state.posdata.data[2].name,
              this.$store.state.posdata.data[3].name,
              this.$store.state.posdata.data[4].name
            ]
          },
          yAxis: {
            type: 'value'
          },
          series: [{
            data: [
              this.$store.state.posdata.data[0].value,
              this.$store.state.posdata.data[1].value,
              this.$store.state.posdata.data[2].value,
              this.$store.state.posdata.data[3].value,
              this.$store.state.posdata.data[4].value
            ],
            type: 'bar',
            itemStyle: {
              normal: {
                color: "#3182bd", //主色调
                // shadowBlur: 400,
                // shadowColor: "rgba(0, 0, 0, 0.5)"
              }
            }
          }]
        }
      }
    };
  },
  watch: {
    "$store.state.posdata.data" (newData, oldData) {
      let posData = this.$store.state.posdata.data
      try {
        for (let i in posData) {
          this.optionObj.option.xAxis.data[i] = posData[i].name
          this.optionObj.option.series[0].data[i] = posData[i].value
        }
      } catch (error) {

      }
      this.chart.setOption(this.optionObj.option);
    },
  },
  mounted () {
    this.initChart();
  },
  beforeDestroy () {
    if (!this.chart) {
      return;
    }
    this.chart.dispose();
    this.chart = null;
  },
  methods: {
    initChart (data) {
      this.chart = echarts.init(this.$refs.myEchart);
      // 配置、数据
      this.chart.setOption(this.optionObj.option);
    }
  }
};
</script>

<style>
</style>