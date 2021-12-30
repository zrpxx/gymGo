
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: '/register', component: () => import('pages/Register.vue') },
      { path: '/login', component: () => import('pages/Login.vue') },
      { path: '/all_course', component: () => import('pages/AllCourse.vue') },
      { path: '/purchased_course', component: () => import('pages/PurchaseCourse') },
      { path: '/course_history', component: () => import('pages/CourseHistory') },
      { path: '/appointment', component: () => import('pages/MyAppointment') },
      { path: '/home', component: () => import('pages/Index.vue') },
      { path: '/equipment', component: () => import('pages/Equipment.vue') },
      { path: '/booked_equipment', component: () => import('pages/Reserved_equipment.vue') },
      { path: '/profile', component: () => import('pages/Profile.vue') },
      { path: '/login', component: () => import('pages/Login.vue') },
      { path: '/zone', component: () => import('pages/Zone.vue') },
      { path: '/class', component: () => import('pages/Class.vue') },
      { path: '/locker', component: () => import('pages/Locker.vue') },

    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
