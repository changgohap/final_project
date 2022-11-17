<template>
  <div id="app">
    <nav>
      <h3>MDDM</h3>
      <router-link :to="{ name: 'movies' }">Movie</router-link> |
      <router-link :to="{ name: 'articles' }">Article</router-link> |
      <router-link :to="{ name: 'profile' }">Profile</router-link> | 
      <router-link :to="{ name: 'login' }">Login</router-link> | 
      <router-link :to="{ name: 'signup' }">SignUp</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
