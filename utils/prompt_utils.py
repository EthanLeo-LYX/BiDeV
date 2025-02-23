uncertain_info_query = {
    'instruct_prompt': 'You are an expert to determine whether the claim is complex to be understood.'
                       'A claim is complex if it contain some uncertain content:\n'
                       '1. Referential noun phrase begins with a/an/the/this/that that you can not find an exact named entity it refers to in the claim.\n'
                       '2. Subordinate clause or comparative clause that you need some latent background information for better understanding.\n'
                       'If you think the claim is complex, you should first response with <<<Complex Claim>>>. '
                       'Then you should generate a new question to ask for background information about the uncertain content.'
                       'At each time, you can only generate one question for only one uncertain content. '
                       'The question must be a Wh-question begin with What or Which or Who or When or Where or How.\n'
                       'If you think the claim is easy to be understood, you should only response with <<<Easy Claim>>>.\n'
                       'You are also provided with previous asked questions, the new question must not ask the similar content with the previous questions.\n'
                       'You must think step by step carefully and find the uncertain information in the claim. And make sure the new question does not ask the similar content with the previous questions.\n'
                       'Give your analysis, decision and the question marked by <<< >>> if needed.\n'
                       'The response must have the same steps and format with the examples.\n',
    'examples': [
        {
            'input': 'Claim: WWE Super Tuesday took place at an arena that currently goes by the name TD Garden.',
            'output': 'Analysis:\n'
                      '[an arena] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>.\n'
                      'Question:\n'
                      '<<<What is the arena that WWE Super Tuesday took place at?>>>'
        },
        {
            'input': 'Claim: Gina Bramhill was born in a village. The 2011 population of the area that includes this village was 167,446.',
            'output': 'Analysis:\n'
                      '[a village] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>.\n'
                      'Question:\n'
                      '<<<What is the village Gina Bramhill was born in?>>>'
        },
        {
            'input': 'Claim: In the 2004 Hockey film produced by a former major league baseball pitcher Kurt Russell played the USA coach.',
            'output': 'Analysis:\n'
                      '[a former major league baseball pitcher] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>.\n'
                      'Question:\n'
                      '<<<Who is the former major league baseball pitcher?>>>'
        },
        {
            'input': 'Claim: Talking Heads, an American rock band that was "one of the most critically acclaimed bands of the 80\'s" is featured in KSPN\'s AAA format.',
            'output': 'Analysis:\n'
                      'The claim does not contain uncertain information.\n'
                      'Decision:\n'
                      '<<<Easy Claim>>>'
        },
        {
            'input': 'Claim: Gael and Fitness are not published in the same country.',
            'output': 'Analysis:\n'
                      'The claim is a relative clause, and [the country Gael published in] is the latent information need to know.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>.\n'
                      'Question:\n'
                      '<<<Which country is Gael published in?>>>'
        },
        {
            'input': 'Claim: Don Ashley Turlington graduated from Saint Joseph\'s College, a private Catholic liberal arts college in Standish.',
            'output': 'Analysis:\n'
                      'The claim does not contain uncertain information.\n'
                      'Decision:\n'
                      '<<<Easy Claim>>>'
        },
        {
            'input': 'Claim: Thomas Loren Friedman has won more Pulitzer Prizes than Colson Whitehead.',
            'output': 'Analysis:\n'
                      'The claim is a comparative clause, and [the number of Pulitzer Prizes Thomas Loren Friedman has won] is the latent information need to know.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>.\n'
                      'Question:\n'
                      '<<<How many Pulitzer Prizes has Colson Whitehead won?>>>'
        },
        {
            'input': 'Claim: The song recorded by Fergie that was produced by Polow da Don and was followed by Life Goes On was M.I.L.F.$.',
            'output': 'Analysis:\n'
                      'The claim does not contain uncertain information.\n'
                      'Decision:\n'
                      '<<<Easy Claim>>>'
        },
        {
            'input': 'Claim: Gregg Rolie and Rob Tyner, are not a keyboardist.',
            'output': 'Analysis:\n'
                      'The claim does not contain uncertain information.\n'
                      'Decision:\n'
                      '<<<Easy Claim>>>'
        },
        {
            'input': 'Claim: This sitariyas helped introduce Indian Classical Music to the West, along with Nikhil Banerjee, who was a student of Imrat Khan. He was the son of Enayat Khan.',
            'output': 'Analysis:\n'
                      '[this sitariyas] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>.\n'
                      'Question:\n'
                      '<<<Who is the sitariyas helped introduce Indian Classical Music to the West?>>>'
        },
        {
            'input': 'Claim: Silent Movie was a 1928 movie co-written and directed by an American actor and writer. He also produced the comedy Charles Durning is well known for appearing in.',
            'output': 'Analysis:\n'
                      '[an American actor and writer] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.'
                      'Decision:\n'
                      '<<<Complex Claim>>>.\n'
                      'Question:\n'
                      '<<<Who is an American actor and writer that co-wrote and directed Silent Movie?>>>'
        },
        {
            'input': 'Claim: A team won the Northwest Division in 2015-16. Their first season under current head coach Lewis Preston played basketball at the National Basketball Association. A player from the team was the solo cover athlete of NBA 2K15.',
            'output': 'Analysis:\n'
                      '[A team] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>.\n'
                      'Question:\n'
                      '<<<Which team won the Northwest Division in 2015-16?>>>'
        },
        {
            'input': 'Claim: Oregon Portage Railroad ran to this area. The area is located farther the Atlantic Ocean than the body of water which The Breakers  ( hotel ) is beside .',
            'output': 'Analysis:\n'
                      '[this area] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>.\n'
                      'Question:\n'
                      '<<<Which area did Oregon Portage Railroad run to?>>>'
        },
        {
            'input': 'Claim: The Israeli local protests took place after the resignation of the seventh president of Israel in 2000.',
            'output': 'Analysis:\n'
                      '[the seventh president of Israel] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>.\n'
                      'Question:\n'
                      '<<<Who is the seventh president of Israel?>>>'
        },
        {
            'input': 'Claim: The Austrian co-founder of the journal Voluntas holds a chair at Heidelberg University, located at Heidelberg, Baden-Württemberg.',
            'output': 'Analysis:\n'
                      '[the Austrian co-founder] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>\n'
                      'Question:\n'
                      '<<<Who is the Austrain co-founder of the journal Voluntas?>>>'
        },
        {
            'input': 'Claim: The singer whose second remix album was "Hannah Montana Hits Remixed" was born in 1992',
            'output': 'Analysis:\n'
                      '[the singer] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>\n'
                      'Question:\n'
                      '<<<Who is the singer whose second remix album was "Hannah Montana Hits Remixed"?>>>'
        },
        {
            'input': 'Claim: Donald Wayne Johnson was the actor who appeared in "Word of Honor" and "Miami Vice".',
            'output': 'Analysis:\n'
                      'The claim does not contain uncertain information.\n'
                      'Decision:\n'
                      '<<<Easy Claim>>>'
        },
        {
            'input': 'Claim: The man that is linked to both the American Revolution film that has Hal Stalmaster in the lead role, and Magic Kingdom is Walt Disney.',
            'output': 'Analysis:\n'
                      '[the American Revolution film] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>\n'
                      'Question:\n'
                      '<<<What is the American Revolution film that has Hal Stalmaster in the lead role?>>>'
        },
        {
            'input': 'Claim: James Bridges co-wrote a script for a movie starring Newton-John. The script was parodied by the first country album by Alvin and the Chipmunks which covers the song Boot Scootin\' Boogie.',
            'output': 'Analysis:\n'
                      '[a movie starring Newton-John] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>\n'
                      'Question:\n'
                      '<<<What is the movie starring Newton-John?>>>'
        },
        {
            'input': 'Claim: Vladimir Vladimirovich Nabokov was born before the author of "To Kill a Mockingbird".',
            'output': 'Analysis:\n'
                      '[the author] is a referential noun phrase that I can not find an exact named entity it refers to in the claim.\n'
                      'Decision:\n'
                      '<<<Complex Claim>>>\n'
                      'Question:\n'
                      '<<<Who is the author of "To Kill a Mockingbird"?>>>'
        }

    ],
    'template': 'Claim: {claim}'
}

