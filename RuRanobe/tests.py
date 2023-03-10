import unittest
import desription, mainPage, names, statuses, tags, volumes, downloadLinks

class Tests(unittest.TestCase):

    def testMainPage(self):
        self.assertEqual(bool(mainPage.GetListOnMainPage()), True)
    
    def testDesc(self):
        self.assertEqual(bool(desription.get_desc('https://ruranobe.ru/r/oregairu')), True)
    
    def testName(self):
        self.assertEqual(bool(names.get_names('https://ruranobe.ru/r/oregairu')), True)
        
    def testStatuses(self):
        self.assertEqual(bool(statuses.get_status('https://ruranobe.ru/r/oregairu')), True)
        
    def testTags(self):
        self.assertEqual(bool(tags.get_tags('https://ruranobe.ru/r/oregairu')), True)
        
    def testVolumes(self):
        self.assertEqual(bool(volumes.get_volumes('https://ruranobe.ru/r/oregairu')), True)
    
    def testDownLinks(self):
        self.assertEqual(bool(downloadLinks.downloadLinks('https://ruranobe.ru/r/oregairu/v1')), True)