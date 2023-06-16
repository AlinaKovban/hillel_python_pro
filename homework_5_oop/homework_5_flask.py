from flask import Flask, request
from faker import Faker

app = Flask(__name__)

fake_data = Faker("UK")


@app.route("/stats_by_city")
def stats_by_city():
    existing_genre = ["Pop", "HipHop", "Rock", "Soul",
                      "Reggae", "Country", "Funk", "Folk", "Jazz",
                      "Disco", "Classical", "Electronic", "Blues"]
    cities = [fake_data.city_name() for _ in range(461)]
    getting_genre = request.args.get("genre")

    if getting_genre in existing_genre:
        random_city = fake_data.random_element(cities)
        return random_city
    else:
        return """
                  This genre is doesn't exist or you don't input any genre.
                  Choose one of these genres: Pop, HipHop, Rock, Soul, Reggae,
                  Country, Funk, Folk, Jazz, Disco,
                  Classical, Electronic, Blues
               """


if __name__ == '__main__':
    app.run()
