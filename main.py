import os
from discord_webhook import DiscordWebhook
from plexapi.server import PlexServer
from dotenv import load_dotenv


def deleteShows(playlist, baseurl, token, discord_webhook_url):
    plex = PlexServer(baseurl, token)

    # Delete Shows after admin watches;
    shows = plex.library.section(playlist)

    for show in shows.searchShows():
        print(show.title)
        for seasons in show.seasons():
            print(seasons.title)
            for episode in seasons.episodes():

                if not episode.isWatched:
                    print(episode.title)
                else:
                    print(episode.title + " >> DELETE ME")
                    location = episode.locations[0]
                    os.remove(location)
                    if str(discord_webhook_url) != "NONE":
                        webhook = DiscordWebhook(url=discord_webhook_url,
                                                 content=f"WATCHED & DELETED || SHOW: {show.title} >> {seasons.title} >> {episode.title}")
                        webhook.execute()


def deleteMovies(playlist, baseurl, token, discord_webhook_url):
    plex = PlexServer(baseurl, token)

    movies = plex.library.section(playlist)

    for movie in movies.searchMovies():
        if not movie.isWatched:
            print(movie.title)
        else:
            print(movie.title + " >> DELETE ME")
            location = movie.locations[0]
            os.remove(location)
            if str(discord_webhook_url) != "NONE":
                webhook = DiscordWebhook(url=discord_webhook_url,
                                         content=f"WATCHED & DELETED || MOVIE: {movie.title}")
                webhook.execute()


def main():
    load_dotenv()
    movie_playlist_name = os.getenv('MOVIE-PLAYLIST-NAME')
    TV_show_playlist_name = os.getenv('TV-SHOW-PLAYLIST-NAME')
    token = os.getenv('PLEX-ACCESS-TOKEN')
    baseurl = os.getenv('PLEX-LOCAL-URL')
    webhook_url = os.getenv('DISCORD-WEBHOOK-URL')
    deleteMovies(playlist=movie_playlist_name, token=token, baseurl=baseurl, discord_webhook_url=webhook_url)
    deleteShows(playlist=TV_show_playlist_name, token=token, baseurl=baseurl, discord_webhook_url=webhook_url)


main()
