update() {
    axios.get(this.server + 'current_user')
        .then(response => {
            this.info.data = {
                'user': response['data']['user'],
                'accepted': true,
            };
        })
        .catch(error => {
            this.info.data.accepted = false;
        })
},
