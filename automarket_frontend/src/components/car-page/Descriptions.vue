<template>
    <div class="md:w-[70%] w-[80%] bg-[#E6E6E6] shadow-xl rounded-xl mt-10 flex items-center flex-col py-10">
        <h1 class="uppercase mb-4 text-lg font-bold">{{ $t('description.header') }}</h1>
        <hr class="h-px  bg-black my-4 w-[80%] border-0">
        <p class="px-10">Lorem ipsum dolor sit amet consectetur adipisicing elit. Explicabo error facilis facere, inventore sunt iusto in excepturi dolor nulla fugit ut repellendus maxime at officia tempora. Cupiditate ex nam dicta!</p>
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
export default {
  data() {
    return {
      specifications: {
        manufacturer: 'Mercedes-Benz',
        model: 'GLE 400',
        year: '2018',
        category: 'Jeep',
        'enginevolume': '3.0',
        mileage: '63000 km',
        'fueltype': 'Petrol',
        'gearbox': 'Tiptronic',
        cylinders: '6',
        doors: '4/5',
        'drivewheels': '4x4',
        wheel: 'Left',
        airbags: '6',
        color: 'Black',
        'interiormaterial': 'Leather',
        'interiorcolor': 'Black',
        exchange: 'No',
        'technicalinspection': 'Yes',
        catalyst: 'Yes'
      }
    };
  }
};
</script>