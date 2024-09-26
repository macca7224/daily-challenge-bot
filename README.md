Ensure `.env` fields are set before running.

Then either run manually `python3 bot.py` or setup a cron job to run daily automatically

e.g. for Linux add a record like this
`0 12 * * * /usr/bin/python3 ~/daily-challenge/bot.py > ~/cron_output.log 2>&1`
