<template>
  <div class="flex justify-center items-center flex-col">
    <div class="w-[80%]">
        <h1 class="uppercase pt-40 text-start text-4xl mb-10">bmw f90 - <span class="text-gray-600">2019</span> </h1> 
        <p class="uppercase mb-10 ml-4">batumi</p>
      <div class="flex justify-center">
        <!-- Large image container with navigation buttons -->
        <div class="relative w-[90%] flex justify-center">
          <img :src="images[currentImageIndex]" @click="openImageViewer(currentImageIndex)" class="md:w-[80%] md:h-[550px] h-[270px] cursor-pointer rounded-xl reveal-card" />
          <span class="absolute inset-y-0 left-4 sm:left-2 md:left-12 lg:left-28 p-5 text-white text-lg">{{ currentImageIndex + 1 }}/{{ images.length }}</span>
          <button @click="previousImage" class="absolute inset-y-0 -left-4 sm:left-2 md:left-12 lg:left-28 m-6 text-4xl">
            <span class="px-4 pb-1 flex justify-center items-center bg-white rounded-full text-black">
              ‹
            </span>
          </button>
          <button @click="nextImage" class="absolute inset-y-0 -right-4 sm:right-2 md:right-12 lg:right-28 m-6 text-white text-4xl">
            <span class="px-4 pb-1 flex justify-center items-center bg-white rounded-full text-black">
              ›
            </span>
          </button>
        </div>
        <!-- Small images container with vertical scrolling -->
        <div class="flex-col items-center overflow-y-auto md:flex hidden" style="max-height: 550px;">
          <div v-for="(image, index) in images.slice(1)" :key="index" class="cursor-pointer mb-4">
            <img :src="image" @click="makeImagePrimary(index + 1)" class="w-48 h-40 rounded-xl reveal-card" />
          </div>
        </div>
      </div>
      <div v-if="imageViewerOpen" class="fixed inset-0 bg-black bg-opacity-100 flex justify-center items-center p-4 z-50">
        <button @click="closeImageViewer" class="absolute top-0 right-0 m-6 px-12 text-white text-4xl">×</button>
        <button @click="previousImage" class="absolute inset-y-0 left-0 z-10 m-6 text-white text-4xl">‹</button>
        <button @click="nextImage" class="absolute inset-y-0 right-0 z-10 m-6 text-white text-4xl">›</button>
        <img :src="images[currentImageIndex]" class="max-w-full max-h-full" />
        <span class="absolute bottom-0 left-0 mb-4 ml-4 p-10 text-white text-lg">{{ currentImageIndex + 1 }}/{{ images.length }}</span>
      </div>
    </div>
  </div>
  <div class="flex justify-center items-center flex-col mt-10">
    <Descriptions/>
  </div>
  <div class="mt-20">
    <h1 class="uppercase text-center text-3xl mb-8">Similar cars</h1>
    <Similar/>
  </div>
</template>

<script>
import Similar from './car-page-components/Similar.vue'
import Descriptions from './car-page-components/Descriptions.vue'
import { ref } from 'vue';

export default {
  components: {
    Similar,
    Descriptions
  },
  setup() {
    const images = ref([
      'peakpx.jpg',
      '2.jpg',
      'mercedes.jpg',
      'mechanic.jpeg',
      'car.png',
      'background.jpg'
    ]);
    const imageViewerOpen = ref(false);
    const currentImageIndex = ref(0);

    function openImageViewer(index) {
      if (window.innerWidth >= 768) {
        currentImageIndex.value = index;
        imageViewerOpen.value = true;
      }
    }

    function closeImageViewer() {
      imageViewerOpen.value = false;
    }

    function nextImage() {
      currentImageIndex.value = (currentImageIndex.value + 1) % images.value.length;
    }

    function previousImage() {
      currentImageIndex.value = (currentImageIndex.value - 1 + images.value.length) % images.value.length;
    }

    function makeImagePrimary(index) {
      const selectedImage = images.value.splice(index, 1)[0];
      images.value.unshift(selectedImage);
      currentImageIndex.value = 0;
    }

    // Keyboard navigation
    window.addEventListener('keydown', (event) => {
      if (imageViewerOpen.value) {
        if (event.key === 'ArrowRight') {
          nextImage();
        } else if (event.key === 'ArrowLeft') {
          previousImage();
        } else if (event.key === 'Escape') {
          closeImageViewer();
        }
      }
    });

    return {
      images,
      imageViewerOpen,
      currentImageIndex,
      openImageViewer,
      closeImageViewer,
      nextImage,
      previousImage,
      makeImagePrimary
    };
  },
  mounted() {
    setTimeout(() => {
      const cards = document.querySelectorAll('.reveal-card');
      cards.forEach(card => {
        card.classList.add('active');
      });
    }, 300); // Delay can be adjusted
  }
};
</script>

<style scoped>
/* Add TailwindCSS styles here */

.reveal-card {
  opacity: 0;
  transform: translateY(80px);
  transition: opacity 0.5s ease, transform 2s ease;
}

.reveal-card.active {
  opacity: 1;
  transform: translateY(0);
}
</style>
