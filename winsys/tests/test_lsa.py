from __future__ import unicode_literals

import os, sys
import unittest as unittest0
try:
  unittest0.skipUnless
  unittest0.skip
except AttributeError:
  import unittest2 as unittest
else:
  unittest = unittest0
del unittest0

from winsys.tests import utils as testutils
from winsys import _lsa
from winsys.tests import utils

@unittest.skipUnless(testutils.i_am_admin(), "These tests must be run as Administrator")
class TestLSA (unittest.TestCase):

  def test_LSA_logon_sessions (self):
    with utils.fake_stdout ():
      for logon_session in _lsa.LSA.logon_sessions ():
        logon_session.dump ()

if __name__ == "__main__":
  unittest.main ()
  if sys.stdout.isatty (): raw_input ("Press enter...")
