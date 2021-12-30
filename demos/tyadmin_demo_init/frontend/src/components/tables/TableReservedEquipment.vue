<template>
  <q-card>
    <q-card-section>
      <div class="text-h6 text-grey-8 content-lg-end">
        My appointment and use/
        <q-btn name="map" @click="Reserved">
          <q-icon name="map" />
          <div class="text-h6">Reserved</div>
        </q-btn>
        /
        <q-btn name="map" @click="Using">
          <q-icon name="map" />
          <div class="text-h6">Using</div>
        </q-btn>
      </div>
    </q-card-section>
    <q-separator/>
    <q-card-section class="q-pa-none">
      <q-table grid :rows="data" :columns="columns" :pagination="initialPagination">
        <template v-slot:item="props">
          <div class="q-pa-xs col-xs-12 col-sm-6 col-md-3 col-md-3">
            <card-reserved-equipment :id="props.row.id" :Equipment_photo="props.row.Equipment_photo" :Equipment_name="props.row.Equipment_name" :Equipment_status="props.row.Equipment_status" :Equipment_due="props.row.Equipment_due"></card-reserved-equipment>
          </div>
        </template>
      </q-table>
    </q-card-section>
  </q-card>
</template>

<script>


import {defineComponent} from "vue";
import {Notify} from "quasar";
import CardReservedEquipment from "components/cards/CardReservedEquipment";

export default defineComponent({
  name: "TableReservedEquipment",
  components: {
    CardReservedEquipment
  },
  data () {
    return {
      columns: [
        {name: 'id', label: 'id', field: 'id', sortable: true, align: 'left'},
        {name: 'Equipment_photo', label: 'Equipment_photo', field: 'Equipment_photo', sortable: true, align: 'left'},
        {name: 'Equipment_name', label: 'Equipment_name', field: 'Equipment_name', sortable: true, align: 'left'},
        {name: 'Equipment_status', label: 'Equipment_status', field: 'Equipment_status', sortable: true, align: 'left'},
        {name: 'Equipment_due', label: 'Equipment_due', field: 'Equipment_due', sortable: true, align: 'left'},
      ],

      data: [
        {
          id:'',
          Equipment_photo:'',
          Equipment_name: '',
          Equipment_status:'',
          Equipment_due:''
        },
      ],
      initialPagination:{
        rowsPerPage: 8
        // rowsNumber: xx if getting data from a server

      }
    }
  },
  created() {
    this.getReserveEquipment()
    console.log(this.data)
  },

  methods:{
    getReserveEquipment(){
      let _this=this
      let arr = []
      let ss=['My use','My appointment']
      let uid=sessionStorage.getItem('user_id')
      this.$api.get('/userapi/get_reserve_equipment',{
        params:{
          user_id:uid
        }
      }).then(function (response) {
        console.log(response)
        let res=response.data.reserved
        console.log(res)
        for(let i=0;i<res.length;i++){
          let item ={
            id:0,
            Equipment_photo:"",
            Equipment_name:"",
            Equipment_status:"",
            Equipment_due:""
          }
          item.id=res[i].reserve_id
          item.Equipment_photo=res[i].equipment_img
          item.Equipment_name=res[i].equipment_name
          let status = res[i].equipment_status
          item.Equipment_due=res[i].due_time
          if(status === 2){
            item.Equipment_status=ss[1]
          }else if(status === 3){
            item.Equipment_status=ss[0]
          }
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
    },
    Reserved(){
      let _this=this
      let arr = []
      let ss=['My use','My appointment']
      let uid=sessionStorage.getItem('user_id')
      this.$api.get('/userapi/get_reserve_equipment',{
        params:{
          user_id:uid
        }
      }).then(function (response) {
        console.log(response)
        let res=response.data.reserved
        console.log(res)
        for(let i=0;i<res.length;i++){
          let item ={
            id:0,
            Equipment_photo:"",
            Equipment_name:"",
            Equipment_status:"",
            Equipment_due:""
          }
          item.id=res[i].reserve_id
          item.Equipment_photo=res[i].equipment_img
          item.Equipment_name=res[i].equipment_name
          let status = res[i].equipment_status
          item.Equipment_due=res[i].due_time
          if(status === 2){
            item.Equipment_status=ss[1]
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
    Using(){
      let _this=this
      let arr = []
      let ss=['My use','My appointment']
      let uid=sessionStorage.getItem('user_id')
      this.$api.get('/userapi/get_reserve_equipment',{
        params:{
          user_id:uid
        }
      }).then(function (response) {
        console.log(response)
        let res=response.data.reserved
        console.log(res)
        for(let i=0;i<res.length;i++){
          let item ={
            id:0,
            Equipment_photo:"",
            Equipment_name:"",
            Equipment_status:"",
            Equipment_due:""
          }
          item.id=res[i].reserve_id
          item.Equipment_photo=res[i].equipment_img
          item.Equipment_name=res[i].equipment_name
          let status = res[i].equipment_status
          item.Equipment_due=res[i].due_time
          if(status === 3){
            item.Equipment_status=ss[0]
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

    }
  }
})
</script>

<style scoped>

</style>
