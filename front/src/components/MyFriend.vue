<template>
  <div id="fcard" class="rounded m-2 p-2 shadow-sm" @click="show">
    <p class="fs-6 fw-bold" id="fname">{{ name }}</p>
    <p id="fdisc">친구 정보</p>
  </div>
</template>
<script>
export default {
  name: "MyFriend",
  components: {},
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

#fcard {
  background-color: #ffffff;
  cursor: pointer;
}

#fdisc {
  font-size: 12px;
  color: #cccccc;
}
</style>
