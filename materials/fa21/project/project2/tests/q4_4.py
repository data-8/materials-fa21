test = {   'name': 'q4_4',
    'points': [0, 0],
    'suites': [   {   'cases': [   {   'code': ">>> sample = population.sample(5)\n>>> type(complete_test(sample)) in set([float, np.float64]) # Make sure you're returning a single value!\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> sample = population.sample(100, with_replacement=False)\n'
                                               '>>> p_val = complete_test(sample)\n'
                                               '>>> 0 <= complete_test(sample) <= 1 # Since p_values are proportions, they should be between 0 and 1\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
