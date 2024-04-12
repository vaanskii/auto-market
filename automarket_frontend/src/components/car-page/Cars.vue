<template>
  <div class="flex justify-center items-center flex-col">
    <div class="w-[80%]">
      <h1 class="uppercase pt-40 text-start text-4xl mb-10">Image viewer</h1>
      <div class="flex justify-center">
        <!-- Large image container with navigation buttons -->
        <div class="relative w-[90%] flex justify-center">
          <img :src="images[currentImageIndex]" @click="openImageViewer(currentImageIndex)" class="md:w-[90%] md:h-[550px] h-[300px] cursor-pointer rounded-xl reveal-card" />
          <button @click="previousImage" class="absolute inset-y-0 md:left-14 left-0 z-10 m-6 text-white text-4xl">‹</button>
          <button @click="nextImage" class="absolute inset-y-0 md:right-14 right-0 z-10 m-6 text-white text-4xl">›</button>
        </div>
        <!-- Small images container with vertical scrolling -->
        <div class="flex-col items-center overflow-y-auto md:flex hidden" style="max-height: 550px;">
          <div v-for="(image, index) in images.slice(1)" :key="index" class="cursor-pointer mb-4">
            <img :src="image" @click="makeImagePrimary(index + 1)" class="w-48 h-40 rounded-xl reveal-card" />
          </div>
        </div>
      </div>
      <div v-if="imageViewerOpen" class="fixed inset-0 bg-black bg-opacity-75 flex justify-center items-center p-4 z-50">
        <button @click="closeImageViewer" class="absolute top-0 right-0 m-6 px-12 text-white text-4xl">×</button>
        <button @click="previousImage" class="absolute inset-y-0 left-0 z-10 m-6 text-white text-4xl">‹</button>
        <button @click="nextImage" class="absolute inset-y-0 right-0 z-10 m-6 text-white text-4xl">›</button>
        <img :src="images[currentImageIndex]" class="max-w-full max-h-full" />
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
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
