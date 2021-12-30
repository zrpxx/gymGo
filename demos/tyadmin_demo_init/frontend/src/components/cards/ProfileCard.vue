<template>
  <q-card class="bg-transparent no-shadow no-border">
    <q-card-section class="q-pa-none">
      <div class="row q-col-gutter-sm ">
        <div class="col-md-3 col-sm-12 col-xs-12">
          <q-item :style="`background-color: #546bfa`" class="q-pa-none" clickable @click="charge">
            <q-item-section class=" q-pa-md q-ml-none  text-white">
              <q-item-label class="text-white text-h6 text-weight-bolder">$ {{ balance }}</q-item-label>
              <q-item-label>Balance</q-item-label>
            </q-item-section>
            <q-item-section  side class="q-mr-md text-white">
              <q-icon name="account_balance" color="white" size="44px"></q-icon>
            </q-item-section>

            <q-popup-proxy transition-show="flip-up" transition-hide="flip-down">
              <q-card class="my-card" >
                <q-card-section class="bg-teal text-white">
                  <div class="text-h6">The amount you want to top up</div>
                </q-card-section>

                <q-space></q-space>

                <q-card-actions vertical align="center">
                  <q-input
                    class="amount"
                    filled
                    v-model="Amount"
                    label="Recharge amount"
                  />
                  <q-space></q-space>
                  <q-btn class="confirm">Confirm</q-btn>
                </q-card-actions>
              </q-card>
            </q-popup-proxy>

          </q-item>
        </div>

        <div class="col-md-3 col-sm-12 col-xs-12">
          <q-item :style="`background-color:#3a9688`" class="q-pa-none">
            <q-item-section class=" q-pa-md q-ml-none  text-white">
              <q-item-label class="text-white text-h6 text-weight-bolder">$ {{ recharge }}</q-item-label>
              <q-item-label>Total recharge</q-item-label>
            </q-item-section>
            <q-item-section  side class="q-mr-md text-white">
              <q-icon :name="attach_money" color="white" size="44px"></q-icon>
            </q-item-section>
          </q-item>
        </div>

          <div class="col-md-3 col-sm-12 col-xs-12">
            <q-item :style="`background-color: #7cb342`" class="q-pa-none">
              <q-item-section class=" q-pa-md q-ml-none  text-white">
                <q-item-label class="text-white text-h6 text-weight-bolder">{{ level }}</q-item-label>
                <q-item-label>VIP level</q-item-label>
              </q-item-section>
              <q-item-section  side class="q-mr-md text-white">
                <q-icon :name="grade" color="white" size="44px"></q-icon>
              </q-item-section>
            </q-item>
          </div>

        <div class="col-md-3 col-sm-12 col-xs-12">
          <q-item :style="`background-color: #f88c2b`" class="q-pa-none">
            <q-item-section class=" q-pa-md q-ml-none  text-white">
              <q-item-label class="text-white text-h6 text-weight-bolder">{{ username }}</q-item-label>
              <q-item-label>NAME</q-item-label>
            </q-item-section>
            <q-item-section  side class="q-mr-md text-white">
              <q-icon name="person" color="white" size="44px"></q-icon>
            </q-item-section>
          </q-item>
        </div>
        <q-space></q-space>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
import {defineComponent} from 'vue'

export default defineComponent({
  name: "ProfileCard",
  props: ['username', 'level', 'recharge', 'balance']
})
</script>

<style scoped>
.confirm{
  width: 90%;
  margin-top: 10%;
}
.amount{
  width: 90%;
}
</style>
