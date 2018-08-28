import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story","A story of toy and boys",
                        "http://t0.gstatic.com/images?q=tbn:ANd9GcRKk8fPFSi83NmjO4hlth9VpXsqigxNXrG10hXum8ljJ_fZ07c1",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toy_story.title)
avatar_story = media.Movie("Avatar","A story of land where human wants to capture",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                           "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print(avatar_story.title)
#avatar_story.show_trailer()
gold = media.Movie("Gold","A dream that united our Nation",
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcTETJZB4YCUqB_KoEZ9Oyvfd_fQmjfsTeoeqfzxVEGR-II2wkv9",
                           "https://www.youtube.com/watch?v=Pcv0aoOlsLM")

satyameva_jayate = media.Movie("Satyameva Jayate","Truth alone triumphs",
                           "http://t2.gstatic.com/images?q=tbn:ANd9GcRMPBpPgxmkD0S4jcl0vCFsEUNFVKvZ9BmJKWmHVq96jymPfI4B",
                           "https://www.youtube.com/watch?v=odXKXLG43co")

khakhi = media.Movie("Khakee","DCP Anant and his team are assigned to escort an alleged terrorist to Mumbai.",
                           "https://cdn8.bigcommerce.com/s-21la3u/images/stencil/1280x1280/products/29273/12884/DVD_KHAKEE&AANKHEN_LRG__31722.1411313620.jpg?c=2&imbypass=on",
                           "https://www.youtube.com/watch?v=nuo5cq2QBcg")

loc = media.Movie("LOC","The war that happened on mountain",
                           "https://img.bumppy.com/bumppy/2017/06/loc-kargil-full-movie-poster.png",
                           "https://www.youtube.com/watch?v=5I4MrraEmwo")
hera_pheri = media.Movie("HeraPheri","Comdey film",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/5/51/Hera_Pheri_%28poster%29.jpg/220px-Hera_Pheri_%28poster%29.jpg",
                           "https://www.youtube.com/watch?v=9Pfit4SC_jk")
phir_hera_pheri = media.Movie("Phir HeraPheri","Comdey film",
                           "https://m.media-amazon.com/images/M/MV5BNzgzYjZjYzMtNjcyYy00NWI3LTg1NDItOTMzMzdhMjhjNWExXkEyXkFqcGdeQXVyNjA3OTI5MjA@._V1_QL50_.jpg",
                           "https://www.youtube.com/watch?v=qQcLuLRZ3Ec")

hosefull_3 = media.Movie("Housefull3","Comdey film",
                           "https://images-na.ssl-images-amazon.com/images/I/81oV86YGnLL._SY445_.jpg",
                           "https://www.youtube.com/watch?v=ss8YHOCbkZ8")

list_of_movies = [phir_hera_pheri,hosefull_3,hera_pheri,loc,khakhi,satyameva_jayate,gold,avatar_story,toy_story]
fresh_tomatoes.open_movies_page(list_of_movies)
#print(loc.__lt__)
'''Below text is predefined varible of a python class'''
#['title', 'storyline', 'poster_image_url', 'trailer_youtube_url',
# '__module__', '__doc__', '__init__', 'show_trailer', '__dict__',
# '__weakref__', '__repr__', '__hash__', '__str__', '__getattribute__',
# '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__',
# '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__',
#  '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
