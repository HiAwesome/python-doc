from string import Template

t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))  # Nottinghamfolk send $10 to the ditch fund.

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')

try:
    t.substitute(d)
except KeyError as e:
    assert str(e) == "'owner'"

print(t.safe_substitute(d))  # Return the unladen swallow to $owner.

import time, os.path

photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']


class BatchRename(Template):
    delimiter = '%'


# Enter: Ashley_%n%f
fmt = input('Enter rename style (%d-date %n-seqnum %f-format): ')

t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    new_name = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, new_name))

"""
Nottinghamfolk send $10 to the ditch fund.
Return the unladen swallow to $owner.
Enter rename style (%d-date %n-seqnum %f-format): Ashley_%n%f
img_1074.jpg --> Ashley_0.jpg
img_1076.jpg --> Ashley_1.jpg
img_1077.jpg --> Ashley_2.jpg
"""
