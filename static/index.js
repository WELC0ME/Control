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
            token: 'IB1jiktwudOP8eLfoVXbIRrgp8KxRYlpqnzByVXS0EATLeZ0ZO6yynHN',
            curr_location: 'profile',
            next_location: '',
            transition: 0,
            nicknameInput: '',
            passwordInput: '',
            loginError: ''
        }
    },
    mounted() {
        axios.post(this.server + 'current_user', {
            'token': this.token
        })
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
                        loginError = result
                    };
                    this.info.data.accepted = 1
                })
                .catch(error => {
                    loginError = 'unknown error';
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
