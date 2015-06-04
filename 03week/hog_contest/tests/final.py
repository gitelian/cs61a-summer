test = {
  'name': 'Final',
  'points': 0,
  'suites': [
    {
      'type': 'doctest',
      'setup': """
      >>> from hog import *
      """,
      'cases': [
        {
          'code': """
          >>> i, j = 0, 0
          >>> for i in range(GOAL_SCORE):
          ...    for j in range(GOAL_SCORE):
          ...        assert final_strategy(i, j) == final_strategy(i, j)
          """,
          'locked': False,
        },
        {
          'code': """
          >>> 0 <= final_bid < 100
          True
          """,
          'locked': False,
        }
      ]
    }
  ]
}
