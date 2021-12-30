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
      label="前往"
      type="submit"
      color="primary"
    />
  </div>
  <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12">
    <zone-chart></zone-chart>
  </div>
</template>

<script>
import { Notify } from "quasar";

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
      setTimeout(() => {
        this.$router.go("0");
      }, 2000);
      this.$q
        .dialog({
          title: "Confirm",
          message: "Are sure to enter this zone?",
          cancel: true,
          persistent: true,
        })
        .onOk(() => {
          setTimeout(() => {}, 100);
        })
        .onCancel(() => {
          return;
        })
        .onDismiss(() => {
          return;
        });
      if (this.model === "") {
        Notify.create({
          type: "negative",
          icon: "warning",
          message: "请选择区域",
          position: "bottom",
          timeout: 2000,
        });
      } else if (this.model === "离开") {
        let user_id = sessionStorage.getItem("user_id");
        api
          .get("/userapi/leave?user_id=" + user_id)
          .then(() => {
            // if (res.data.code == 200) {
            //   Notify.create({
            //     type: "positive",
            //     icon: "check_circle",
            //     message: "离开成功",
            //     position: "bottom",
            //     timeout: 2000,
            //   });
            // } else {
            //   Notify.create({
            //     type: "negative",
            //     icon: "warning",
            //     message: "离开失败",
            //     position: "bottom",
            //     timeout: 2000,
            //   });
            // }
          })
          .catch((err) => {
            Notify.create({
              type: "negative",
              icon: "warning",
              message: "离开失败",
              position: "bottom",
              timeout: 2000,
            });
            console.log(err);
          });
      } else {
        api
          .get("/api/xadmin/v1/zones")
          .then((res) => {
            let resArr = res.data.data;
            console.log("eeee");

            for (let i = 0; i < resArr.length; i++) {
              if (this.model === resArr[i].name) {
                let user_id = sessionStorage.getItem("user_id");
                api
                  .get(
                    "/userapi/enter_zone?user_id=" +
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
