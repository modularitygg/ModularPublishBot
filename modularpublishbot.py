# -*- coding: utf-8 -*-
# !/usr/bin/env python
import discord
import json
import os
import sys

from data						import Constants, Variables
from events 					import PublishBotEvents

sep = os.path.sep

def main():
	os.environ['TZ'] = 'Europe/Amsterdam'

	Variables.publishBotClient = discord.Client(intents=Constants.publishBotIntents)
	PublishBotEvents.setupEvents()
	Variables.publishBotClient.run(Constants.getPublishBotToken())

	return


if __name__ == "__main__":
	main()