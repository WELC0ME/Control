update() {
    axios.get(this.server + 'current_user')
        .then(response => {
            this.info = response['data']['user'];
        })
        .catch(error => {
            this.info = {
                "authorized": false,
            };
        })
},
