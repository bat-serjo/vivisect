import os
import time
import unittest

import vtrace
import vtrace.tests as vt_tests


class ThreadNotifier(vtrace.Notifier):
    def __init__(self):
        vtrace.Notifier.__init__(self)
        self.threadexit = False
        self.threadcreate = False

    def notify(self, event, trace):
        if event == vtrace.NOTIFY_CREATE_THREAD:
            self.threadcreate = True
            return

        if event == vtrace.NOTIFY_EXIT_THREAD:
            self.threadexit = True
            return


class VtraceThreadTest(vt_tests.VtraceProcessTest):
    pypath = os.path.join('vtrace', 'tests', 'mains', 'mainthreads.py')

    def test_vtrace_threads(self):
        # if self.trace.getMeta('Platform') not in ('windows',):
        # raise unittest.SkipTest('Thread Catching Fails...')

        n = ThreadNotifier()

        self.trace.registerNotifier(vtrace.NOTIFY_ALL, n)
        self.runUntilExit()

        self.assertTrue(n.threadexit)
        self.assertTrue(n.threadcreate)
