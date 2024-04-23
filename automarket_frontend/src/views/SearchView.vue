<template>
  <div class="pt-14">
    <h1>Search results</h1>
  </div>
</template>

<script>
import axios from 'axios'
export default {
data() {
  return {
    query: this.$route.query.q || ''
  }
},
watch: {
$route(to, from) {
  this.query = to.query.q || '';
  this.fetchSearchResults();
},
},
methods: {
fetchSearchResults() {
  const params = this.$route.query
  axios.get('/api/filters/', { params })
    .then(response => {
      console.log('Filtered results:', response.data);
    })
    .catch(error => {
      console.error('Error fetching search results:', error);
    });
  }
},
mounted() {
  this.fetchSearchResults()
}
}
</script>