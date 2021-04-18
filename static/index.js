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
            error: '',
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
        //
    },
    methods: {

        move(newLocation) {
            this.location = newLocation;
            console.log(this.location)
            if (
                this.location != 'profile' &&
                this.location != 'menu' &&
                this.location != 'rules'
            ) {
                this.info.data.accepted = 0
                setInterval(this.getData, 1000)
            };
        },

        getLocation(location) {
            return location == this.location
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
                        this.info.data = {
                            'data': response.data.data,
                            'accepted': 1,
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
            axios.post(this.server + 'do_bet', {
              'token': this.token,
              'index': index,
              'side': side - 1,
              'value': this.betInput
            })
                .then(response => {
                    if (response.data.result != 'OK') {
                        this.error = response.data.result
                    };
                })
                .catch(error => {
                    this.error = 'unknown error';
                })
            this.betInput = ''
        },

        sendData(index, _type) {
            console.log(this.server + _type, index)
            axios.post(this.server + _type, {
              'token': this.token,
              'production_id': index,
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
    }
}

Vue.createApp(App).mount('#app')
