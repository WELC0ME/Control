update() {
    axios.get(this.server + 'productions')
        .then(response => {
            this.info = response['data']['productions'];
        })
        .catch(error => {
            this.info = {};
        })
},

start(index) {
    axios.get(this.server + 'start_production', {
        'production_id': index,
    })
},

promote(index, value) {
    axios.get(this.server + 'promote_production', {
        'production_id': index,
        'value': value,
    })
},
