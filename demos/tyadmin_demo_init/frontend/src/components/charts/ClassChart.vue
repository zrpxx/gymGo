<template>
  <div style="width: 1400px">
    <q-card>
      <q-card-section class="text-h6"> Class Booking Chart </q-card-section>
      <q-card-section>
        <div ref="areachart" id="areaChart" style="height: 600px"></div>
      </q-card-section>
      <q-resize-observer @resize="onResize" />
    </q-card>
  </div>
</template>

<script>
import { api } from "src/boot/axios";
const hours = ["8a", "10a", "12p", "2p", "4p", "6p", "8p", "10p"];
// prettier-ignore
const days = [
    'Sunday', 'Saturday', 'Friday', 'Thursday',
    'Wednesday', 'Tuesday', 'Monday'
];

export default {
  name: "AreaChart",
  props: ["coach_id"],
  created() {
    api
      .get(
        "/userapi/get_coach_agenda?coach_id=" +
          this.coach_id
      )
      .then((res) => {
        console.log(res.data);
        let arr = res.data.result;
        console.log(arr);
        //use for loop to put it into 7*8 matrix
        let _this = this;
        let x = 0;
        let y = 0;
        _this.start = arr[0].id;
        for (let i = 0; i < arr.length; i++) {
          //
          if (arr[i].status == -1) {
            _this.options.series[0].data.push([x, y, "-"]);
          } else {
            _this.options.series[0].data.push([x, y, arr[i].status]);
          }
          y++;
          if (y == 8) {
            y = 0;
            x++;
          }
        }
        console.log(_this.options.series[0].data);
        // }
        // getZone()
        setTimeout(() => {
          this.init();
        }, 100);

        setTimeout(() => {
          this.init();
        }, 100);
      });
  },
  data() {
    return {
      model: false,
      start: 0,
      options: {
        gradientColor: ["white", "#40a070", "#e77c8e"],
        tooltip: {
          position: "top",
        },
        grid: {
          height: "50%",
          top: "10%",
        },
        xAxis: {
          type: "category",
          data: days,
          splitArea: {
            show: true,
          },
        },
        yAxis: {
          type: "category",
          data: hours,
          splitArea: {
            show: true,
          },
        },
        visualMap: {
          min: 0,
          max: 2,
          calculable: true,
          orient: "horizontal",
          left: "center",
          bottom: "15%",
        },
        series: [
          {
            name: "Locker",
            value: "eee",
            type: "heatmap",
            data: [],
            label: {
              normal: {
                show: true,
                formatter: (param) => {
                  if (param.data[2] === 1) {
                    let index = param.data[0] + param.data[1] * 7 + 1;
                    return " available";
                  } else if (param.data[2] === 2) {
                    let index = param.data[0] + param.data[1] * 7 + 1;
                    return " occupied";
                  }
                },
              },
            },
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      },
    };
  },
  mounted() {
    this.init();
  },
  watch: {
    "$q.dark.isActive": function () {
      this.init();
    },
  },
  methods: {
    init() {
      let areaChart = document.getElementById("areaChart");
      echarts.dispose(areaChart);
      let theme = this.model ? "dark" : "light";
      this.area_chart = echarts.init(areaChart, theme);
      this.area_chart.setOption(this.options);
      this.area_chart.on("click", (params) => {
        console.log(params);
        let index = this.start + params.data[0] * 8 + params.data[1];
        console.log(index);
        if (params.data[2] == 2) {
          this.$q
            .dialog({
              title: "Confirm",
              message: "Are sure to cancel this agenda?",
              cancel: true,
              persistent: true,
            })
            .onOk(() => {
              setTimeout(() => {
                this.$router.go("0");
              }, 1000);
            })
            .onOk(() => {
              // console.log('>>>> second OK catcher')
            })
            .onCancel(() => {
              return;
            })
            .onDismiss(() => {
              return;
            });
          let user_id = sessionStorage.getItem("user_id");
          api
            .get(
              "/userapi/cancel_coach_agenda?agenda_id=" +
                index +
                "&user_id=" +
                user_id
            )
            .then((res) => {
              console.log(res);
            });
          return;
        } else {
          this.$q
            .dialog({
              title: "Confirm",
              message: "Are sure to set the agenda?",
              cancel: true,
              persistent: true,
            })
            .onOk(() => {
              setTimeout(() => {
                this.$router.go("0");
              }, 1000);
            })
            .onOk(() => {
              // console.log('>>>> second OK catcher')
            })
            .onCancel(() => {
              return;
            })
            .onDismiss(() => {
              return;
            });
          let user_id = sessionStorage.getItem("user_id");

          api
            .get(
              "/userapi/set_coach_agenda?agenda_id=" +
                index +
                "&user_id=" +
                user_id
            )
            .then((res) => {
              console.log(res);
            });
          return;
        }
      });
    },
    onResize() {
      if (this.area_chart) {
        this.area_chart.resize();
      }
    },
  },
};
</script>

<style scoped></style>
