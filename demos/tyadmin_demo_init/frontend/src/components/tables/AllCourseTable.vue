<template>
  <q-card>
    <q-card-section class="q-pa-none">
      <q-table
               title="All course"
               :rows="data"
               :columns="columns"
               row-key="name"
               :filter="filter"
               hide-bottom
               v-model:pagination="pagination">
        <template v-slot:top-right>
          <q-input v-if="show_filter" filled borderless dense debounce="300" v-model="filter" placeholder="Search">
            <template v-slot:append>
              <q-icon name="search"/>
            </template>
          </q-input>

          <q-btn class="q-ml-sm" icon="filter_list" @click="show_filter=!show_filter" flat/>
        </template>

        <template v-slot:body-cell-Action="props">
          <q-td :props="props">
            <q-btn icon="shopping_cart" size="sm" flat dense @click="courseName= props.row.name ; courseId = props.row.id ;prompt = true" />

          </q-td>
        </template>

      </q-table>

    </q-card-section>
  </q-card>

  <q-dialog v-model="prompt" persistent>
    <q-card style="min-width: 350px">
      <q-card-section>
        <div class="text-h6">Input quantity you want to purchase</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
<!--        <q-input dense v-model="quantity" autofocus @keyup.enter="prompt = false" />-->
        <div class="q-pa-md">
          <q-input
            v-model.number="quantity"
            type="number"
            filled
            style="max-width: 200px"
            autofocus @keyup.enter="prompt = false"
          />
        </div>
      </q-card-section>

      <q-card-actions align="right" class="text-primary">
        <q-btn flat label="Cancel" v-close-popup />
        <q-btn flat label="submit" @click="gkd()" />
      </q-card-actions>
    </q-card>
  </q-dialog>
</template>

<script>
import {defineComponent , ref} from "vue";
import { Notify } from 'quasar'
import { api } from 'boot/axios'
import { getCurrentInstance } from 'vue';

const columns = [
  {name: 'course_id', label: 'Course id', field: row => row.id, sortable: true, align: 'left',format: val => `${val}`},
  {name: 'Name', label: 'Name', field: row => row.name, sortable: true, align: 'left', format: val => `${val}`},
  {name: 'Type', label: 'Type', field: row => row.type, sortable: true, align: 'left', format: val => `${val}`},
  {name: 'Price', label: 'Price', field: row => row.price, sortable: true, align: 'left', format: val => `${val}`},
  {name: 'Coach', label: 'Coach', field: row => row.coach, sortable: true, align: 'left', format: val => `${val}`},
  {name: 'Description', label: 'Description', field: row => row.description, sortable: true, align: 'left', format: val => `${val}`},
  {name: 'Action', label: 'Purchase', field: 'Action', sortable: false, align: 'center'},
];

export default defineComponent({
  name: "TableAllCourse",
  setup() {
    const show_filter = ref(false)
    let {ctx: that} = getCurrentInstance()
    return {
      filter: ref(''),
      show_filter,
      columns,
      prompt: ref(false),
      quantity:0,
      courseName:'',
      courseId:0,
      pagination: {
        rowsPerPage: 10
      },
    }
  },
  data: function (){
    return {
      data: [
        {
          id: 1,
          name: 'Spinning bike I',
          type: 'Fat reducing',
          price: '350',
          coach: 'David Wang',
          description: 'Makes you a perfect shape'
        },
        {
          name: 'Spinning bike II',
          type: 'Fat reducing',
          price: '350',
          coach: 'Lily Ann',
          description: 'Makes you a perfect shape (for woman)'
        },
        {
          name: 'Boxing I',
          type: 'Technical training',
          price: '280',
          coach: 'Ford Pink',
          description: 'Take you to master the basic boxing skill'
        },
        {
          name: 'Muscle training I',
          type: 'Build muscle',
          price: '220',
          coach: 'Kim Long',
          description: 'Help you to build a strong body with good looking'
        },
        {
          name: 'Muscle training II',
          type: 'Build muscle',
          price: '240',
          coach: 'Kim Long',
          description: 'Help you to build a strong body with good looking (ADVANCED)'
        }
      ]
    }
  },
  created() {
    // const show_filter = ref(false)
    // return {
    //   filter: ref(''),
    //   show_filter,
    //   data,
    //   columns,
    //   prompt: ref(false),
    //   quantity:0,
    //   pagination: {
    //     rowsPerPage: 10
    //   }
    // }
    this.request_data()
  },
  methods: {
    gkd() {
      let _this = this
      let flag = true

      api.get('/userapi/buy_course',{
        params: {
          user_id: sessionStorage.getItem('user_id'),
          course_id: _this.courseId,
          time:_this.quantity
        }

      }).then(function (response){
        console.log('hihi' + response)
        let res = response.data
        if(res.status === 'ok'){
          Notify.create({
            message: "Buy course succeeded",
            color: "positive"
          })
        }else{
          Notify.create({
            message: "Insufficient account balance",
            color: "negative"
          })
        }

      }).catch(function (error){
        Notify.create({
          message: "Load error",
          color: "Negative"
        })
      })

      _this.quantity = 0
      _this.courseId = 0
      _this.prompt = false
    },
    request_data()  {
      let _this = this
      let arr = []
      api.get("/api/xadmin/v1/curriculums").then(function (response) {
        console.log(response)
        let Res = response.data
        let res = Res.data
        for (let i = 0; i < res.length; i++) {
          let item = {
            id: 0,
            name: "",
            type: "",
            price: 0,
            coach: "",
            description: ""
          }
          item.id = res[i].id
          item.name = res[i].name
          item.type = res[i].type
          item.price = res[i].price
          item.coach = res[i].coach.username
          item.description = res[i].description
          arr.push(item)
        }
        _this.data = arr
        console.log(_this.data)

      }).catch(function (error) {
        Notify.create({
          message: "Load error",
          color: "Negative"
        })
      })
    }
  }
})
</script>

<style scoped>

</style>
