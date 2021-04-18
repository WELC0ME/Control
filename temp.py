import os
# import requests
#
# print(requests.post('http://127.0.0.1:5000/api/admin/init', json={
#     'token': 'IB1jiktwudOP8eLfoVXbIRrgp8KxRYlpqnzByVXS0EATLeZ0ZO6yynHN'
# }))

ends = ['.py']
counter = 0
for a, b, c in os.walk('.'):
    for d in c:
        if any([d.endswith(i) for i in ends]):
            counter += len(open(a + '/' + d, 'r', encoding='utf8').readlines())
print(counter)
