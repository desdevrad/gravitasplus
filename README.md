# Gravitas+ — site architecture

Open `index.html`. Static files, no build step, no dependencies. A GitHub Pages
workflow is included in `.github/workflows/deploy.yml`.

```
index.html                        Home
topics.html                       Topic index (filter + search)
topic-computable-universe.html    A full worked topic — all seven layers
topic-machine-hypothesis.html     Topic 03 — the roadmap's starting topic
account.html                      Sign in / create an account
magazine.html                     Article archive
article-hypothesis-or-sentence.html  A full article — the Magazine template
lab.html                          Interactive lab
game-hypothesis-machine.html      A game you can actually play
learn.html                        The four learning paths
path-ai-in-research.html          One path, expanded
community.html                    Roles, weekly experiment, events
newsletter.html                   Subscribe + archive
about.html                        What this is, and the editorial rules
assets/                           gravitas.css · site.css · hero.css · chat.css · site.js · hero.js · chat.js
```

---

## The two decisions that shaped everything

### 1. The topic is the unit, not the video

The roadmap says a video is the *beginning* of a path. So the site is not
organised around episodes — it is organised around **questions**. A topic is
one question with every layer wrapped around it:

| Layer | What it does |
|---|---|
| 01 Film | the way in |
| 02 Essay | the argument, at two depths |
| 03 Sources | three levels — start here / go further / primary |
| 04 Timeline | how the question developed |
| 05 Simulation | something to break |
| 06 Viewpoints | the strongest case *against* our own reading, plus a poll |
| 07 Discussion | comments, this week's question, a public correction log |

`topic-computable-universe.html` is built out in full so the pattern is
concrete rather than described.

### 2. One page, two audiences — not two sites

The brief asks for a clear entry for the general reader *and* real depth for
researchers. The obvious answer — a separate "for researchers" section — is the
wrong one: it splits the audience at the door, halves the value of every piece,
and makes people classify themselves before they know what is inside.

Instead there is a **depth switch** in the header. It re-renders the page in
place: the essay has an overview version and an in-depth version carrying the
mathematics, the code and the primary citations. The choice persists across
pages, and neither version is a teaser — both are the whole argument.

---

## Navigation

Five items: **Topics · Magazine · Lab · Learn · Community**

The roadmap lists six spaces, but Newsletter is an *action*, not a place, so it
is a persistent CTA in the header and footer rather than a nav slot. There is
deliberately no "Watch" item either: here a video opens a topic, it is not a
destination of its own.

## What actually works

Not mockups:

- **Depth switch** — swaps the essay, persists across pages
- **Filtering** — type chips plus free-text search, live count, empty state
- **Hypothesis Machine** — the 2-4-6 task with a physics skin. It counts how many
  of your tests were *confirming* versus *falsifying*, and tells you the ratio at
  the end. Most players find they spent their effort trying to be right rather
  than trying to be wrong, which is the whole lesson.
- **Lorenz simulation** — two identical systems started a hair apart. Set the
  initial precision and watch the prediction horizon collapse; divergence time is
  reported live.
- **Hero** — two-body orbit (draggable on touch), pucker grid with click-ripple, comet cursor
- **Generative card art** — lab cards draw themselves instead of shipping photos

Polls, comments and sign-up forms are front-end only, and say so on screen rather
than pretending to be live.

## Verified

- No console errors on any page
- No broken internal links
- Exactly one `h1` per page
- No horizontal overflow at 360 / 390 / 768 / 1024 / 1440 / 1920px
- Mobile menu opens and closes on selection on every page
- Reduced motion honoured throughout

## Notes

- `gravitas.css` is the brand design system, unchanged. Everything new is in `site.css`.
- Copy is placeholder-grade in places — the architecture is the deliverable.
- To go live you need a backend for: newsletter, accounts, comments, polls.


---

## Changes in this pass

