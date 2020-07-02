import VueRouter from "vue-router";
import UploadContent from "./components/UploadContent";

const routes = [
  { path: "/", component: UploadContent }
];

export default new VueRouter({
  routes,
});
