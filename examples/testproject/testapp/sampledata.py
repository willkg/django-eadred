DEFAULT = False

called = DEFAULT


def reset_app():
    global called
    called = DEFAULT


def generate_sampledata(options):
    global called
    assert called == DEFAULT
    called = True

