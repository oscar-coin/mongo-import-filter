import re

subreddits = re.compile(
    "film|movie|oscar|academy|award|^actor|^director|^script|hollywood|critic|flick|cinema|coming soon")
movies = {
    "2011": ['Harry Potter and the Deathly Hallows Part 2?', 'Transformers[:]? Dark of the Moon',
             'The Twilight Saga[:]? Breaking Dawn Part 1', 'The Hangover Part II',
             'Pirates of the Caribbean[:]? On Stranger Tides', 'Fast Five', 'Mission[:]? Impossible - Ghost Protocol',
             'Cars 2', 'Sherlock Holmes[:]? A Game of Shadows', 'Thor', 'Rise of the Planet of the Apes',
             'Captain America[:]? The First Avenger', 'The Help', 'Bridesmaids', 'Kung Fu Panda 2', 'Puss in Boots',
             'X-Men[:]? First Class', 'Rio', 'The Smurfs', 'Alvin and the Chipmunks(:)? Chipwrecked', 'Super 8', 'Rango',
             'Horrible Bosses', 'Green Lantern', 'Hop', 'Paranormal Activity 3', 'Just Go With It',
             'The Girl with the Dragon Tattoo', 'Bad Teacher', 'Cowboys & Aliens', 'Gnomeo and Juliet',
             'The Lion King', 'The Muppets', 'Real Steel', 'Crazy, Stupid, Love.', 'Battle[:]? Los Angeles',
             'Immortals', 'The Descendants', 'Zookeeper', 'War Horse', 'Limitless', 'Tower Heist',
             'The Adventures of Tintin', 'Contagion', 'We Bought a Zoo', 'Moneyball', 'Jack and Jill', 'Hugo',
             'Justin Bieber[:]? Never Say Never', 'Dolphin Tale'],
    "2012": ['Marvel[\']?s The Avengers', 'The Dark Knight Rises', 'The Hunger Games', 'Skyfall',
             'The Hobbit[:]? An Unexpected Journey', 'The Twilight Saga[:]? Breaking Dawn Part 2',
             'The Amazing Spider-Man', 'Brave', 'Ted', 'Madagascar 3[:]? Europe[[\']?s]? Most Wanted',
             'Dr. Seuss[\']? The Lorax', 'Wreck-It Ralph', 'Lincoln', 'MIB 3', 'Django Unchained',
             'Ice Age[:]? Continental Drift', 'Snow White and the Huntsman', 'Les Miserables',
             'Hotel Transylvania', 'Taken 2', '21 Jump Street', 'Argo', 'Silver Linings Playbook',
             'Prometheus', 'Safe House', 'The Vow', 'Life of Pi', 'Magic Mike', 'The Bourne Legacy',
             'Journey 2[:]? The Mysterious Island', 'Rise of the Guardians', 'Zero Dark Thirty', 'Flight',
             'Think Like a Man', 'The Campaign', 'The Expendables 2', 'Wrath of the Titans', 'Jack Reacher',
             'Dark Shadows', 'Parental Guidance', 'John Carter', 'Mama', 'Act of Valor', 'This Is 40', 'Looper',
             'Tyler Perry[[\']?s]? Madea[\'s]? Witness Protection', 'Battleship', 'Pitch Perfect', 'Mirror Mirror',
             'Chronicle'],
    "2013": ['The Hunger Games[:]? Catching Fire', 'Iron Man 3', 'Frozen', 'Despicable Me 2', 'Man of Steel', 'Gravity',
             'Monsters University', 'The Hobbit[:]? The Desolation of Smaug', 'Fast & Furious 6',
             'Oz The Great and Powerful', 'Star Trek Into Darkness', 'Thor[:]? The Dark World', 'World War Z',
             'The Croods', 'The Heat', 'We\'re the Millers', 'American Hustle', 'The Great Gatsby',
             'The Conjuring', 'Ride Along', 'Identity Thief', 'Grown Ups 2', 'The Wolverine',
             'Anchorman 2[:]? The Legend Continues', 'Lone Survivor', 'G.I. Joe[:]? Retaliation',
             'Cloudy with a Chance of Meatballs 2', 'Now You See Me', 'The Wolf of Wall Street',
             'Lee Daniels[\']? The Butler', 'The Hangover Part III', 'Epic', 'Captain Phillips',
             'Jackass Presents[:]? Bad Grandpa', 'Pacific Rim', 'This is the End', 'Olympus Has Fallen',
             '42', 'Elysium', 'Planes', 'The Lone Ranger', 'Oblivion', 'Insidious Chapter 2',
             'Saving Mr. Banks', 'Turbo', '2 Guns', 'White House Down', 'Safe Haven', 'The Smurfs 2',
             'The Best Man Holiday'],
    "2014": ['American Sniper', 'The Hunger Games[:]? Mockingjay - Part 1', 'Guardians of the Galaxy',
             'Captain America[:]? The Winter Soldier', 'The LEGO Movie',
             'The Hobbit[:]? The Battle of the Five Armies', 'Transformers[:]? Age of Extinction',
             'Maleficent', 'X-Men[:]? Days of Future Past', 'Big Hero 6', 'Dawn of the Planet of the Apes',
             'The Amazing Spider-Man 2', 'Godzilla', '22 Jump Street', 'Teenage Mutant Ninja Turtles',
             'Interstellar', 'How to Train Your Dragon 2', 'Gone Girl', 'Divergent', 'Neighbors', 'Rio 2',
             'Into the Woods', 'Lucy', 'The Fault in our Stars', 'Unbroken',
             'Night at the Museum[:]? Secret of the Tomb', 'Mr. Peabody & Sherman', '300[:]? Rise of An Empire',
             'The Maze Runner', 'The Equalizer', 'Noah', 'Edge of Tomorrow', 'Non-Stop', 'Heaven is for Real',
             'The Imitation Game', 'Taken 3', 'Dumb and Dumber To', 'Annie', 'Fury', 'Tammy',
             'Annabelle', 'The Other Woman', 'Penguins of Madagascar', 'Let[[\']?s]? Be Cops',
             'The Monuments Men', 'Paddington', 'Hercules', 'The Purge[:]? Anarchy',
             'Alexander and the Terrible, Horrible, No Good, Very Bad Day', 'Think Like a Man Too'],
    "2015": ['52 Tuesdays', 'Jurassic World', 'Avengers[:]? Age of Ultron', 'Inside Out', 'Furious 7', 'Minions',
             'Cinderella', 'Mission[:]? Impossible - Rogue Nation', 'Pitch Perfect 2', 'Ant-Man', 'Home',
             'The Martian', 'Fifty Shades of Grey', 'The SpongeBob Movie[:]? Sponge Out of Water',
             'Straight Outta Compton', 'San Andreas', 'Mad Max[:]? Fury Road', 'Hotel Transylvania 2',
             'The Divergent Series[:]? Insurgent', 'Kingsman[:]? The Secret Service', 'Spy', 'Trainwreck',
             'Tomorrowland', 'Get Hard', 'Terminator[:]? Genisys', 'Ted 2', 'Pixels', 'Maze Runner[:]? The Scorch Trials',
             'Paul Blart[:]? Mall Cop 2', 'War Room', 'Magic Mike XXL', 'The Intern', 'The Visit', 'Black Mass',
             'Vacation', 'The Perfect Guy', 'Fantastic Four', 'Focus', 'Southpaw', 'Insidious Chapter 3',
             'Poltergeist', 'Jupiter Ascending', 'Goosebumps', 'The Man From U.N.C.L.E.',
             'McFarland, USA', 'The Gift', 'Max', 'The Age of Adaline', 'Everest', 'Sicario']
}
captureGroup = {}

