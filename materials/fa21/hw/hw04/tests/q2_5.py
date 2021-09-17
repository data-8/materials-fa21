test = {   'name': 'q2_5',
    'points': [2, 2],
    'suites': [   {   'cases': [   {   'code': '>>> # Make sure that the table has a column called Organization Group and a column called count.\n'
                                               '>>> set(["Organization Group", "count"]) == set(org_group_and_counts.labels)\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # Make sure you do not include departments that don't have positions with average salary above 125k.\n>>> org_group_and_counts.num_rows\n5",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
