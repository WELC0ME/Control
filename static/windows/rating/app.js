update() {
    axios.get(this.server + 'rating')
        .then(response => {
            this.info = response['data']['rating'];
        })
        .catch(error => {
            this.info = {};
        })
},
