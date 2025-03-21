"""Tests for preprocess_4km.py"""

import csv
import os
import sys
import tempfile
import unittest

# Allows the following module imports to work when running as a script
FOURkm_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(FOURkm_DIR)
import preprocess_4km


class ProcessTest(unittest.TestCase):

    def test_preprocess(self):
        _TESTDIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                                'test_data')
        src_fldr = os.path.join(_TESTDIR, 'input')
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_csv = f"{tmp_dir}/WeatherVariability_4km.csv"
            preprocess_4km.main(src_fldr, output_csv)
            with open(output_csv) as gotf:
                csvreader = csv.reader(gotf)
                header = next(csvreader)
                print(header)
                self.assertEqual(len(header), 14)
                numrows = 0
                for row in csvreader:
                    if numrows == 0:
                        print("first row:", row)
                    numrows += 1
                self.assertEqual(numrows, 2410575)


if __name__ == '__main__':
    unittest.main()
