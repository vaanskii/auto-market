<template>
    <div class="m-10 w-full max-w-[85%] -mt-[320px] sm:-mt-80 md:mt-44 lg:mt-60 xl:mt-60">
      <div class="flex flex-col">
        <div class="rounded-xl border h-[890px] md:h-[450px] lg:h-[360px] xl:h-[270px] border-gray-200 bg-[#E6E6E6] p-6 shadow-4xl">
          <form id="opa" @submit.prevent="searchCars">
            <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
              <!-- Manufacturer -->
              <div class="flex flex-col">
                <label for="manufacturer" class="text-sm font-medium text-stone-600 uppercase">{{ $t('filter.manufacturer') }}</label>
                <select v-model="selectedManufacturer" id="manufacturer" class="mt-2 uppercase cursor-pointer text-black block w-full rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none">
                  <option disabled>Choose manufacturer</option>
                  <option 
                      v-for="(manufacturerName, index) in choices.manufacturer"
                      :key="index"
                      :value="manufacturerName"
                  >
                      {{ manufacturerName }}
                  </option>
                </select>
              </div>
              <!-- Car -->
              <div class="flex flex-col">
                <label for="car" class="text-sm font-medium text-stone-600 uppercase">{{ $t('filter.model') }}</label>
                <select v-model="selectedCarModel" id="car" class="mt-2 uppercase block w-full cursor-pointer rounded-md border text-black border-white bg-white px-2 py-2 shadow-sm outline-none">
                  <option disabled>Choose model</option>
                  <option
                      v-for="model  in carModels"
                      :key="model"
                      :value="model"
                  >
                      {{ model }}
                  </option>
                </select>
              </div>
              <!-- Gasoline -->
              <div class="flex flex-col">
                <label for="type" class="text-sm font-medium text-stone-600 uppercase">{{ $t('filter.types') }}</label>
                <select v-model="selectedType" id="type" class="mt-2 cursor-pointer uppercase text-black block w-full rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none">
                  <option disabled>Choose type</option>
                  <option 
                      v-for="(type, index) in choices.types"
                      :key="index"
                      :value="type"
                  >
                      {{ type }}
                  </option>
                </select>
                </div>
              <!-- Location -->
              <div class="flex flex-col">
                <label for="location" class="text-sm font-medium text-stone-600 uppercase">{{ $t('filter.location') }}</label>
                <select v-model="selectedLocation" id="location" class="mt-2 uppercase block w-full cursor-pointer rounded-md border text-black border-white bg-white px-2 py-2 shadow-sm outline-none">
                  <option disabled>Choose location</option>
                  <option
                      v-for="(loc, index) in choices.location"
                      :key="index"
                      :value="loc"
                  >
                      {{ loc }}
                  </option>
                </select>
              </div>
              <!-- Year Range -->
              <div class="flex flex-col">
                <label for="startYear" class="text-sm font-medium text-stone-600 uppercase">{{ $t('filter.startyear') }}</label>
                <input :placeholder="$t('filter.pl-from-year')" type="number" id="startYear" v-model="startYear" class="placeholder-black mt-2 block w-full cursor-pointer text-black rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none" />
              </div>
              <div class="flex flex-col">
                <label for="endYear" class="text-sm font-medium text-stone-600 uppercase">{{ $t('filter.endyear') }}</label>
                <input type="number" id="endYear" v-model="endYear" :placeholder="$t('filter.pl-to-year')" class="mt-2 block w-full cursor-pointer placeholder-black text-black rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none" />
              </div>

              <div class="flex flex-col">
                <label for="startPrice" class="text-sm font-medium text-stone-600 uppercase">{{ $t('filter.startprice') }}</label>
                <input :placeholder="$t('filter.pl-from-price')" type="number" id="startPrice" v-model="startPrice" class="mt-2 block w-full cursor-pointer placeholder-black text-black rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none" />
              </div>
              <div class="flex flex-col">
                <label for="endPrice" class="text-sm font-medium text-stone-600 uppercase">{{ $t('filter.endprice') }}</label>
                <input type="number" id="endPrice" v-model="endPrice" :placeholder="$t('filter.pl-to-price')" class="mt-2 block w-full cursor-pointer placeholder-black text-black rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none" />
              </div>
            </div>
            
            <div class="mt-6 grid w-full items-center grid-cols-1 justify-end md:flex">
              <div class="sm:w-full sm:space-y-4 space-y-4 md:w-full md:space-x-4 md:space-y-0 lg:w-[65.8%] xl:w-[49%] md:flex md:flex-row flex-col">
                <button type="button" @click="resetFields" class="rounded-lg  w-full bg-white px-8 py-2 font-medium text-black outline-none hover:opacity-70 focus:ring">Reset</button>
              <button type="submit" class="rounded-lg bg-[#222] px-8 py-2  w-full font-medium text-white outline-none hover:opacity-80 focus:ring">Search</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