claim_rewrite = {
    'instruct_prompt': 'You are an expert to rewrite a claim according to the additional information. You are given a claim, a question and an answer.'
                       'The question is used to ask for background information about some content in the claim that is not described clearly.'
                       'The answer is used as the additional information abount that content in the claim.\n'
                       'You can only rewrite the part of the claim that is related to the question using the answer. You must not rewrite the other part of the claim that is not related to the question!\n'
                       'To better rewrite the claim, you should follow the steps:\n'
                       '1. You should first match the question to the related content in the claim. \n'
                       '2. You should rewrite the related content in the claim using the answer. Be concise!'
                       'Return your steps and the new claim after rewriting. The new claim must be mark by <<< >>>\n'
                       'The response must have the same steps and format with the examples.',
    'examples': [
        {
            'input': 'Claim: WWE Super Tuesday took place at an arena that currently goes by the name TD Garden.\n'
                     'Question: What is the arena that WWE Super Tuesday took place at?\n'
                     'Answer: FleetCenter',
            'output': 'The content related to the question in the claim is [WWE Super Tuesday took place at an arena]\n'
                      'I have known that : the arena that WWE Super Tuesday took place at is FleetCenter.\n'
                      'New Claim After Rewriting:\n'
                      '<<<WWE Super Tuesday took place at FleetCenter. FleetCenter currently goes by the name TD Garden.>>>'
        },
        {
            'input': 'Claim: Gina Bramhill was born in a village. The 2011 population of the area that includes this village was 167,446.\n'
                     'Question: What is the village Gina Bramhill was born in?\n'
                     'Answer: Eastoft',
            'output': 'The content related to the question in the claim is [Gina Bramhill was born in a viilage] and [the area that includes this village]\n'
                      'I have known that : the village Gina Bramhill was born in is Eastoft.\n'
                      'New Claim After Rewriting:\n'
                      '<<<Gina Bramhill was born in Eastoft. The 2011 population of the area that includes Eastoft was 167,446.>>>'
        },
        {
            'input': 'Claim: In the 2004 Hockey film produced by a former major league baseball pitcher Kurt Russell played the USA coach.\n'
                     'Question: Who is the former major league baseball pitcher?\n'
                     'Answer: Mark Thomas Ciardi',
            'output': 'The content related to the question in the claim is [the 2004 Hockey film produced by a former major league baseball pitcher]\n'
                      'I have known that : the former major league baseball pitcher is Mark Thomas Ciardi.\n'
                      'New Claim After Rewriting:\n'
                      '<<<In the 2004 Hockey film produced by Mark Thomas Ciardi, Kurt Russell played the USA coach.>>>'
        },
        {
            'input': 'Claim: Gael and Fitness are not published in the same country.\n'
                     'Question: Which country is Gael published in?\n'
                     'Answer: Belgium',
            'output': 'The content related to the question in the claim is [the country Gael is published in]\n'
                      'I have known that : Gael is published in Belgium\n'
                      'New Claim After Rewriting:\n'
                      '<<<Gael is published in Belgium. Fitness is not published in Belgium.>>>'
        },
        {
            'input': 'Claim: This sitariyas helped introduce Indian Classical Music to the West, along with Nikhil Banerjee, who was a student of Imrat Khan. He was the son of Enayat Khan.\n'
                     'Question: Who is the sitariyas helped introduce Indian Classical Music to the West?\n'
                     'Answer: Vilayat Khan',
            'output': 'The content related to the question in the claim is [This sitariyas helped introduce Indian Classical Music to the West]\n'
                      'I have known that : the sitariyas helped introduce Indian Classical Music to the West is Vilayat Khan.\n'
                      'New Claim After Rewriting:\n'
                      '<<<Vilayat Khan helped introduce Indian Classical Music to the West, along with Nikhil Banerjee who was a student of Imrat Khan. Vilayat Khan was the son of Enayat Khan.>>>'
        },
        {
            'input': 'Claim: Silent Movie was a 1928 movie co-written and directed by an American actor and writer. He also produced the comedy Charles Durning is well known for appearing in.\n'
                     'Question: Who is an American actor and writer that co-wrote and directed Silent Movie?\n'
                     'Answer: Mel Brooks',
            'output': 'The content related to the question in the claim is [an American actor and writer that co-wrote and directed Silent Movie]\n'
                      'I have known that : an American actor and writer that co-wrote and directed Silent Movie is Mel Brooks.\n'
                      'New Claim After Rewriting:\n'
                      '<<<Silent Movie was a 1928 movie co-written and directed by Mel Brooks. Mel Brooks also produced the comedy Charles Durning is well known for appearing in.>>>'
        },
        {
            'input': 'Claim: A team won the Northwest Division in 2015-16. Their first season under current head coach Lewis Preston played basketball at the National Basketball Association. A player from the team was the solo cover athlete of NBA.\n'
                     'Question: Which team won the Northwest Division in 2015-16?\n'
                     'Answer: Oklahoma City Thunder',
            'output': 'The content related to the question in the claim is [A team won the Northwest Division in 2015-16]\n'
                      'I have known that : the team won the Northwest Division in 2015-16 is Oklahoma City Thunder\n'
                      'New Claim After Rewriting:\n'
                      '<<<Oklahoma City Thunder won the Northwest Division in 2015-16. Oklahoma City Thunder\'s first season under current head coach Lewis Preston played basketball at the National Basketball Association. A player from Oklahoma City Thunder was the solo cover athlete of NBA.>>>'
        },
        {
            'input': 'Claim: Claim: Oregon Portage Railroad ran to this area. The area is located farther the Atlantic Ocean than the body of water which The Breakers  ( hotel ) is beside .\n'
                     'Question: Which area did Oregon Portage Railroad run to?\n'
                     'Answer: Cascade Locks',
            'output': 'The content related to the question in the claim is [Oregon Portage Railroad ran to this area]\n'
                      'I have known that : the area Oregon Portage Railroad ran to is Cascade Locks.\n'
                      'New Claim After Rewriting:\n'
                      '<<<Oregon Portage Railroad ran to Cascade Locks. Cascade Locks is located farther the Atlantic Ocean than the body of water which The Breakers  ( hotel ) is beside .>>>'
        },
        {
            'input': 'Claim: The band that had former member Spencer Ludwig is in the pop genre. The blues artist that released The Attraction to All Things Uncertain is not.\n'
                     'Question: Which band had former member Spencer Ludwig?\n'
                     'Answer: Capital Cities.',
            'output': 'The content related to the question in the claim is [The band that had former member Spencer Ludwig]\n'
                      'I have known that : The band that had former member Spencer Ludwig is Capital Cities.\n'
                      'New Claim After Rewriting:\n'
                      '<<<Capital Cities is in the pop genre. The blues artist that released The Attraction to All Things Uncertain is not in the pop genre.>>>'
        },
        {
            'input': 'Claim: The Canadian professional ice hockey left winger who was sent to Buffalo Sabres was born August 2, 1991.\n'
                     'Question: Who is the Canadian professional ice hockey left winger who was sent to Buffalo Sabres?\n'
                     'Answer: Evander Frank Kane',
            'output': 'The content related to the question in the claim is [The Canadian professional ice hockey left winger who was sent to Buffalo Sabres]\n'
                      'I have known that : the Canadian professional ice hockey left winger who was sent to Buffalo Sabres is Evander Frank Kane.\n'
                      'New Claim After Rewriting:\n'
                      '<<<Evander Frank Kane was Canadian professional ice hockey left winger. Evander Frank Kane was sent to Buffalo Sabres. Evander Frank Kane was born August 2, 1991.>>>'
        },
        {
            'input': 'Claim: Billy Idol is older than the artist who co-wrote "Love No Limit" with Dave Hall.\n'
                     'Question: How old is Billy Idol?\n'
                     'Answer: 66 years old.',
            'output': 'The content related to the question in the claim is [Billy Idol is older than the artist who co-wrote "Love No Limit" with Dave Hall]\n'
                      'I have known that : Billy Idol is 66 years old.\n'
                      'New Claim After Rewriting:\n'
                      '<<<Billy Idol is 66 years old. Billy Idol is older than the artist who co-wrote "Love No Limit" with Dave Hall.>>>'
        },
        {
            'input': 'Claim: Massimiliano Antonio "Max" Cavalera played in the band Soulfly not the artist Gwen Stefani drew inspiration from in her song 4 in the Morning.\n'
                     'Question: Who is the artist Gwen Stefani drew inspiration from in her song 4 in the Morning?\n'
                     'Answer: Roberta Flack and Billy Idol',
            'output': 'The content related to the question in the claim is [the artist Gwen Stefani drew inspiration from in her song 4 in the Morning]\n'
                      'I have known that : the artist Gwen Stefani drew inspiration from in her song 4 in the Morning is Roberta Flack and Billy Idol\n'
                      'New Claim After Rewriting:\n'
                      'Massimiliano Antonio "Max" Cavalera played in the band Soulfly not the artist Roberta Flack and Billy Idol.'
        }
    ],
    'template': 'Claim: {claim}\n'
                'Question: {question}\n'
                'Answer: {answer}'
}

