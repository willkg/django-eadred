DEFAULT = None

called_with_param = DEFAULT


def reset_app():
    global called_with_param
    called_with_param = DEFAULT


def generate_sampledata(options):
    global called_with_param

    assert called_with_param == DEFAULT
    called_with_param = options['dataset']
