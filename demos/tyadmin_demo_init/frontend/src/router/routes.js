
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Login.vue') },
      { path: '/register', component: () => import('pages/Register.vue') },
      { path: '/home', component: () => import('pages/Index.vue') },
      { path: '/equipment', component: () => import('pages/Equipment.vue') },
      { path: '/booked_equipment', component: () => import('pages/Reserved_equipment.vue') },
      { path: '/profile', component: () => import('pages/Profile.vue') },
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
