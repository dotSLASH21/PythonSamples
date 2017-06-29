import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 2.5,
                     "A story of a boy and his toys that come to life",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                     "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", 3,
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

fantastic_beasts = media.Movie("Fantastic Beasts and Where to Find Them", 2.7,
                     "The adventures of writer Newt Scamander in New York's secret community of witches and wizards seventy years before Harry Potter reads his book in school.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/8/8d/Fantastic_beasts.JPG/220px-Fantastic_beasts.JPG",
                     "https://www.youtube.com/watch?v=Vso5o11LuGU")

ratatouille = media.Movie("Ratatouille", 2.6,
                        "A story of a mouse who's dream is to be a famous cook!",
                        "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                        "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", 3,
                        "Gil Pender (Owen Wilson) is a screenwriter and aspiring novelist. Vacationing in Paris with his fiancee (Rachel McAdams), he has taken to touring the city alone. On one such late-night excursion, Gil encounters a group of strange -- yet familiar -- revelers, who sweep him along, apparently back in time, for a night with some of the Jazz Age's icons of art and literature. The more time Gil spends with these cultural heroes of the past, the more dissatisfied he becomes with the present.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/220px-Midnight_in_Paris_Poster.jpg",
                        "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("The Hunger Games", 3,
                        "In what was once North America, the Capitol of Panem maintains its hold on its 12 districts by forcing them each to select a boy and a girl, called Tributes, to compete in a nationally televised event called the Hunger Games. Every citizen must watch as the youths fight to the death until only one remains. District 12 Tribute Katniss Everdeen (Jennifer Lawrence) has little to rely on, other than her hunting skills and sharp instincts, in an arena where she must weigh survival against love.",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                        "https://www.youtube.com/watch?v=4S9a5V9ODuY")


movies = [toy_story, avatar, fantastic_beasts, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.__doc__)
#print(media.Movie.__module__)
#print(media.Movie.__name__)
#print(media.Movie.__dict__)
