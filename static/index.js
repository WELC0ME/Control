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
            server: 'http://127.0.0.1:5000/api/',
            token: 'IB1jiktwudOP8eLfoVXbIRrgp8KxRYlpqnzByVXS0EATLeZ0ZO6yynHN',
            curr_location: 'profile',
            next_location: '',
            transition: 0,
            nicknameInput: '',
            passwordInput: '',
            loginError: '',
            requestError: ''
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
                this.info.data.accepted = 0
                axios.post(this.server + this.curr_location, {
                    'token': this.token,
                })
                    .then(response => {
                        if (response.data.result == 'OK') {
                            this.info.data = {
                                'data': response.data.data,
                                'accepted': 1,
                            }
                        } else {
                            this.requestError = response.data.result
                            this.info.data.accepted = 1
                        };
                    })
                    .catch(error => {
                        this.requestError = 'unknown error';
                        this.info.data.accepted = 1
                    })
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

        login(_type) {
            this.info.data.accepted = 0
            axios.post(this.server + _type, {
                'token': this.token,
                'nickname': this.nicknameInput,
                'password': this.passwordInput,
            })
                .then(response => {
                    if (response.data.result == 'OK') {
                        this.info.user = response.data.user
                    } else {
                        this.loginError = response.data.result
                    };
                    this.info.data.accepted = 1
                })
                .catch(error => {
                    this.loginError = 'unknown error';
                    this.info.data.accepted = 1
                })
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
    }
}

Vue.createApp(App).mount('#app')
