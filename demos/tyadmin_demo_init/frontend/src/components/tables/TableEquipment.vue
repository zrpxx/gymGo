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
      <q-table grid :rows="data" :columns="columns" hide-bottom>
        <template v-slot:item="props">
          <div class="q-pa-xs col-xs-12 col-sm-6 col-md-4 col-lg-3">
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

const columns = [
  {name: 'Equipment_photo', label: 'Equipment_photo', field: 'Equipment_photo', sortable: true, align: 'left'},
  {name: 'Equipment_name', label: 'Equipment_name', field: 'Equipment_name', sortable: true, align: 'left'},
  {name: 'Equipment_status', label: 'Equipment_status', field: 'Equipment_status', sortable: true, align: 'left'},
];

const data = [
  {
    Equipment_photo:'https://cdn.quasar.dev/img/chicken-salad.jpg',
    Equipment_name: 'Swimming pool',
    Equipment_status:'Booked'
  },
  {
    Equipment_photo:'https://cdn.quasar.dev/img/chicken-salad.jpg',
    Equipment_name: 'Swimming pool',
    Equipment_status:'Booked'
  },
  {
    Equipment_photo:'https://cdn.quasar.dev/img/chicken-salad.jpg',
    Equipment_name: 'Swimming pool',
    Equipment_status:'Booked'
  },
  {
    Equipment_photo:'https://cdn.quasar.dev/img/chicken-salad.jpg',
    Equipment_name: 'Swimming pool',
    Equipment_status:'Booked'
  },

];
export default defineComponent({
  name: "TableEquipment",
  components: {
    CardEquipment
  },
  setup () {
    return {
      columns,
      data
    }
  }
})
</script>

<style scoped>

</style>
