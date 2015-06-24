import unittest

def parse_url(url):
    class UrlObject():
        def __init__(self, protocol, site):
            self.protocol = protocol
            self.site  = site 
    site = url.split('//')[1]
    if url[0] == 'h':
        return UrlObject('http', site)
    return UrlObject('ftp', site)

class test_basic_example(unittest.TestCase):
    def test_finds_correct_protocol(self):
        url_object = parse_url("http://www.mysite.com")
        protocol = url_object.protocol
        self.assertEqual('http', protocol)
        
    def test_finds_ftp_protocol(self):
        url_object = parse_url("ftp://www.mysite.com")
        protocol = url_object.protocol
        self.assertEqual('ftp', protocol)

class test_site_parsing(unittest.TestCase):  
    def assertSite(self, url, site):
        url_object = parse_url(site)
        got_site = url_object.site
        self.assertEqual(site, got_site)

    def test_finds_site(self):
        # url_object = parse_url('http://www.site.com')
        # site = url_object.site
        # self.assertEqual( 'www.site.com', site)
        self.assertSite('http://www.site.com', 'www.site')
    
    
    def test_finds_another_site(self):
        self.assertSite('http://www.site2.com', 'www.site2.com')
        # url_object = parse_url('http://www.site2.com')
        # site = url_object.site
        # self.assertEqual('www.site2.com', site)