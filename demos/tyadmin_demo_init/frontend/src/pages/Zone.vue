<template>
  <div class="row">
    <q-select
      class="col-11"
      v-model="model"
      :options="options"
      label="前往区域"
    />

    <q-btn
      class="col-1"
      @click="clickTo"
      label="Submit"
      type="submit"
      color="primary"
    />
  </div>
  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
    <zone-chart></zone-chart>
  </div>
</template>

<script>
import { api } from "src/boot/axios";
import { defineComponent, defineAsyncComponent } from "vue";
export default defineComponent({
  components: {
    ZoneChart: defineAsyncComponent(() =>
      import("components/charts/ZoneChart")
    ),
  },
  data() {
    return {
      options: [
        "离开",
        "动感单车区",
        "游泳池",
        "有氧区",
        "拳击区",
        "器械区",
        "瑜伽区",
      ],
      model: "",
    };
  },
  methods: {
    clickTo() {
      if (this.model === "") {
        Notify.create({
          type: "negative",
          icon: "warning",
          message: "请选择区域",
          position: "top-right",
          timeout: 2000,
        });
      } else if (this.model === "离开") {
        let user_id = sessionStorage.getItem("user_id");

        api
          .get("http://192.168.31.88:8000/userapi/leave?user_id=" + user_id)
          .then((res) => {
            if (res.data.code == 200) {
              Notify.create({
                type: "positive",
                icon: "check_circle",
                message: "离开成功",
                position: "top-right",
                timeout: 2000,
              });
            } else {
              Notify.create({
                type: "negative",
                icon: "warning",
                message: "离开失败",
                position: "top-right",
                timeout: 2000,
              });
            }
          });
      } else {
        api
          .get("http://192.168.31.88:8000/api/xadmin/v1/zones")
          .then((res) => {
            let resArr = res.data.data;
            console.log("eeee");

            for (let i = 0; i < resArr.length; i++) {
              if (this.model == resArr[i].name) {
                let user_id = sessionStorage.getItem("user_id");
                api
                  .get(
                    "http://192.168.31.88:8000/userapi/enter_zone?user_id=" +
                      user_id +
                      "&zone_id=" +
                      resArr[i].id
                  )
                  .then((res) => {
                    console.log("eeee");
                  })
                  .catch((err) => {
                    console.log(err);
                  });
              }
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
  },
});
</script>

<style scoped>
.chart {
  height: 1000px;
}
</style>
