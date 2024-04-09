<template>
    <Main/>
</template>

<script>
import Main from '../components/main/Main.vue'
export default{
  mounted() {
    this.setPageTitle('Explore New And Used Cars')
  },
  methods: {
    setPageTitle(title){
      document.title = title
    }
  },
  components:{
    Main,
  }
}
</script>