<template>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <section class="grid h-[1600px] md:h-[1140px] lg:h-[990px] xl:h-screen w-full grid-cols-1 bg-transparent md:grid-cols-1 bg-gradient-to-r ">
    <div class="flex flex-col justify-between bg-no-repeat bg-fixed bg-cover bg-right md:bg-center">
      <div class="-mt-44 py-4 text-center text-6xl font-bold text-yellow-300">
      </div>
      <div>
        <div class="flex items-center justify-center w-full">
          <h1 class="typed-text absolute md:top-40 font-[700] w-[90%] top-32 text-center uppercase text-3xl sm:text-3xl md:text-3xl lg:text-4xl xl:text-5xl">
            <span v-for="(word, index) in words" :key="index" :class="'word-' + index">{{ $t(`main-header.words.${word}`) }}</span>
          </h1>
          <h1 class="typed-text absolute top-[21rem] font-[600] w-[90%] text-center uppercase text-xl sm:text-xl md:text-2xl lg:text-2xl xl:text-4xl">
            <span v-for="(word, index) in words2" :key="index" :class="'word2-' + index">{{ $t(`main-header.words2.${word}`) }}</span>
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
  <div class="my-20 flex justify-center items-center">
    <Vin class="w-[70%]"/>
  </div>

  <section class="w-full bg-lights mt-10 mb-32 py-52 bg-start bg-cover my-20 border bg-no-repeat"></section>
  <!-- Recently vue -->
  <Recently/>
  <!-- Blogs vue -->
  <Blogs/>
</template>


<script>
import Filter from '../components/main/Filter.vue'
import Cards from '../components/main/Cards.vue'
import Recently from '../components/main/Recently.vue'
import Blogs from '../components/main/Blogs.vue'
import Vin from '../components/main/Vin.vue'
import { useI18n } from 'vue-i18n'

export default {
  components: {
    Filter,
    Cards,
    Recently,
    Blogs,
    Vin
  },
  setup() {
    const { t } = useI18n()

    const words = [
      'discover',
      'a',
      'wide',
      'selection',
      'of',
      'used',
      'and',
      'new',
      'cars',
    ]

    const words2 = [
      'find',
      'your',
      'perfect',
      'ride',
      'today',
    ]

    const animateText = () => {
      const spans = document.querySelectorAll('.typed-text span');
      spans.forEach((span, index) => {
        setTimeout(() => {
          span.classList.add('fade-in');
        }, index * 50);
      });
    };

    const revealHeadingOnScroll = () => {
      const handleScroll = () => {
        const heading = document.querySelector('.reveal-heading');
        if (!heading) return;
        const windowHeight = window.innerHeight;
        const revealTop = heading.getBoundingClientRect().top;
        const revealPoint = 150;

        if (revealTop < windowHeight - revealPoint) {
          heading.classList.add('active');
        } else {
          heading.classList.remove('active');
        }
      };

      window.addEventListener('scroll', handleScroll);

      return () => {
        window.removeEventListener('scroll', handleScroll);
      };
    };

    return { t, words, words2, animateText, revealHeadingOnScroll };
  },
  mounted() {
    this.animateText();
    this.revealHeadingOnScroll();
    this.setPageTitle('Explore New And Used Cars');
  },
  beforeUnmount() {
    // Cleanup scroll event listener
    window.removeEventListener('scroll', this.revealHeadingOnScroll);
  },
  methods: {
    setPageTitle(title) {
      document.title = title
    }
  }
}
</script>



<style scoped>
.bg-lights {
  background-image: url('/sales-desktop.jpg');
  background-position: start;
  height: 500px;
}

@media (max-width: 1024px){
  .bg-lights {
  background-image: url('/sales-mobile.jpg');
  background-position: start;
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