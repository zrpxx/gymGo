<template>
  <q-page class="q-pa-sm">

    <profile-card
      :balance="balance"
      :level="level"
      :recharge="recharge"
      :username="name"
    />

    <q-space />

    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
      <ProfileChart></ProfileChart>
    </div>
  </q-page>
</template>

<script>
import {defineComponent} from 'vue'
import ProfileCard from "components/cards/ProfileCard";
import ProfileChart from "components/charts/ProfileChart";
import {api} from "boot/axios";

export default defineComponent({
  name: 'PageIndex',
  components: {
    ProfileCard,
    ProfileChart,
  },
  setup() {
    return {}
  },
  data() {
    return {
      balance: 0,
      level: 0,
      recharge: 0,
      username: ''
    }
  },
  created() {
    let user_id = sessionStorage.getItem('user_id')
    if(user_id)
      api.get('/userapi/get_profile', {
        params: {
          user_id: user_id
        }
      }).then(res => {
        let data = res.data
        this.balance = data.balance
        this.recharge = data.total_charge
        this.level = data.vip_level
        this.name = data.username
      })
  }

})
</script>

<style>
</style>
