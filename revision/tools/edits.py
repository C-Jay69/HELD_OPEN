# -*- coding: utf-8 -*-
# Edit list for the D3 revision pass.
# Each edit: (id, category, paragraph_index, old_substring, new_substring, note)
# old_substring must occur exactly once in that paragraph.

EDITS = [
# ---------------- A. CONTINUITY: the March window ----------------
("A1","Continuity — March window",2228,
 "Four days for the category review. Two more to generate the appointment.",
 "Eleven days for the category review. Three more to generate the appointment.",
 "FLAG 1. Application filed Day 91 (2 March); the appointment must land on Day 105 (16 March). 91+11+3 = 105. The old estimate (6 days) landed on Day 97."),

("A2","Continuity — March window",2279,
 "Day 105","Day 105 — the sixteenth of March",
 "FLAG 5. Ch. 23 now carries the same 'Day + date' stamp convention already used by Ch. 28 and Ch. 31, so the reader is never in doubt which day the port interview is."),

("A3","Continuity — March window",2365,
 "Days 97\u2013104","Days 105\u2013108",
 "FLAG 3. The chapter opens on the vault collection, which begins on the 16th, and closes in its own small hours — so its span is Days 105–108, not 97–104. This also removes the reading-order inversion of FLAG 5: the chapter no longer starts in the past."),

("A4","Continuity — March window",2448,
 "After the interview on the eighth of March, the Office wrote to them.",
 "After the interview at the western facility on the eighteenth of February, the Office wrote to them.",
 "FLAG 2. Mesa's intake interview is at the facility; the port completion is the 16th. The eighth of March belonged to neither. This is the one place in the audit's fix list where I depart from its recommendation — see the note on FLAG 2 in the change log."),

("A5","Continuity — March window",2452,
 "a person was interviewed on the eighth of March and has been entered",
 "a person was interviewed at the western facility on the eighteenth of February and has been entered",
 "FLAG 2, inside the letter. Same reasoning as A4."),

("A6","Continuity — March window",2540,
 "his request of the eighth of March had been recorded",
 "his request of the second of March had been recorded",
 "FLAG 2. Kavanagh signs the sponsoring certification on Day 91 = 2 March; the receipt must acknowledge that date."),

("A7","Continuity — March window",2610,
 "since the ninety-eighth day","since the nineteenth of March",
 "FLAG 4, and refined on the re-read: Sal's application is written in the small hours of Day 108 (Ch. 24) and posted on 2 April, so 'Two weeks' in the next clause is exactly right. The date is given as 19 March rather than 'the hundred and eighth day' — day-numbers in this book are the crew's shorthand, but Sal is a man of dates, and the next clause of his own sentence is a date."),

("A8","Continuity — number slip",2615,
 "I have 411 items of ash","I have two hundred and eleven items of ash",
 "FLAG 6. 411 is the book's other motif number (desks, entries, exceptions, the June movement). The ash is 211 in Ch. 24 and Ch. 27; here it had drifted."),

("A9","Continuity — number slip",3219,
 "eight hundred and eighty people standing in a doorway in the rain tonight",
 "three thousand eight hundred and forty-one people standing in a doorway in the rain tonight",
 "FLAG 7. Makes Ch. 33 deliberate: 3,841 stand in the rain, 2,961 are counted, and in Ch. 34 the difference — eight hundred and eighty — becomes persons."),

("A10","Continuity — typo",3137,
 "Completion of the marital schedule review","Completion of the maritime schedule review",
 "Housekeeping. It is the maritime schedule everywhere else in the book; a second deliberate typo ('accommodated', Ch. 24) already carries that joke."),

# ---------------- B. HOUSEKEEPING ----------------
("B1","Housekeeping — interlude numbering",25,
 "Notices of the Office of Records and Accommodation","CUSTOS Interlude II: Notices of the Office of Records and Accommodation",
 "Housekeeping. The four interstitials are I / – / – / IV; this restores the scheme in the contents."),

("B2","Housekeeping — interlude numbering",2139,
 "Notices of the Office of Records and Accommodation","CUSTOS Interlude II: Notices of the Office of Records and Accommodation",
 "Housekeeping, body heading. Same as B1."),

("B3","Housekeeping — interlude numbering",27,
 "CUSTOS Section: Kestrel Field","CUSTOS Interlude III: Kestrel Field",
 "Housekeeping. Kestrel Field is one of the best pieces in the book and was labelled as an appendix to Ch. 22."),

("B4","Housekeeping — interlude numbering",2245,
 "CUSTOS Section: Kestrel Field","CUSTOS Interlude III: Kestrel Field",
 "Housekeeping, body heading. Same as B3."),

("B5","Housekeeping — interlude numbering",37,
 "CUSTOS Interlude IV","CUSTOS Interlude IV: Held Open",
 "Housekeeping. The interlude's own first line is 'Internal notice. Matters held open.' — the title now matches the pattern of I and III. Fully reversible."),

("B6","Housekeeping — interlude numbering",3047,
 "CUSTOS Interlude IV","CUSTOS Interlude IV: Held Open",
 "Housekeeping, body heading. Same as B5."),

("B7","Housekeeping — motif",3309,
 "The receipt for four hundred and eleven euro is still in his good coat",
 "The receipt is still in his good coat",
 "Housekeeping. In Ch. 34 the €411 is deliberate and funny; repeated in the coda it shows the machinery. The reader who remembers it will supply it."),

# ---------------- C. LINE RULE 3: the meta-book register ----------------
("C1","Line rule 3 — meta register",336,
 "said the thing that changed the chapter of her life she was in.",
 "said the thing that changed what came next.",
 "Rule 3. Keeps the beat; removes the author's hand on the scale. The one fourth-wall moment worth keeping is the postcard's (coda, untouched)."),

("C2","Line rule 3 — meta register",1091,
 "for the rest of the book.","for the rest of the year.",
 "Rule 3. In-world horizon instead of the book's."),

("C3","Line rule 3 — meta register",1696,
 "And then she thought the thing she would think for the rest of the book, which had no arithmetic in it and did not want any:",
 "And then she thought the thing that had no arithmetic in it and did not want any:",
 "Rule 3."),

("C4","Line rule 3 — meta register",1889,
 ", and she would think about it for the rest of the book.",".",
 "Rule 3. The sentence is stronger ending on 'stayed hers'."),

("C5","Line rule 3 — meta register",1979,
 ", which was the point of the chapter of their lives they were in","",
 "Rule 3."),

("C6","Line rule 3 — meta register",2413,
 ", whatever the chapter is called in your notebook","",
 "Rule 3. Sal's 'It is an application' is the payoff; the aside was stepping forward to explain the joke."),

# ---------------- D. LINE RULE 2: scene before summary ----------------
("D1","Line rule 2 — summary tic",984,
 ", which she would think about for years, and which she would have given anything, later, to be able to say had been a strategy","",
 "Rule 2. Cut the hindsight forecast; the speech that follows does the work."),

("D2","Line rule 2 — summary tic",1029,
 "Then the room did the thing Mara would think about for the rest of her life: for about eleven minutes, it acted like a room in which somebody was in charge.",
 "Then, for about eleven minutes, the room acted like a room in which somebody was in charge.",
 "Rule 2. This was the clearest case in the book of the narrator telling the reader which eleven minutes mattered."),

("D3","Line rule 2 — summary tic",1283,
 " \u2014 and would return to it at two in the morning for the rest of her life \u2014 that whether it was good did not matter.",
 " that whether it was good did not matter.",
 "Rule 2."),

("D4","Line rule 2 — summary tic",1539,
 "She would think about that for a long time afterwards, and it never got better.",
 "It never got better.",
 "Rule 2. Three words instead of twelve, and colder."),

("D5","Line rule 2 — summary tic",2043,
 "which Mara would think about for years, because","because",
 "Rule 2. The 'because' clause is the point and stays."),

("D6","Line rule 2 — summary tic",2305,
 ", and the third she heard she would carry for the rest of her life.",".",
 "Rule 2. The interview's content is in the scene; the promise of future grief is the narrator leaning in. Also removes one of the book's densest 'nineteen minutes' echoes."),

("D7","Line rule 2 — summary tic",2356,
 "and then \u2014 and this was the thing Mara would remember from that afternoon, out of everything, more than the page and the handshake and the lorries \u2014 he laughed",
 "and then he laughed",
 "Rule 2. The best example of a summary clause standing in front of its own image."),

("D8","Line rule 2 — summary tic",2415,
 "She should have taken it. She sat there for a full minute with the whole of her authority in the room and the one page in front of her, and she did not take it, and she would spend the rest of the book being unable to decide whether that was the most humane decision she ever made or the worst one, and in the end she settled on the truth, which was that it was the same decision twice.",
 "She had the whole of her authority in the room and one page in front of her, and she did not take it. She would never decide whether that was the most humane thing she did or the worst; it was the same decision twice.",
 "Rule 2, and the worked example from the assessment (§6.2) applied as written: 80 words to 45, same meaning, no narrator leaning on the scale."),

("D9","Line rule 2 — summary tic",2776,
 "That was what Mara turned over on the drive, while Kavanagh talked about a filly. The number was in the register",
 "The number was in the register",
 "Rule 2. The closing 'still, two kilometres inland…' beat survives; the run-up to it was the narrator summarising a scene the reader had just read."),

# ---------------- E. LINE RULES 4 AND 5: numbers and similes ----------------
("E1","Line rule 5 — similes",663,
 "and he watched them the whole way past the way a man watches a thing from a moving train.",
 "and he watched them the whole way past.",
 "Rule 5. The simile restated the verb. This one is narrator-side, not Mesa's register — which is where nearly all of this book's similes live and should stay."),

("E2","Line rule 5 — similes",683,
 ", the way a man raps a table.",".",
 "Rule 5, same principle."),

("E3","Line rule 4 — numbers",2418,
 "Sal looked at the page for eleven seconds.","Sal looked at the page.",
 "Rule 4, light touch. This is the third 'eleven seconds' in four pages; the beat is stronger unmeasured."),

("E4","Line rule 1 — mechanism",2177,
 "There is no field for it. So the office keeps the maritime schedule short and verifies seafarers where they are, in ports, because a port is not a waiting room.",
 "So the office verifies seafarers where they are, in ports, because a port is not a waiting room.",
 "Rule 1. 'There is no field for it' repeats the sentence before it, and 'keeps the maritime schedule short' pre-empts the port idea that the next clause lands. Note: the audit's claim that the five-line plan is stated in Ch. 26, restated in Ch. 27 and re-explained in Ch. 30 does not hold up — see pushback 3 in the change log."),

# ---------------- F. LINE RULES 1 AND 2: second batch ----------------
("F1","Line rule 2 — summary tic",649,
 "and that was the thing she could not stop thinking about afterwards \u2014 that she had been allowed to watch a working thing.",
 "and she had been allowed to watch a working thing.",
 "Rule 2. The image is the book's quietest hinge; it does not need the narrator pointing at it in retrospect."),

("F2","Line rule 2 — summary tic",1505,
 "She would never know whether the letter was kindness, calculation or both",
 "She never knew whether the letter was kindness, calculation or both",
 "Rule 2. Same meaning, past tense, no promise of future uncertainty."),

("F3","Line rule 2 — summary tic",1550,
 ", long enough that she would remember the exact length of it, and would never be able to decide whether it mattered or whether it was only a man being old and visible in the dark.",
 ". He was only a man being old and visible in the dark.",
 "Rule 2. Garrity taking four seconds of applause is the scene; the four lines about what Mara will make of it forty years later were the paragraph after the scene. (Re-read fix: the cut left the final clause hanging on a pronoun, so it starts a sentence of its own.)"),

("F4","Line rule 1 — mechanism",2890,
 "Then she did the thing she had learnt to do in February and had been doing ever since, which was to take a person at his word and put it on the record.",
 "Then she took him at his word and put it on the record.",
 "Rule 1. This was a near-verbatim repeat of the same sentence in Ch. 26 (\"did the thing she had been learning to do since February, which was to take a person at his word\")."),

("F5","Line rule 2 — summary tic",2226,
 "Mara watched him do it \u2014 the name, the registration number, the date \u2014 and understood that she was looking at a document about a person, and that the person was Kavanagh, and that a page with his name on it",
 "Mara watched him do it \u2014 the name, the registration number, the date. A page with his name on it",
 "Rule 2. The paragraph ends on 'the word authorize', which is the point; the scaffolding in front of it was explaining the point. (Re-read fix: the sentence is broken after the em-dash aside rather than left as a comma splice.)"),

# ---------------- G. PASS TWO: the read-through, and submission form ----------------
("G1","Continuity \u2014 pass-two fixes",2480,
 "Days 105\u2013107","Days 108\u2013110",
 "Pass two. Ch. 25 still began before Ch. 24 ended (Ch. 24 now runs to Day 108), the last backwards step in the sequence. The chapter has no internal day anchors of its own, so the stamp moves rather than the scene."),

("G2","Continuity \u2014 pass-two fixes",2549,
 "Days 108\u2013115","Days 110\u2013115",
 "Pass two. Touches Ch. 25's new close, so the March chapters run strictly forward: 105 | 105\u2013108 | 108\u2013110 | 110\u2013115. The meeting itself is still after Sal's letter (Day 108); the wider span is the planning run-up to 2 April."),

("G6","Continuity \u2014 pass-two fixes",3333,
 "what his handwriting did in the last week of April","what his handwriting did in April",
 "Pass two. The page reached Elena two days before the twenty-first of April interview (Ch. 31), so 'the last week of April' was one week out. In a book whose whole argument is that dates are the only thing that holds, the coda should not be the one place that rounds."),

("G3","Line rule 3 \u2014 meta register",3323,
 "are not in this book.","are not written down anywhere.",
 "Pass two, rule 3 \u2014 and a genuine trip-up: 'this book' in that sentence meant the novel, while 'the book' two paragraphs later means Mara's exercise book. One word, two objects, four lines apart."),

("G4","Line rule 3 \u2014 meta register",3329,
 "and the letter is in the book.","and the letter is in her book.",
 "Pass two. Same fix from the other side: the letter is in Mara's book, not in this one."),

("G5","Line rule 3 \u2014 meta register",3348,
 "because the answer does not change a single thing about the people in the book.",
 "because the answer does not change a single thing about any of them.",
 "Pass two, rule 3. The last remaining fourth-wall touch apart from the postcard's, and it was there to be cut."),
]

# Presentation normalisation (all scene dividers to one style) — logged separately, not paragraph-specific.
DIVIDER_FROM = "---"
DIVIDER_TO = "\u2022 \u2022 \u2022"
