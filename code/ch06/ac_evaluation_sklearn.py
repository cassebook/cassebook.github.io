#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple example how to evaluate acoustic scene classification systems with
# sklearn.metrics.
#
# Author: Toni Heittola (toni.heittola@tut.fi)

import sklearn.metrics
import numpy

reference = [
    {
        'scene_label': 'supermarket',
        'file': 'supermarket09.wav'
    },
    {
        'scene_label': 'tubestation',
        'file': 'tubestation10.wav'
    },
    {
        'scene_label': 'quietstreet',
        'file': 'quietstreet08.wav'
    },
    {
        'scene_label': 'office',
        'file': 'office10.wav'
    },
    {
        'scene_label': 'bus',
        'file': 'bus01.wav'
    },
]

estimated = [
    {
        'scene_label': 'supermarket',
        'file': 'supermarket09.wav'
    },
    {
        'scene_label': 'bus',
        'file': 'tubestation10.wav'
    },
    {
        'scene_label': 'quietstreet',
        'file': 'quietstreet08.wav'
    },
    {
        'scene_label': 'park',
        'file': 'office10.wav'
    },
    {
        'scene_label': 'car',
        'file': 'bus01.wav'
    },
]

y_true = numpy.array([])
y_pred = numpy.array([])
for estimated_item in estimated:
    reference_item_matched = {}
    for reference_item in reference:
        if estimated_item['file'] == reference_item['file']:
            reference_item_matched = reference_item
            break

    y_true = numpy.append(y_true, reference_item_matched['scene_label'])
    y_pred = numpy.append(y_pred, estimated_item['scene_label'])

accuracy = sklearn.metrics.accuracy_score(y_true=y_true, y_pred=y_pred)
print("accuracy = {0:0.4}%".format(accuracy*100.0))

print(sklearn.metrics.classification_report(y_true=y_true, y_pred=y_pred))

# accuracy = 40.0%
#
#   'recall', 'true', average, warn_for)
#              precision    recall  f1-score   support
#
#         bus       0.00      0.00      0.00         1
#         car       0.00      0.00      0.00         0
#      office       0.00      0.00      0.00         1
#        park       0.00      0.00      0.00         0
# quietstreet       1.00      1.00      1.00         1
# supermarket       1.00      1.00      1.00         1
# tubestation       0.00      0.00      0.00         1
#
# avg / total       0.40      0.40      0.40         5
