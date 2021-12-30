<template>
      <div class="row">
              <q-select class="col-11" v-model="model" :options="options" label="前往区域" />

        <q-btn class="col-1" @click="clickTo" label="Submit" type="submit" color="primary"/>
      </div>
   <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
        <zone-chart></zone-chart>
      </div>
</template>

<script>
import {defineComponent, defineAsyncComponent} from 'vue'
export default defineComponent({
components: {
    ZoneChart: defineAsyncComponent(() => import('components/charts/ZoneChart')),
    
},
data(){
      return{
        options:['离开','舞蹈区',  '游泳区', '器械区', '拳击区','器械区','瑜伽区'],
        model:''
      }
    },
    methods:{
      clickTo(){
        console.log(this.model)
      }
    }
})

</script>

<style scoped>
.chart {
  height: 1000px;
}
</style>