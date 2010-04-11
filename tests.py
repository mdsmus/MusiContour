#!/usr/bin/env python
# -*- coding: utf-8 -*-

from contour import contour_class
from contour import contours_count
from contour import kern_file_process

### data
## soprano, choral 002
contour = [440.00, 493.88, 392.00, 369.99, 329.63, 493.88, 554.37,
493.88, 440.00, 415.30, 369.99, 415.30, 369.99, 329.63, 659.26,
587.33, 554.37, 493.88, 440.00, 493.88, 554.37, 493.88, 554.37,
587.33, 554.37, 493.88, 466.16, 493.88, 329.63, 440.00, 493.88,
554.37, 587.33, 659.26, 587.33, 554.37, 493.88, 587.33, 554.37,
493.88, 659.26, 587.33, 554.37, 493.88, 440.00, 493.88, 554.37,
493.88, 440.00]


contour_cc = contour_class(contour)


print(contours_count(contour_cc, 4))


print(kern_file_process('/tmp/teste-python/002.krn'))
