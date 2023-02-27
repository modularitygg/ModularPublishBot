# -*- coding: utf-8 -*-
#!/usr/bin/env python
from pathlib 					import Path
from glob						import glob
from datetime 					import datetime, timedelta
from discord.ext 				import tasks
import discord
import shutil
import requests
import time
import os
import sys

from data						import Constants, Folders, Variables

def setupEvents():

	@Variables.publishBotClient.event
	async def on_ready():
		print('Initialized client as {0.user}.'.format(Variables.publishBotClient))

		update_presence.start()

		return

	@tasks.loop(seconds=60.0)
	async def update_presence():
		if Constants.isDevEnvironment:
			await Variables.publishBotClient.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="ModularPublishBot"))
			return

		serverCount = len(Variables.publishBotClient.guilds)
		status = str(serverCount) + " server"
		if serverCount > 1:
			status += "s"

		await Variables.publishBotClient.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))

		return

	@Variables.publishBotClient.event
	async def on_message(message):
		if message.author == Variables.publishBotClient.user:
			return

		if str(message.channel.type) == "news":
			await message.publish()

		return

	return