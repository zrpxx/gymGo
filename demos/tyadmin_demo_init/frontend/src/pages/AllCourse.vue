<template>

  <q-page>
    <table-all-course class="q-mt-lg"></table-all-course>
<!--    <table-all-course></table-all-course>-->
  </q-page>
</template>

<script>
import TableAllCourse from "components/tables/AllCourseTable";
export default {
  name: "AllCourse",
  components:{
    // eslint-disable-next-line vue/no-unused-components
    TableAllCourse
  }
}
</script>

<style scoped>

</style>