movieRegEx = {}


def _numbertoword(number):
    word = ""
    length = int(number/25)
    for i in range(0, length):
        word += chr(i + ord('a'))
    word += chr(number % 25 + ord('a'))
    return word



for _year in movies:
    movieRegEx[_year] = []
    captureGroup[_year] = {}
    id = 0
    for movie in movies[_year]:
        # movie = ' ' + re.escape(movie)
        # name capture group to reference the matched movie later
        moviename = re.sub("\[|\]|\?", "", movie)
        capturename = _numbertoword(id)
        movie = "(?P<" + capturename + ">(?<!\w)" + movie + "(?!\w))"
        captureGroup[_year][capturename] = moviename
        movieRegEx[_year].append(movie)
        id += 1
    movieRegEx[_year] = re.compile("|".join(movieRegEx[_year]), re.I)


def filter_row(row, year):
    if not subreddits.findall(row["subreddit"]):
        return None
    mre = movieRegEx[year]
    if mre is None:
        print("ERROR - No Movie Titles for year " + str(year))
        return None
    matches = mre.search(row["body"])
    if not matches:
        return None

    groups = list(k for k, v in matches.groupdict().items() if v is not None)
    matchedmovies = list(map(lambda g: captureGroup[year][g], groups))
    new_row = {"movies": matchedmovies, "author": row["author"], "id": row["id"], "body": row["body"],
               "subreddit": row["subreddit"], "created_utc": row["created_utc"], "score": row["score"]}
    return new_row

