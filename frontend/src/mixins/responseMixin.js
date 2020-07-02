export default {
  methods: {
    handleResponse(response) {
      if (response && response.data && response.data.status) {
        return response.data.message || {};
      } else if (response && response.data) {
        alert(response.data.message);
      } else {
        alert("Something strange happened here, please check!!");
      }
      return null;
    },
  },
};
