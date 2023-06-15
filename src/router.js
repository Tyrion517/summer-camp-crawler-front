import { createWebHistory, createRouter } from "vue-router";

const routes = [
    {
        path: '/:name',
        component: () => import('@/components/ListData.vue'),
    }
]


const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router;