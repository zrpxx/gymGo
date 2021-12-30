<template>
    <q-card>
      <q-card-section>
        <div class="text-h6 text-grey-8 content-lg-end">
          Equipment reservation/
          <q-btn name="map" @click="Available">
            <q-icon name="map" />
            <div class="text-h6">Available</div>
          </q-btn>
        </div>
      </q-card-section>
      <q-separator/>
      <q-card-section class="q-pa-none">
        <q-table grid :rows="data" :columns="columns">
          <template v-slot:item="props">
            <div class="q-pa-xs col-xs-12 col-sm-6 col-md-3 col-md-3">
              <card-equipment :Equipment_photo="props.row.Equipment_photo" :Equipment_name="props.row.Equipment_name" :Equipment_status="props.row.Equipment_status"></card-equipment>
            </div>
          </template>
        </q-table>
      </q-card-section>
    </q-card>
</template>

<script>


import {defineComponent} from "vue";
import CardEquipment from "components/cards/CardEquipment";
import { ref } from 'vue'
import {Notify} from "quasar";

const columns = [
  {name: 'Equipment_photo', label: 'Equipment_photo', field: 'Equipment_photo', sortable: true, align: 'left'},
  {name: 'Equipment_name', label: 'Equipment_name', field: 'Equipment_name', sortable: true, align: 'left'},
  {name: 'Equipment_status', label: 'Equipment_status', field: 'Equipment_status', sortable: true, align: 'left'},
];

export default defineComponent({
  name: "TableEquipment",
  components: {
    CardEquipment
  },
  data () {
    return {
      columns,
      data: [
        {
          Equipment_photo:'https://cdn.quasar.dev/img/chicken-salad.jpg',
          Equipment_name: 'Swimming pool',
          Equipment_status:'Booked'
        },
      ]
    }
  },
  created() {
    this.getEquipment()
    console.log(this.data)
  },

  methods:{
    Available(){
      let _this=this
      let arr = []
      this.$api.get('/api/xadmin/v1/equipment').then(function (response) {
        console.log(response)
        let res=response.data.data
        console.log(res)
        for(let i=0;i<res.length;i++){
          let item ={
            Equipment_photo:"",
            Equipment_name:"",
            Equipment_status:""
          }
          item.Equipment_photo=res[i].image
          item.Equipment_name=res[i].name
          item.Equipment_status=res[i].status
          if(item.Equipment_status=="1"){
            arr.push(item)
          }
        }
        _this.data = arr
        console.log(_this.data)
      }).catch(function (error) {
        Notify.create({
          message:""
        })
        console.log(error)
      })
    },
    getEquipment(){
      let _this=this
      let s=['Available','booked','Being used','broken']
      let arr = []
      this.$api.get('/api/xadmin/v1/equipment').then(function (response) {
        console.log(response)
        let res=response.data.data
        console.log(res)
        for(let i=0;i<res.length;i++){
          let item ={
            equipment_id:0,
            Equipment_photo:"",
            Equipment_name:"",
            Equipment_status:""
          }
          item.equipment_id=res[i].id
          item.Equipment_photo=res[i].image
          item.Equipment_name=res[i].name
          item.Equipment_status=s[res[i].status]
          sessionStorage.setItem('equipment_id',res[i].id)
          arr.push(item)
        }
        _this.data = arr
        console.log(_this.data)
      }).catch(function (error) {
        Notify.create({
          message:""
        })
        console.log(error)
      })
    }
  }
})
</script>

<style scoped>

</style>
