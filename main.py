from windows.admin import *
from windows.bets import *
from windows.login import *
from windows.productions import *
from windows.profile import *
from windows.rating import *
from windows.stock_exchange import *


@config.APP.route('/')
def index():
    return open('static/index.html', 'r', encoding='utf8').read()


if __name__ == '__main__':
    # начало работы программы
    # config.APP.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    config.APP.run()
