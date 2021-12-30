<template>

        <locker-chart class="full-screen"></locker-chart>
</template>

<script>
import {defineComponent, defineAsyncComponent} from 'vue'
export default defineComponent({
components: {
    LockerChart: defineAsyncComponent(() => import('components/charts/LockerChart')),
}})
</script>

<style scoped>
.chart {
  height: 2000px;
}
</style>