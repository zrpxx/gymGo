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
      <q-btn flat color="primary" size="20px" @click="tryClick">
        Book
      </q-btn>
    </q-card-actions>
  </q-card>
</template>

<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "CardEquipment",
  props: ['Equipment_photo', 'Equipment_name', 'Equipment_status']
})

</script>

<style scoped>

</style>

