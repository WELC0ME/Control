const App = {
    data() {
        return {
            info: {
                user: {
                    "authorized": false
                },
                data: {
                    "accepted": false
                },
            },
            server: 'http://127.0.0.1:5000/api/'
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
        setInterval(this.update, 1000)
    },
    methods: {
        __METHODS__
    }
}

Vue.createApp(App).mount('#app')
