<template>
  <div class="pt-14">
    <div v-if="cars.length" v-for="car in cars" :key="car.id">
      <div class="bg-gray-300 mb-10">
        <h1>{{ car.location }}</h1>
        <img v-if="car.main_image" :src="car.main_image.image_url" class="w-96 cursor-pointer">
        <h1 class="cursor-pointer"><span class="font-bold">{{ car.manufacturer }}</span> - {{ car.car_model }} </h1>
        <p>{{ car.price }} $</p>
      </div>
    </div>
  </div>
</template>


<script>
import axios from 'axios'
export default {
data() {
  return {
    query: this.$route.query.q || '',
    cars: []
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
      this.cars = response.data
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