<template>
  <div class="container">
    <section class="row">
      <MovieListItem
        v-for="movie in movies"
        :key="movie.id"
        :movie="movie"
      />
    </section>
  </div>
</template>

<script>
import MovieListItem from '@/components/MovieListItem';

export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {
    movies() {
      return this.$store.state.movies
    }
  },
  created() {
    this.$store.dispatch('getMovies')
  }
}
</script>

<style>
  .border-here {
    border: 1px solid lightgray;
  }

</style>