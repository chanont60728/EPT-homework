import media
import fresh_tomatoes


avatar= media.Movie("avatar","A marine on an alien planet" , "http://4.bp.blogspot.com/_1qPLMlz01yQ/SwTA3GFVzxI/AAAAAAAADts/irJykYj7hJs/s400/MarketSaw_03+Nov.+18+23.51.jpg",
                    "www.youtube.com/watch?v=5PSNL1qE6VY")

titanic= media.Movie("Titanic","A seventeen-year-old aristocrat, expecting to be married to a rich claimant by her mother, falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic" , "http://1.bp.blogspot.com/-0N7vyEnl0XU/T4CEbUlhhVI/AAAAAAAABTs/GohXEW3MGNw/s1600/titanic01.jpg",
                    "https://www.youtube.com/watch?v=MtSTrceeFZY")


movies = [avatar,titanic,avatar,avatar,avatar]
fresh_tomatoes.open_movies_page(movies)