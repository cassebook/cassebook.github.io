#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple example how to evaluate sound event detection systems with
# sed_eval toolbox.
#
# Author: Toni Heittola (toni.heittola@tut.fi)

import sed_eval

reference_event_list = sed_eval.util.EventList(
    [
        {
            'event_label': 'car',
            'event_onset': 0.0,
            'event_offset': 2.5,
            'file': 'audio/street/b099.wav',
            'scene_label': 'street'
        },
        {
            'event_label': 'car',
            'event_onset': 2.8,
            'event_offset': 4.5,
            'file': 'audio/street/b099.wav',
            'scene_label': 'street'
        },
        {
            'event_label': 'car',
            'event_onset': 6.0,
            'event_offset': 10.0,
            'file': 'audio/street/a001.wav',
            'scene_label': 'street'
        }
    ]
)

estimated_event_list = sed_eval.util.EventList(
    [
        {
            'event_label': 'car',
            'event_onset': 1.0,
            'event_offset': 3.5,
            'file': 'audio/street/b099.wav',
            'scene_label': 'street'
        },
        {
            'event_label': 'car',
            'event_onset': 7.0,
            'event_offset': 8.0,
            'file': 'audio/street/a001.wav',
            'scene_label': 'street'
        }
    ]
)

# Initialize evaluators
segment_based_metrics = sed_eval.sound_event.SegmentBasedMetrics(
    event_label_list=reference_event_list.unique_event_labels,
    time_resolution=1.0
)
event_based_metrics = sed_eval.sound_event.EventBasedMetrics(
    event_label_list=reference_event_list.unique_event_labels,
    t_collar=0.20
)

# Go through evaluated files file-by-file
for file in reference_event_list.unique_files:
    # Get reference event list for file by filtering reference_event_list
    reference_event_list_for_current_file = reference_event_list.filter(file=file)

    # Get estimated event list for file by filtering estimated_event_list
    estimated_event_list_for_current_file = estimated_event_list.filter(file=file)

    # Evaluate 
    segment_based_metrics.evaluate(
        reference_event_list=reference_event_list_for_current_file,
        estimated_event_list=estimated_event_list_for_current_file
    )
    event_based_metrics.evaluate(
        reference_event_list=reference_event_list_for_current_file,
        estimated_event_list=estimated_event_list_for_current_file
    )

# Print all metrics as report
print(segment_based_metrics)
print(event_based_metrics)

# Segment based metrics
# ----------------------------------------------------------------------
#     Evaluated length  : 14.5  sec
#     Evaluated files   : 2     files
#     Segment length    : 1.00  sec
#
#   Overall metrics (micro-average)
#   ===============
#   F-measure
#     F-measure (F)     :  61.5 %
#     Precision         : 100.0 %
#     Recall            :  44.4 %
#   Error rate
#     Error rate (ER)   :  0.56
#     Substitution rate :  0.00
#     Deletion rate     :  0.56
#     Insertion rate    :  0.00
#   Accuracy
#     Sensitivity       :  44.4 %
#     Specificity       : 100.0 %
#     Balanced accuracy :  72.2 %
#     Accuracy          :  66.7 %
#
#   Class-wise average metrics (macro-average)
#   ===============
#   F-measure
#     F-measure (F)     :  61.5 %
#     Precision         : 100.0 %
#     Recall            :  44.4 %
#   Error rate
#     Error rate (ER)   :  0.56
#     Deletion rate     :  0.56
#     Insertion rate    :  0.00
#   Accuracy
#     Sensitivity       :  44.4 %
#     Specificity       : 100.0 %
#     Balanced accuracy :  72.2 %
#     Accuracy          :  66.7 %
#
#   Class-wise metrics
#   ===============
#     Event label       | Nref | Nsys |    F    :   Pre   :   Rec   |  ER   :  Del  :  Ins  |  Sens   :  Spec   :  Bacc   |   Acc   |
#     ------------------+------+------+---------+---------+---------+-------+-------+-------+---------+---------+---------+---------+
#     car               |    9 |    4 |  61.5 %   100.0 %    44.4 % |  0.56    0.56    0.00 |  44.4 %   100.0 %    72.2 % |  66.7 % |
#
#
#
# Event based metrics (onset-offset)
# ----------------------------------------------------------------------
#     Evaluated length  :  14.5 sec
#     Evaluated files   : 2     files
#     Evaluate onset    : True
#     Evaluate offset   : True
#     T collar          : 200   ms
#     Offset (length)   : 50    %
#
#   Overall metrics (micro-average)
#   ===============
#   F-measure
#     F-measure (F)     :   0.0 %
#     Precision         :   0.0 %
#     Recall            :   0.0 %
#   Error rate
#     Error rate (ER)   :  1.67
#     Substitution rate :  0.00
#     Deletion rate     :  1.00
#     Insertion rate    :  0.67
#
#   Class-wise average metrics (macro-average)
#   ===============
#   F-measure
#     F-measure (F)     :   0.0 %
#     Precision         :   0.0 %
#     Recall            :   0.0 %
#   Error rate
#     Error rate (ER)   :  1.67
#     Deletion rate     :  1.00
#     Insertion rate    :  0.67
#
#   Class-wise metrics
#   ===============
#     Event label       | Nref | Nsys |    F    :   Pre   :   Rec   |  ER   :  Del  :  Ins  |
#     ------------------+------+------+---------+---------+---------+-------+-------+-------+
#     car               |    3 |    2 |   0.0 %     0.0 %     0.0 % |  1.67    1.00    0.67 |
