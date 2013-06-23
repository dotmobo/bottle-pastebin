# -*- coding: utf-8 -*-
import unittest
from utils import encryptAES256, decryptAES256, encryptSHA256, dateLimit
import datetime

class UtilsTest(unittest.TestCase):
    """ unit test for utils """
    
    def setUp(self):
        self.txt = "My encrypted text"
    
    def test_encryptAES256(self):
        """ test the encryption into aes256 """
        enc = encryptAES256(self.txt)
        self.assertEqual(len(enc['iv']), 32)
        self.assertEqual(len(enc['text']), 64)
        self.assertEqual(len(enc['key']), 64)
            
    def test_decryptAES256(self):
        """ decrypt the aes 256 text """
        enc = encryptAES256(self.txt)
        dec = decryptAES256(enc['text'], enc['key'], enc['iv'])       
        self.assertEqual("My encrypted text", dec)
        
    def test_encryptSHA256(self):
        """ test the sha256 encryption """
        sha = encryptSHA256(self.txt)
        self.assertEqual(sha, "e1f7785845cac9d0719b902eaef13bdf7fb9442a368c1fadac2570c1f6579f42")
        
    def test_dateLimit(self):
        """ test the datelimit function """
        now = datetime.date(2013,1,1)
        duration = 86400000
        datelimit = dateLimit(now, duration)
        datestr = datetime.datetime.strftime(datelimit, "%Y-%m-%d %Hh:%Mm:%Ss")
        self.assertEqual("2013-01-02 00h:00m:00s", datestr)
        
        
        