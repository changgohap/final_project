<template>
  <div>
    <h3>MyCommentList</h3>
    <MyCommentListItem/>
  </div>
</template>

<script>
import MyCommentListItem from '@/components/MyCommentListItem';

export default {
  name: "MyCommentList",
  components: {
    MyCommentListItem,
  }
}
</script>

<style>

</style>