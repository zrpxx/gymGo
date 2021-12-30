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
              <q-btn class="login" label="Confirm" type="button" color="primary" @click="tryConfirm"/>
            </div>
          </q-form>
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import * as echarts from "echarts";
import {useQuasar} from 'quasar'
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
          data: ['Email', 'Union Ads', 'Video Ads', 'Direct', 'Search Engine']
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
          data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
          type: 'value'
        },
        series: [
          {
            name: 'Email',
            type: 'line',
            stack: 'Total',
            data: [120, 132, 101, 134, 90, 230, 210]
          },
          {
            name: 'Union Ads',
            type: 'line',
            stack: 'Total',
            data: [220, 182, 191, 234, 290, 330, 310]
          },
          {
            name: 'Video Ads',
            type: 'line',
            stack: 'Total',
            data: [150, 232, 201, 154, 190, 330, 410]
          },
          {
            name: 'Direct',
            type: 'line',
            stack: 'Total',
            data: [320, 332, 301, 334, 390, 330, 320]
          },
          {
            name: 'Search Engine',
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
      let lineChart = document.getElementById('lineChart');
      echarts.dispose(lineChart);
      let theme = this.model ? 'dark' : 'light';
      this.line_chart = echarts.init(lineChart, theme);
      this.line_chart.setOption(this.options)
    },
    onResize() {
      if (this.line_chart) {
        this.line_chart.resize();
      }
    },

    tryConfirm(){

    }
  }
}
</script>

<style scoped>
.login{
  width: 100%;
}
</style>
