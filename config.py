BASE_FOLDER = 'static/'
TEMPLATE_FOLDER = 'templates/'
HEADER_TEMPLATE_PATH = BASE_FOLDER + TEMPLATE_FOLDER + 'header'

APP = None


def show_template(template_name):
    header = open(HEADER_TEMPLATE_PATH + '.html', 'r', encoding='utf8').read()
    template = open(BASE_FOLDER + TEMPLATE_FOLDER + template_name + '.html',
                    'r', encoding='utf8').read()
    return header.replace('ANOTHER_TEMPLATE', template)
