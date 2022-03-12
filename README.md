Setup:

Install Requirements.txt

`pip install requirements.txt`

create a .env file,

`
MOVIE-PLAYLIST-NAME=NONE
TV-SHOW-PLAYLIST-NAME=NONE
PLEX-ACCESS-TOKEN=     *REQUIRED*
PLEX-LOCAL-URL=        *REQUIRED*
DISCORD-WEBHOOK-URL=NONE
`

Keep `DISCORD-WEBHOOK-URL` NONE to disable,
Keep `MOVIE-PLAYLIST-NAME` NONE to disable,
Keep `TV-SHOW-PLAYLIST-NAME` NONE to disable


run a cron job just run the file, `plex-purge.py`

Boom all done, Watch your favorite content, and save storage!
