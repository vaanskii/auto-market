<template>
    <div :class="[ 'g-cursor', { 'g-cursor_hover': hover.value }, {'g-cursor_hide': hideCursor.value} ]" class="md:block hidden">
      <div :style="cursorCircle" class="g-cursor__circle"></div>
      <div class="g-cursor__point" :style="cursorPoint"></div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const xChild = ref(0);
const yChild = ref(0);
const xParent = ref(0);
const yParent = ref(0);
const hover = ref(false);
const hideCursor = ref(true);

const cursorCircle = computed(() => {
  return `transform: translateX(${xParent.value}px) translateY(${yParent.value}px) translateZ(0) translate3d(0, 0, 0);`;
});

const cursorPoint = computed(() => {
  return `transform: translateX(${xChild.value - 3}px) translateY(${yChild.value - 3}px) translateZ(0) translate3d(0, 0, 0);`;
});

const moveCursor = (e) => {
  xChild.value = e.clientX;
  yChild.value = e.clientY;
  setTimeout(() => {
    xParent.value = e.clientX - 15;
    yParent.value = e.clientY - 15;
  }, 100);
};

document.addEventListener("mousemove", moveCursor);
document.addEventListener('mouseleave', () => {
  hideCursor.value = true;
});
document.addEventListener('mouseenter', () => {
  hideCursor.value = false;
});
</script>

<style>
html {
    cursor: none;
}

.g-cursor_hide {
  opacity: 0;
  width: 60px;
  height: 60px;
  transition: width .6s ease,
    height .6s ease,
    opacity .6s ease;
}

.g-cursor__circle {
  pointer-events: none;
  user-select: none;
  top: 0;
  left: 0;
  position: fixed;
  width: 30px;
  height: 30px;
  border: 2px solid black;
  border-radius: 100%;
  z-index: 5555;
  backface-visibility: hidden;
  transition: opacity .6s ease;
}

.g-cursor__point {
  top: 0;
  left: 0;
  position: fixed;
  width: 8px;
  height: 8px;
  pointer-events: none;
  user-select: none;
  border-radius: 100%;
  background: black;
  z-index: 55555555;
  backface-visibility: hidden;
  will-change: transform;
}

.g-cursor_hover .g-cursor__circle {
  opacity: 0;
  width: 60px;
  height: 60px;
  transition: width .6s ease,
    height .6s ease,
    opacity .6s ease;
}
</style>
