<template>
  <q-card>
    <q-card-section class="text-center">
      <q-avatar size="10px" className="shadow-5" class="photo">
        <img :src="Equipment_photo">
      </q-avatar>
    </q-card-section>

    <q-space></q-space>

    <q-card-section>
      <div class="row no-wrap items-center">
        <div class="col text-h6 ellipsis">
          Name:   {{ Equipment_name }}
        </div>
      </div>
    </q-card-section>

    <q-card-section>
      <div class="row no-wrap items-center">
        <div class="col text-h6 ellipsis " >
          Status:   {{ Equipment_status }}
        </div>
      </div>
    </q-card-section>

    <q-separator />

    <q-card-actions>
      <q-btn flat round icon="event" />
      <q-btn flat color="primary" size="20px" @click="tryBook">
        Book
      </q-btn>
    </q-card-actions>
  </q-card>
</template>

<script>
import {defineComponent} from 'vue'
import {Notify} from "quasar";
import { LocalStorage, SessionStorage } from 'quasar'

export default defineComponent({
  name: "CardEquipment",
  props: ['Equipment_photo', 'Equipment_name', 'Equipment_status'],
  date(){
   return{

   }
  },
  methods:{
    tryBook() {
      let _this=this
      let arr = []
      let id=sessionStorage.getItem(equipment_id)
      console.log(equipment_id)
      this.$api.post('/api/xadmin/v1/book_equipment',{
        id:id
      }).then(function (response) {
        console.log(response)
        let res=response.data.data
        if(res.status=="1"){
          Notify.create({
            message:"success"
          })
        }else if(res.status=="2"){
          Notify.create({
            message:"Already used"
          })
        }else if(res.status=="3"){
          Notify.create({
            message:"Already booked"
          })

        }else if(res.status=="4"){
          Notify.create({
            message:"broken"
          })
        }
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

