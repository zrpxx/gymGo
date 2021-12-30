<template>
  <q-page class="q-pa-sm">
    <table-equipment class="q-mt-lg"></table-equipment>
  </q-page>
</template>

<script>
import TableEquipment from "components/tables/TableReservedEquipment";

export default {
  name: "Reserved_Equipment",
  components: {
    TableEquipment,
  },
  methods:{
    tryClick(){

    }
  }
}
</script>

<style>

</style>


