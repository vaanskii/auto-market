<template>
  <div class="vin-decoder pt-14">
    <div v-if="vinData">
      <h3>Vehicle Information</h3>
      <ul>
        <li v-for="(value, key) in vinData" :key="key">
          <strong>{{ key.split('_').join(' ') }}:</strong> {{ value || 'no-info' }}
        </li>
      </ul>
    </div>
    <div v-else>
      <p>Loading VIN data...</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      vinData: null,
      error: null
    };
  },
  created() {
    this.decodeVin();
  },
  methods: {
    decodeVin() {
      const vin = this.$route.query.q;
      if (vin) {
        axios.get(`/api/vin/?vin=${vin}`)
          .then(response => {
            this.vinData = Object.fromEntries(
              Object.entries(response.data).map(([key, value]) => [key, value || 'No information provided'])
            );
            this.error = null;
          })
          .catch(error => {
            console.error('Error decoding VIN:', error);
            this.vinData = null;
            this.error = 'Failed to decode VIN. Please try again.';
          });
      } else {
        this.error = 'No VIN provided.';
      }
    }
  }
};
</script>
