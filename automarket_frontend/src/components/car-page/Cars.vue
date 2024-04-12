<template>
    <div class="gallery grid grid-cols-3 gap-4 pt-16">
      <div v-for="(image, index) in images" :key="index" class="cursor-pointer">
        <img :src="image" @click="openImageViewer(index)" class="w-full h-96" />
      </div>
      <div v-if="imageViewerOpen" class="fixed inset-0 bg-black bg-opacity-75 flex justify-center items-center p-4 z-50">
        <button @click="closeImageViewer" class="absolute top-0 right-0 m-6 text-white text-4xl">×</button>
        <button @click="previousImage" class="absolute left-0 m-6 text-white text-4xl">‹</button>
        <button @click="nextImage" class="absolute right-0 m-6 text-white text-4xl">›</button>
        <img :src="images[currentImageIndex]" class="max-w-full max-h-full" />
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onUnmounted } from 'vue';
  
  export default {
    setup() {
      const images = ref([
        '1.jpg',
        '2.jpg',
        'peakpx.jpg'
      ]);
      const imageViewerOpen = ref(false);
      const currentImageIndex = ref(0);
  
      function openImageViewer(index) {
        currentImageIndex.value = index;
        imageViewerOpen.value = true;
      }
  
      function closeImageViewer() {
        imageViewerOpen.value = false;
      }
  
      function nextImage() {
        if (currentImageIndex.value >= images.value.length - 1) {
          currentImageIndex.value = 0; 
        } else {
          currentImageIndex.value++;
        }
      }
  
      function previousImage() {
        if (currentImageIndex.value <= 0) {
          currentImageIndex.value = images.value.length - 1;
        } else {
          currentImageIndex.value--;
        }
      }
  
      // Keyboard navigation
      function handleKeydown(event) {
        switch (event.key) {
          case 'ArrowRight':
            nextImage();
            break;
          case 'ArrowLeft':
            previousImage();
            break;
          case 'Escape':
            closeImageViewer();
            break;
        }
      }
  
      window.addEventListener('keydown', handleKeydown);
  
      onUnmounted(() => {
        window.removeEventListener('keydown', handleKeydown);
      });
  
      return {
        images,
        imageViewerOpen,
        currentImageIndex,
        openImageViewer,
        closeImageViewer,
        nextImage,
        previousImage
      };
    }
  };
  </script>
  
  <style scoped>

  </style>
  