const App = {
    data() {
        return {
            server: "http://127.0.0.1:5000/api/productions",
            data: 0,
        }
    },
    mounted() {
        setInterval(this.update, 1000)
    },
    methods: {
        update() {
            axios.get(this.server).then(response => (this.data = response))
        }
    }
}

Vue.createApp(App).mount('#app')
