<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <NavBar class="col-2 p-0"></NavBar>
        <FriendChat class="col-10 p-0"></FriendChat>
      </div>
    </div>
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

<style>
/* .my-nav {
  position: fixed;
  width: 280px;
  height: 100vh;
}
.my-fchat {
  position: absolute;
  left: 280px;
} */
</style>
