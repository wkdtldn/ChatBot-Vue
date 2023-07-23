<template>
  <div id="fcard" class="rounded m-2 p-2 shadow-sm" @click="show">
    <div class="row">
      <img
        :src="require(`@/assets/images/${src}`)"
        class="col-4 avatar shadow-sm"
      />
      <div class="col">
        <p class="fw-bold m-0 name row">{{ name }}</p>
        <p class="cardInfo m-0 cardInfo row">마지막 문자</p>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "MyFriend",
  components: {},
  data() {
    return {};
  },
  props: {
    name: String,
    src: String,
  },
  emits: ["chatTag"],
  methods: {
    show() {
      console.log(this.name)
      this.$emit("chatTag", this.name);     //^^🤬
    },
  },
};
</script>
<style>
@import url("../css/bootstrap.min.css");
.cardInfo {
  font-size: 14px;
}
.avatar {
  width: 50px;
  height: 50px;
  object-fit: fill;
  padding: 0 !important;
  margin-left: 16px;
  border-radius: 100%;
}
.name {
  font-size: 18.5px;
}
</style>
