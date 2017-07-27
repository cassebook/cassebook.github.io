#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple example how to evaluate audio tagging systems with
# sklearn.metrics.
#
# Author: Toni Heittola (toni.heittola@tut.fi)

import sklearn.metrics
import numpy

def equal_error_rate(y_pred, y_true):
    fpr, tpr, thresholds = metrics.roc_curve(gt, pred, drop_intermediate=True)

    eps = 1E-6
    Points = [(0,0)]+zip(fpr, tpr)
    for i, point in enumerate(Points):
        if point[0]+eps >= 1-point[1]:
            break
    P1 = Points[i-1]; P2 = Points[i]

    #Interpolate between P1 and P2
    if abs(P2[0]-P1[0]) < eps:
        EER = P1[0]
    else:
        m = (P2[1]-P1[1]) / (P2[0]-P1[0])
        o = P1[1] - m * P1[0]
        EER = (1-o) / (1+m)
    return EER



reference = {
    'audio1.wav': [
        {
            'file': 'audio1.wav',
            'tags': ['a', 'b'],
        }
    ],
    'audio2.wav' : [
        {
            'file': 'audio2.wav',
            'tags': ['b', 'c'],
        }
    ],
    'audio3.wav' : [
        {
            'file': 'audio3.wav',
            'tags': ['c'],
        }
    ]
}

estimated = {
    'audio/street/b099.wav': [
        {
            'event_label': 'car',
            'event_onset': 1.0,
            'event_offset': 3.5,
            'file': 'audio/street/b099.wav',
            'scene_label': 'street'
        }
    ],
    'audio/street/a001.wav' : [
        {
            'event_label': 'car',
            'event_onset': 7.0,
            'event_offset': 8.0,
            'file': 'audio/street/a001.wav',
            'scene_label': 'street'
        }
    ]
}

from IPython import embed
embed()
