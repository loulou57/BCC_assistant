import re
import urllib.parse

import discord
from discord.ext import commands

AMAZON_TAG = ('bricolagecest-21')
ALIEXPRESS_TAG = ('BricolageCestCool')

ALIEXPRESS_REGEX = "(http[s]?://[a-zA-Z0-9.-]+aliexpress.com(?:.+?dl_target_url=(.+)|[^ \n?]+?(?:.html)|[^ \n?]+))"
AMAZON_REGEX = "(http[s]?://[a-zA-Z0-9.-]*(?:amazon|amzn).[a-zA-Z]+(?:.+?(?:ref=[^?]+)|.+(?= )|[^?]+))"

class affiliation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, ctx):
   	
        if ctx.author == self.bot.user:
            return

        affiliate_links = []

        if ALIEXPRESS_REGEX:
            for match in re.findall(ALIEXPRESS_REGEX, ctx.content):
                affiliate_links.append(get_aliexpress_affiliate_link(
                    match[1] if len(match[1]) > 0 else urllib.parse.quote_plus(match[0])))
        if AMAZON_TAG:
            for match in re.findall(AMAZON_REGEX, ctx.content):
                affiliate_links.append(get_amazon_affiliate_link(match))

        if affiliate_links:
            response = f"Salut, {ctx.author.mention} pour soutenir Bricolage C'est Cool je t'invite à commander avec ce lien affilié! Merci! <:smiley:1006248598025011320>"
            for affiliate_link in affiliate_links:
                response += "\n" + affiliate_link

            await ctx.channel.send(response)


def get_aliexpress_affiliate_link(url):
    return f'https://s.click.aliexpress.com/deep_link.htm?aff_short_key={ALIEXPRESS_TAG}&dl_target_url={url}'

def get_amazon_affiliate_link(url):
    return url + f'?tag={AMAZON_TAG}'