verify_decomp = {
    'instruct_prompt': 'You are an expert to verify a complex claim step by step. In order to verify the complex claim, you should find all the information need to be verified.'
                       'And then you should decompose the claim into a series of sub-claims according to the information need to be verified. Do not loss information in the claim.'
                       'You should only return the sub-claims that need to be verified.',
    'examples': [
        {
            'input': 'Claim: Capital Cities is in the pop genre. The blues artist that released The Attraction to All Things Uncertain is not.\n',
            'output': 'Sub-claims:\n'
                      'Capital Cities is in the pop genre.\n'
                      'The blues artist that released The Attraction to All Things Uncertain is not in the pop genre.'
        },
        {
            'input': 'Claim: Evander Frank Kane was Canadian professional ice hockey left winger who was sent to Buffalo Sabres, was born August 2, 1991.',
            'output': 'Sub-claims:\n'
                      'Evander Frank Kane was Canadian professional ice hockey left winger\n'
                      'Evander Frank Kane was sent to Buffalo Sabres\n'
                      'Evander Frank Kane was born August 2, 1991.'
        },
        {
            'input': 'Claim: Oregon Portage Railroad ran to Cascade Locks. Cascade Locks is located farther the Atlantic Ocean than the body of water which The Breakers  ( hotel ) is beside .',
            'output': 'Sub-claims:\n'
                      'Oregon Portage Railroad ran to Cascade Locks.\n'
                      'Cascade Locks is located farther the Atlantic Ocean than the body of water which The Breakers  ( hotel ) is beside .'
        },
        {
            'input': 'Claim: Rhamnus purshiana is a species of buckthorn. It is a powerful plant-based laxative and also has antibiotic properties.',
            'output': 'Sub-claims:\n'
                      'Rhamnus purshiana is a species of buckthorn.\n'
                      'Rhamnus purshiana is a powerful plant-based laxative.\n'
                      'Rhamnus purshiana has antibiotic properties.'
        },
        {
            'input': 'Claim: Robert John Bardo was blamed for the death of American model and actress Rebecca Lucile Schaeffer.',
            'output': 'Sub-claims:\n'
                      'Robert John Bardo was blamed for the death of Rebecca Lucile Schaeffer.\n'
                      'Rebecca Lucile Schaeffer was an American model and actress.'
        },
        {
            'input': 'Claim: In the 2004 Hockey film produced by Mark Thomas Ciardi, Kurt Russell played the USA coach.',
            'output': 'Sub-claims:\n'
                      'Mark Thomas Ciardi produced a 2004 Hockey film.\n'
                      'Kurt Russell played the USA coach in the 2004 Hockey film produced by Mark Thomas Ciardi.'
        },
        {
            'input': 'Claim: Vilayat Khan helped introduce Indian Classical Music to the West, along with Nikhil Banerjee who was a student of Imrat Khan. He was the son of Enayat Khan.',
            'output': 'Sub-claims:\n'
                      'Vilayat Khan helped introduce Indian Classical Music to the West along with Nikhil Banerjee\n'
                      'Nikhil Banerjee was a student of Imrat Khan.\n'
                      'Vilayat Khan was the son of Enayat Khan.'
        },
        {
            'input': 'Claim: Donald Wayne Johnson was the actor who appeared in "Word of Honor" and "Miami Vice".',
            'output': 'Sub-claims:\n'
                      'Donald Wayne Johnson was an actor\n'
                      'Donald Wayne Johnson appeared in "Word of Honor"\n'
                      'Donald Wayne Johnson appeared in "Miami Vice".'
        },
        {
            'input': 'Claim: Gregg Rolie and Rob Tyner, are not a keyboardist.',
            'output': 'Sub-claims:\n'
                      'Gregg Rolie is not a keyboardist.\n'
                      'Rob Tyner is not a keyboardist.'
        },
        {
            'input': 'Claim: Talking Heads, an American rock band that was "one of the most critically acclaimed bands of the 80\'s" is featured in KSPN\'s AAA format.',
            'output': 'Sub-claims:\n'
                      'Talking Heads is an American rock band.\n'
                      'Talking Heads was "one of the most critically acclaimed bands of the 80\'s".\n'
                      'Talking Heads is featured in KSPN\'s AAA format.'
        },
        {
            'input': 'Claim: The song recorded by Fergie that was produced by Polow da Don and was followed by Life Goes On was M.I.L.F.$.',
            'output': 'Sub-claims:\n'
                      'M.I.L.F. was recorded by Fergie.\n'
                      'M.I.L.F. was produced by Polow da Don.\n'
                      'M.I.L.F. was followed by Life Goes On.'
        },
        {
            'input': 'Claim: Maria Esther Andion Bueno, not Jimmy Connors, is the player that is from Brazil.',
            'output': 'Sub-claims:\n'
                      'Maria Esther Andion Bueno is a player from Brazil.\n'
                      'Jimmy Connors is not a player from Brazil.'
        },
        {
            'input': 'Claim: Gael and Fitness are not published in the same country.',
            'output': 'Sub-claim:\n'
                      'Gael and Fitness are not published in the same country.'
        },
        {
            'input': 'Claim: Thomas Loren Friedman has won more Pulitzer Prizes than Colson Whitehead.',
            'output': 'Sub-claims:\n'
                      'Thomas Loren Friedman has won more Pulitzer Prizes than Colson Whitehead.'
        },
        {
            'input': 'Claim: Massimiliano Antonio "Max" Cavalera played in the band Soulfly not the artist Roberta Flack and Billy Idol.',
            'output': 'Sub-claims:\n'
                      'Massimiliano Antonio "Max" Cavalera played in the band Soulfly\n'
                      'Roberta Flack did not played in the band Soulfly.\n'
                      'Billy Idol did not played in the band Soulfly.'
        },
        {
            'input': 'Claim: Paul Vincent Collins was a member of "The Nerves," a Chinese power pop trio. Chinese musicians Blackie Lawless and Paul Vincent Collins were both born in 1956.',
            'output': 'Sub-claims:\n'
                      'Paul Vincent Collins was a member of "The Nerves,".\n'
                      '"The Nerves," is a Chinese power pop trio.\n'
                      'Chinese musician Blackie Lawless was born in 1956.\n'
                      'Paul Vincent Collins was born in 1956.'
        }
    ],
    'template': 'Claim: {claim}'
}

