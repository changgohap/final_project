<template>
  <article class="d-flex justify-content-center align-items-center col-xs-12 col-sm-3 mb-3">
    <div @click="showModal" class="card h-100" style="width: 30rem; cursor:pointer">
      <img :src="imgURL" class="card-img-top" :alt="movie.title">
    </div>

    <MovieDetailModal v-if="movieModal" @close="movieModal = false">
      <!-- <h3 slot="header">
        알림!
        <i class="fas fa-times" @click="movieModal = false"></i>
      </h3> -->
      <div slot="body">
        <iframe :src="vedioURL" frameborder="0" allowfullscreen></iframe>
        <img :src="imgURL" alt="movie.title">
      </div>
    </MovieDetailModal>
  </article>
</template>


<script>
import MovieDetailModal from '@/components/MovieDetailModal';

export default {
  name: 'MovieListItem',
  data () {
    return {
      imgURL: `https://image.tmdb.org/t/p/w500${this.movie.poster_path}`,
      vedioURL: `https://www.youtube.com/embed/${this.movie.youtube_key}?autoplay=1&mute=1`,
      movieModal: false,
    }
  },
  components: {
    MovieDetailModal,
  },
  props: {
    movie: Object,
  },
  methods: {
    showModal() {
      this.movieModal = !this.movieModal
    }
  }
}
</script>

<style>

</style>