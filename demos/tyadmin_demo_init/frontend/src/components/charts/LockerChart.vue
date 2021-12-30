<template>
  <div>
    <q-card>
      <q-card-section class="text-h6"> Locker Used Chart </q-card-section>
      <q-card-section>
        <div ref="areachart" id="areaChart" style="height: 100em"></div>
      </q-card-section>
      <q-resize-observer @resize="onResize" />
    </q-card>
  </div>
</template>

<script>
import { api } from "src/boot/axios";
const hours = ["1", "2", "3", "4", "5", "6", "7", "8"];
// prettier-ignore
const days = [
    '1', '2', '3', '4',
    '5', '6', '7'
];

export default {
  name: "AreaChart",
  created() {
    //get the weekdays
    api
      .get("/api/xadmin/v1/lockers?pageSize=56")
      .then((res) => {
        console.log(res.data);
        this.lockers = res.data.data.reverse();
        console.log(this.lockers);
        //use for loop to put it into 7*8 matrix
        let _this = this;
        let x = 0;
        let y = 0;
        let user_id = sessionStorage.getItem("user_id");

        for (let i = 0; i < _this.lockers.length; i++) {
          //

          if (
            this.lockers[i].occupied_by.id == user_id &&
            this.lockers[i].status == 2
          ) {
            _this.options.series[0].data.push([x, y, 3]);
            _this.occupied_by = true;
          } else {
            _this.options.series[0].data.push([x, y, this.lockers[i].status]);
          }
          x++;
          if (x == 7) {
            x = 0;
            y++;
          }
        }
        // }
        // getZone()
        setTimeout(() => {
          this.init();
        }, 100);

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
      occupied_by: false,
      data_all: [],
      model: false,
      lockers: [],
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
          max: 3,
          calculable: true,
          orient: "horizontal",
          left: "center",
          bottom: "15%",
        },
        series: [
          {
            name: "Punch Card",
            type: "heatmap",
            textStyle: {
              fontFamily: "sans-serif",
              fontSize: 20,
            },
            data: [],
            label: {
              normal: {
                show: true,
                formatter: (param) => {
                  if (param.data[2] === 1) {
                    let index = param.data[0] + param.data[1] * 7 + 1;
                    return index + " is available";
                  } else if (param.data[2] === 2) {
                    let index = param.data[0] + param.data[1] * 7 + 1;
                    return index + " is occupied";
                  } else {
                    let index = param.data[0] + param.data[1] * 7 + 1;
                    return index + " is used by me";
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
      this.area_chart.setOption(this.options),
        this.area_chart.on("click", (params) => {
          console.log(params.data);

          //use for loop to put it into 7*8 matrix
          let _this = this;
          let x = 0;
          let y = 0;
          let index = 0;
          let user_id = sessionStorage.getItem("user_id");
          index = params.data[0] + params.data[1] * 7 + 1;
          console.log(index);
          if (params.data[2] == 2) {
            this.$q.notify({
              color: "negative",
              message: "This locker is occupied",
              position: "top",
            });
            return;
          }
          if (params.data[2] == 1 && this.occupied_by) {
            this.$q.notify({
              color: "negative",
              message: "You have used a locker",
              position: "top",
            });
            return;
          }

          if (params.data[2] == 1) {
            console.log("locker is used");
            this.$q
              .dialog({
                title: "Confirm",
                message: "Are sure to take this locker?",
                cancel: true,
                persistent: true,
              })
              .onOk(() => {
                api
                  .get(
                    "/userapi/occupy_locker?user_id=" +
                      user_id +
                      "&" +
                      "locker_id=" +
                      index
                  )
                  .then((res) => {
                    this.$router.go("0");
                  })
                  .catch((err) => {
                    console.log(err);
                  });
              })
              .onCancel(() => {
                return;
              })
              .onDismiss(() => {
                return;
              });
            this.occupied_by = true;
          } else if (params.data[2] == 3) {
            this.$q
              .dialog({
                title: "Confirm",
                message: "Are sure to free this locker?",
                cancel: true,
                persistent: true,
              })
              .onOk(() => {
                api
                  .get(
                    "/userapi/free_locker?user_id=" +
                      user_id
                  )
                  .then((res) => {
                    this.$router.go("0");
                  });
              })
              .catch((err) => {
                console.log(err);
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
            console.log("locker is free");
            this.occupied_by = false;
            console.log(
              "/userapi/free_locker?user_id=" + user_id
            );
          }
        });
    },
    onResize() {
      if (this.area_chart) {
        this.area_chart.resize();
      }
    },
    //   clickTo(params){

    // alert("Clicked: " + params.name + ", ID: " + params.dataIndex);
    //   }
  },
};
</script>

<style scoped></style>