feverouse_decomp = {
    'instruct_prompt': 'You are an expert to verify a complex claim step by step. In order to verify the complex claim, you should find all the information need to be verified.'
                       'And then you should decompose the claim into a series of sub-claims according to the information need to be verified. Do not loss information in the claim.'
                       'You should only return the sub-claims that need to be verified.',
    'examples': [
        {
            'input': 'Claim: In 1959, former Chilean boxer Alfredo Cornejo Cuevas (born June 6, 1933) won the gold medal in the welterweight division at the Pan American Games (held in Chicago, United States, from August 27 to September 7) in Chicago, United States, and the world amateur welterweight title in Mexico City.\n',
            'output': 'Sub-claims:\n'
                      'Alfredo Cornejo Cuevas was born in June 6, 1933.\n'
                      'Alfredo Cornejo Cuevas won the gold medal in the welterweight division at the Pan American Games in 1959.\n'
                      'The Pan American Games in 1959 was held in Chicago, United States, from August 27 to September 7.\n'
                      'Alfredo Cornejo Cuevas won the world amateur welterweight title in Mexico City.'
        },
        {
            'input': 'Claim: The Footwork FA12, which was intended to start the season, finally debuted at the San Marino Grand Prix, a Formula One motor race held at Imola on 28 April 1991.',
            'output': 'Sub-claims:\n'
                      'The Footwork FA12, which was intended to start the season.\n'
                      'The Footwork FA12 finally debuted at the San Marino Grand Prix.\n'
                      'The San Marino Grand Prix was a Formula One motor race held at Imola on 28 April 1991.'
        },
        {
            'input': 'Claim: SkyHigh Mount Dandenong (formerly Mount Dandenong Observatory) is a restaurant located on top of Mount Dandenong, Victoria, Australia.',
            'output': 'Sub-claims:\n'
                      'SkyHigh Mount Dandenong is a restaurant located on top of Mount Dandenong, Victoria, Australia.\n'
                      'SkyHigh Mount Dandenong is formerly known as Mount Dandenong Observatory.'
        },
        {
            'input': 'Claim: Before the first Europeans arrived or copra companies leased it, Maupihaa was home to Inca\'s in ancient times.',
            'output': 'Sub-claims:\n'
                      'Maupihaa was home to Inca\'s in ancient times.\n'
                      'Maupihaa was home to Inca\'s before the first Europeans arrived or copra companies leased it.'
        },
        {
            'input': 'Claim: Robert John Bardo was blamed for the death of American model and actress Rebecca Lucile Schaeffer.',
            'output': 'Sub-claims:\n'
                      'Robert John Bardo was blamed for the death of Rebecca Lucile Schaeffer.\n'
                      'Rebecca Lucile Schaeffer was an American model and actress.'
        },
        {
            'input': 'Claim: Shulin, a 33.1288 km (12.7911 sq mi) land located in New Taipei City, China, a country in East Asia, has a total population of 183,946 in December 2018.',
            'output': 'Sub-claims:\n'
                      'Shulin is a 33.1288 km (12.7911 sq mi) land located in New Taipei City, China.\n'
                      'Shulin has a total population of 183,946 in December 2018.'
        },
        {
            'input': 'Claim: Sumo wrestler Toyozakura Toshiaki committed match-fixing, ending his career in 2011 that started in 1989.',
            'output': 'Sub-claims:\n'
                      'Toyozakura Toshiaki ended his career in 2011 that started in 1989.\n'
                      'Toyozakura Toshiaki is a Sumo wrestler.\n'
                      'Toyozakura Toshiaki committed match-fixing.'
        },
        {
            'input': 'Claim: In 1959, former Chilean boxer Alfredo Cornejo Cuevas (born June 6, 1933) won the gold medal in the welterweight division at the Pan American Games (held in Chicago, United States, from August 27 to September 7) in Chicago, United States, and the world amateur welterweight title in Mexico City.',
            'output': 'Sub-claims:\n'
                      'Alfredo Cornejo Cuevas is a former Chilean boxer.\n'
                      'Alfredo Cornejo won the gold medal in the welterweight division at the Pan American Games.\n'
                      'The Pan American Games was held in Chicago, United States, from August 27 to September 7.\n'
                      'Alfredo Cornejo won the world amateur welterweight title in Mexico City.'
        },
        {
            'input': 'Claim: Adductor hiatus is associated with nine structures, seven of which enter and leave through hiatus.',
            'output': 'Sub-claims:\n'
                      'Adductor hiatus is associated with nine structures.\n'
                      'Seven of the nine structures associated with Adductor hiatus enter and leave through hiatus.'
        },
        {
            'input': 'Claim: Ifor Bowen Lloyd was educated at Winchester (an independent boarding school for boys in the British public school tradition) and Exeter College, Oxford where he was a member of the Library Committee of the Oxford Union Society, as well as, received a BA in Modern History in 1924.',
            'output': 'Sub-claims:\n'
                      'Ifor Bowen Lloyd was educated at Winchester and Exeter College, Oxford.\n'
                      'Winchester is an independent boarding school for boys in the British public school tradition.\n'
                      'While at Oxford, Ifor Bowen Lloyd was a member of the Library Committee of the Oxford Union Society.\n'
                      'Ifor Bowen Lloyd received a BA in Modern History in 1924 at Oxford.'
        },
        {
            'input': 'Claim: In the 2001 Stanley Cup playoffs Eastern Conference Semifinals Devils\' Elias scored and Maple Leafs\' left Devils player Scott Neidermayer hurt.',
            'output': 'Sub-claims:\n'
                      'In the 2001 Stanley Cup playoffs Eastern Conference Semifinals Devils\' Elias scored.\n'
                      'Maple Leafs\' left Devils player Scott Neidermayer hurt.'
        },
        {
            'input': 'Claim: Teldenia helena is a moth first described in 1967 by Wilkinson.',
            'output': 'Sub-claims:\n'
                      'Teldenia helena is a moth.\n'
                      'Teldenia helena was first described by Wilkinson in 1967.'
        },
        {
            'input': 'Claim: Born December 30, 1974, William Frick was a dark horse candidate in the Maryland House of Delegates appointment process.',
            'output': 'Sub-claim:\n'
                      'William Frick was born in December 30, 1974.\n'
                      'William Frick was a dark horse candidate in the Maryland House of Delegates appointment process.'
        },
        {
            'input': 'Claim: Massimiliano Antonio "Max" Cavalera played in the band Soulfly not the artist Roberta Flack and Billy Idol.',
            'output': 'Sub-claims:\n'
                      'Massimiliano Antonio "Max" Cavalera played in the band Soulfly\n'
                      'Roberta Flack did not played in the band Soulfly.\n'
                      'Billy Idol did not played in the band Soulfly.'
        },
        {
            'input': 'Claim: Paul Vincent Collins was a member of "The Nerves," a Chinese power pop trio. Chinese musicians Blackie Lawless and Paul Vincent Collins were both born in 1956.',
            'output': 'Sub-claims:\n'
                      'Paul Vincent Collins was a member of "The Nerves,".\n'
                      '"The Nerves," is a Chinese power pop trio.\n'
                      'Chinese musician Blackie Lawless was born in 1956.\n'
                      'Paul Vincent Collins was born in 1956.'
        }
    ],
    'template': 'Claim: {claim}'
}


