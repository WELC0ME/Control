const App = {
    data() {
        return {
            info: {
                user: {
                    "authorized": false
                },
                data: {
                    "accepted": 1
                },
            },
            server: 'http://127.0.0.1:5000/api/',
            token: 'IB1jiktwudOP8eLfoVXbIRrgp8KxRYlpqnzByVXS0EATLeZ0ZO6yynHNiib03piq',
            curr_location: 'profile',
            next_location: '',
            transition: 0,
        }
    },
    mounted() {
        axios.get(this.server + 'current_user')
            .then(response => {
                this.info.user = response.data.user;
            })
            .catch(error => {
                this.info.user.authorized = false;
            })
        // setInterval(this.update, 1000)
    },
    methods: {

      move(newLocation) {
        if (newLocation == this.location) {
          return ''
        }
        this.transition = 1
        this.next_location = newLocation
        setTimeout(() => {
          this.curr_location = this.next_location;
          this.next_location = '';
          this.transition = 2;
        }, 700)
        setTimeout(() => {
          this.transition = 0;
          axios.get(this.server + this.curr_location)
              .then(response => {
                  this.info.data = {
                      'data': response.data.productions,
                      'accepted': 1,
                  };
              })
              .catch(error => {
                  this.info.data.accepted = -1;
              });
        }, 1400)
      },

      getClass(_class) {
        if (this.transition == 0) {
          return ''
        }

        if (this.transition == 1) {
          if (_class == this.curr_location) {
            return 'hide'
          }
          return ''
        }

        if (this.transition == 2) {
          if (_class == this.curr_location) {
            return 'show'
          }
          return ''
        }
      },

      getLocation(location) {
          return location == this.curr_location
      },

      update() {
          axios.get(this.server + 'productions')
              .then(response => {
                  this.info.data = {
                      'productions': response.data.productions,
                      'accepted': true,
                  };
              })
              .catch(error => {
                  this.info.data.accepted = false;
              })
      },

      start(index) {
          axios.get(this.server + 'start_production', {
              params: {
                  'production_id': index,
              }
          })
      },

      promote(index, value) {
          axios.get(this.server + 'promote_production', {
              params: {
                  'production_id': index,
                  'value': value,
              }
          })
      },
    }
}

Vue.createApp(App).mount('#app')
