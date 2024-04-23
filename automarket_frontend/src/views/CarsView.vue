<template>
  <div class="flex justify-center items-center flex-col">
    <div class="w-[80%]">
        <h1 class="uppercase pt-40 text-start text-4xl mb-10">{{ car.manufacturer }} {{ car.car_model }} - <span class="text-gray-600">{{ car.year }}</span> </h1> 
        <p class="uppercase mb-10 ml-4">{{ car.location }}</p>
        
      <div class="flex justify-center">
        <!-- Large image container with navigation buttons -->
        <div class="relative w-[90%] flex justify-center">
          <img :src="images[currentImageIndex]" @click="openImageViewer(currentImageIndex)" class="md:w-[80%] lg:max-h-[600px] max-h-[450px] cursor-pointer rounded-xl reveal-card" />
            <div class="absolute inset-y-0 left-4 sm:left-5 md:left-20 lg:left-28 xl:left-36 p-3 mt-5 text-black flex justify-center items-center  bg-white rounded-full h-10 text-lg">
              <span>{{ currentImageIndex + 1 }}/{{ images.length }}</span>
            </div>
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
        <div class="flex-col items-center overflow-y-auto md:flex hidden lg:max-h-[600px] max-h-[450px]">
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
    <h1 class="uppercase text-center text-3xl mb-8">{{ $t('similar') }}</h1>
    <Similar/>
  </div>
</template>

<script>
import Similar from '../components/car-page/Similar.vue'
import Descriptions from '../components/car-page/Descriptions.vue'
import axios from 'axios';
export default {
components: {
  Similar,
  Descriptions
},
data() {
  return {
    car: [],
    images: [],
    imageViewerOpen: false,
    currentImageIndex: 0
  };
},
methods: {
  openImageViewer(index) {
    if (window.innerWidth >= 768) {
      this.currentImageIndex = index;
      this.imageViewerOpen = true;
    }
  },
  closeImageViewer() {
    this.imageViewerOpen = false;
  },
  nextImage() {
    this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length;
  },
  previousImage() {
    this.currentImageIndex = (this.currentImageIndex - 1 + this.images.length) % this.images.length;
  },
  makeImagePrimary(index) {
    const selectedImage = this.images.splice(index, 1)[0];
    this.images.unshift(selectedImage);
    this.currentImageIndex = 0;
  },
  getCars() {
    axios
      .get(`/api/${this.$route.params.id}/`)
      .then(response => {
        this.car = response.data.car
        this.images = response.data.car.images.map(img => img.image_url);
      })
      .catch(error => {
        console.log('error:', error);
      });
  },
  handleKeydown(event) {
    if (this.imageViewerOpen) {
      if (event.key === 'ArrowRight') {
        this.nextImage();
      } else if (event.key === 'ArrowLeft') {
        this.previousImage();
      } else if (event.key === 'Escape') {
        this.closeImageViewer();
      }
    }
  }
},
mounted() {
  this.getCars();
  setTimeout(() => {
    const cards = document.querySelectorAll('.reveal-card');
    cards.forEach(card => {
      card.classList.add('active');
    });
  }, 300);
// Keyboard navigation
window.addEventListener('keydown', (event) => {
  if (this.imageViewerOpen) {
    if (event.key === 'ArrowRight') {
      this.nextImage();
    } else if (event.key === 'ArrowLeft') {
      this.previousImage();
    } else if (event.key === 'Escape') {
      this.closeImageViewer();
    }
  }
})
},
beforeDestroy() {
  window.removeEventListener('keydown', this.handleKeydown);
},
beforeUnmount() {
  window.removeEventListener('keydown', this.handleKeydown);
},
};
</script>