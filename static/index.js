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
            location: 'profile',
            nicknameInput: '',
            passwordInput: '',
            betInput: '',
            loginError: '',
            requestError: '',
            betError: '',
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
            this.curr_location = this.newLocation;

            if (
                this.curr_location != 'profile' &&
                this.curr_location != 'menu' &&
                this.curr_location != 'rules'
            ) {
                this.info.data.accepted = 0
                setInterval(this.update, 1000)
            };
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
                    };
                })
                .catch(error => {
                    this.requestError = 'unknown error';
                })
        },

        doBet(index, side) {
            axios.post(this.server + 'do_bet', {
              'token': this.token,
              'index': index,
              'side': side - 1,
              'value': this.betInput
            })
                .then(response => {
                    if (response.data.result != 'OK') {
                        this.betError = response.data.result
                    };
                })
                .catch(error => {
                    this.requestError = 'unknown error';
                })
            this.betInput = ''
        },
    }
}

Vue.createApp(App).mount('#app')
