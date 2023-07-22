<template>
  <div>
    <div class="chat-content hide p-0">
      <div class="line">
        <span class="chat-box mine me-2 rounded"> 안녕? </span>
      </div>
      <div class="line">
        <span class="chat-box bot ms-2 rounded">반가워!</span>
      </div>
      <div v-for="(item, index) in msgList" :key="index">
        <div v-if="item.tag === 'user'">
          <div v-if="item.msg === ''"></div>
          <div v-else>
            <div class="line">
              <span class="chat-box mine me-2 rounded" scoped>{{
                item.msg
              }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="container-fluid" style="position: fixed; bottom: 0; width: 84%">
      <div class="row my-2">
        <div class="col-11">
          <input
            class="form-control input"
            id="input"
            v-model="msg"
            placeholder="Message for here"
            v-on:keyup.enter="mySend()"
            ref="cursor"
          />
        </div>
        <div class="col-1 pe-5">
          <button
            class="btn btn-primary"
            style="width: 100% !important"
            id="send"
            @click="mySend()"
          >
            ▶️
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "FriendChat",
  components: {},
  props: {
    name: String,
  },
  data() {
    return {
      text: "",
      msg: "",
      msgList: [
        {
          tag: "computer",
          msg: "hi",
        },
        {
          tag: "user",
          msg: "",
        },
      ],
    };
  },
  methods: {
    mySend() {
      this.msgList.push({ tag: "user", msg: this.msg });
      var data = { msg: this.msg };
      console.log(data);
      axios
        .post("http://127.0.0.1:5000/", data)
        .then((res) => {
          console.log(res.staus);
          console.log(res.data);
          var template = `<div class="line">
        <span class="chat-box bot ms-2 rounded">${res.data}</span>
      </div>`;
          document
            .querySelector(".chat-content")
            .insertAdjacentHTML("beforeend", template);
        })
        .catch((error) => {
          console.log(error);
        })
        .finally(() => {
          console.log("항상 마지막에 실행");
        });
      this.msg = "";
      this.$refs.cursor.focus();
    },
  },
};
</script>

<style>
@import url("../css/bootstrap.min.css");
.line {
  margin-top: 10px;
  display: flex;
}
.mine {
  color: #262630;
  background-color: #ffec42;
  margin-left: auto;
}
.chat-content {
  background-color: #9bbad8;
  height: 94vh;
  overflow-y: scroll;
}
.hide {
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.hide::-webkit-scrollbar {
  display: none;
}
.chat-box {
  max-width: 200px;
  padding: 5px;
}
.bot {
  background-color: #fdfefe;
  color: #0b0b0b;
}
</style>
