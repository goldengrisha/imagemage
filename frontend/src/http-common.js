/* eslint-disable no-debugger */
import axios from "axios";

const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:5000",
  headers: {
    "Content-type": "application/json",
  },
});

const requestHandler = (request) => {
  return request;
};

const errorHandler = (error) => {
  return Promise.reject({ ...error });
};

const successHandler = (response) => {
  return response;
};

axiosInstance.interceptors.response.use(
  (response) => successHandler(response),
  (error) => errorHandler(error),
  (request) => requestHandler(request)
);

export default axiosInstance;
