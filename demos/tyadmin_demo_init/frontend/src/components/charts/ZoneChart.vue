<template>
  <div>
    <q-card>
      <q-card-section class="text-h6"> Gym Zone Chart </q-card-section>
      <q-card-section>
        <div ref="areachart" id="areaChart" style="height: 800px"></div>
      </q-card-section>
      <q-resize-observer @resize="onResize" />
    </q-card>
  </div>
</template>

<script>
import { api } from "src/boot/axios";
export default {
  name: "AreaChart",
  created() {
    let _this = this;
    api
      .get("/api/xadmin/v1/zones")
      .then(function (res) {
        let resArr = res.data.data;
        console.log(resArr);
        console.log(resArr.length);
        for (let i = 0; i < resArr.length; i++) {
          _this.options.series[0].data[i].name =
            resArr[i].name +
            " " +
            "\n目前人数为" +
            resArr[i].current_number +
            "\n" +
            "最大人数为" +
            resArr[i].max_number;
          // get random number from 6 to 10
          _this.options.series[0].data[i].value = 10;
          if (resArr[i].current_number <= resArr[i].max_number / 2) {
            _this.options.color[i] = "#32CD32";
            console.log("area " + resArr[i].name + " is green");
          } else if (
            resArr[i].current_number > resArr[i].max_number / 2 &&
            resArr[i].current_number < resArr[i].max_number
          ) {
            _this.options.color[i] = "#FFD700";
            console.log("area " + resArr[i].name + " is gold");
          } else {
            _this.options.color[i] = "#FF0000";
            console.log("area " + resArr[i].name + " is red");
          }
        }
        _this.options.color.reverse();
        console.log(_this.options.color);
      })
      .catch(function (error) {
        console.log(error);
      });

    setTimeout(() => {
      this.init();
    }, 200);
    setTimeout(() => {
      this.init();
    }, 300);
    setTimeout(() => {
      this.init();
    }, 400);
    setTimeout(() => {
      this.init();
    }, 700);
  },
  data() {
    return {
      model: false,
      options: {
        title: {
          show: false,
        },
        textStyle: {
          fontFamily: "sans-serif",
          fontSize: 20,
        },
        color: [],

        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ",
          textStyle: {},
        },
        legend: {
          orient: "vertical",
          left: "left",

          data: [
            "Direct",
            "Email",
            "Ad Networks",
            "Video Ads",
            "Search Engines",
          ],
        },
        series: [
          {
            name: "Gym",
            nodeClick: "false",
            type: "treemap",
            radius: "55%",
            center: ["50%", "60%"],
            nodeClick: "false",
            data: [
              {
                name: "ee",
                value: 10,
              },
              {
                name: "eee",
                value: 20,
              },
              {
                name: "",
                value: 20,
              },
              {
                name: "",
                value: 20,
              },
              {
                name: "",
                value: 20,
              },
              {
                name: "",
                value: 20,
              },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
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
    setTimeout(() => {
      this.init();
    }, 1);
    setTimeout(() => {
      this.init();
    }, 2);
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
