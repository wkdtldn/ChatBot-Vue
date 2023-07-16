<template>
  <div>
    <FriendChat></FriendChat>
    <NavBar></NavBar>
  </div>
</template>

<script>
import NavBar from "./components/Navbar.vue";
import FriendChat from "./components/FriendChat.vue";

export default {
  name: "App",
  components: {
    NavBar,
    FriendChat,
  },
};
</script>

<style></style>
