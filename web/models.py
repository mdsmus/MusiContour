from django.db import models
from django.core.exceptions import ValidationError


def validate_cps(str):

    def cps_type(str):
        try: [int(x) for x in str.strip().split()]
        except:
            m1 = u'< {0} > is not a valid contour.'.format(str)
            m2 = u'Please enter valid contour points, like 0 2 1.'
            raise ValidationError(' '.join([m1, m2]))

    def cps_size(lst, maximum, minimum):
        absolute = max(maximum, abs(minimum))
        if absolute > 30:
            m1 = u'The value {0} is very big.'.format(absolute)
            m2 = u'Please enter contour points lower than 30.'
            raise ValidationError(' '.join([m1, m2]))

    def cps_positive(minimum):
        if minimum < 0:
            m1 = u'The value {0} is negative.'.format(minimum)
            m2 = u'Please enter only positive contour points.'
            raise ValidationError(' '.join([m1, m2]))

    cps_type(str)
    lst = [int(x) for x in str.strip().split()]
    maximum = max(lst)
    minimum = min(lst)
    cps_size(lst, maximum, minimum)
    cps_positive(minimum)


class Operation(models.Model):

    OP_CHOICES = (('translation', 'Normal form'),
                  ('prime_form_sampaio', 'Prime form Sampaio'),
                  ('prime_form_marvin_laprade', 'Prime form ML'),
                  ('retrograde', 'Retrograde'),
                  ('inversion', 'Inversion'))

    CL_CHOICES = (('b', 'Blue'),
                  ('k', 'Black'),
                  ('y', 'Yellow'),
                  ('g', 'Green'),
                  ('r', 'Red'))

    TP_CHOICES = (('g', 'Graphic'),
                  ('d', 'Description'),
                  ('c', 'Comparison'))

    operation = models.CharField(max_length=30, choices=OP_CHOICES)
    color = models.CharField(max_length=6, choices=CL_CHOICES)
    op_type = models.CharField(max_length=15, choices=TP_CHOICES)

    def __unicode__(self):
        return self.operation


class Contour(models.Model):

    contour_points = models.CharField(max_length=20, default='0 2 1 3 4 5',
                                      validators=[validate_cps])
    operation = models.ManyToManyField(Operation)

    def __unicode__(self):
        return self.contour_points, self.operation
