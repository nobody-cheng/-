import re
result = re.match('\w{4,20}@(126|139|qq|189|hotmail|gmail)\.com$', '13823875990@139.com')
print(result.group())