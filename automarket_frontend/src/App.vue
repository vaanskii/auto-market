<template>
  <Navigation/>
  <RouterView/>
  <Mouse/>
</template>

<script>
import Navigation from './components/Navigation.vue'
import Mouse from './components/Mouse.vue'
export default {
  components: {
    Navigation,
    Mouse
  },
}
</script>