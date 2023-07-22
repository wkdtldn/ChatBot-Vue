<template>
  <div id="fcard" class="rounded m-2 p-2 shadow-sm" @click="show">
    <div class="row">
      <img src="@/assets/lion.png" class="img col-4" />
      <div class="col">
        <p class="fw-bold m-0 name row">{{ name }}</p>
        <p class="cardInfo m-0 cardInfo row">마지막 내용</p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "MyFriend",
  components: {},
  data() {
    return {
      friendsinfo: [
        "best friend",
        "old friend",
        "busy friend",
        "academy friend",
      ],
    };
  },
  props: {
    name: String,
  },
  methods: {
    show() {
      console.log(this.name);
    },
  },
};
</script>
<style>
@import url("../css/bootstrap.min.css");
.cardInfo {
  font-size: 14px;
}
.name {
  font-size: 18.5px;
}
</style>
