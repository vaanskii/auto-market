<template>
  <Navigation/>
  <RouterView/>
</template>

<script>
import Navigation from './components/Navigation.vue'
export default{
components:{
  Navigation,
}
}
</script>