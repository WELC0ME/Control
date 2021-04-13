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

start(index) {
    axios.get(this.server + 'start_production', {
        params: {
            'production_id': index,
        }
    })
},

promote(index, value) {
    axios.get(this.server + 'promote_production', {
        params: {
            'production_id': index,
            'value': value,
        }
    })
},
