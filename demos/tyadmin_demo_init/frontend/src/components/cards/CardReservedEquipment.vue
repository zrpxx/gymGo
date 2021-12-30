<template>
  <q-card>
    <q-card-section class="text-center">
      <q-avatar size="10px" className="shadow-5" class="photo">
        <img :src="Equipment_photo" class="im">
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

    <q-card-section>
      <div class="row no-wrap items-center">
        <div class="col text-h6 ellipsis " >
          Due:   {{ Equipment_due }}
        </div>
      </div>
    </q-card-section>
    <q-separator />
    <q-card-actions>
      <q-btn flat color="primary" size="20px" @click="tryCancel">
        Cancel
      </q-btn>
      <q-btn flat color="primary" size="20px" @click="tryUse" >
        Use
      </q-btn>
    </q-card-actions>
  </q-card>
</template>

<script>
import {defineComponent} from 'vue'
import {Notify} from "quasar";
import { LocalStorage, SessionStorage } from 'quasar'

export default defineComponent({
  name: "CardReservedEquipment",
  props: ['id', 'Equipment_photo', 'Equipment_name', 'Equipment_status','Equipment_due'],
  date(){
    return{

    }
  },
  methods:{
    tryCancel() {
      let _this=this
      let uid =sessionStorage.getItem('user_id')
      console.log(uid)
      console.log(_this.id)
      this.$api.get('/userapi/cancel_reserve_equipment',{
        params: {
          reserve_id: _this.id
        }
      }).then(function (response) {
        console.log(response)
        let res=response.data
        if(res.status=="ok"){
          Notify.create({
            type: 'active',
            message: 'success'
          })
        }else if(res.status=="error"){
          Notify.create({
            pe: 'negative',
            message: 'Equipment has been reserved'
          })
        }
      }).catch(function (error) {
        Notify.create({
          message:""
        })
        console.log(error)
      })
    },
    tryUse(){
      let _this=this
      console.log(_this.id)
      this.$api.get('/userapi/activate_reserve_equipment',{
        params: {
          reserve_id: _this.id
        }
      }).then(function (response) {
        console.log(response)
        let res=response.data
        if(res.status=="ok"){
          Notify.create({
            type: 'active',
            message: 'success'
          })
        }else if(res.status=="error"){
          Notify.create({
            pe: 'negative',
            message: 'Equipment has been reserved'
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
.im{
  max-height: 200px;
}
</style>

