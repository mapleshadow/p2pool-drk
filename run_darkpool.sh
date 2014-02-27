#!/bin/sh
SERVICE='python ./run_p2pool.py --net darkcoin'

if ps ax | grep -v grep | grep "$SERVICE" > /dev/null
then
        echo "$SERVICE is already running!"
else
        screen -d -m -S P2P_DRK_DIFF python ./run_p2pool.py --net darkcoin --give-author 0 --disable-upnp -f 1

	wait
fi
