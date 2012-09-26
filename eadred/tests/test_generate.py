from eadred.management.commands import generatedata


def test_generatedata():
    """Basic test to make sure function gets called."""
    from testproject.testapp import sampledata

    assert sampledata.called == False
    cmd = generatedata.Command()
    cmd.run_from_argv(['manage.py', ''])
    assert sampledata.called == True
