<template>
    <div class="m-10 w-screen max-w-screen-md md:mt-24 mt-56">
      <div class="flex flex-col">
        <div class="rounded-xl border border-gray-200 bg-white p-6 shadow-lg">
          <form id="opa">
            <div class="grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
              <div class="flex flex-col text-black">
                <label for="date" class="text-sm font-medium text-stone-600 uppercase">MANUFACTURER</label>
                <select v-model="selectedBrand" class="mt-2 block w-full rounded-md border border-gray-100 bg-gray-100 px-2 py-2 shadow-sm outline-none">
                    <option>BMW</option>
                    <option>MERCEDES</option>
                    <option>AUDI</option>
                </select>
              </div>
              <div class="flex flex-col">
                <label for="date" class="text-sm font-medium text-stone-600 uppercase">car</label>
                <select v-model="selectedCar" class="mt-2 block w-full cursor-pointer rounded-md border text-black border-gray-100 bg-gray-100 px-2 py-2 shadow-sm outline-none">
                  <option v-for="(car, index) in filteredCars" :key="index">{{ car }}</option>
                </select>
              </div>
              <div class="flex flex-col">
                <label for="date" class="text-sm font-medium text-stone-600 uppercase">Location</label>
                <select class="mt-2 block w-full cursor-pointer rounded-md border text-black border-gray-100 bg-gray-100 px-2 py-2 shadow-sm outline-none">
                    <option value="">TBILISI</option>
                    <option value="">BATUMI</option>
                    <option value="">KUTAISI</option>
                </select>
              </div>
              <div class="flex flex-col">
                <label for="date" class="text-sm font-medium text-stone-600 uppercase">year</label>
                <input type="date" id="date" class="mt-2 block w-full cursor-pointer text-black rounded-md border border-gray-100 bg-gray-100 px-2 py-2 shadow-sm outline-none" />
              </div>
            </div>
  
            <div class="mt-6 grid w-full grid-cols-2 justify-end space-x-4 md:flex">
              <button class="rounded-lg bg-gray-200 px-8 py-2 font-medium text-gray-700 outline-none hover:opacity-80 focus:ring">Reset</button>
              <button class="rounded-lg bg-blue-600 px-8 py-2 font-medium text-white outline-none hover:opacity-80 focus:ring">Search</button>
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
    }
  };
  </script>
  

<style scoped>

</style>