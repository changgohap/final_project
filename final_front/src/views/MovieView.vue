<template>
  <div class="border-here">
    <h1>MovieView</h1>
    <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'MovieView',
  components: {
    MovieList,
  }
}
</script>

<style>
  .border-here {
    border: 1px solid lightblue;
  }

</style>