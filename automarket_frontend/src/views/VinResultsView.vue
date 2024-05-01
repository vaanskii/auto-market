<template>
  <div class="pt-14">
    <div v-if="vinData" class="flex mt-10 justify-center overflow-x-auto items-center flex-col">
      <h3 class="uppercase font-bold md:text-4xl text-xl mt-10">{{ $t('vin.information') }}</h3>
      <div class="overflow-x-auto mt-10 shadow-2xl bg-zinc-200">
        <table class="min-w-full shadow-2xl table-auto border-collapse border border-gray-200">
          <tbody>
            <tr v-for="(value, key) in vinData" :key="key" class="hover:bg-gray-100">
              <td class="border md:max-w-full max-w-[15rem] truncate md:text-lg text-xs uppercase border-black px-4 py-2">{{ key }}</td>
              <td class="border md:text-lg text-xs uppercase border-black px-4 py-2">{{ value || 'no-info' }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <div v-else class="h-screen">
      <p class="text-center text-4xl mt-80">{{ $t('vin.loading') }}</p>
      <div id="loading-bar-spinner" class="spinner"><div class="spinner-icon"></div></div>
    </div>
  </div>
</template>


<script>
import axios from 'axios';
import Trans from '@/i18n/translation';
export default {
  setup() {
    return {
      Trans
    }
  },
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
              Object.entries(response.data).map(([key, value]) => [key, value || 'NO INFORMATION PROVIDED'])
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
    },
    setPageTitle(title) {
      document.title = title
    }
  },
  mounted() {
    this.setPageTitle('Vin results');
  }
};
</script>

<style scoped>
#loading-bar-spinner.spinner {
    left: 50%;
    margin-left: -20px;
    top: 50%;
    margin-top: -20px;
    position: absolute;
    z-index: 19 !important;
    animation: loading-bar-spinner 400ms linear infinite;
}

#loading-bar-spinner.spinner .spinner-icon {
    width: 40px;
    height: 40px;
    border:  solid 4px transparent;
    border-top-color:  black !important;
    border-left-color: black !important;
    border-radius: 50%;
}

@keyframes loading-bar-spinner {
    0%   { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

</style>