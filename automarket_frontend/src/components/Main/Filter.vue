<template>
    <div class="m-10 w-full max-w-[85%] -mt-[320px] sm:-mt-80 md:mt-44 lg:mt-60 xl:mt-80">
      <div class="flex flex-col">
        <div class="rounded-xl border h-[890px] md:h-[450px] lg:h-[360px] xl:h-[270px] border-gray-200 bg-[#E6E6E6] p-6 shadow-4xl">
          <form id="opa" @submit.prevent="handleSubmit">
            <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
              <!-- Manufacturer -->
              <div class="flex flex-col">
                <label for="manufacturer" class="text-sm font-medium text-stone-600 uppercase">Manufacturer</label>
                <select v-model="selectedBrand" id="manufacturer" class="mt-2 text-black block w-full rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none">
                  <option>BMW</option>
                  <option>MERCEDES</option>
                  <option>AUDI</option>
                </select>
              </div>
              <!-- Car -->
              <div class="flex flex-col">
                <label for="car" class="text-sm font-medium text-stone-600 uppercase">Car</label>
                <select v-model="selectedCar" id="car" class="mt-2 block w-full cursor-pointer rounded-md border text-black border-white bg-white px-2 py-2 shadow-sm outline-none">
                  <option v-for="(car, index) in filteredCars" :key="index">{{ car }}</option>
                </select>
              </div>
              <!-- Gasoline -->
              <div class="flex flex-col">
                <label for="type" class="text-sm font-medium text-stone-600 uppercase">Types</label>
                <select v-model="selectedType" id="type" class="mt-2 text-black block w-full rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none">
                    <option>FOR SELL</option>
                    <option>FOR RENT</option>
                </select>
                </div>
              <!-- Location -->
              <div class="flex flex-col">
                <label for="location" class="text-sm font-medium text-stone-600 uppercase">Location</label>
                <select id="location" class="mt-2 block w-full cursor-pointer rounded-md border text-black border-white bg-white px-2 py-2 shadow-sm outline-none">
                  <option value="">TBILISI</option>
                  <option value="">BATUMI</option>
                  <option value="">KUTAISI</option>
                </select>
              </div>
              <!-- Year Range -->
              <div class="flex flex-col">
                <label for="startYear" class="text-sm font-medium text-stone-600 uppercase">Start Year</label>
                <input placeholder="FROM" type="number" id="startYear" v-model="startYear" class="placeholder-black mt-2 block w-full cursor-pointer text-black rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none" />
              </div>
              <div class="flex flex-col">
                <label for="endYear" class="text-sm font-medium text-stone-600 uppercase">End Year</label>
                <input type="number" id="endYear" v-model="endYear" placeholder="TO" class="mt-2 block w-full cursor-pointer placeholder-black text-black rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none" />
              </div>

              <div class="flex flex-col">
                <label for="startPrice" class="text-sm font-medium text-stone-600 uppercase">start price</label>
                <input placeholder="FROM" type="number" id="startPrice" v-model="startPrice" class="mt-2 block w-full cursor-pointer placeholder-black text-black rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none" />
              </div>
              <div class="flex flex-col">
                <label for="endPrice" class="text-sm font-medium text-stone-600 uppercase">End price</label>
                <input type="number" id="endPrice" v-model="endPrice" placeholder="TO" class="mt-2 block w-full cursor-pointer placeholder-black text-black rounded-md border border-white bg-white px-2 py-2 shadow-sm outline-none" />
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
export default {
data() {
    return {
    selectedBrand: '',
    selectedCar: '',
    selectedType: '',
    startYear: '',
    endYear: '',
    startPrice: '',
    endPrice: '',
    cars: {
        BMW: ['BMW - 5 SERIES', 'BMW - 3 SERIES', 'BMW - X5'],
        MERCEDES: ['MERCEDES - E CLASS', 'MERCEDES - C CLASS', 'MERCEDES - GLE'],
        AUDI: ['AUDI - A4', 'AUDI - Q5', 'AUDI - TT']
    }
    };
},
computed: {
    filteredCars() {
    return this.selectedBrand ? this.cars[this.selectedBrand] : [];
    }
},
methods: {
    resetFields() {
    this.selectedBrand = '',
    this.selectedCar = '',
    this.selectedType = '',
    this.startYear = '',
    this.endYear = '',
    this.startPrice= '',
    this.endPrice= ''
    }
}
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