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
            <q-btn icon="edit" size="sm" flat dense @click="courseName= props.row.name ; courseId = props.row.name ;prompt = true" />

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
            v-model.number="score"
            type="number"
            filled
            style="max-width: 200px"
            :rules="[val => 1<=val<=5 || 'The score must between 1 and 5']"
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
  {name: 'course_id', label: 'Course id', field: row => row.course_id, sortable: true, align: 'left',format: val => `${val}`},
  {name: 'customer_id', label: 'Customer id', field: row => row.user_id, sortable: true, align: 'left',format: val => `${val}`},
  {name: 'Course_date', label: 'Course date', field: row => row.date, sortable: true, align: 'left', format: val => `${val}`},
  {name: 'Evaluation', label: 'Evaluation from coach', field: row => row.des, sortable: true, align: 'left', format: val => `${val}`},
  {name: 'Evaluation2', label: 'Evaluation of this course (stars)', field: row => row.score, sortable: true, align: 'left', format: val => `${val}`},
  {name: 'Action', label: 'Operate', field: 'Action', sortable: false, align: 'center'},
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
      score:0,
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
          course_id: 1,
          user_id:2,
          date: '2021-12-30-07:50',
          des: 'Good',
          score: '5',
        },
        {
          course_id: 1,
          user_id:2,
          date: '2021-12-30-07:50',
          des: 'Good',
          score: '4',
        },
        {
          course_id: 1,
          user_id:2,
          date: '2021-12-30-07:50',
          des: 'Good',
          score: '3',
        },
      ]
    }
  },
  created() {

    this.request_data()
  },
  methods: {
    gkd() {
      let _this = this
      let flag = true

      api.post('',{
        customer: sessionStorage.getItem('user_id'),
        course: _this.courseId,
        course_left:_this.score
      }).then(function (response){
        console.log('hihi' + response)

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
      api.get("api/xadmin/v1/attends").then(function (response1) {

        api.get("api/xadmin/v1/reviews",).then(function (response2){

          //console.log(response1)
          let Res = response1.data
          let res = Res.data
          let Res2 = response2
          let res2 = Res2.data

          for (let i = 0; i < res.length; i++) {
            for (let j = 0; j < res2.length; j++) {
              if(res[i].user_id === sessionStorage.getItem('user_id')){
                let item = {
                  course_id: 0,
                  user_id: "",
                  date: "",
                  des: "",
                  score: ""
                }
                item.course_id = res[i].course
                item.name = res[i].name
                item.date = res[i].course_date_time
                item.coach = res[i].coach
                item.description = res[i].description
                if(res2[j].user_id === res[i].user_id){
                  item.score = res2[j].score
                }
                arr.push(item)

              }
            }
          }
          _this.data = arr
          console.log(_this.data)
        })

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

