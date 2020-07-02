import http from "../http-common";

class ApiService {
  getPing() {
    return http.get("/ping");
  }
}

export default new ApiService();
