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
      friendsinfo: [
        "best friend",
        "old friend",
        "busy friend",
        "academy friend",
      ],
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
</style>
