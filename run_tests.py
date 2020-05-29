import unittest

tests = unittest.TestLoader().discover('tests')
result = unittest.TextTestRunner(verbosity=2).run(tests)