</template>
  
<script>
import axios from 'axios';
import Trans from '@/i18n/translation'
export default {
setup() {
  return {
    Trans,
    filteredCars: [],
  }
},
data() {
  return {
    startYear: 0,
    endYear: new Date().getFullYear(),
    startPrice: 0,
    endPrice: 0,
    selectedManufacturer: 'Choose manufacturer',
    selectedCarModel: 'Choose model',
    selectedType: 'Choose type',
    selectedLocation: 'Choose location',
    choices: {
        manufacturer: [],
        car_model: {},
        types: [],
        location: [],
    },
    carModels: [],
  };
},
watch: {
  selectedManufacturer(newVal, oldVal) {
    if (newVal !== oldVal) {
      this.updateCarModels();
    }
  }
},
methods: {
fetchChoices() {
  axios
  .get('/api/choices')
  .then(response => {
      this.choices = response.data
  })
  .catch(error => {
      console.log('error: ',error)
  })
},
updateCarModels() {
    if (this.selectedManufacturer && this.choices.car_model[this.selectedManufacturer]){
        this.carModels = this.choices.car_model[this.selectedManufacturer]
    }
},
searchCars() {
  let params = {};
  if (this.selectedManufacturer && this.selectedManufacturer !== 'Choose manufacturer') {
    params.manufacturer = this.selectedManufacturer;
  }
  if (this.selectedCarModel && this.selectedCarModel !== 'Choose model') {
    params.car_model = this.selectedCarModel;
  }
  if (this.selectedType && this.selectedType !== 'Choose type') {
    params.types = this.selectedType;
  }
  if (this.selectedLocation && this.selectedLocation !== 'Choose location') {
    params.location = this.selectedLocation;
  }
  if (this.startYear) {
    params.start_year = this.startYear;
  }
  if (this.endYear) {
    params.end_year = this.endYear;
  }
  if (this.startPrice) {
    params.start_price = this.startPrice;
  }
  if (this.endPrice) {
    params.end_price = this.endPrice;
  }

  axios.get('/api/filters/', { params })
    .then(response => {
      if (Object.keys(params).length !== 0) {
        this.$router.push(this.Trans.i18nRoute({ name: 'search', query: params }));
      }
    })
    .catch(error => {
      console.error('Error searching cars:', error);
  });
},
resetFields() {
  this.selectedManufacturer = 'Choose manufacturer',
  this.selectedCarModel = 'Choose model',
  this.selectedType = 'Choose type',
  this.selectedLocation = 'Choose location',
  this.startYear = 0
  this.endYear = new Date().getFullYear(),
  this.startPrice= 0,
  this.endPrice= 0
  }
},
created() {
  this.fetchChoices()
},
computed: {
  filteredModels() {
  return this.selectedBrand ? this.cars[this.selectedBrand] : [];
  }
},
};
</script>

<style>
.shadow-4xl {
    --tw-shadow: 0 50px 100px -20px rgba(0, 0, 0, 0.4);
    --tw-shadow-colored: 0 50px 100px -20px var(--tw-shadow-color);
    box-shadow: var(--tw-ring-offset-shadow, 0 0 #0000), var(--tw-ring-shadow, 0 0 #0000), var(--tw-shadow);
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>