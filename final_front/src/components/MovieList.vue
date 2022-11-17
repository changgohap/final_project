<template>
  <div class="border-here">
    <h3>MovieList</h3>
    <MovieListItem/>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem';

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  }
}
</script>

<style>
  .border-here {
    border: 1px solid lightgray;
  }

</style>