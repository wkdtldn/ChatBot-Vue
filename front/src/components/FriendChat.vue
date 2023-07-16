<template>
  <div id="chatpage">
    <div class="chat-content bg-light" style="height: 90vh; width= 100%;">
      <div class="line">
        <span class="chat-box mine me-2 bg-secondary text-white rounded"
          >안녕?</span
        >
      </div>
      <div class="line">
        <span class="chat-box bg-primary text-white ms-2 rounded">반가워!</span>
      </div>
    </div>
    <div class="row" style="width: 100% !important">
      <input class="col ms-4 form-control" id="input" />
      <button class="col-2 ms-2 btn btn-primary" id="send">send</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "FriendChat",
  components: {},
  props: {
    name: String,
  },
};
</script>

<style>
@import url("../css/bootstrap.min.css");
#chatpage {
  background-color: #d1eef9;
  width: 1661px;
  height: 100vh;
  position: fixed;
  left: 13.5%;
  top: 0;
}
.chat-content {
  height: 350px;
  overflow-y: scroll;
}

.line {
  margin-top: 10px;
  display: flex;
}

.chat-box {
  background: #eee;
  padding: 5px;
  max-width: 200px;
}

.mine {
  margin-left: auto;
}
</style>
