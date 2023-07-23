<template>
  <div>
    <div class="container-fluid">
      <div class="row">
        <NavBar class="col-2 p-0"></NavBar>
        <FriendChat
          class="col-10 p-0"
          @chatTag="tagshow"
          :giveFin="message"
        ></FriendChat>
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
  data() {
    return {
      message: this.chatTag,
    };
  },
  methods: {
    tagshow() {
      console.log(this.message);
    },
  },
};
</script>

<style></style>
