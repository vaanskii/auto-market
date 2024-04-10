<template>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <section class="grid h-[1600px] md:h-[1140px] lg:h-[990px] xl:h-screen w-full grid-cols-1 bg-transparent md:grid-cols-1 bg-gradient-to-r ">
    <div class="flex flex-col justify-between bg-no-repeat bg-fixed bg-cover bg-right md:bg-center">
      <div class="-mt-44 py-4 text-center text-6xl font-bold text-yellow-300">
      </div>
      <div>
        <div class="flex items-center justify-center w-full">
          <h1 class="typed-text absolute md:top-40 font-[700] w-[90%] top-32 text-center uppercase text-3xl sm:text-3xl md:text-3xl lg:text-4xl xl:text-5xl">
            <span v-for="(word, index) in words" :key="index" :class="'word-' + index">{{ word }}</span>
          </h1>
          <h1 class="typed-text absolute top-[21rem] font-[600] w-[90%] text-center uppercase text-xl sm:text-xl md:text-2xl lg:text-2xl xl:text-4xl">
            <span v-for="(word, index) in words2" :key="index" :class="'word2-' + index">{{ word }}</span>
          </h1>
        </div>
      </div>
      <div class="text-white flex items-center justify-center">
        <!-- Filter vue -->
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
  <div class="flex items-center justify-center mt-20 reveal-heading">
    <h1 class="md:text-6xl text-3xl font-[700] uppercase smaller text-[#222]">vip cars</h1>
  </div>
  <div class="my-20 flex justify-center items-center">
    <Cards/>
  </div>

  <section class="w-full h-[550px] bg-lights mt-36 py-52 bg-start bg-cover my-20 border bg-no-repeat mb-52"></section>
  <!-- Recently vue -->
  <Recently/>
  <!-- Blogs vue -->
  <Blogs/>
</template>


<script>
import Filter from './main_components/Filter.vue'
import Cards from './main_components/Cards.vue'
import Recently from './main_components/Recently.vue'
import Blogs from './main_components/Blogs.vue'

export default {
  components: {
    Filter,
    Cards,
    Recently,
    Blogs
  },
  data() {
    return {
      words: [
        'Explore',
        ' ',
        'a',
        ' ',
        'Wide',
        ' ',
        'selection',
        ' ',
        'of',
        ' ',
        'used',
        ' ',
        'and',
        ' ',
        'new',
        ' ',
        'cars',
      ],
      words2: [
        'Find',
        ' ',
        'Your',
        ' ',
        'Perfect',
        ' ',
        'Ride',
        ' ',
        'Today!',
      ]
    };
  },
  mounted() {
    this.animateText();
    this.revealHeadingOnScroll();
  },
  methods: {
    revealHeadingOnScroll() {
      window.addEventListener('scroll', () => {
        const heading = document.querySelector('.reveal-heading');
        const windowHeight = window.innerHeight;
        const revealTop = heading.getBoundingClientRect().top;
        const revealPoint = 150;

        if (revealTop < windowHeight - revealPoint) {
          heading.classList.add('active');
        } else {
          heading.classList.remove('active');
        }
      });
    },
    animateText() {
      const spans = document.querySelectorAll('.typed-text span');
      spans.forEach((span, index) => {
        setTimeout(() => {
          span.classList.add('fade-in');
        }, index * 50);
      });
    }
  }
}
</script>


<style>
.bg-lights {
  background-image: url('1.jpg');
}

@media (max-width: 1024px){
  .bg-lights {
  background-image: url('2.jpg');
  background-position: center;
  height: 400px;
  margin-top: 0;
  margin-bottom: 120px;
}
}

.reveal-heading {
  opacity: 0;
  transform: translateY(100px);
  transition: opacity 0.5s ease, transform 2s ease;
}

.reveal-heading.active {
  opacity: 1;
  transform: translateY(0);
}


.typed-text {
  font-family: "Montserrat Medium";
  text-align: center;
  transform: scale(2);
  animation: scale 0.2s forwards cubic-bezier(0.5, 1, 0.89, 1);
}

@keyframes scale {
  100% {
    transform: scale(1);
  }
}

.typed-text span {
  display: inline-block;
  opacity: 0;
  filter: blur(4px);
  padding: 3px;
}

.typed-text span.fade-in {
  animation: fade-in 0.8s forwards cubic-bezier(0.11, 0, 0.5, 0);
}

@keyframes fade-in {
  100% {
    opacity: 1;
    filter: blur(0);
  }
}

@media (max-width:300px) {
  .smaller{
    font-size: 1.4rem;
    line-height: 2rem;
  }
}
</style>
