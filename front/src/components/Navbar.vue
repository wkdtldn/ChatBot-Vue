<template>
  <div id="nav">
    <MyFriend
      v-for="(item, index) in friends"
      :key="index"
      :name="item.name"
      :src="item.src"
    />
  </div>
</template>

<script>
import MyFriend from "./MyFriend.vue";
export default {
  name: "NavBar",
  data() {
    return {
      friends: [
        {
          name: "John",
          src: "lion.png",
        },
        { name: "Jane", src: "muzi.png" },
        { name: "Kevin", src: "apeach.png" },
        { name: "Andrew", src: "neo.png" },
      ],
    };
  },
  components: {
    MyFriend,
  },
  emits: ["chatTag"],
  methods: {},
};
</script>
<style>
@import url("../css/bootstrap.min.css");
</style>
