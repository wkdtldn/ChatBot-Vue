<template>
  <div id="nav">
    <MyFriend v-for="(item, index) in friends" :key="index" :name="item" />
  </div>
</template>

<script>
import MyFriend from "./MyFriend.vue";
export default {
  name: "NavBar",
  data() {
    return {
      friends: ["John", "Jane", "Kevin", "Andrew"],
    };
  },
  components: {
    MyFriend,
  },
  methods: {},
};
</script>
<style>
@import url("../css/bootstrap.min.css");

#nav {
  background-color: #f5f5f5;
  width: 260px;
  height: 100vh;
  position: fixed;
  left: 0;
  top: 0;
}
</style>
