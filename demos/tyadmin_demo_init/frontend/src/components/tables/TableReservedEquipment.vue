<template>
  <q-card>
    <q-card-section>
      <div class="text-h6 text-grey-8">
        My device appointment
      </div>
    </q-card-section>
    <q-separator/>
    <q-card-section class="q-pa-none">
      <q-table grid :rows="data" :columns="columns">
        <template v-slot:item="props">
          <div class="q-pa-xs col-xs-12 col-sm-6 col-md-4 col-lg-3">
            <card-reserved-equipment :Equipment_photo="props.row.Equipment_photo" :Equipment_name="props.row.Equipment_name"></card-reserved-equipment>
          </div>
        </template>
      </q-table>
    </q-card-section>
  </q-card>
</template>

<script>


import {defineComponent} from "vue";
import CardReservedEquipment from "components/cards/CardReservedEquipment";
import {Notify} from "quasar";

const columns = [
  {name: 'Equipment_photo', label: 'Equipment_photo', field: 'Equipment_photo', sortable: true, align: 'left'},
  {name: 'Equipment_name', label: 'Equipment_name', field: 'Equipment_name', sortable: true, align: 'left'},
];

export default defineComponent({
  name: "TableReservedEquipment",
  components: {
    CardReservedEquipment
  },
  data () {
    return {
      columns,
      data : [
        {
          Equipment_photo:'https://cdn.quasar.dev/img/chicken-salad.jpg',
          Equipment_name: 'Swimming pool',
        },
      ],
      created() {
        this.getBooked()
      },
      methods:{
        getBooked(){
          let _this=this
          let arr = []
          let uid=sessionStorage.getItem('user_id')
          this.$api.put('/api/xadmin/v1/equipment',{
            user_id:uid
          }).then(function (response) {
            console.log(response)
            let res=response.data.data
            console.log(res)
            for(let i=0;i<res.length;i++){
              let item ={
                booked_equipment_id:0,
                Equipment_photo:"",
                Equipment_name:"",
              }
              item.booked_equipment_id=res[i].id
              item.Equipment_photo=res[i].image
              item.Equipment_name=res[i].name
              sessionStorage.setItem('booked_equipment_id',res[i].id)
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
    }
  }
})
</script>

<style scoped>

</style>
