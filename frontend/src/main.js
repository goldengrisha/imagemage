import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import VueRouter from "vue-router";
import VModal from "vue-js-modal";
import VuePaginate from "vue-paginate";

Vue.config.productionTip = false;
Vue.use(VModal);
Vue.use(VueRouter);
Vue.use(VuePaginate);

new Vue({
  router: router,
  render: (h) => h(App),
}).$mount("#app");
