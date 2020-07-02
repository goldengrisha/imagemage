<template>
  <div class="row">
    <div class="col-4">Test</div>
  </div>
</template>

<script>
/* eslint-disable no-debugger */
import ApiService from "../services/ApiService";
import responseMixin from "../mixins/responseMixin";

export default {
  mixins: [responseMixin],
  name: "upload-content",
  data() {
    return {
      text_content: "",
      text_title: "",
      progress: 0,
      texts: [],
      paginate: ["paginatedTexts"]
    };
  },
  computed: {},
  methods: {},
  async mounted() {}
};
</script>

<style scoped>
textarea {
  margin: 0px 0px;
  padding: 5px;
  min-height: 16px;
  line-height: 16px;
  width: 100%;
  height: calc(100vh - 20px);
  display: block;
  margin: 0px auto;
}
#text_title {
  width: 100%;
}
</style>
