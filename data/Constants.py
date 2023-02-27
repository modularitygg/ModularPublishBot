# -*- coding: utf-8 -*-
#!/usr/bin/env python
import discord
import os

sep = os.path.sep

publishBotIntents = discord.Intents.default()
publishBotIntents.message_content = True

isDevEnvironment = not os.getcwd().startswith(sep)

def getPublishBotToken():
	if isDevEnvironment:
		return os.environ.get('ModularDevBotToken')
	return os.environ.get('ModularPublishBotToken')