
import unittest
import json
import requests
#from urllib3 import Request, urlopen

class Chat(unittest.TestCase):


   def test_response(self):
       url = 'http://127.0.0.1:5000'
       response = requests.get(url)
       try:
           self.assertEqual(response.status_code,200)
       except requests.exceptions.ConnectionError as e:
         print(e)
         exit(1)



if __name__ =='__main__':
      unittest.main()