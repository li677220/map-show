<template>
  <div>
    <layouthead></layouthead>
    <layoutside></layoutside>
    <br><br><br><br><br><br>
    <layoutmain></layoutmain>
    <layoutfoot></layoutfoot>
  </div>
</template>

<script>
import layouthead from "./Layout/LayoutHead"
import layoutmain from "./Layout/LayoutMain"
import layoutfoot from "./Layout/LayoutFoot"
import layoutside from "./Layout/LayoutSide"
export default {
  name: "index",
  components: { layouthead, layoutmain, layoutfoot, layoutside },

}
</script>

<style>
</style>