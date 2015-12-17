#!/bin/bash
pushd ~/code/hiphop-links &>/dev/null
. env/bin/activate &>/dev/null
hiphop-generate ~/.weechat/logs/irc.bitlbee.#hiphop.weechatlog
mv hiphop.html /var/smiley
cp static/* /var/smiley
popd &>/dev/null
