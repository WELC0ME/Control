update() {
    axios.get(this.server + 'rating')
        .then(response => {
            this.info.data = {
                'rating': response.data.rating,
                'accepted': true,
            };
        })
        .catch(error => {
            this.info.data.accepted = false;
        })
},
