from quorapy import Quora
import os
from quorapy.browser import Browser

browser = Browser(os.getenv('WINDOWS'))
quora = Quora(browser)

results = quora.search('Python')

print(results)


