#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple example how to evaluate audio tagging systems with
# sed_eval toolbox.
#
# Author: Toni Heittola (toni.heittola@tut.fi)

import sed_eval
import dcase_util

# Reference tag activity
reference_tag_list = dcase_util.containers.MetaDataContainer([
    {
        'filename': 'test1.wav',
        'tags': 'cat,dog'
    },
    {
        'filename': 'test2.wav',
        'tags': 'dog'
    },
    {
        'filename': 'test3.wav',
        'tags': 'bird,cat'
    },
    {
        'filename': 'test4.wav',
        'tags': 'cat'
    },
    {
        'filename': 'test5.wav',
        'tags': 'bird,speech'
    },
    {
        'filename': 'test6.wav',
        'tags': 'dog,speech'
    },
    {
        'filename': 'test7.wav',
        'tags': 'speech'
    },
])

# Tag probabilities for each tag per file
estimated_tag_probabilities = dcase_util.containers.ProbabilityContainer([
    {
        'filename': 'test1.wav',
        'label': 'bird',
        'probability': 0.2
    },
    {
        'filename': 'test1.wav',
        'label': 'cat',
        'probability': 0.99
    },
    {
        'filename': 'test1.wav',
        'label': 'dog',
        'probability': 0.88
    },
    {
        'filename': 'test1.wav',
        'label': 'speech',
        'probability': 0.01
    },

    {
        'filename': 'test2.wav',
        'label': 'bird',
        'probability': 0.1
    },
    {
        'filename': 'test2.wav',
        'label': 'cat',
        'probability': 0.3
    },
    {
        'filename': 'test2.wav',
        'label': 'dog',
        'probability': 0.8
    },
    {
        'filename': 'test2.wav',
        'label': 'speech',
        'probability': 0.1
    },

    {
        'filename': 'test3.wav',
        'label': 'bird',
        'probability': 0.7
    },
    {
        'filename': 'test3.wav',
        'label': 'cat',
        'probability': 0.6
    },
    {
        'filename': 'test3.wav',
        'label': 'dog',
        'probability': 0.4
    },
    {
        'filename': 'test3.wav',
        'label': 'speech',
        'probability': 0.3
    },

    {
        'filename': 'test4.wav',
        'label': 'bird',
        'probability': 0.323
    },
    {
        'filename': 'test4.wav',
        'label': 'cat',
        'probability': 0.6
    },
    {
        'filename': 'test4.wav',
        'label': 'dog',
        'probability': 0.56
    },
    {
        'filename': 'test4.wav',
        'label': 'speech',
        'probability': 0.4
    },

    {
        'filename': 'test5.wav',
        'label': 'bird',
        'probability': 0.8
    },
    {
        'filename': 'test5.wav',
        'label': 'cat',
        'probability': 0.7
    },
    {
        'filename': 'test5.wav',
        'label': 'dog',
        'probability': 0.45
    },
    {
        'filename': 'test5.wav',
        'label': 'speech',
        'probability': 0.43
    },

    {
        'filename': 'test6.wav',
        'label': 'bird',
        'probability': 0.9
    },
    {
        'filename': 'test6.wav',
        'label': 'cat',
        'probability': 0.53
    },
    {
        'filename': 'test6.wav',
        'label': 'dog',
        'probability': 0.83
    },
    {
        'filename': 'test6.wav',
        'label': 'speech',
        'probability': 0.95
    },

    {
        'filename': 'test7.wav',
        'label': 'bird',
        'probability': 0.2
    },
    {
        'filename': 'test7.wav',
        'label': 'cat',
        'probability': 0.2
    },
    {
        'filename': 'test7.wav',
        'label': 'dog',
        'probability': 0.89
    },
    {
        'filename': 'test7.wav',
        'label': 'speech',
        'probability': 0.45
    },
])

# Process estimations and make decisions with 0.5 threshold
estimated_tag_list = dcase_util.containers.MetaDataContainer()
for file in estimated_tag_probabilities.unique_files:
    k = estimated_tag_probabilities.filter(filename=file)
    tags = []
    for item in k:
        if item.probability > 0.5:
            tags.append(item.label)

    estimated_tag_list.append(
        {
            'filename': file,
            'tags': tags
        }
    )

# Initialize evaluator
tag_evaluator = sed_eval.audio_tag.AudioTaggingMetrics(
    tags=reference_tag_list.unique_tags
)

# Evaluate
tag_evaluator.evaluate(
    reference_tag_list=reference_tag_list,
    estimated_tag_list=estimated_tag_list,
    estimated_tag_probabilities=estimated_tag_probabilities
)

# Print all metrics as report
print(tag_evaluator)

# Audio tagging metrics
# ========================================
#   Tags                              : 4
#   Evaluated units                   : 11
#
#   Overall metrics (micro-average)
#   ======================================
#   F-measure
#     F-measure (F1)                  : 72.00 %
#     Precision                       : 64.29 %
#     Recall                          : 81.82 %
#   Equal error rate
#     Equal error rate (EER)          : 18.18 %
#
#   Class-wise average metrics (macro-average)
#   ======================================
#   F-measure
#     F-measure (F1)                  : 70.00 %
#     Precision                       : 71.67 %
#     Recall                          : 83.33 %
#   Equal error rate
#     Equal error rate (EER)          : 17.50 %
#
#   Class-wise metrics
#   ======================================
#     Tag               | Nref        Nsys      | F-score     Pre         Rec       | EER
#     ----------------- | ---------   --------- | ---------   ---------   --------- | ---------
#     bird              | 2           3         | 80.0%       66.7        100.0     | 20.0%
#     cat               | 3           5         | 75.0%       60.0        100.0     | 25.0%
#     dog               | 3           5         | 75.0%       60.0        100.0     | 25.0%
#     speech            | 3           1         | 50.0%       100.0       33.3      | 0.0%
