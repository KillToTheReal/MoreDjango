
<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
/* eslint-disable */
import HelloWorld from './components/HelloWorld.vue';
import axios from 'axios';
export default {
  name: 'App',
  components: {
    HelloWorld
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/department').then((response) => {
      console.log(response.data);
    });
  }
}

</script>
 
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
