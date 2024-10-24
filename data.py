#utilities
import re
from datetime import timedelta
from collections import defaultdict

from textblob import TextBlob
import spacy

#bytewax
#	Simple, open source, scalable framework for data processing 	#

from bytewax.dataflow import DataFlow
from bytewax.inputs import ManualInputConfig
from bytewax.outputs import StdOutputConfig, ManualOutputConfig
from bytewax.execution import run_main
from bytewax.window import TumblingWindowConfig, SystemClockConfig

#X utilities
from twitter import get_rules, delete_all_rules, get_stream, set_stream_rules

def remove_emoji(tweet):
	#	Thinking for a sec... could we apply this to sentiment? 	#
	#	Emojis do provide sentiment. Perhaps we may iterate on this	#
	emoji_list = re.compile(
		"["
		u"\U0001F600 - \U0001F64F"

		"]+",
		flags = re.UNICODE)
	return emoji_list.sub(r'', tweet)

#	Removes user's handle denoted by @ sign 	#
def clean_handle(tweet):
	return re.sub('@[/w]+', '', tweet)

def clean_tweet(tweet):
	return ' '.join(re.sub("()"))