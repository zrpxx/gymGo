<template>
  <q-layout>
    <q-page-container>
      <q-page class="flex bg-image flex-center">
        <q-card v-bind:style="$q.screen.lt.sm?{'width': '80%'}:{'width':'30%'}">
<!--          <q-card-section>-->
<!--            <q-avatar size="103px" class="absolute-center shadow-10">-->
<!--              <img src="https://cdn.quasar.dev/img/avatar.png">-->
<!--            </q-avatar>-->
<!--          </q-card-section>-->
          <q-card-section>
            <div class="text-center q-pt-lg">
              <div class="col text-h6 ellipsis">
                Register your Account
              </div>
            </div>
          </q-card-section>
          <q-card-section>
            <q-form
              class="q-gutter-md"
            >
              <q-input
                filled
                v-model="username"
                label="Username"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Please input your username']"
              />

              <q-input
                type="password"
                filled
                v-model="password"
                label="Password"
                lazy-rules
                :rules="[ val => val && val.length > 0 || 'Please input your password']"

              />
              <q-input
                type="password"
                filled
                v-model="confirm"
                label="confirm"
              />

              <div>
                <q-btn class="register" label="Register" type="button" color="primary" @click="tryRegister"/>
              </div>
            </q-form>
          </q-card-section>
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>

import {Notify} from "quasar";

export default {
  data () {
    return {
      username: '',
      password: '',
      confirm:''
    }
  },
  methods:{
    tryRegister(){
      let _this=this
      this.$api.get('/userapi/register',{
        params: {
          username:this.username,
          password:this.password
        }
      }).then(function (response) {
        console.log(response)
        console.log(response)
        let res = response.data
        if(res.status === "ok") {
          Notify.create(
            {
              type: 'positive',
              message: 'Success'
            })
          _this.$router.push("/")
        }else if (res.status === "Failed" && res.message === "User exist") {
          Notify.create(
            {
              type: 'negative',
              message: 'User exist'
            })
        } else{
          Notify.create(
            {
              type: 'negative',
              message: 'error'
            })
        }
      }).catch(function (error) {
          console.log(error)
        Notify.create(
          {
            type: 'negative',
            message: '内部错误'
          })
      })
    }
  }
}
</script>

<style scoped>
.bg-image {
  background-image: linear-gradient(135deg, #7028e4 0%, #e5b2ca 100%);
}
.register{
  width: 100%;
}
</style>
