<template>
  <q-card>
    <q-card-section class="q-pa-none">
      <q-table
        title="Purchased course"
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
            <q-btn icon="shopping_cart" size="sm" flat  @click="courseName= props.row.name ; courseId = props.row.name ;prompt = true" />
            <q-btn icon="bookmark_add" size="sm" flat   />

          </q-td>
        </template>


      </q-table>

    </q-card-section>
  </q-card>

  <q-dialog v-model="prompt" persistent>
    <q-card style="min-width: 350px">
      <q-card-section>
        <div class="text-h6">Input quantity you want to purchase more</div>
      </q-card-section>

      <q-card-section class="q-pt-none">

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
  {name: 'Coach', label: 'Coach', field: row => row.coach, sortable: true, align: 'left', format: val => `${val}`},
  {name: 'Remaining_course', label: 'Remaining course', field: row => row.remaining, sortable: true, align: 'left', format: val => `${val}`},
  {name: 'Action', label: 'Operate', field: 'Action', sortable: false, align: 'center'},
];

export default defineComponent({
  name: "TablePurchasedCourse",
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
          coach: 'David Wang',
          remaining: 6
        },
        {
          id: 4,
          name: 'Spinning bike II',
          coach: 'David Wang',
          remaining: 3
        },
        {
          id: 3,
          name: 'Boxing',
          coach: 'David Li',
          remaining: 6
        }
      ]
    }
  },
  created() {

    this.request_data()
  },
  methods: {
    gkd() {
      let _this = this

      api.post('/api/xadmin/v1/buys',{
        customer: sessionStorage.getItem('user_id'),
        course: _this.courseId,
        course_left:_this.quantity
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
      api.get("").then(function (response) {
        console.log(response)
        let Res = response.data
        let res = Res.data
        for (let i = 0; i < res.length; i++) {
          let item = {
            id: 0,
            name: "",
            coach: "",
            remaining: 0
          }
          item.id = res[i].id
          item.name = res[i].name
          item.coach = res[i].coach
          item.remaining = res[i].remaining
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
