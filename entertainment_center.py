import fresh_tomatoes
import media


kill_bill = media.Movie("Kill Bill",
						"A former assassin, known simply as The Bride (Uma Thurman), wakes from a coma four years after her jealous ex-lover Bill (David Carradine) attempts to murder her on her wedding day.",
						"https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
						"https://www.youtube.com/watch?v=7kSuas6mRpk",
						"https://itunes.apple.com/us/movie/kill-bill-vol.-1/id432516627",
						"http://www.rottentomatoes.com/m/kill_bill_vol_1/",
						"000001")


the_departed = media.Movie("The Departed",
							"South Boston cop Billy Costigan (Leonardo DiCaprio) goes under cover to infiltrate the organization of gangland chief Frank Costello (Jack Nicholson). As Billy gains the mobster's trust, a career criminal named Colin Sullivan (Matt Damon) infiltrates the police department and reports on its activities to his syndicate bosses. When both organizations learn they have a mole in their midst, Billy and Colin must figure out each other's identities to save their own lives.",
							"https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
							"https://www.youtube.com/watch?v=auYbpnEwBBg",
							"https://itunes.apple.com/us/movie/the-departed/id284563157",
							"http://www.rottentomatoes.com/m/departed/",
							"000002")


inception = media.Movie("Inception",
						"Dom Cobb (Leonardo DiCaprio) is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someone's mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobb's every move.",
						"https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
						"https://www.youtube.com/watch?v=8hP9D6kZseM",
						"https://itunes.apple.com/us/movie/inception/id400763833",
						"http://www.rottentomatoes.com/m/inception/",
						"000003")


the_party = media.Movie("The Party",
						"While trying to tie his shoe, bumbling extra Hrundi V. Bakshi (Peter Sellers) unwittingly triggers explosives that destroy the set of an epic war film. The furious director tells executive Fred Clutterbuck (J. Edward McKinley) to fire him. Because of a misunderstanding, Bakshi instead mistakenly receives an invitation to an exclusive party at Clutterbuck's Hollywood mansion, where he proceeds to wreak havoc on partygoers as he stumbles through what will become the wildest night he's ever seen.",
						"https://upload.wikimedia.org/wikipedia/en/4/4f/Party_moviep.jpg",
						"https://www.youtube.com/watch?v=SU9s8L7Sewg",
						"https://itunes.apple.com/us/movie/the-party/id834720314",
						"https://www.rottentomatoes.com",
						"000004")


the_grand_budapest_hotel = media.Movie("The Grand Budapest Hotel",
										"In the 1930s, the Grand Budapest Hotel is a popular European ski resort, presided over by concierge Gustave H. (Ralph Fiennes). Zero, a junior lobby boy, becomes Gustave's friend and protege. Gustave prides himself on providing first-class service to the hotel's guests, including satisfying the sexual needs of the many elderly women who stay there. When one of Gustave's lovers dies mysteriously, Gustave finds himself the recipient of a priceless painting and the chief suspect in her murder.",
										"https://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg",
										"https://www.youtube.com/watch?v=1Fg5iWmQjwk",
										"https://itunes.apple.com/us/movie/the-grand-budapest-hotel/id828777452",
										"http://www.rottentomatoes.com/m/the_grand_budapest_hotel/",
										"000005")


in_bruges = media.Movie("In Bruges",
						"After a particularly difficult job, hit men Ray (Colin Farrell) and Ken (Brendan Gleeson) head to Belgium to hide out until things cool down. Ray hates the medieval city they land in, but Ken finds its beauty and peacefulness enchanting. Their experiences become increasingly surreal and possibly life-changing as they encounter tourists, locals, an American dwarf and a potential romance for Ray.",
						"http://www.joblo.com/posters/images/full/2008-in_bruges-1.jpg",
						"https://www.youtube.com/watch?v=p-gG2qo_l_A",
						"https://itunes.apple.com/us/movie/in-bruges/id281077778",
						"http://www.rottentomatoes.com/m/in_bruges/",
						"000006")


movies = [kill_bill, the_departed, inception, the_party, the_grand_budapest_hotel, in_bruges]

fresh_tomatoes.open_movies_page(movies)

#print (media.Movie.VALID_RATINGS)
print (media.Movie.__doc__)
