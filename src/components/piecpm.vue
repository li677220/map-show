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
            // text: "这里放省份",
            left: "center",
            top: 20,
            textStyle: {
              color: "#000",
            }
          },
          tooltip: {
            trigger: "item",
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          visualMap: {
            show: false,
            min: 0,
            max: 0,
            inRange: {
              colorLightness: [0, 1]
            }
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
              name: "比例",
              type: "pie",
              radius: "55%",
              center: ["50%", "50%"],
              data: this.$store.state.posdata.data.sort(function (a, b) {
                return a.value - b.value;
              }),
              roseType: "radius",
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
              //     color: "#6baed6", //主色调
              //     // shadowBlur: 400,
              //     // shadowColor: "rgba(0, 0, 0, 0.5)"
              //   }
              // },

              animationType: "scale",
              animationEasing: "elasticOut",
              animationDelay: function (idx) {
                return Math.random() * 200;
              }
            }
          ]
        }
      },

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
  mounted () {
    this.initChart();
  },
  beforeMount () {
    // this.initChart();
  },
  beforeDestroy () {
    if (!this.chart) {
      return;
    }
    this.chart.dispose();
    this.chart = null;
  },
  methods: {
    initChart () {
      this.chart = echarts.init(this.$refs.myEchart);
      // 配置、数据
      this.chart.setOption(this.optionObj.option);

    }
  }
};
</script>

<style>
</style>