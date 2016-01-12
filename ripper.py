from radionewsripper.radionewsripper import RadioNewsRipper

# Record 'Ö3' for 5 minutes... Just for testing

url = "http://mp3stream7.apasf.apa.at:8000/"
length = 5 * 60

ripper = RadioNewsRipper(url, length)
ripper.record()
