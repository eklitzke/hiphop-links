# About

This is some code to pull links from HipChat and make an HTML page with URLs to
YouTube, SoundCloud, Spotify, etc.

## How It Works

I'm using the Hipchat [XMPP](https://en.wikipedia.org/wiki/XMPP) gateway to talk
on Hipchat. Then I use [BitlBee](https://www.bitlbee.org/) as an XMPP to
[IRC](https://en.wikipedia.org/wiki/Internet_Relay_Chat) gateway. I have all of
this configured so that my [IRC client](https://weechat.org/) is connected to
Hipchat 24/7, even when I'm not at my computer.

I've written a couple of blog posts about how my Hipchat setup works,
[here's one](https://eklitzke.org/bitlbee-and-hipchat) and
[here's another](https://eklitzke.org/bitlbee-accounts).

The scripts in this repo simply scan my IRC client logs for links matching
particular regular expressions and then generate HTML pages from that.q
