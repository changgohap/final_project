import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/MovieView'
import ArticleView from '@/views/ArticleView'
import MyProfile from '@/views/MyProfile'
import LoginView from '@/views/LoginView'
import SignUpView from '@/views/SignUpView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movies',
    component: MovieView
  },
  {
    path: '/articles',
    name: 'articles',
    component: ArticleView
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/signup',
    name: 'signup',
    component: SignUpView
  },
  {
    path: '/profile',
    name: 'profile',
    component: MyProfile,
    children: [
      {
        path: 'recommendation',
        name: 'recommendation',
        component: () => import('@/views/MyRecommendation')
      },
      {
        path: 'myArticles',
        name: 'myArticles',
        component: () => import('@/views/MyArticleList')
      },
      {
        path: 'myComments',
        name: 'myComments',
        component: () => import('@/views/MyCommentList')
      },
      {
        path: 'myReviews',
        name: 'myReviews',
        component: () => import('@/views/MyReviewList')
      },
      {
        path: 'myLikes',
        name: 'myLikes',
        component: () => import('@/views/MyLikeList')
      },
    ]
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
