#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple example how to evaluate sound event detection systems.
#
# This example code is adapted and simplified from
# sed_eval.sound_event.SegmentBasedMetrics (https://github.com/TUT-ARG/sed_eval)
#
# Author: Toni Heittola (toni.heittola@tut.fi)

import numpy
from six import iteritems

def convert_list_to_roll(event_list, max_offset_value, event_label_list=None, time_resolution=0.01):

    # Initialize event roll with zeros
    event_roll = numpy.zeros((int(numpy.ceil(max_offset_value * 1 / time_resolution)), len(event_label_list)))

    # Fill-in event_roll
    for event in event_list:
        pos = event_label_list.index(event['event_label'])

        onset = int(numpy.floor(event['event_onset'] * 1 / time_resolution))
        offset = int(numpy.ceil(event['event_offset'] * 1 / time_resolution))

        event_roll[onset:offset, pos] = 1

    return event_roll

reference = {
    'audio/street/b099.wav': [
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
        }
    ],
    'audio/street/a001.wav' : [
        {
            'event_label': 'car',
            'event_onset': 6.0,
            'event_offset': 10.0,
            'file': 'audio/street/a001.wav',
            'scene_label': 'street'
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

event_labels = ['car']

# Initialize intermediate values
intermediate_values = {
    'Ntp': 0.0,
    'Ntn': 0.0,
    'Nfp': 0.0,
    'Nfn': 0.0,
    'Nref': 0.0,
    'Nsys': 0.0,
    'ER': 0.0,
    'S': 0.0,
    'D': 0.0,
    'I': 0.0,
}

for estimated_file, estimated_event_list in iteritems(estimated):
    # Fetch reference event list
    reference_event_list = reference[estimated_file]

    # Get size of event roll
    max_offset_value = max([x['event_offset'] for x in reference_event_list] +[x['event_offset'] for x in estimated_event_list])

    # Generate event rolls
    reference_event_roll = convert_list_to_roll(
        event_list=reference_event_list,
        max_offset_value=max_offset_value,
        event_label_list=event_labels,
        time_resolution=1.0
    )
    estimated_event_roll = convert_list_to_roll(
        event_list=estimated_event_list,
        max_offset_value=max_offset_value,
        event_label_list=event_labels,
        time_resolution=1.0
    )

    # Compute segment-based overall metrics, go through segment-by-segment
    for segment_id in range(0, reference_event_roll.shape[0]):
        annotated_segment = reference_event_roll[segment_id, :]
        system_segment = estimated_event_roll[segment_id, :]

        # Calculate intermediate values
        Ntp = sum(system_segment + annotated_segment > 1)
        Ntn = sum(system_segment + annotated_segment == 0)
        Nfp = sum(system_segment - annotated_segment > 0)
        Nfn = sum(annotated_segment - system_segment > 0)

        # Count active segments
        Nref = sum(annotated_segment)
        Nsys = sum(system_segment)

        # Count Substitutions, Deletions, Insertions
        S = min(Nref, Nsys) - Ntp
        D = max(0, Nref - Nsys)
        I = max(0, Nsys - Nref)

        # Accumulate intermediate values
        intermediate_values['Ntp'] += Ntp
        intermediate_values['Ntn'] += Ntn
        intermediate_values['Nfp'] += Nfp
        intermediate_values['Nfn'] += Nfn
        intermediate_values['Nref'] += Nref
        intermediate_values['Nsys'] += Nsys
        intermediate_values['S'] += S
        intermediate_values['D'] += D
        intermediate_values['I'] += I

# Overall metrics (micro-average)
print('Overall metrics (micro-average)')

# F-measure
precision = intermediate_values['Ntp'] / float(intermediate_values['Nsys'])
recall = intermediate_values['Ntp'] / float(intermediate_values['Nref'])
beta = 1.0
f_measure = (1 + beta**2)*precision*recall/((beta**2)*precision + recall)

print('===============================')
print('F-measure')
print('  precision         = {0:0.4} %'.format(precision*100))
print('  recall            = {0:0.4} %'.format(recall*100))
print('  f_measure         = {0:0.4} %'.format(f_measure*100))


# Error rate
substitution_rate = float(intermediate_values['S'] / float(intermediate_values['Nref']))
deletion_rate = float(intermediate_values['D'] / float(intermediate_values['Nref']))
insertion_rate = float(intermediate_values['I'] / float(intermediate_values['Nref']))
error_rate = float(substitution_rate + deletion_rate + insertion_rate)

print('===============================')
print('Error rate')
print('  substitution_rate = {0:0.2}'.format(substitution_rate))
print('  deletion_rate     = {0:0.2}'.format(deletion_rate))
print('  insertion_rate    = {0:0.2}'.format(insertion_rate))
print('  error_rate        = {0:0.2}'.format(error_rate))

# Overall metrics (micro-average)
# ===============================
# F-measure
#   precision         = 100.0 %
#   recall            = 44.44 %
#   f_measure         = 61.54 %
# ===============================
# Error rate
#   substitution_rate = 0.0
#   deletion_rate     = 0.56
#   insertion_rate    = 0.0
#   error_rate        = 0.56
