# HW3 test file

import unittest

import random
import copy

from hw3 import *

SHORT_TIMEOUT = 1
LONG_TIMEOUT = 10

class tester_is_unique(unittest.TestCase):

	def test__given(self):
		self.assertTrue(is_unique('g'))
		self.assertFalse(is_unique('hello world'))

class tester_is_anagram(unittest.TestCase):
	
	def test__given(self):
		self.assertTrue(is_anagram('sc961', 'cs196'))
		self.assertFalse(is_anagram('abcabc', 'golf'))
		self.assertFalse(is_anagram('long', 'longer'))

class tester_tic_tac_toe(unittest.TestCase):
	
	def test__given(self):
		self.assertEqual(tic_tac_toe([['X', 'X', 'X'], ['-', '-', '-'], ['-', '-', '-']]), 2)
		self.assertEqual(tic_tac_toe([['-', '-', '-'], ['O', 'O', 'O'], ['-', '-', '-']]), 1)
		self.assertEqual(tic_tac_toe([['-', '-', '-', 'O'], ['-', '-', 'O', '-'], ['-', 'O', '-', '-'], ['O', '-', '-', '-']]), 1)
		self.assertEqual(tic_tac_toe([['X', '-', '-', '-'], ['-', 'X', '-', '-'], ['-', '-', 'X', '-'], ['-', '-', '-', 'X']]), 2)
		self.assertEqual(tic_tac_toe([['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]), 0)

class tester_matrix_transpose(unittest.TestCase):
	
	def test__given(self):
		self.assertEqual(
			matrix_transpose([[1,2],[3,4],[5,6]]),
			[[1, 3, 5], [2, 4, 6]])
		
		self.assertEqual(
			matrix_transpose(
				[['a','b','c','d'],
				['e','f','g','h'],
				['i','j','k','l'],
				['m','n','o','p']]),
			[['a','e','i','m'],
			['b','f','j','n'],
			['c','g','k','o'],
			['d','h','l','p']])

#==========================================

class tester_initialize_counts(unittest.TestCase):

	def test__given(self):
		mf = [[0 for i in range(3)] for j in range(3)]
		mf[1][1] = -1
		
		mf_key = [[1 for i in range(3)] for j in range(3)]
		mf_key[1][1] = -1
		
		initialize_counts(mf)
		self.assertEqual(mf, mf_key)


#============================================================
# BOILERPLATE CODE

from io import StringIO
import sys

class ReplaceStd(object):
	""" Let's make it pythonic. """

	def __init__(self):
		self.stdout = None
		#self.stderr = None

	def __enter__(self):
		self.stdout = sys.stdout
		#self.stderr = sys.stderr

		# as it was suggested already:
		sys.stdout = StringIO()
		#sys.stderr = StringIO()

	def __exit__(self, type, value, traceback):
		sys.stdout.close()
		#sys.stderr.close()

		sys.stdout = self.stdout
		#sys.stderr = self.stderr

if __name__ == "__main__":

	with ReplaceStd():
		unittest.main(module=__name__, buffer=True, exit=False)

