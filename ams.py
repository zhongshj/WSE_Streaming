from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json

consumer_key = "Xv9W0XpiZxntW9ntXcBjf1bvo"
consumer_secret = "JH5KQ3eYiEsrVOccpPIyurJe77A7a4xOgiDMOx4DvbJ8jDTDRY"

access_token = "793735961691746304-nVMRnoVguoz6v62jdYYMdKAmELQU4AC"
access_token_secret = "Miu9EXCrc34yGZr6nkWm3JA8rvSlyTHPFOZMpEyOlOeuB"

geobox_amsterdam = [4.73, 52.29, 4.98, 52.42]
file = open('ams.json', 'a')


class StdOutListener(StreamListener):

	def on_data(self,data):
		print(data)
		json_data = json.loads(data)
		file.write(str(json_data))
		file.write('\r\n')

	def on_error(self,status):
		print(status)


if __name__ == '__main__':

	l = StdOutListener()
	auth = OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)

	stream = Stream(auth,l)
	stream.filter(locations=geobox_amsterdam)

