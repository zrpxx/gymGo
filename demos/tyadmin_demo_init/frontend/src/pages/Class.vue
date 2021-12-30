<template>
  <class-chart class="full-screen"></class-chart>
</template>

<script>
import { defineComponent, defineAsyncComponent } from "vue";
export default defineComponent({
  components: {
    ClassChart: defineAsyncComponent(() =>
      import("components/charts/ClassChart")
    ),
  },
});
</script>

<style scoped>
.chart {
  height: 2000px;
}
</style>
