const App = {
    data() {
        return {
        }
    },
    mounted() {
        setInterval(this.update, 1000)
    },
    methods: {
        update() {
        }
    }
}

Vue.createApp(App).mount('#app')
