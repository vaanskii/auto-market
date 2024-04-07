<template>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <section class="grid h-[1500px] md:h-[1140px] lg:h-[990px] xl:h-screen w-full grid-cols-1 bg-transparent md:grid-cols-1 bg-gradient-to-r ">
    <div class="flex flex-col justify-between bg-no-repeat bg-fixed bg-cover bg-right md:bg-center">
      <div class="-mt-44 py-4 text-center text-6xl font-bold text-yellow-300">
      </div>
      <div class="flex items-center justify-center md:-mt-0 -mt-[600px]">
        <h1 class="absolute top-40 text-center uppercase text-xl sm:text-2xl md:text-3xl lg:text-4xl xl:text-5xl">Explore a Wide Selection of Used and New Cars</h1>
        <p class="absolute top-72 text-center uppercase text-md sm:text-lg md:text-xl lg:text-2xl xl:text-4xl">Find Your Perfect Ride Today!</p>
      </div>
      <div class="text-white flex items-center justify-center">
        <Filter/>
      </div>
      <div class="flex items-center md:w-6/12 md:self-center md:-mt-0 -mt-80">
        <div class="flex w-1/3 justify-center items-center py-4 px-4 gap-5 text-black">
          <span class="uppercase">Sell car</span>
          <span class="material-icons">sell</span>

        </div>
        <div class="flex w-1/3 justify-center items-center py-4 px-4 gap-5 text-black">
          <span class="uppercase">Rent car</span>
          <span class="material-icons">directions_car</span>
        </div>
        <div class="flex w-1/3 justify-center items-center py-4 px-4 gap-5 text-black">
          <span class="uppercase">Buy car</span>
          <span class="material-icons">credit_card</span>
        </div>
      </div>
    </div>
  </section>
  <hr class="h-[1.5px] my-8 bg-[#222] -mt-[-0px] border-0">
  <div class="flex items-center justify-center mt-20">
    <h1 class="md:text-6xl text-2xl uppercase text-[#222]">Most viewed cars</h1>
  </div>
  <div class="my-20 flex justify-center items-center">
    <Cards/>
  </div>

  <section class="w-full bg-lights md:py-52 mt-36 py-28 md:bg-cover md:bg-center bg-cover bg-center my-20 border bg-fixed bg-no-repeat"></section>
  <section class="w-5/6 m-auto mt-10 grid grid-col-1 gap-x-3 gap-y-10 md:grid-cols-2 max-w-6xl items-center mb-20  ">
 
  <div class="py-3 px-2">
    <div class="parallax flex rounded-sm bg-no-repeat bg-center bg-cover md:bg-center"></div>
  </div>
  <div class="py-3 px-2 ">
   <h1 class="text-5xl mb-8">New interior</h1>
   <p class="text-md">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse in turpis at libero euismod luctus vel sit amet lorem.<br/>  Maecenas lorem metus, semper in lobortis imperdiet, pulvinar sed felis. Maecenas aliquam velit in ligula tincidunt imperdiet. Integer interdum enim ut placerat dignissim. Maecenas turpis orci, facilisis vitae ligula non, luctus convallis risus. </p>
  </div>
  </section>
</template>



<script>
import Filter from './Filter.vue'
import Cards from './Cards.vue'

export default {
  components: {
    Filter,
    Cards
  },
}
</script>


<!-- STYLES -->
<style>
.bg-lights {
  background-image: url('peakpx.jpg');
}
.parallax {
  background-image: url('https://images.unsplash.com/photo-1616790151040-47661836dd26?q=80&w=3387&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D');
  height: 385px;
}

@media only screen and (max-device-width: 1366px) {
  .parallax {
    background-attachment: scroll;
  }
}
</style>