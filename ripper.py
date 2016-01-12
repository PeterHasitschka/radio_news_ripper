#!/usr/bin/python3

from radionewsripper.radionewsripper import RadioNewsRipper

import argparse


p = argparse.ArgumentParser(description='Recording a livestream for X seconds and move it as mp3 to a specific location')
p.add_argument('url', metavar='url', type=str, help='Url of the livestream (e.g "http://mystream_xyz42.org:8000")')
p.add_argument('length', metavar='length', type=int, help='Length of recording in seconds')
p.add_argument('location', metavar='location', type=str, help='Location to move the mp3 after ' +
                                                              'recording. (e.g. "~/my_existing_recfolder"')
p.add_argument('name', metavar='name', type=str, help='Name of the mp3 (without ending). e.g. "myfavradiostation"')
args = p.parse_args()


ripper = RadioNewsRipper(args.url, args.length, args.location, args.name)
ripper.record()
