from settings import get_app_settings
from collectors import get_client


def main():
    print("Hello from spotify-stats-collector!")
    app_settings = get_app_settings()
    spotify_auth_settings = app_settings.apis.spotify
    print("Authenticating with spotify via spotipy...")
    client = get_client(spotify_settings=spotify_auth_settings)

    if client:
        print("Authentication successful.")
        print("Querying for top 20 artist from the last 4 weeks...")
        results = client.current_user_top_artists(time_range='short_term')
        if results:
            print("Results found.")
            top_artists = results['items']
            print("Top 20 Artists:")
            print("-"*40)
            print()
            for i, artist in enumerate(top_artists, start=1):
                print(f"\t{i}. {artist['name']}")
        else:
            print("None returned.")
    else:
        input("Program stopped, press any enter to exit.")


if __name__ == "__main__":
    main()
