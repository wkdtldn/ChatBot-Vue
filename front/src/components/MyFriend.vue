<template>
    <div id="fcard" class="rounded m-2 p-2 shadow-sm">
      <p class="fs-6 fw-bold" id="fname">Temp</p>
      <p id="fdisc">친구 정보</p>
    </div>
  </template>
  <script>
    export default {
      name: 'MyFriend',
      components: {
      }
    }
  </script>
  <style>
  @import url("../css/bootstrap.min.css");
  
  #fcard {
    background-color: #FFFFFF;
  }

  #fdisc {
    font-size: 12px;
    color: #CCCCCC;
  }
  </style>