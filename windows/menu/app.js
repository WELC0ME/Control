const App = {
    data() {
        return {
            // server: 'http://resource-control.herokuapp.com/api/',
            server: 'http://127.0.0.1:5000/api/',
            authorized: false,
            user_name: '',
        }
    },
    mounted() {
        axios.get(this.server + 'authorized')
            .then(response => {
                this.authorized = response['data']['authorized'];
                this.user_name = response['data']['user_name'];
            })
            .catch(error => {
                this.authorized = false;
                this.user_name = '';
            })
    },
    methods: {}
}

Vue.createApp(App).mount('#app')
