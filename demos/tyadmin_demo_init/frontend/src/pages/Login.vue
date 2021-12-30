<template>
  <q-layout>
    <q-page-container>
      <q-page class="flex bg-image flex-center">
        <q-card v-bind:style="$q.screen.lt.sm?{'width': '80%'}:{'width':'30%'}">
          <q-card-section>
            <q-avatar size="103px" class="absolute-center shadow-10">
              <img src="https://cdn.quasar.dev/img/avatar.png">
            </q-avatar>
          </q-card-section>
          <q-card-section>
            <div class="text-center q-pt-lg">
              <div class="col text-h6 ellipsis">
                Log in
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
                :rules="[ val => val && val.length > 0 || 'Please input your username']"
              />

              <div>
                <q-btn class="login" label="Login" type="button" color="primary" @click="tryLogin"/>
              </div>
              <div>
                <q-btn to="/register" class="login" label="Register" type="button" color="primary"/>
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
      password: ''
    }
  },
  methods:{
    tryLogin(){
      let _this=this
      this.$api.get('/userapi/login',{
        params: {
          username:this.username,
          password:this.password
        }
      }).then(function (response) {
        console.log(response)
        let res=response.data
        if(res.status=="ok"){
          sessionStorage.setItem('user_id', res.id)
          _this.$router.push('/profile')
        }else {
          Notify.create(
            {
              type: 'negative',
              message: 'username or password error'
            })
        }
      }).catch(function (error) {
        Notify.create({
          message:""
        })
          console.log(error)
      })
    }
  }
}
</script>

<style>
.bg-image {
  background-image: linear-gradient(135deg, #7028e4 0%, #e5b2ca 100%);
}
.login{
  width: 100%;
}
</style>
