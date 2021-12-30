<template>
  <div>
    <q-card>
      <q-card-section class="text-h6">
        Body Data/
        <q-btn class="text-h6" label="record" icon="map" @click="card = true" />
      </q-card-section>

      <q-card-section>
        <div ref="linechart" id="lineChart" style="height: 600px;"></div>
      </q-card-section>
      <q-resize-observer @resize="onResize"/>
      <q-space></q-space>
    </q-card>


    <q-dialog v-model="card">
      <q-card v-bind:style="$q.screen.lt.sm?{'width': '80%'}:{'width':'30%'}">
        <q-card-section>
          <div class="text-center q-pt-lg">
            <div class="col text-h6 ellipsis">
              Please input your body data
            </div>
          </div>
        </q-card-section>
        <q-card-section>
          <q-form
            class="q-gutter-md"
          >
            <q-input
              filled
              v-model="weight"
              label="weight"
            />
            <q-input
              filled
              v-model="height"
              label="height"
            />
            <q-input
              filled
              v-model="fat"
              label="fat"
            />
            <q-input
              filled
              v-model="muscle"
              label="muscle"
            />
            <q-input
              filled
              v-model="bmi"
              label="BMI"
            />
            <div>
              <q-btn class="login" label="Confirm" type="button" color="primary" @click="record_body_data()"/>
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import * as echarts from "echarts";
import {Notify, useQuasar} from 'quasar'
import { ref } from 'vue'
export default {
  name: "ProfileChart",
  data () {
    return {
      height:'',
      weight:'',
      fat:'',
      muscle:'',
      bmi:'',
      model: false,
      card: ref(false),
      options: {
        tooltip: {
          trigger: 'axis',
        },
        legend: {
          data: ['height', 'weight', 'fat', 'muscle', 'BMI']
        },
        grid: {
          left: '3%',
          right: '4%',
          bottom: '3%',
          containLabel: true
        },
        toolbox: {
          feature: {
            saveAsImage: {}
          }
        },
        xAxis: {
          type: 'category',
          boundaryGap: false,
          data: ['1', '2', '3', '4', '5', '6', '7', '8']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'height',
            type: 'line',
            stack: 'Total',
            data: [120, 132, 101, 134, 90, 230, 210]
          },
          {
            name: 'weight',
            type: 'line',
            stack: 'Total',
            data: [220, 182, 191, 234, 290, 330, 310]
          },
          {
            name: 'fat',
            type: 'line',
            stack: 'Total',
            data: [150, 232, 201, 154, 190, 330, 410]
          },
          {
            name: 'muscle',
            type: 'line',
            stack: 'Total',
            data: [320, 332, 301, 334, 390, 330, 320]
          },
          {
            name: 'BMI',
            type: 'line',
            stack: 'Total',
            data: [820, 932, 901, 934, 1290, 1330, 1320]
          }
        ]
      },
      line_chart: null
    }
  },
  mounted() {
    this.init();
  },
  watch: {
    '$q.dark.isActive': function () {
      this.init();
    }
  },
  methods: {
    init() {

      console.log(this.options)
      let lineChart = document.getElementById('lineChart');
      echarts.dispose(lineChart);
      let theme = this.model ? 'dark' : 'light';
      this.line_chart = echarts.init(lineChart, theme);
      this.request_body_data()
      // this.line_chart.setOption(this.options)
    },
    onResize() {
      if (this.line_chart) {
        // this.line_chart.resize();
      }
    },

    record_body_data() {
      let _this=this
      let uid = sessionStorage.getItem('user_id')
      this.$api.get('/userapi/record_body_data', {
        params: {
          user_id: uid,
          height: _this.height,
          weight: _this.weight,
          fat: _this.fat,
          muscle: _this.muscle,
          bmi: _this.bmi,
        }
      }).then(function (response) {
        let res=response.data
        if (res.status === "ok") {
          Notify.create({
            type: "positive",
            message:"record successful"
          })
        }
      }).catch(function (error) {
        Notify.create({
          message:"error"
        })
        console.log(error)
      })
    },

    request_body_data(){
      let _this=this
      let arr = []
      let uid = sessionStorage.getItem('user_id')
      this.$api.get('/userapi/get_profile', {
        params: {
          user_id: uid
        }
      }).then(function (response) {
        console.log(response)
        let res=response.data
        let body_data_set = res.body_data
        let height_list = []
        let weight_list = []
        let fat_list = []
        let muscle_list = []
        let bmi_list = []
        for(let i=0;i<body_data_set.length;i++){
          height_list.push(body_data_set[i].height)
          weight_list.push(body_data_set[i].weight)
          fat_list.push(body_data_set[i].fat)
          muscle_list.push(body_data_set[i].muscle)
          bmi_list.push(body_data_set[i].bmi)
        }
        _this.options.series = []
        _this.options.series.push({
          name: 'height',
          type: 'line',
          stack: 'Total',
          data: height_list
        })
        _this.options.series.push({
          name: 'weight',
          type: 'line',
          stack: 'Total',
          data: weight_list
        })
        _this.options.series.push({
          name: 'fat',
          type: 'line',
          stack: 'Total',
          data: fat_list
        })
        _this.options.series.push({
          name: 'muscle',
          type: 'line',
          stack: 'Total',
          data: muscle_list
        })
        _this.options.series.push({
          name: 'bmi',
          type: 'line',
          stack: 'Total',
          data: bmi_list
        })
        _this.options.xAxis.data = []
        for (let i = 0; i < body_data_set.length; i++) {
          _this.options.xAxis.data.push((i+1).toString())
        }
        _this.line_chart.setOption(_this.options)
      }).catch(function (error) {
        Notify.create({
          message:""
        })
        console.log(error)
      })
    }
  }
}
</script>

<style scoped>
.login{
  width: 100%;
}
</style>
