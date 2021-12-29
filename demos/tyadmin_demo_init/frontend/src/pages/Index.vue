<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    >

  </q-page>
</template>

<script>

import { defineComponent,defineAsyncComponent } from 'vue';

export default defineComponent({
  name: 'PageIndex',
  components: {
   // CardSocial: defineAsyncComponent(() => import('components/cards/CardSocial')),
  },
})
</script>
