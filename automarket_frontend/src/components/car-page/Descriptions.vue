<template>
    <div class="md:w-[70%] w-[80%] bg-[#E6E6E6] shadow-xl rounded-xl mt-10 flex items-center flex-col py-10">
        <h1 class="uppercase mb-4 text-lg font-bold">{{ $t('description.header') }}</h1>
        <hr class="h-px  bg-black my-4 w-[80%] border-0">
        <p class="px-10">{{ carDescription }}</p>
    </div>
    <div class="md:w-[70%] w-[80%] bg-[#E6E6E6] shadow-xl rounded-xl mt-10">
    <h1 class="uppercase mb-4 text-center text-lg font-bold mt-8">{{ $t('description.specifications') }}</h1>
    <div class="flex justify-center">
      <hr class="h-px bg-black my-4 w-[80%] border-0">
    </div>
    <dl class="flex flex-col items-center justify-center py-10 w-full">
      <div v-for="(spec, key) in specifications" :key="key" class="flex flex-row justify-between md:w-[80%] w-[90%] hover:px-3 hover:rounded-lg cursor-pointer">
        <dt class="uppercase text-start grid gap-y-4 md:text-[16px] sm:text-[16px] mb-4 text-[10px]">{{ $t('description.' + key.toLowerCase()) }}:</dt>
        <dd class="uppercase text-start grid gap-y-4 md:text-[16px] sm:text-[16px] mb-4 text-[10px]">{{ spec }}</dd>
      </div>
    </dl>
  </div>

</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      specifications: {},
      carDescription: ''
    };
  },
  methods: {
  getCars() {
    axios
      .get(`/api/${this.$route.params.id}/`)
      .then(response => {
        const carData = response.data.car
          this.specifications = {
            manufacturer: carData.manufacturer,
            model: carData.car_model,
            year: carData.year,
            category: carData.categories,
            enginevolume: carData.engine_volume,
            mileage: carData.milage + ' km',
            fueltype: carData.fuel_type,
            gearbox: carData.transmission,
            cylinders: carData.cylinders,
            doors: carData.doors,
            drivewheels: carData.drive_wheels,
            wheel: carData.wheel,
            airbags: carData.airbags,
            color: carData.car_colors,
            interiormaterial: carData.interior,
            interiorcolor: carData.interior_color,
          },
          this.carDescription = carData.description
      })
      .catch(error => {
        console.log('error:', error)
      })
    }
  },
  mounted() {
    this.getCars()
  }
};
</script>