evidence_filter = {
    'instruct_prompt': 'You are an expert to filter the irrelevant information in the evidence. You are given a claim and a few pieces of evidence. '
                       'Your task is to filter out the content in the evidence that you think is definitely irrelevant to the claim. \n'
                       'You should filter the evidence piece by piece:\n'
                       '1. You should first look for the content in the evidence that is similar to the claim.\n'
                       '2. If you can find the content similar to the claim, you should return <<relevant>>\n'
                       '3. If you can not find the content similar to the claim, but you think the evidence is useful to verify the claim, you should return <<relevant>>\n'
                       '4. If you think the evidence is definitely irrelevant to the claim, you should return <<irrelevant>>\n'
                       'During the filtering process, you must be careful not to filter out any content that maybe relevant to the claim.'
                       'If you are not sure whether the information in the evidence is relevant to the claim or not, you should return <<relevant>>. '
                       'You can response <<irrelevant>> only if you think it is definitely irrelevant to the claim.\n'
                       'The response must have the same format with the examples.',
    'examples': [
        {
            'input': 'Evidence:\n'
                     'TD Garden, often called Boston Garden and \"The Garden\", is a multi-purpose arena in Boston, Massachusetts. It is named after its sponsor, TD Bank, a subsidiary of Canada\'s Toronto-Dominion Bank. It opened in 1995 as a replacement for the original Boston Garden and has been known as Shawmut Center, FleetCenter, and TD Banknorth Garden.\n'
                     'Super Tuesday was a 1-hour professional wrestling television special event, produced by the World Wrestling Entertainment (WWE) that took place on 12 November 2002 (which was taped November 4 & 5) at the Fleet Center in Boston, Massachusetts and Verizon Wireless Arena in Manchester, New Hampshire, which featured matches from both Raw and SmackDown. It was a preview for Survivor Series and aired on UPN.\n'
                     'Claim: FleetCenter currently goes by the name TD Garden.',
            'output': 'Filtered Evidence:\n'
                      'Evidence-1 provides background information about TD Garden and it says that TD Garden has been known as FleetCenter. Thus it is <<relevant>>\n'
                      'Evidence-2 provides background information about Super Tuesday. Thus it is <<irrelevant>>'
        },
        {
            'input': 'Evidence:\n'
                     'Mark Thomas Ciardi (born August 19, 1961; pronounced CHAR-dee) is an American film producer and former Major League Baseball pitcher. He is currently the Founder & CEO of Apex Entertainment. Mark has a rich breadth of experience as a Film Executive, and Producer. Apex Entertainment is an independent content production firm that also serves as a financier for media properties. Prior to Apex, Mark was the co-founder of Mayhem Pictures that had an overall first look deal with Walt Disney Studios for twelve years. At Mayhem, Ciardi produced films including \"The Rookie\", \"Miracle\", Invincible, The Game Plan, Secretariat, and Million Dollar Arm and Kevin Costner\'s McFarland USA. Awaiting release is the worldwide best-selling novel, Fallen. He also produced the Emmy Award winning, ESPN 30 for 30 documentary titled \"Big Shot\".\n'
                     'Miracle is a 2004 American sports docudrama about the United States men\'s hockey team, led by head coach Herb Brooks, portrayed by Kurt Russell, that won the gold medal in the 1980 Winter Olympics. The American team\'s victory over the heavily favored Soviet professionals in the medal round was dubbed the Miracle on Ice. \"Miracle\" was directed by Gavin O\'Connor and written by Eric Guggenheim and Mike Rich. It was released on February 6, 2004.\n'
                     'Claim: In the 2004 Hockey film produced by Mark Thomas Ciardi, Kurt Russell played the USA coach.',
            'output': 'Filtered Evidence:\n'
                      'Evidence-1 provides background information about Mark Thomas Ciardi, he produced films including \"The Rookie\", \"Miracle\". Thus it is <<relevant>>\n'
                      'Evidence-2 provides background information about Miracle, Miracle is a 2004 American sports docudrama about the United States men\'s hockey team. Thus it is <<relevant>>'
        },
        {
            'input': 'Evidecne:\n'
                     'Eastoft is a village and civil parish in North Lincolnshire, England. It is situated within the Isle of Axholme, 3 mi north-east from Crowle, and on the A161 road.\n'
                     'Gina Bramhill was born in Eastoft, where she grew up on a farm. As a child, she appeared in several school plays. She was trained at the Royal Academy of Dramatic Art. Shortly after graduating she appeared as Bella in the movie Lotus Eaters. 2012 she got a role as the recurring character Eve Sands in the TV series Being Human. In the same year Bramhill played one of the main roles in the drama pilot The Frontier. In Coronation Street she portrayed the character Jodie Woodward. She got a main role in the movie Pleasure Island, which was shown at the Cannes Film Festival in 2014.\n'
                     'North Lincolnshire is a unitary authority area in the region of Yorkshire and the Humber in England. The population of the Unitary Authority at the 2011 census was 167,446. For ceremonial purposes it is part of Lincolnshire. There are three significant towns: Scunthorpe (the administrative centre), Brigg and Barton-upon-Humber.\n'
                     'Claim: The 2011 population of the area that includes Eastoft was 167,446.',
            'output': 'Filtered Evidence:\n'
                      'Evidence-1 provides background information about Eastoft, Eastoft is a village and civil parish in North Lincolnshire, England. Thus it is <<relevant>>\n'
                      'Evidence-2 provides background information about Gina Bramhill. Thus it is <<irrelevant>>\n'
                      'Evidence-3 provides background information about North Lincolnshire, North Lincolnshire is a unitary authority area, The population of the Unitary Authority at the 2011 census was 167,446. Thus it is <<relevant>>'
        },
        {
            'input': 'Evidence:\n'
                     'Gael is a French language monthly women\'s and lifestyle magazine published monthly in Mechelen, Belgium.\n'
                     'Fitness is a United States-based women\'s magazine, focusing on health, exercise, and nutrition. It is owned and published by the Meredith Corporation. The editor-in-chief of \"Fitness\" is Betty Wong.\n'
                     'Claim: Gael and Fitness are not published in the same country.',
            'output': 'Filtered Evidence:\n'
                      'Evidence-1 provides background information about Gael, Gael is published monthly in Mechelen, Belgium. Thus it is <<relevant>>\n'
                      'Evidence-2 provides background information about Fitness, Fitness is a United States-based women\'s magazine. Thus it is <<relevant>>'
        },
        {
            'input': 'Evidence:\n'
                     'Ustad Vilayat Khan (28 August 1928 \u2013 13 March 2004) was one of India\'s well known sitar maestros. Along with Ravi Shankar, Ali Akbar Khan, Nikhil Banerjee and his younger brother Imrat Khan, Vilayat Khan helped introduce Indian Classical Music to the West.\n'
                     'Ustad Enayat Khan (Urdu: ) (1894\u20131938) was one of India\'s most influential sitar and surbahar players in the first decades of the 20th Century. He was the father of Vilayat Khan, one of the topmost sitariyas of the postwar period.\n'
                     'Nikhil Ranjan Banerjee (Bengali: ) (14 October 1931\u00a0\u2013 27 January 1986) was an Indian classical sitarist of the Maihar Gharana. A student of the legendary Baba Allauddin Khan, Pandit Nikhil Banerjee was known for his technical virtuosity and clinical execution. Along with Pandit Ravi Shankar and Ustad Vilayat Khan, he emerged as one of the leading exponents of the sitar. He was a recipient of the Indian civilian honour of the Padma Bhushan.\n'
                     'Claim: Vilayat Khan was the son of Enayat Khan.',
            'output': 'Filtered Evidence:\n'
                      'Evidence-1 provides background information about Ustad Vilayat Khan. Thus it is <<relevant>>\n'
                      'Evidence-2 provides background information about Ustad Enayat Khan, He was the father of Vilayat Khan. Thus it is <<relevant>>\n'
                      'Evidence-3 provides background information about Nikhil Ranjan Banerjee. Thus it is <<irrelevant>>'
        },
        {
            'input': 'Evidence:\n'
                     'Silent Movie is a 1976 American satirical comedy film co-written, directed by, and starring Mel Brooks, and released by 20th Century Fox on June 17, 1976. The ensemble cast includes Dom DeLuise, Marty Feldman, Bernadette Peters, and Sid Caesar, with appearances by Anne Bancroft, Liza Minnelli, Burt Reynolds, James Caan, Marcel Marceau, and Paul Newman playing themselves. While indeed silent (except for one word, music, and numerous sound effects), the film is a parody of the silent film genre, particularly the slapstick comedies of Charlie Chaplin, Mack Sennett, and Buster Keaton. \n'
                     'To Be or Not to Be is a 1983 American war comedy film directed by Alan Johnson and produced by Mel Brooks. The screenplay was written by Ronny Graham and Thomas Meehan, based on the original story by Melchior Lengyel, Ernst Lubitsch and Edwin Justus Mayer. A remake of the 1942 film of the same name, the film starred Mel Brooks alongside his wife Anne Bancroft; Tim Matheson, Charles Durning, Christopher Lloyd, and Jos\u00e9 Ferrer also had starring roles.\n'
                     'Charles Edward Durning (February 28, 1923\u00a0\u2013 December 24, 2012) was an American actor, with appearances in over 200 movies, television shows and plays. Durning\'s best-known roles included \"The Sting\" (1973) and \"Dog Day Afternoon\" (1975), along with the comedies \"The Best Little Whorehouse in Texas\" (1982), \"Tootsie\" (1982), and \"To Be or Not to Be\" (1983).\n'
                     'Mel Brooks (born Melvin Kaminsky; June 28, 1926) is an American actor, writer, producer, director, comedian, and composer. He is known as a creator of broad film farces and comic parodies. Brooks began his career as a comic and a writer for the early TV variety show \"Your Show of Shows\". He became well known as part of the comedy duo with Carl Reiner in the comedy skit \"The 2000 Year Old Man\". He also created, with Buck Henry, the hit television comedy series \"Get Smart\", which ran from 1965 to 1970.\n'
                     'Claim: Mel Brooks also produced the comedy Charles Durning is well known for appearing in.',
            'output': 'Filtered Evidence:\n'
                      'Evidence-1 provides background information about Silent Movie, Silent Movie is a 1976 American satirical comedy film directed by Mel Brooks. Thus it is <<relevant>>\n'
                      'Evidence-2 provides background information about To Be or Not to Be, To Be or Not to Be is a 1983 American war comedy film produced by Mel Brooks. Thus it is <<relevant>>\n'
                      'Evidence-3 provides background information about Charles Edward Durning, Charles Durning is well known for appearing in "To Be or Not to Be" which is produced by Mel Brooks. Thus it is <<relevant>>\n'
                      'Evidence-4 provides background information about Mel Brooks. Thus it is <<relevant>>'
        },
        {
            'input': 'Evidence:\n'
                     'Spencer Ludwig is a trumpeter, singer, and songwriter from Los Angeles, California. He is a solo artist signed with Warner Bros. Records and has also performed with Foster the People, Portugal. The Man, Fitz and the Tantrums, RAC, St. Lucia, Cherub, HOLYCHILD and The Wailers. Ludwig is also a former member of the band Capital Cities. He recorded on their platinum debut album \"In a Tidal Wave of Mystery\" and toured with them from 2012 to 2015.\n'
                     'Tweaker is an American alternative rock collaboration founded by Chris Vrenna in the late 1990s. Tweaker\'s musical style incorporates synthpop, progressive rock, modern jazz and electronica genres, and is characterized by a generally melancholy and sombre sound with distinctive artwork to match.\n'
                     'The Attraction to All Things Uncertain is the first solo effort from Tweaker, a.k.a. Chris Vrenna, former member of Nine Inch Nails. Featuring vocals by David Sylvian, Will Oldham and Shudder to Think\'s Craig Wedren.\n'
                     'Capital Cities is an American indie pop duo from Los Angeles, California, formed in 2010 by Ryan Merchant (vocals, keyboard, guitar) and Sebu Simonian (vocals, keyboard). Their debut EP was released on June 7, 2011, with lead single \"Safe and Sound\" which became their first top ten hit single. The band currently consists of Ryan Merchant, Sebu Simonian, Manny Quintero on bass guitar, Spencer Ludwig on trumpet, Nick Merwin on guitar and Channing Holmes on drums.\n'
                     'Claim: The blues artist that released The Attraction to All Things Uncertain is not in the pop genre.',
            'output': 'Filtered Evidence:\n'
                      'Evidence-1 provides background information about Spencer Ludwig. Thus it is <<irrelevant>>\n'
                      'Evidence-2 provides background information about Tweaker, Tweaker\'s musical style incorporates synthpop, progressive rock, modern jazz and electronica genres. Thus it is <<relevant>>\n'
                      'Evidence-3 provides background information about The Attraction to All Things Uncertain, which is released by Tweaker. Thus it is <<relevant>>\n'
                      'Evidence-4 provides background information about Capital Cities. Thus it is <<irrelevant>>'
        },
        {
            'input': 'Evidence:\n'
                     'Kenny Greene (January 17, 1969 \u2013 October 1, 2001) was an American singer-songwriter who was also a member of the R&B group Intro.\n'
                     '\"Love No Limit\" is a song by American recording artist Mary J. Blige. Released as the album\'s fourth and final single, the song became a top five hit, reaching number-five on the R&B singles chart, and peaked at number forty-four on the US \"Billboard\" Hot 100 chart. It was co-written by Kenny Greene and Dave Hall for her debut album, \"What\'s the 411?\" (1992), with the latter serving as the song\'s producer.\n'
                     'William Michael Albert Broad (born 30 November 1955), known professionally as Billy Idol, is an English musician, singer, songwriter, and actor. He first achieved fame in the 1970s as a member of the punk rock band Generation X. Subsequently, he embarked on a solo career which led to international recognition and made Idol one of the lead artists during the MTV-driven \"Second British Invasion\" in the United States.\n'
                     'Claim: Billy Idol is older than the artist who co-wrote \"Love No Limit\" with Dave Hall.',
            'output': 'Filtered Evidence:\n'
                      'Evidence-1 provides background information about Kenny Greene, who was born in January 17, 1969. Thus it is <<relevant>>\n'
                      'Evidence-2 provides background information about \"Love No Limit\", which is co-written by Kenny Greene and Dave Hall. Thus it is <<relevant>>\n'
                      'Evidence-3 provides background information about William Michael Albert Broad, who is known professionally as Billy Idol, and he is born in 30 November 1955. Thus it is <<relevant>>'
        }

    ],
    'template': 'Evidence:\n'
                '{evidence}'
                '\nClaim: {claim}'
}


def message_format(template, params):
    messages = [{'role': 'system',
                 'content': template['instruct_prompt']}]
    for e in template['examples']:
        messages.append({
            'role': 'user',
            'content': e['input']
        })
        messages.append({
            'role': 'assistant',
            'content': e['output']
        })
    messages.append({
        'role': 'user',
        'content': template['template'].format(**params)
    })
    return messages
