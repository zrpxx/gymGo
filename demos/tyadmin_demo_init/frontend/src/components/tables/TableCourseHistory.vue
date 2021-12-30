<template>
  <q-card>
    <q-card-section class="q-pa-none">
      <q-table
        title="All course"
        :rows="data"
        :columns="columns"
        row-key="name"
        :filter="filter"
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
            <q-btn icon="edit" :disable="props.row.rating !== -1" size="sm" flat dense @click="show_review_dialog(props.row.id)" />
          </q-td>
        </template>

      </q-table>

    </q-card-section>
  </q-card>

  <q-dialog v-model="prompt" persistent>
    <q-card style="min-width: 350px">
      <q-card-section>
        <div class="text-h6">Add review of attendance # {{ review_id }}</div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        <!--        <q-input dense v-model="quantity" autofocus @keyup.enter="prompt = false" />-->
        <div class="q-pa-md">
          <q-input
            v-model.number="star"
            placeholder="Stars (1-5)"
            type="number"
            filled
            style="max-width: 200px"
            :rules="[val => 1<=val<=5 || 'The score must between 1 and 5']"
            autofocus
          />
          <q-input
            v-model="review_text"
            placeholder="Your review text"
            filled
            style="max-width: 200px"
            required
            autofocus
          />
        </div>
      </q-card-section>

      <q-card-actions align="right" class="text-primary">
        <q-btn flat label="Cancel" v-close-popup />
        <q-btn flat label="submit" @click="submit_review()" />
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
  {name: 'id', label: 'ID', field: row => row.id, sortable: false},
  {name: 'course_id', label: 'Course id', field: row => row.course_id, sortable: false, align: 'left',format: val => `${val}`},
  {name: 'coach_id', label: 'Coach id', field: row => row.coach_id, sortable: false, align: 'left',format: val => `${val}`},
  {name: 'Course_date', label: 'Course date', field: row => row.course_date_time, sortable: false, align: 'left', format: val => `${val}`},
  {name: 'Coach desc', label: 'Coach description', field: row => row.coach_description, sortable: false, align: 'left', format: val => `${val}`},
  {name: 'rating', label: 'Customer rating (stars)', field: row => row.rating, sortable: false, align: 'left', format: val => val === -1 ? 'N/A' : `${val}`},
  {name: 'review', label: 'Review', field: row => row.review, sortable: false, align: 'center'},
  {name: 'Action', label: 'Action', field: row => row.action, sortable: false, align: 'center'}
];

export default defineComponent({
  name: "TableAllCourse",
  setup() {
    const show_filter = ref(false)
    return {
      filter: ref(''),
      show_filter,
      columns,
      pagination: {
        rowsPerPage: 20
      },
    }
  },
  data() {
    return {
      data: [],
      review_id: -1,
      star: null,
      review_text: "",
      prompt: false
    }
  },
  created() {
    api.get('/userapi/get_user_attend', {
      params: {
        user_id: sessionStorage.getItem('user_id')
      }
    }).then(res => {
      console.log(res)
      this.data = res.data.data
    })
  },
  methods: {
    show_review_dialog(id) {
      this.review_id = id
      this.prompt = true
    },
    submit_review() {
      if(this.star > 5 || this.star < 0)
      {
        Notify.create({
          message: 'Invalid star!',
          type: 'negative'
          }
        )
        return
      }
      if(this.review_text === "")
      {
        Notify.create({
            message: 'Please input your review!',
            type: 'negative'
          }
        )
        return
      }
      api.post('/api/xadmin/v1/reviews', {
        rating: this.star,
        review_text: this.review_text,
        attend_course: this.review_id
      }).then(res => {
        console.log(res)
        Notify.create({
          message: 'Success',
          type: 'postive'
        })
        this.prompt = false
        this.$router.go(0)
      }).catch(err => {
        console.log(err)
        Notify.create({
          message: 'Internal error',
          type: 'negative'
        })
      })
    }
  }
})
</script>

<style scoped>

</style>

