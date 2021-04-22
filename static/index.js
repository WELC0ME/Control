const App = {
    data() {
        return {
            info: {
                user: {
                    "authorized": false
                },
                data: {
                    "accepted": 0
                },
            },
            // server: 'http://127.0.0.1:5000/api/',
            server: 'https://resource-control.herokuapp.com/api/',
            token: 'IB1jiktwudOP8eLfoVXbIRrgp8KxRYlpqnzByVXS0EATLeZ0ZO6yynHN',
            location: 'profile',
            error: '',
            resources: [
                'Energy',
                'Water',
                'Food',
                'Apple',
                'Cider',
                'Wheat',
                'Flour',
                'Fuel',
                'Planks',
                'Bread',
                'Iron',
                'Iron ore',
                'Tools',
                'Bricks',
                'Steel',
                'Leather',
                'Hide',
                'Salt',
                'Clay',
                'Paper',
                'Books',
                'Quartz',
                'Glass',
                'Battery',
                'Frame',
                'Gold',
                'Stone',
                'Coin',
            ]
        }
    },
    mounted() {
        axios.post(this.server + 'profile', {
            'token': this.token
        })
            .then(response => {
                this.info.user = response.data.user;
                this.info.data.accepted = 1;
            })
            .catch(error => {
                this.info.user.authorized = false;
                this.info.data.accepted = 1;
            })
        // setInterval(this.getData, 1000)
    },
    methods: {

        move(newLocation) {
            this.location = newLocation
            this.info.data.accepted = 0
            this.getData()
        },

        getLocation(location) {
            return location == this.location
        },

        login(_type) {
            this.info.data.accepted = 0
            axios.post(this.server + _type, {
                'token': this.token,
                'nickname': this.$refs.nickname.value,
                'password': this.$refs.password.value,
            })
                .then(response => {
                    if (response.data.result == 'OK') {
                        this.info.user = response.data.user
                    } else {
                        this.error = response.data.result
                    };
                    this.info.data.accepted = 1
                })
                .catch(error => {
                    this.error = 'unknown error';
                    this.info.data.accepted = 1
                })
        },

        getData() {
            axios.post(this.server + this.location, {
              'token': this.token,
            })
                .then(response => {
                    if (response.data.result == 'OK') {
                        if (this.location == 'profile') {
                            this.info.user = response.data.user
                            this.info.data.accepted = 1
                        }
                        else {
                            this.info.data = {
                                'data': response.data.data,
                                'accepted': 1,
                            }
                        }
                    } else {
                        this.error = response.data.result
                    };
                })
                .catch(error => {
                    this.error = 'unknown error';
                })
        },

        doBet(index, side) {
            if (!this.info.user.authorized) {
                this.error = 'Authorize to do bets'
            }
            else {
                console.log(this.$refs.bet_test)
                axios.post(this.server + 'do_bet', {
                  'token': this.token,
                  'bet_id': index,
                  'side': side - 1,
                  'value': this.$refs.bet_test.value
                })
                    .then(response => {
                        if (response.data.result != 'OK') {
                            this.error = response.data.result
                        };
                    })
                    .catch(error => {
                        this.error = 'unknown error';
                    })
                this.$refs.bet_test.value = ''
            }
        },

        sendData(index, _type, param) {
            if (!this.info.user.authorized) {
                this.error = 'Unable production interaction without login'
            } else {
                axios.post(this.server + _type, {
                  'token': this.token,
                  'production_id': index,
                  'param': param,
                })
                    .then(response => {
                        if (response.data.result != 'OK') {
                            this.error = response.data.result
                        };
                    })
                    .catch(error => {
                        this.error = 'unknown error';
                    })
            }
        },

        add() {
            axios.post(this.server + 'create', {
                'token': this.token,
                'input': this.$refs.input_resource.options[this.$refs.input_resource.selectedIndex].text,
                'output': this.$refs.output_resource.options[this.$refs.output_resource.selectedIndex].text,
                'input_number': this.$refs.input_number.value,
                'output_number': this.$refs.output_number.value,
            })
                .then(response => {
                    if (response.data.result != 'OK') {
                        this.error = response.data.result
                    };
                })
                .catch(error => {
                    this.error = 'unknown error';
                })
        },

        accept(index) {
            if (!this.info.user.authorized) {
                this.error = 'Authorize to accept deals'
            }
            else {
                axios.post(this.server + 'accept', {
                    'token': this.token,
                    'bet_id': index,
                })
                    .then(response => {
                        if (response.data.result != 'OK') {
                            this.error = response.data.result
                        };
                    })
                    .catch(error => {
                        this.error = 'unknown error';
                    })
            }
        },

        logout() {
            axios.post(this.server + 'logout', {
                'token': this.token,
            })
                .then(response => {
                    if (response.data.result != 'OK') {
                        this.error = response.data.result
                    } else {
                        this.info.user = {
                            "authorized": false
                        }
                    };
                })
                .catch(error => {
                    this.error = 'unknown error';
                })
        },
    }
}

Vue.createApp(App).mount('#app')
