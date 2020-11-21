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
          title: {
            top: 20,
            // text: '某站点用户访问来源',
            // subtext: '纯属虚构',
            left: 'center'
          },
          tooltip: {
            trigger: 'item',
            formatter: '{a} <br/>{b} : {c} ({d}%)'
          },
          legend: {
            orient: 'vertical',
            left: 'left',
            data: [
              this.$store.state.posdata.data[0].name,
              this.$store.state.posdata.data[1].name,
              this.$store.state.posdata.data[2].name,
              this.$store.state.posdata.data[3].name,
              this.$store.state.posdata.data[4].name
            ]
          },
          series: [
            {
              name: '比例',
              type: 'pie',
              radius: '55%',
              center: ['50%', '50%'],
              data: this.$store.state.posdata.data,
              emphasis: {
                itemStyle: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              },
              label: {
                normal: {
                  textStyle: {
                    color: "#000"
                  }
                }
              },
              labelLine: {
                normal: {
                  lineStyle: {
                    color: "gray"
                  },
                  smooth: 0.2,
                  length: 10,
                  length2: 20
                }
              },
              // itemStyle: {
              //   normal: {
              //     color: "#3792c8", //主色调
              //     // shadowBlur: 400,
              //     // shadowColor: "rgba(0, 0, 0, 0.5)"
              //   }
              // },
            }
          ]
        }
      }
    };
  },
  watch: {
    "$store.state.posdata.data" (newData, oldData) {
      let posData = this.$store.state.posdata.data
      try {
        for (let i in posData) {
          this.optionObj.option.legend.data[i] = posData[i].name
        }
      } catch (error) {

      }
      // console.log(this.optionObj.option.legend);
      // console.log(posData);
      this.optionObj.option.series[0].data = posData
      this.chart.setOption(this.optionObj.option);
    },
  },
  beforeMount () {

  },
  mounted () {
    this.initChart();
    // console.log(this.optionObj.option.legend.data);
    // console.log(this.optionObj.option.series[0].data);
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