**The depth switch is now contextual.** It was rendering on all eleven pages but
only doing something on one. A persistent control that is inert nine times out of
eleven teaches people to ignore it, and then it is invisible on the pages where
it matters. It now appears only on the topic and the magazine — the two places
that respond to it.

**The magazine gained a second axis.** Depth now works there as reading level
alongside the topic filters: technical pieces recede in Overview and come forward
In depth. They are dimmed rather than hidden, because a list whose count silently
drops looks broken.

**A real article page.** `article-hypothesis-or-sentence.html` is the lead essay
built out — two depths, its own graded sources, and a hand-off to the topic,
the game and the open question. It doubles as the Magazine template.

**Nothing is a dead click any more.** Cards for content that does not exist yet
keep their place, but lose their `href`, gain a **Planned** chip, and cannot be
clicked or focused. Six cited papers were wired to real DOIs and arXiv entries
(Turing 1936, Feynman 1982, Lorenz 1963, Deutsch 1985, Lloyd 2002, Landauer
1961) — a citation that goes nowhere looks like scholarship and isn't.

**A real bug, found and fixed.** The mobile menu never opened on the home page.
`site.js` and `hero.js` both bound the hamburger; both fired on the same tap, the
second read the state the first had just set, and it toggled straight back shut —
so it failed on exactly the one page that loads `hero.js`. The duplicate is gone.

## Verified

| | |
|---|---|
| Pages | 12 |
| Broken links | 0 |
| Unreachable pages | 0 |
| Clickable dead links | 0 |
| Horizontal overflow | none at 360 / 390 / 768 / 1024 / 1440 / 1920px |
| Console errors | none on any page |
| Accessibility | one `h1` per page, skip link, `lang`, no unlabelled buttons, no missing `alt` |
| Mobile menu | opens, closes on selection, navigates |
| Depth switch | +597px of content on the topic, persists across pages |
| Topic simulation | animating and responds to its control |

The only remaining `href="#"` are the five social icons — outbound profiles for
you to fill in, not missing pages.

## Second pass

**Topic 03 is now built out.** The roadmap names AI and ML in scientific
research as the starting point, but the site was leading with *Is the universe
computable?* — a strategic mismatch. `topic-machine-hypothesis.html` carries
all seven layers and the roadmap's harder questions rather than a
tools-and-prompts tour.

Its simulation earns its place: a hidden relationship, noisy measurements, and a
model whose flexibility you control. Raise it and the fit keeps improving while
the prediction gets worse — the essay's argument made touchable rather than
asserted. Measured across the range, fit-error falls monotonically while
prediction-error turns around and climbs.

**The link wiring now lives in the build.** Last pass I repaired the dead links
by editing the output, so the next rebuild wiped every one of them. Source
wiring, the contact address, the community actions and the defusing of unbuilt
cards are all part of `defuse.py` now, and the build is idempotent — running it
twice gives the same clean result.

## Known gaps

Content, not structure: two topics of four, one article, one path of four, one
game of six. The generators mean the next topic is data entry rather than a
rebuild.


---

## Third pass

**Hero** read *Science, and the gravity of questions underneath it*, with
**gravity** carrying the emphasis.

**Grids no longer orphan a card.** `auto-fit` packs as many as will fit and
strands the remainder on a row of its own — that is where the 5+1 and 4+1 came
from. Each grid now declares a column count that divides its item count: six
spaces as 3+3, six roles as 3+3, five programmes as 3+2. Verified at six widths;
every row fills its full width, and the headings no longer count the items
("One path through the site", "What we make", "Roles").

**Join was rebuilt.** It was a form dropped on a flat band. It now uses the
hero's own treatment — the spacetime well and starfield behind it, real vertical
room, and the six roles shown as things you become rather than a sentence
describing them.

**Sign in / create an account** (`account.html`). One page, two panels, switched
rather than navigated, deep-linkable via `#in` and `#up`, with role selection at
sign-up. A **Sign in** action sits in the header on all fourteen pages.

