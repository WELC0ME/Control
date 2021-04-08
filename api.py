import config


@config.APP.route('/api/rating')
def rating():
    pass


@config.APP.route('/api/users')
def get_users():
    pass


@config.APP.route('/api/users/<user_id>')
def get_user(user_id):
    pass


@config.APP.route('/api/productions')
def productions():
    pass


@config.APP.route('/api/promote')
def promote():
    pass


@config.APP.route('/api/start_production')
def start_production():
    pass


@config.APP.route('/api/start')
def start():
    pass
