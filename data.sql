DROP TABLE IF EXISTS tblFilms;

CREATE TABLE tblFilms (
    filmID INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    ReleaseYear INTEGER NOT NULL,
    rating TEXT NOT NULL,
    duration INTEGER NOT NULL,
    genre TEXT NOT NULL,
    trailer TEXT NOT NULL,
    description TEXT NOT NULL
);

insert into tblFilms (title, ReleaseYear, rating, duration, genre, trailer, description) values ('Superbad', 2007, 'R', 113, 'Comedy', '4eaZ_48ZYog', 'Two co-dependent high school seniors are forced to deal with separation anxiety after their plan to stage a booze-soaked party goes awry.');
insert into tblFilms (title, ReleaseYear, rating, duration, genre, trailer, description) values ('The Muppets', 2011, 'U', 120, 'Comedy','C4YhbpuGdwQ', 'A Muppet fanatic with some help from his 2 human compatriots must regroup the Muppet gang to stop an avaricious oil mogul from taking down one of their precious life-longing treasures.');
insert into tblFilms (title, ReleaseYear, rating, duration, genre, trailer, description) values ('The Legend of Tarzan', 2016, 'PG', 110, 'Adventure', 'Aj7ty6sViiU', 'Tarzan, having acclimated to life in London, is called back to his former home in the jungle to investigate the activities at a mining encampment.');
insert into tblFilms (title, ReleaseYear, rating, duration, genre, trailer, description) values ('Jason Bourne', 2016, 'G', 125, 'Action', '7uLVIUuEfFY', 'The CIAs most dangerous former operative is drawn out of hiding to uncover more explosive truths about his past.');
insert into tblFilms (title, ReleaseYear, rating, duration, genre, trailer, description) values ('The Nice Guys', 2016, 'R', 116, 'Action', 'GQR5zsLHbYw', 'In 1970s Los Angeles, a mismatched pair of private eyes investigate a missing girl and the mysterious death of a porn star.');
insert into tblFilms (title, ReleaseYear, rating, duration, genre, trailer, description) values ('The Secret Life of Pets', 2016, 'U', 86, 'Adventure', 'i-80SGWfEjM', 'The quiet life of a terrier named Max is upended when his owner takes in Duke, a stray whom Max instantly dislikes.');
insert into tblFilms (title, ReleaseYear, rating, duration, genre, trailer, description) values ('The Lion King', 2019, 'PG', 118, 'Adventure', '4CbLXeGSDxg', 'After the murder of his father, a young lion prince flees his kingdom only to learn the true meaning of responsibility and bravery.');
insert into tblFilms (title, ReleaseYear, rating, duration, genre, trailer, description) values ('The Dark Knight', 2008, 'G', 152, 'Action', 'EXeTwQWrcwY', 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.' );
insert into tblFilms (title, ReleaseYear, rating, duration, genre, trailer, description) values ('Finding Nemo', 2003, 'U', 100, 'Comedy', '9oQ628Seb9w', 'After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.');
insert into tblFilms (title, ReleaseYear, rating, duration, genre, trailer, description) values ('Zootopia', 2016, 'PG', 108, 'Adventure', 'jWM0ct-OLsM', 'In a city of anthropomorphic animals, a rookie bunny cop and a cynical con artist fox must work together to uncover a conspiracy.');

