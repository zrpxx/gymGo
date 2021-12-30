<template>
  <q-layout view="lHh Lpr lFf">
    <q-header
      elevated
      v-if="this.$route.path !== '/' && this.$route.path !== '/register'"
    >
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          @click="toggleLeftDrawer"
          icon="menu"
          aria-label="Menu"
        />
        <q-toolbar-title> GymGo </q-toolbar-title>
        <q-space />
        <div class="q-gutter-sm row items-center no-wrap"></div>
        <q-btn round flat>
          <q-avatar size="26px">
            <img src="https://cdn.quasar.dev/img/boy-avatar.png" />
          </q-avatar>
        </q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      class="bg-primary text-white"
      v-if="this.$route.path !== '/' && this.$route.path !== '/register'"
    >
      <q-list class="q-mt-xl">
        <!--        预约-->
        <q-item
          class="q-my-sm"
          to=""
          active-class="q-item-no-link-highlighting"
        >
          <q-item-section avatar>
            <q-icon name="date_range" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Agenda</q-item-label>
          </q-item-section>
        </q-item>

        <!--  课程      -->
        <q-expansion-item
          class="q-my-sm"
          icon="insert_chart"
          label="Curriculum"
        >
          <q-list class="q-pl-lg">
            <q-item to="/all_course" active-class="q-item-no-link-highlighting">
              <q-item-section>
                <q-item-label>All course</q-item-label>
              </q-item-section>
            </q-item>
            <q-item
              to="/purchased_course"
              active-class="q-item-no-link-highlighting"
            >
              <q-item-section>
                <q-item-label>Purchased</q-item-label>
              </q-item-section>
            </q-item>

            <q-item
              to="/course_history"
              active-class="q-item-no-link-highlighting"
            >
              <q-item-section>
                <q-item-label>History</q-item-label>
              </q-item-section>
            </q-item>

            <q-item
              to="/appointment"
              active-class="q-item-no-link-highlighting"
            >
              <q-item-section>
                <q-item-label>Appointment</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-expansion-item>
        <q-expansion-item class="q-my-sm" icon="dashboard" label="Equipment">
          <q-list class="q-pl-lg">
            <q-item to="/equipment" active-class="q-item-no-link-highlighting">
              <q-item-section>
                <q-item-label>All equipment</q-item-label>
              </q-item-section>
            </q-item>
            <q-item
              to="/booked_equipment"
              active-class="q-item-no-link-highlighting"
            >
              <q-item-section>
                <q-item-label>My booked</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </q-expansion-item>

        <q-item
          to="/locker"
          active-class="q-item-no-link-highlighting"
          class="q-my-sm"
        >
          <q-item-section avatar>
            <q-icon name="map" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Locker</q-item-label>
          </q-item-section>
        </q-item>
        <q-item
          to="/zone"
          active-class="q-item-no-link-highlighting"
          class="q-my-sm"
        >
          <q-item-section avatar>
            <q-icon name="dashboard" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Zone</q-item-label>
          </q-item-section>
        </q-item>
        <q-item
          to="/profile"
          active-class="q-item-no-link-highlighting"
          class="q-my-sm"
        >
          <q-item-section avatar>
            <q-icon name="person" />
          </q-item-section>
          <q-item-section>
            <q-item-label>Profile</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container class="bg-grey-2">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import EssentialLink from "components/EssentialLink.vue";

import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "MainLayout",

  components: {
    // eslint-disable-next-line vue/no-unused-components
    EssentialLink,
  },

  setup() {
    const leftDrawerOpen = ref(false);

    return {
      //essentialLinks: linksList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>
