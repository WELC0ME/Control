const App = {
    data() {
        return {
            user: {
                "authorized": false,
            },
            info: {},
            server: 'http://127.0.0.1:5000/api/'
        }
    },
    mounted() {
        axios.get(this.server + 'current_user')
            .then(response => {
                this.user = response['data']['user'];
            })
            .catch(error => {
                this.user = {
                    "authorized": false,
                };
            })
        setInterval(this.update, 1000)
    },
    methods: {
        __METHODS__
    }
}

Vue.createApp(App).mount('#app')
