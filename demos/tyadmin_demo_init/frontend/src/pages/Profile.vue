<template>
  <q-page class="q-pa-sm">

    <profile-card />

    <q-space />

    <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
      <ProfileChart></ProfileChart>
    </div>
  </q-page>
</template>

<script>
import {defineComponent,defineAsyncComponent} from 'vue'
import ProfileCard from "components/cards/ProfileCard";
import ProfileChart from "components/charts/ProfileChart";

export default defineComponent({
  name: 'PageIndex',
  components: {
    ProfileCard,
    ProfileChart,
  },
  setup() {
    return {}
  }

})
</script>

<style>
</style>
