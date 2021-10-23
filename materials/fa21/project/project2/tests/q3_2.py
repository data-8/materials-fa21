test = {   'name': 'q3_2',
    'points': [0, 0],
    'suites': [   {   'cases': [   {   'code': ">>> check_options = [1 if i in ['greater than', 'less than', 'equal to'] else 0 for i in [blank_1a, blank_2a, blank_3a]]\n"
                                               '>>> sum(check_options) == 3 # Make sure that blank_1a, blank_2a, and blank_3a are set to one of the following options: "greater than", "less than" or '
                                               '"equal to"\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> check_options = [1 if i in ["higher", "lower", "equal"] else 0 for i in [blank_1b, blank_2b, blank_3b]]\n'
                                               '>>> sum(check_options) == 3 # Make sure that blank_1b, blank_2b, and blank_3b are set to one of the following options: "higher", "lower", "equal"\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
