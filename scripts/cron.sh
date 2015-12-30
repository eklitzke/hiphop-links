#!/bin/bash
pushd ~/hiphop-links &>/dev/null
. env/bin/activate &>/dev/null
hiphop-generate --title="hiphop links" --outfile="hiphop.html" ~/.weechat/logs/irc.bitlbee.#hiphop.weechatlog
hiphop-generate --title="edm links" --outfile="edm.html" ~/.weechat/logs/irc.bitlbee.#edm.weechatlog
mv hiphop.html edm.html /var/www
cp static/* /var/www
popd &>/dev/null