**The host is only on About.** Name and photo removed from the hero, the footer,
the topic byline and the sample comment, ready for other contributors.

**Design-system corrections.** Topic 03's poll was a bespoke component; it now
uses the same result-bar poll as the other topics. The lab's number entry
suppressed the browser spin buttons — small grey chrome that was the ugliest
thing on the page — and reads as a value you are about to test. Both topic
simulations were pinned to the top of their panel and are now vertically centred
(20px above and below).

**Removed:** the Overview / In depth control from the Magazine; "English first"
from the footer and About.


---

## Fourth pass

**The depth switch moved out of the header** into a labelled bar at the top of
the section it governs. In the header it was permanent chrome competing with
navigation on all fourteen pages; in place it reads as a property of the content
and can say what it does.

**Switching depth no longer disturbs the layout.** The rule was
`[data-level="deep"] { display: block }`, which stamped on whatever the element's
own layout was — a flex source row became a block, its level badge lost
`flex: none` and stretched, and the text beside it shifted. `revert` had the same
fault in reverse (an `li` came back as `list-item`, not the author's `flex`). The
rule now only ever *hides* the other side, so every visible element keeps exactly
the display its own CSS gives it. Measured across a switch: badge width and link
position identical, `display: flex` in both states. It also means the content is
all visible with no JavaScript at all.

**Topic 04's simulation fills its panel.** The attractor was drawn from a fixed
baseline at 62% of the height and extends upward from there, so the bottom of the
box was empty — the panel was centred but the figure inside it was not. It now
measures the trajectory's own bounds and derives scale and offset from them:
16px of padding on all four sides, at any size.

**About has a team section** with the photo, built as a list rather than a
one-off block, with an open slot for the contributors to come.

**Also:** TikTok added to the footer on all fourteen pages; the sign-in row's
checkbox and "Forgotten password" now share a baseline; the role cards at sign-up
are all the same height.


---

## Fifth pass

**The Lorenz simulation sits still.** Fitting the view to the live trail meant
scale and offset were recomputed every frame as the trail grew, so the whole
figure breathed — that was the tweaking. It now frames the attractor's known
extent once, on resize only, so the view is constant: 42px above, 40px below,
zero drift between samples. (Hoisting caught me out on the way: `var VIEW` was
declared after its first use, so the script threw and nothing drew at all.)

**Topic 03 was never actually designed.** I had invented `dsr-head`,
`dsr-rail` and `tl` class names that exist nowhere in the stylesheet, so the
page fell back to unstyled defaults — content against the top edge, and a
section rail with no spacing between its links. It is now built from the same
components as Topic 04 (`head_block`, `.layer`, `.topic-nav`, `.split`,
`.video`), and the timeline is a dated list rather than a decorated one.

**Also:** footer icons reordered — YouTube, Instagram, TikTok, X, LinkedIn,
Telegram. About's introduction cut to about a third, team cards enlarged with
LinkedIn and Google Scholar links. The host's comment restored in Topic 04.
Sign-in row separated from the submit button. The community's "How it works"
card now sits level with the poll (0px difference). The join block reduced to one
dominant line and one quiet answer. The magazine drop cap set to a true two-line
cap, so nothing is left hanging under it.

## Sixth pass

**Dossiers are Topics.** The word is gone from the interface, the copy, the class
names (`.topic-nav`), the custom property (`--g-topic-nav-h`) and the filenames —
`topics.html`, `topic-computable-universe.html`, `topic-machine-hypothesis.html`.
Renaming the files breaks any link anyone already holds to the old URLs; that is
a real cost, and worth paying once rather than carrying two vocabularies.

**Hero rewritten.** It now reads *Science, AI and the gravity of underlying
questions*, with **gravity** still carrying the emphasis, over a lede that names
what the project is actually about: how science works, how it changes the world,
and what AI/ML does to research and education. The two calls to action are
**Explore Topics** and **Try Lab** — the first now goes to the index rather than
straight into one topic, because sending a first-time reader into a single
28-minute film was a narrower door than the site deserves. Its icon changed from
a play triangle to an arrow to match.

**The hero no longer fights the reader's finger.** Two things were wrong on touch.
A press-and-drag over the hero started a text selection — magnifier, handles, the
lot — and the gravity interaction was lost behind a selection nobody wanted; hero
copy is now unselectable on coarse pointers (`user-select`, `touch-callout`, plus
`selectstart`/`contextmenu` guards in `hero.js` for engines that ignore the CSS).
Links and buttons keep their long-press menus, and everything below the hero stays
selectable, quotable and translatable.

Second, there was no way to play with the orbit at all: any drag scrolled the
page, which fired `pointercancel` and dropped the third mass the moment it
appeared. There is now a `touch-action: none` patch centred on the pair
(`.lp-orbit__hit`), sized to about 70% of the canvas so it covers the
strong-influence radius with margin. Inside it a drag perturbs the orbit; a few
dozen pixels outside it the page scrolls normally. Locking the whole hero would
have been simpler and would also have trapped the reader on a screen the orbit
nearly fills — the escape route is the point.

## Seventh pass

**A light theme, and the reason there wasn't one.** The stylesheet said dark was
"the default and only mode", and it meant it — the dark values were written as
literals in about ninety places. Adding a mode therefore started with finding
them all once and routing them through named channels: `--g-tint` for the
translucent overlays, `--g-accent` for Sisal, `--g-chrome` for the sticky bars,
`--g-solid-bg/fg` for pressed chips and primary buttons, `--g-canvas-*` for the
things a canvas paints. After that `:root[data-theme="light"]` is a single block.

The light theme is not the dark one with the lights on. The brand is a night
sky, so the star field, the meteors and the comet cursor switch **off** rather
than render as grey dust on cream, and the orbit stops compositing with
`lighter` (which adds toward white — correct on deep space, a wash-out on
paper). The well is one SVG with White Tint strokes; inverting the render is
cheaper and more reliable than shipping a second file, and alpha survives it.
Sisal itself is unreadable on white, so the light theme substitutes the same
warmth at ink weight (`#7b6242`) instead of dropping the accent or borrowing a
fifth hue. Every text pair measures 4.5:1 or better, which is where dark was.

The toggle is a sun/moon button in the header. Three states, not two: **system**
is the default and a real choice, so a visitor who never touches the control
follows their OS when it changes at dusk. Pressing the button leaves system and
pins a value. The attribute is set by an inline snippet in `<head>`, before any
stylesheet — a theme applied after first paint means every light-mode visitor
sees a flash of the dark site, which is the one bug a theme toggle cannot ship
with.

Canvases can't inherit a CSS colour, so the hero grid, the orbit, the Lorenz
figure and the lab's generated card art read their palette from the tokens at
paint time and repaint on a `gravitas:theme` event. The inline logos were
`fill="#f1efec"` — a white logo on a cream page — and are now `currentColor`.

**Ask Gravitas.** A floating assistant on every page. It does not open itself
and it does not nag; a bubble that pops up unasked on a reading site interrupts
the one thing the site is for. There is no backend here, and a widget that
*sounds* like an assistant will confidently invent facts about a site it cannot
see — so this ships as a router, not an oracle: it matches a question against a
hand-written index of what actually exists, answers with real destinations, and
says so at the foot of the panel. When it can't match, it says that instead of
guessing. Set `window.GRAVITAS_CHAT = { endpoint }` before the script and it
defers to a real API, with the local index as the fallback for when that call
fails — which is the behaviour you want at 3am anyway.

**The community stops being card 05 of six.** The header CTA was a mailing-list
signup; it is now **Join Us**, pointing at a `#join` target that previously did
not exist. On the home page the community moved to slot 02 with an accent rail,
and the last band on the page — which was a newsletter form — is now the door
into the community, with the newsletter as the quieter second button. The
footer's "Do" column became "Take Part" with Join Us at the head of it.

**Less landing page, not less writing.** Card descriptions cut to a single
clause, the `<dl>` of "what's in a topic" replaced by a six-noun strip, the
latest-work list reduced to headline and metadata. The hero lede was left
word-for-word and *split* instead: the promise at lead size, the detail a step
quieter. It was three sentences of real information set as one block, and the
eye was bouncing off it to the buttons — which is a hierarchy problem wearing a
length problem's clothes.

Topics and Magazine pieces stay dense, because that density is the product.
What changed there is the page holding them: measure down from 68ch to 62ch
(a 68ch line at lead size runs to ~100 characters, past where the eye loses the
return sweep), paragraph spacing raised above line spacing, `h2`s marked by a
short accent rule rather than more size, and a reading-progress hairline —
two thousand words with no visible end is a different experience from two
thousand words that end.

**Two casing registers.** `h2` section heads stay sentence case; `h3`/`h4`
sub-section headings take Title Case. Editorial headlines and the
question-titles of Topics and articles are deliberately excluded — "Can A Model
Produce A Hypothesis, Or Only A Sentence That Looks Like One?" reads as a shout,
not a heading. Two registers applied consistently *is* the hierarchy;
title-casing everything would flatten it again.

**It is not a physics site.** Nothing ever said it was, but every worked example
came from one, and a visitor from immunology or labour economics reads that in
about four seconds. So: a fields band under the hero (ten disciplines, one line
— a list of nouns is read at a glance, a sentence claiming breadth is read as
marketing); two planned Topics from outside the physical sciences, on
replication and on whole-cell modelling, because the claim is cheap and the
Topic list is where a visitor checks it; "Computational Physics" became
"Computational Science"; and the About page now says plainly that a
haematologist, a climate modeller and a labour economist are downstream of the
same arguments.

**Also:** the lab's card canvases were `class="art"` — the same selector the
Magazine article body uses for its prose column. Two unrelated components
sharing a class is a bug waiting for someone to write a rule for one of them,
and the new reading measure was exactly that rule. The canvases are `.cardart`
now, and the long-form rules are scoped to `div.art` besides.

## Eighth pass — corrections

**Favicon.** `assets/favicon.svg` had been sitting unused since the first build.
Wired up on all fourteen pages, with `monogram.svg` as the Safari mask icon and
a pair of `theme-color` metas so the browser chrome follows the theme.

**Reading time, back on the home page.** The parts strip replaced a `<dl>` that
said what six nouns say — but the thing a reader actually wants before opening a
28-minute film and an 18-minute essay is the number, and the six nouns were not
it. The `<dl>` is back, restyled: a mono label above the value so the commitment
can be found without reading for it.

**Ask Gravitas+ wears the brand.** The launcher had a generic sparkle and said
"Ask", which reads as a bolted-on vendor widget. It now carries the channel's
own G and its full name, in the panel header too.

**Casing, corrected.** The last pass title-cased the wrong level: `h3`/`h4` card
and callout labels, when what was meant was the section heads — *The current
topic*, *Six ways in*, and their equivalents on every other page. Those are now
Title Case, along with the short page titles (*Interactive Lab*, *Learning
Paths*, *The Newsletter*). Still excluded, deliberately: essay headings inside
`.art`, the display lines on the join and account panels, and Topic and article
titles, which are sentences rather than labels.

**The simulation moved down the phone.** It was pulled above the copy with
`order: -1`, where a square canvas and its caption ate most of the first screen
and the headline started below the fold. It now follows the pitch — title,
lede, buttons, then the thing you can play with — which also puts the drag
target under the thumb instead of under the status bar, and it is a little
smaller besides.

**Two bugs from the light theme.**

The comet *is* the cursor: the hero sets `cursor: none` and lets the canvas draw
the pointer instead. Hiding the comet in light mode therefore did not remove a
decoration, it removed the mouse pointer. It composites source-over and takes
all its colour from the tokens, so it needed no hiding at all — on paper it is
simply a dark comet. The same trap was waiting for anyone with reduced motion,
which also hides the comet canvas, so the `cursor: none` rule now requires
`prefers-reduced-motion: no-preference` as well.

The grid caches its last frame and skips the redraw when the warp has not
changed — that is what makes an idle grid free. A theme flip changes the ink
without changing the warp, so the canvas kept displaying white lines on a cream
page, which is nothing at all, until a mouse move happened to invalidate the
cache. The theme hook now marks it dirty.

**The reading-depth switch was unreachable on a phone.** `.depth` was hidden
below 900px from when it lived in the header, where there is genuinely no room
for it. It does not live there any more — it sits in the `.depthbar` above the
text it governs — so the rule left the bar announcing "this essay reads two
ways" with no way to pick either. Now hidden only in the header, and stacked
full-width under its own sentence on narrow screens.

**Footer restored** to Read / Do, and Join Us removed from it. It is still the
header CTA, which is the loud slot; repeating it in the footer was a second ask
in a place people go to find a link, not to be sold one.

**Moon icon, optically centred.** Its bounding box was centred to within a
quarter of a unit, but its *mass* was not: the area centroid measures
(9.97, 14.03) against a 12,12 viewBox centre, which is exactly why it read as
sitting low and left inside a circular button. Correcting the full 2.03 units
would push the upper tip out of the box, so the glyph is shifted part of the way
back — splitting the difference between the two centres, which is what optical
centring is. The sun was already symmetric on both axes; checked, not touched.

**The community card is a card again.** Its accent rail made one of six equal
doors look like a different kind of object. Removed rather than extended to all
six, since a rail on every card is just a border.

## Ninth pass — the assistant panel

**One close, not two.** The launcher morphed into an X while the panel's own
header showed a second X six inches above it. Two controls that do the same
thing make a reader stop and pick, and neither is obviously the right one. The
launcher now has a single job — open — and steps aside while the panel is up.
It stays in the layout while hidden, because the panel is anchored to it.

**Closing has an animation now.** It never did: the panel was toggled with
`display`, which is not an animatable property, so it vanished on the frame the
class came off while opening had a keyframe. The panel is absolutely positioned
above the launcher and toggled with opacity, transform and a *delayed*
visibility, which does transition if you name it. Its transform origin is the
launcher's corner, so it grows out of the button it came from and collapses back
into it. The launcher's fade-out needed the same treatment — a `transition-delay`
on a property that isn't in the transition list is ignored, which would have
snapped the button out of existence mid-fade.

**The header was doing three jobs and none of them well.** It held the mark
inside a bordered circle, which is avatar styling — this is a logo, and a logo
does not need a container to read as one. Beside it sat the name and, under
that, a mono uppercase strapline saying "FIND YOUR WAY AROUND", which is the
same claim as the note at the foot of the panel, one line below the name, in the
loudest typographic treatment in the widget. So the busiest element in a thing
whose whole job is to stay out of the way was a sentence the reader was about to
be told twice.

What is left is a lockup and a close: the bare mark, "Ask Gravitas+" with the
plus in the accent the brand gives it everywhere else, and a close button that
only draws its circle on hover. The honesty line stays where it was, once, under
the input — available without being read on the way in. The kept parts are kept:
suggested openers, destination chips instead of blue links, the typing beat, and
the widget not opening itself.

**Also fixed on the way past:** the mark now carries one class in both homes, so
the colour it used to set on itself no longer overrides the launcher's own
foreground (dark ink on a dark fill); `.gchat` is a block again, so the
inline-flex button stopped inheriting the body's leading as phantom space under
a viewport-anchored control; and the panel height has a `vh` fallback under its
`dvh`.

## Tenth pass

**The assistant panel sat a launcher's height too high.** It was anchored above
the button with `bottom: calc(100% + 0.6rem)` — which made sense while the
launcher stayed on screen and turned into an X. It doesn't any more: it hides
while the panel is open, so those 3.85rem under the panel were a band of
nothing. The panel is anchored to the bottom of the widget now and takes the
space, which also gives it 3.5rem more height on a short screen.

**The fields band is a ticker.** Ten quiet words in a wrapped row read as a
footer and got skipped — which is a poor fate for the one line on the page that
answers "is this for me?". It now runs: a fixed mono label with an accent dot,
a hairline, and the fields sliding past it on a masked rail so words arrive and
leave rather than being clipped by a box edge. It pauses on hover and on focus,
because a ticker you cannot stop is a ticker you cannot read. Same type size and
the same band height — the change is layout, not volume.

Two things it needs to be honest and correct. The track is tripled: each copy
slides left by exactly its own width, so at the end of a cycle copy 2 stands
where copy 1 began and the restart is invisible; two copies suffice at most
widths but can come up short on a wide viewport, and the third closes that gap.
Only the first copy is exposed to assistive technology. And reduced motion needs
handling by name, not by the site-wide clamp — that rule only caps duration and
iteration count, which on a ticker would snap the track to its end position and
park the visible copy off-screen. Under reduced motion the animation is off, the
duplicates are gone, and what remains is a plain scrollable row.

## Eleventh pass

**The ticker is a signal, not a control.** It no longer pauses under the
cursor, and nothing in the band can be selected. Both changes are the same
decision: a strip of moving text that reacts to a pointer invites people to try
to grab it, and on a phone a long press on a moving line puts selection handles
over the one band on the page whose entire job is to be glanced at.

**The separators were off centre.** As an `::after` inside each item, the dot
had `.85rem` of margin on its left and `.85rem` plus the *next* item's padding
on its right — sitting about a third of the way off centre, closer to the word
it followed. A separator belongs between two things, so it is now drawn as a
`::before` on each field with equal margins on both sides, and the item padding
that was doing the other half of the spacing is gone. Copies stay identical
widths, so the loop is still seamless.

**The hero credit line ran off the side of a phone.** It was `inline-flex` with
the default `nowrap`, left over from when it held a logo lockup — and three
stats plus two separators do not fit one phone line. Worse, "312K" and
"subscribers" were separate anonymous flex items, so even with wrapping they
could have parted company. Each stat is now its own element that wraps as a
unit, and the row breaks between facts rather than through them.

**The drop cap is ink again.** It was set in the accent, which on dark is Sisal
against White Tint body copy — a hairline of difference that reads as emphasis.
On light the same token is bronze, and two lines tall that stops being an
initial and becomes a brown blob at the top of the article. Weight and scale
already do everything an initial needs.

## Twelfth pass — the social icons

**They were six different sizes on the same grid.** Measured inside their
24-unit boxes, with stroke, the silhouettes came out: YouTube 21.3 wide,
Telegram 21.3, Instagram and LinkedIn 19.7 square, X 19.2 — and TikTok 13.2 by
15.2, a third smaller than its neighbours. Worse, TikTok's centre sat at
(14.15, 10.05) rather than (12, 12): two units up and two right, which is why it
looked like it was escaping its circle rather than sitting in it.

Every glyph now carries a transform that centres its measured bounding box on
(12, 12) and scales it to a common cap — 19.6 units for the outline icons, 17.4
for X. The two figures are not a mistake: a solid shape reads heavier than an
outline of the same size, so filled marks are set a notch smaller, which is the
standard compensation. The scale would otherwise change the stroke weight along
with the geometry, so each group carries a counter-scaled `stroke-width` and
every icon still draws at 1.7. Verified by re-measuring the shipped markup
through its own transforms: all six centre on (12, 12) to within a fiftieth of a
unit.

With the glyphs finally filling their boxes, the old 1.05rem render size left
the mark under 40% of a 2.25rem button. 1.2rem puts it at about 45%, which is
where an icon button stops looking half-empty.

**Telegram was two paths that missed each other.** The outline began at
(21.3, 4.4) and the crease ran only as far as (18.4, 7.6) — they were meant to
be the same corner, so the glyph forked at the top. Redrawn: the outline is one
closed path through the origin, the left tip, the tail notch and the lower tip,
and the crease terminates on the outline's own start vertex. They meet because
they are the same point, not because two sets of numbers were eyeballed close.

## Thirteenth pass

**Telegram, measured properly this time.** The last pass centred every icon's
bounding box, which is the wrong quantity for an asymmetric glyph. Rasterising
each icon at 20px per unit and taking the alpha-weighted centroid gives where
the ink actually sits, and Telegram's sat 1.27 units right and 0.36 up of its
box centre: a long thin left wing carrying almost no weight against a body
bunched on the right. TikTok's was 0.64 left and 1.07 down. Both are corrected
at 70% of the measured gap; the last third would push a tip within a unit of
the frame, and a glyph touching its own edge reads as clipped. Re-measured after
the fix, every icon's ink now falls within 0.3 units of centre, against 1.27
before.

**Dark is the default outright.** Boot was resolving `prefers-color-scheme`,
which is why the site opened dark on one machine and light on another: it was
inheriting a decision the visitor made for some other app. The site has a look;
you get it until you say otherwise, and saying otherwise is one button. The
runtime OS listener is gone with it, and the `theme-color` metas no longer split
on scheme either, so the browser chrome cannot go cream on a dark page.

**Every em dash is gone.** 107 in visible copy, plus link-preview titles and
meta descriptions, plus the strings inside inline scripts that end up on screen
as verdicts and hints. Not deleted, rewritten: each dash was doing one of three
jobs and each got the right punctuation instead. Appositives took commas or
parentheses ("no one, including its authors, can say why"). Elaborations took
colons ("Explanation, evidence and demarcation: the arguments underneath every
methods section"). And the ones hiding a sentence boundary got the full stop
they were standing in for ("You may run as many tests as you like. The
interesting question is which ones you choose"). Page titles used the dash as a
separator, so they take a middot now. Placeholder readouts waiting for a value
take an en dash, which is that glyph's actual job. Code comments were cleared
too. `README.md` is the exception: it is build documentation rather than site
copy, and mechanically repunctuating a hundred sentences of it would do more
harm than the dashes.

**The sign-in page had a star field.** At that size on a plain panel the stars
read as dead pixels rather than sky. Removed; the page keeps the well and the
gradient.

**Favicon replaced** with the supplied file, and verified rendering.

## Fourteenth pass

**The hero headline was sized against the wrong thing.** It used a viewport
clamp topping out at 5.25rem, but it wraps inside a column, not a window. At
1440px that put 84px type in a 558px track: about twelve and a half characters a
line, so "underlying" took a line by itself and the block ran four or five lines
deep with one or two words on each. The block was tall, the rag was ragged, and
none of it had anything to do with how wide the screen actually was, which is
why it looked worst on a big display.

Two changes. The text column takes more of the grid, 1.15fr against 0.85fr
instead of 1fr against 0.95fr. And the type is measured against that column
rather than the window: `10.8cqw` holds the headline near seventeen characters a
line at every width, which is about where a display line stops reading as a list
of words. The viewport clamp survives as the fallback, retuned so browsers
without container queries land in the same place. Measured across widths, the
headline now sets in three lines from 880px up, and three on a phone, against
four or five before.

`text-wrap: balance` on the headline evens the rag instead of leaving a two-word
orphan on the last line, and the lede goes from a 26ch ribbon to 34ch, which
stopped it reading as a narrow column pinned under a wide one.
