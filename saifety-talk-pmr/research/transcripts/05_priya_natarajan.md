# Synthetic PMR Interview Transcript: 05 Priya Natarajan

| Persona # | Name | Role | Role tag | Anchor group | Simulated date | Duration |
|---|---|---|---|---|---|---|
| 5 | Priya Natarajan | SIMOPS & Interface Planning Lead, Owner's CM team, $6.5B LNG export terminal (Louisiana) | [M] (with [B] budget influence) | B (Low-first: $24,000 then $150,000) | 2026-09-27 | ~50 min |

Synthetic transcript — simulation only; must be validated with real human stakeholders.

---

**Interviewer (Intro):** Thanks for making the time. I'm doing research on how work coordination and safety information move around on large industrial sites. There are no right or wrong answers, and I'm not here to evaluate you or your project. I'd like to record the call for notes only. Nothing will be attributed to you or your company by name. Is that okay?

**Priya:** Yes, that's fine. I'm on call for night permit conflicts this week, so if my phone goes off I may have to step away for two minutes.

**Interviewer (Intro):** Understood. Let's start.

---

## Section 1: Warm-up

**Interviewer (W1):** Walk me through yesterday from the moment you got to the gate until you left. What took most of your attention?

**Priya:** Okay. Badge in at about 5:40. I'm at my desk by 5:50 and the first ninety minutes are always the same: I rebuild the SIMOPS matrix for the day. I pull the EPC's lookahead export out of P6, the permit export from the e-permit system, the commissioning team's schedule for the next 48 hours, and the isolation register. I merge them in Excel, mostly with Power Query now, then I do the part I can't automate. I look at exclusion zones on the plot plan and check whether anything overlaps in space and time. I publish that around 7:15.

Then yesterday specifically... most of my attention went to Train 2. Commissioning wanted to move a leak test on a fuel gas header up by a day, and the EPC had an insulation crew and a scaffold crew in the same pipe rack bay. So I spent the morning on Teams going back and forth with the EPC planner and our commissioning lead about who moves. I did a walkdown at about 10:30 to look at the barricades myself. The 14:00 SIMOPS meeting ran long, fifty minutes instead of thirty. After that I updated the matrix again, because by then half of what I published at 7:15 was stale. I left around 17:45.

**Interviewer (W1 probe):** Why did the 14:00 meeting run long?

**Priya:** Because the EPC planner showed up with a different sequence than the one in the lookahead they gave me on Monday. That happens a lot. Their lookahead is... let's say it's conservative about what they actually intend to do. So we spent twenty minutes figuring out what's really happening in Train 2 tomorrow before we could even talk about conflicts.

**Interviewer (W2):** Who do you have to coordinate with on a normal day, other trades, other contractors or other departments? How does that coordination actually happen?

**Priya:** On the owner side it's our commissioning team, the early operations group for Train 1, since Train 1 has had gas in for a few months, and my CM. On the contractor side it's the EPC's planners and area superintendents, their permit coordinators, and the three big subs: mechanical, electrical and I&E, and the scaffold/insulation/paint contractor. Plus heavy lift when there's a big pick.

How it actually happens: the 14:00 meeting is the formal part. Everything else is Teams. I have a channel with the EPC planners, and there's a separate chat with the permit coordinators. And a lot of it is people sending me photos of the permit-to-work board in the permit office, because it's faster than asking what's been issued.

**Interviewer (W2 probe):** Can you give me an example of something that got coordinated outside the meeting recently?

**Priya:** Last Thursday night. I was on call, and a night-shift permit coordinator called me at about 11 p.m. because a hot work permit request for a pipe support modification was inside the zone of a line commissioning had planned to pressurize at 4 a.m. We sorted it on the phone. He held the permit until 6. I wrote it up in my tracker the next morning. None of that was in any system except his permit log and my notes.

**Interviewer (W3):** When something on site looks "off" to you or your crew, what typically happens next? Walk me through the most recent example.

**Priya:** I don't have a crew. I should be clear about that. I'm owner staff. The people who see things first are the craft. For me personally, "off" usually means something I see on the matrix or on a walkdown that doesn't match what's supposed to be happening.

Most recent one was yesterday on the walkdown. There was a barricade for the leak test, and inside it was a scaffold with a green tag and two guys on it doing insulation prep. The test wasn't live yet, so nobody was in danger right then. But the barricade was up for a test the insulation foreman didn't know had been pulled forward. I found the foreman, told him, and then went to the EPC area superintendent. Then I sent a Teams message to the planner so it was written down somewhere.

**Interviewer (W3 probe):** What happened next?

**Priya:** The insulation crew got moved to another bay by lunch. The superintendent was a bit annoyed with me, not because I was wrong, but because it meant resequencing his afternoon. Nobody made a formal report. From their side nothing had happened.

**Interviewer (W4):** What do you use day to day to keep track of work, permits, observations or issues: paper, radio, phone, software, anything else? What do you like and dislike about each?

**Priya:** P6, but I only read it. The EPC owns the schedule. I like that it's the official logic. I dislike that the lookahead they export is only as honest as the person exporting it.

The Excel SIMOPS matrix. I like that I control it. I dislike that it's out of date by lunch, and it depends on me. If I'm sick, it's thin.

The e-permit system. That's the actual source of truth for what's authorized. I like that it's controlled and auditable. I dislike that it knows nothing about schedule or about the commissioning state of the systems. It knows a permit was issued for a location, but not that the line next to it goes to 900 psi at 2 p.m.

I built a Power Apps tracker for interface issues and open SIMOPS items. I like it because the fields are the ones I need: location, affected permits, systems, owner of resolution, due date. I dislike that only owner staff can use it. The EPC won't put their people on our tenant.

Teams and SharePoint, which are fine, but Teams is where information goes to die. Photos of the permit board, which are ugly but honestly very reliable. Radio, I carry one, but I'm not on the craft channels.

On weekends I play with some of the newer AI tools, to be honest, but nothing like that on site. IT wouldn't allow it anyway.

**Interviewer (W4 probe):** What do you rebuild or re-enter by hand across those?

**Priya:** Locations, mostly. P6 has activity codes and areas. The e-permit system has its own location tree. Commissioning works by system and subsystem. None of them map cleanly to each other. So every morning I'm translating "Train 2, rack 3, bay 14" into a permit location and into "subsystem 21-FG-03". I've built a lookup table, but it breaks every time someone adds an area.

**Interviewer (W5):** How do you find out what happened on site when you weren't there?

**Priya:** For night shift: the permit log, the night permit coordinator's handover email if he writes one, and the EPC's daily report, which lands around 9 a.m. and is mostly about production. For safety items, the EPC's weekly HSE report to the owner, which is summarized to the point of being useless for me. "Three near-misses, mechanical, housekeeping." Where? Which permits? No idea.

Honestly, a lot of it is hallway. The commissioning lead tells me something at lunch and I realize it was a SIMOPS event I should have known about two days ago.

**Interviewer (W5 probe):** Can you give me an example of finding out that way?

**Priya:** Yes, and it's the one that bothers me most. I'll probably come back to it. Last quarter, twice, a crew started hot work near a line under pressure test. Both times I found out days later, informally.

---

## Section 2: Core Assessment

**Interviewer (C1):** Tell me about the last time someone on your crew or site noticed something unsafe and *didn't* formally write it up. What was going on?

**Priya:** That's the second of those two, in August. Commissioning had a pneumatic test on a section of header in Train 2. It had been scheduled for a Tuesday night. It got moved to Wednesday morning. The change was made in the commissioning schedule, and the test permit was updated in the e-permit system. But my matrix for Wednesday was built from Tuesday's data, because the change was made after I pulled. So Wednesday's matrix showed no conflict.

Meanwhile a structural sub had a hot work permit for welding on a pipe support maybe thirty, forty feet away, inside the exclusion zone for a pneumatic test at that pressure. The permit issuer signed it off the matrix, and the matrix was wrong.

A pipefitter from the mechanical sub saw the test barricade going up and the welding habitat right there, and he radioed his foreman. His foreman radioed the EPC permit issuer, the hot work stopped, the test went ahead an hour later. Nobody got hurt. Nothing failed.

And nobody wrote it up. I found out on Friday at lunch, from our commissioning lead, almost as a funny story.

**Interviewer (C1 probe):** Why wasn't it written up?

**Priya:** A few reasons, and I asked. The pipefitter did what he's supposed to do, he told his foreman. In his mind the system worked. The foreman thought it was handled. The permit issuer, and I understand this, did not want a record saying he signed a hot work permit inside a test exclusion zone, even though he was working from my matrix. And in the EPC's culture a near-miss report is for when something almost physically hits someone. "A weld was near a test" doesn't feel like a near-miss to them. To me it's a potential loss of containment with a crew right next to it. That's the difference between how craft see it and how process safety sees it.

**Interviewer (C1 probe):** What would have happened to them if they had written it up?

**Priya:** To the pipefitter, probably nothing bad. Maybe a "good catch" at the safety meeting. To the permit issuer, there'd have been an investigation and his name on it. To the EPC, it would have been an owner-visible event on Train 2, which goes to the monthly owner HSE review. So there's an institutional reason not to write it up, even if nobody gets personally punished.

**Interviewer (C2):** When someone raises a hazard that involves another company's crew or their own supervisor, what happens to *the person who raised it*? Can you share an example, good or bad?

**Priya:** For me, nothing. I'm the owner. I'm allowed to be annoying. That's partly my job.

For craft it's different, but I want to be careful, because I don't see it firsthand. I can tell you what I've heard. There's a scaffold foreman who's been vocal about the EPC's crews using his scaffolds without a tag check. I've heard, from him, that his requests started getting lower priority in the scaffold request queue. Is that retaliation or just the queue? I can't prove it. He believes it.

The good example is the pipefitter from August. His foreman backed him, and I made a point of thanking him through the mechanical sub's superintendent. I don't know if that helped him or embarrassed him.

**Interviewer (C2 probe):** Has it ever affected someone's assignments, layoffs or reputation, that you know of?

**Priya:** Reputation, yes. There's definitely a label, "that guy stops work over nothing." I've heard EPC supers say it about specific people. Layoffs, I have no evidence either way. On this site I think what happens is quieter than retaliation. People learn which issues are worth the hassle, and interface issues, where it's another company's problem, usually aren't worth it to them.

**Interviewer (C3):** Think of a hazard you or your crew reported in the last month. What did you see or hear back afterward, and how long did it take?

**Priya:** Two weeks ago, in the 14:00 meeting, I flagged that the lookahead had an insulation crew in the same bay as a leak test on a Thursday. The EPC planner said, "we'll resequence." Next morning I got a Teams message from him: "resequenced." So one day, which is good.

Except nobody told the insulation foreman, and I only found that out because I walked it. So what I heard back was that it was closed, and it wasn't actually closed in the field. That's the pattern. Closure in the office is not closure at the work face.

**Interviewer (C3 probe):** What's the longest you've waited?

**Priya:** Six weeks, on one item. When Train 1 got gas in, the area classification boundary moved. Suddenly a big chunk of the area was a classified area and there was still non-rated temporary power in it: spider boxes, temporary lighting strings, a couple of extension cords run by the scaffold contractor. I logged it the day after gas-in. The last spider box came out six weeks later. That's not because anyone didn't care. It's because temp power was owned by the EPC's electrical sub, the lighting belonged to the scaffold contractor, and the area now belonged to owner commissioning. Three owners, so nobody.

**Interviewer (C3 probe):** How did that affect whether you'd report again?

**Priya:** It doesn't stop me. It changes how I report. Now I don't just report, I name a person and a date in the 14:00 meeting in front of everyone, because that's the only thing that works.

**Interviewer (C4):** What has your site or company tried in the past to get more people to report (cards, quotas, rewards, apps)? What happened to it after the first few weeks?

**Priya:** The EPC runs an observation card program. Each foreman has a monthly quota. At peak it was something like twelve thousand cards a month. I looked at a month's export once. About sixty percent were housekeeping, and a lot of them were written in the last three days of the month. It's feeding the beast.

There was a raffle, gift cards for "quality observations." That lasted maybe two months. The owner did a "Good Catch" program with a branded jacket for the catch of the month. People liked the jacket. I don't think it changed what got reported.

And the EPC moved their cards from paper to a mobile module in their safety software earlier this year. Card counts dropped by about a third in the first month, because it needed a login and most craft didn't have their credentials set up. They went back to allowing paper in parallel.

**Interviewer (C4 probe):** Why did it fade, in your view?

**Priya:** Because nothing visible came back to anyone. You fill in a card, it goes into a box or a database, and it becomes a number on a slide. The quota measures activity, not whether anything got fixed. The crews figured that out within a few weeks.

**Interviewer (C4 probe):** What did people say about it in the trailer or break room?

**Priya:** "Did you do your cards?" Like homework. That's the phrase. It's a chore, not a safety tool.

**Interviewer (C5):** Describe the moment you notice a hazard mid-task: where are you, what's in your hands, what's around you, and how much time do you realistically have to tell someone?

**Priya:** For me, on a walkdown in Train 1: FRC, hardhat, glasses, gloves, personal gas monitor clipped on, radio, and the intrinsically safe phone, because that's the only phone allowed in the classified area. If I want a photo inside the boundary with anything that isn't IS-rated, that needs a permit. Around the compressors you can't hear the radio at all. I can take maybe a minute or two to make a note on the IS phone. Usually I just try to remember and write it up when I'm out.

For the craft it's much worse. A pipefitter in the rack has both hands busy, he's tied off, his phone isn't allowed in the classified area or he left it in the truck because the EPC's phone rules are strict. He's got maybe fifteen, twenty seconds before his partner needs him again. That's why he radios. The radio is the only thing he has.

**Interviewer (C5 probe):** What's the longest you'd spend before you'd "just deal with it later"?

**Priya:** Me, a couple of minutes, then it goes in my notebook for after the walk, which could be forty minutes later. For crews, if it's more than a radio call, later means end of shift, and end of shift means never. I'm obsessive about that. Every time someone proposes a new form for the crews, I ask them how many seconds it takes, and they never know.

**Interviewer (C5 probe):** Does language come into it on your site?

**Priya:** Some. There's a meaningful share of Spanish-speaking craft, especially in civil, scaffold and insulation. Most foremen are bilingual. Written English on a form is a barrier for some of them. On the radio it's mostly fine.

**Interviewer (C6):** When a report does get made, walk me through its journey from the person who saw it to the person who fixes it. Where does it slow down, get lost or go to the wrong place?

**Priya:** Typical path: craft to foreman by radio. Foreman to the EPC area superintendent, or to the permit issuer if it's permit-related. If it's safety, maybe the EPC HSE coordinator, who might enter it in the EPC's system. From there it shows up for the owner in the weekly HSE report, summarized, without location detail. If it's an interface or SIMOPS issue, it's supposed to come to me or the area authority. In practice it reaches me when someone remembers.

Where it slows down: shift handover. Night shift is the worst. Something raised at 3 a.m. becomes a line in a handover email, if there is one. Where it gets lost: between the EPC's system and ours. They're separate. Where it goes wrong: it goes to HSE when it's really a permit or commissioning issue, so it gets treated as housekeeping. The pneumatic test thing, if it had been written up, would probably have been categorized as "hot work, housekeeping" and routed to the structural sub. Wrong owner. The real owner was the permit process, meaning me and the permit issuer.

**Interviewer (C6 probe):** Duplicates? Missing location or photo?

**Priya:** Duplicates, yes. The temp power thing had five or six separate entries across the EPC's cards and my tracker, all described differently. Location is the biggest gap. "Train 2 rack" isn't a location. The rack is a quarter mile long. I need a bay or a grid, and ideally a tag number or a line number.

**Interviewer (C6 probe):** Who decides who owns it?

**Priya:** Whoever it lands with first, unfortunately. Officially, for anything touching permits or commissioning systems, it's the area authority. In practice I end up owning interface issues by default, because I'm the one who notices that no one else does.

**Interviewer (C7):** How do you currently sort incoming observations to decide what's urgent and who owns it? How long does that take on a typical day?

**Priya:** I don't triage general safety observations. That's the EPC's HSE team. What I triage is SIMOPS inputs, the overlaps. The morning rebuild is about ninety minutes. Then another forty-five to an hour after the 14:00 meeting to update. On a bad day, when commissioning resequences, maybe three hours total. Plus on-call at night maybe twice a week.

**Interviewer (C7 probe):** What information do you need to decide?

**Priya:** Location at a granularity where exclusion zones mean something. Time window. The permit type and permit number. The energy state of the adjacent systems: is hydrocarbon in, is it under test, is it isolated, what pressure. Who the area authority is. And who owns the resolution, a person, not a company. If I have those six things, I can decide in about a minute. Usually I have three of them and I spend my morning finding the other three.

**Interviewer (C7 probe):** What do you get wrong most often?

**Priya:** Timing. Things move after I pull the data, like the August test. And I miss informal changes, where an EPC super decides at 6 a.m. to put a crew somewhere that's not in the lookahead. The exclusion-zone overlaps I do by hand on the plot plan PDF, with colored polygons. It's embarrassing, honestly, for a $6.5B project, but I haven't found anything that does it with our data.

**Interviewer (C8):** Tell me about a time a report or instruction was passed along *automatically* or by someone who didn't know the area well. How did people react?

**Priya:** Two examples. The e-permit system sends automatic notifications to an area authority distribution list. When Train 1 was handed over from construction to commissioning, the distribution list wasn't updated for about three weeks. So permit notifications for Train 1 kept going to EPC construction people who no longer had authority there. They ignored them, because they get a few hundred a day and they had set up email rules to file them. Commissioning didn't get them at all.

The second one is mine, and I'm not proud of it. I built a Power Automate flow that emailed the SIMOPS matrix to about sixty people every morning. I checked the read receipts after a month. About eight people were opening it. So automation reached people, but it didn't make them read it.

**Interviewer (C8 probe):** What would make you trust or ignore an automatically routed item?

**Priya:** Trust: it's specific to me and my area, it has a permit number or a line number I can click and verify in the source system, it has an exact location, and there's a clear owner. If it's right nineteen times out of twenty, I'll read it.

Ignore: if it's generic, if it's noisy, or if it's wrong about something that matters even once. If it routes a live-gas item to the wrong person once and that person sits on it, I'm done with it, and I'll tell everyone why. On this kind of site, trust is lost on the one bad item, not the average.

**Interviewer (C9):** Describe the last time two crews or contractors needed the same space, equipment or permit window at the same time. How was it discovered and resolved?

**Priya:** That's every day for me. The last one that escalated was last Tuesday. The EPC had a heavy lift planned over the Train 2 rack, a large cold box component on a crawler. The lift path and exclusion zone overlapped a commissioning N2 purge on a subsystem underneath. I found it on the matrix Monday morning. At the 14:00 meeting on Monday the EPC wouldn't move the lift, because the crane was booked and it's expensive standby. Commissioning didn't want to move the purge because it was holding up a loop check sequence. I escalated to my CM Monday evening. He called the EPC construction manager. The lift moved to Wednesday.

**Interviewer (C9 probe):** How often does that happen in a week?

**Priya:** The matrix flags maybe fifteen to twenty-five overlaps a week. Most of them we resolve by time separation in the meeting, one crew mornings, the other afternoons. Two to four a week need a real resequence. One or two a month go up to my CM. And then there are the ones I don't see, like August, which is what I actually worry about.

**Interviewer (C9 probe):** What did it cost in time? Who "owned" the conflict?

**Priya:** The lift moved a day. The EPC will send a notice claiming crane standby, and it'll be argued about. Commissioning lost about half a shift re-planning. Owner of the conflict: on paper, the area authority for Train 2. In practice, me, until my CM took it.

**Interviewer (C10):** Tell me about the most recent stop-work, permit revocation or safety stand-down you were affected by. What led up to it, and what did it cost the schedule?

**Priya:** About three weeks ago in Train 1. A fixed gas detector alarmed near a flange on a system that commissioning had just brought into service. Early ops declared it, and per procedure all hot work permits in Train 1 and the interface area with Train 2 were suspended. It turned out to be a minor fugitive leak at a flange that needed re-torquing. It was about nine hours before permits were reinstated, after the leak was fixed and the area was gas-tested.

**Interviewer (C10 probe):** Was the hazard known beforehand? By whom?

**Priya:** Partly, yes, and that's the uncomfortable part. A commissioning tech had noticed the flange "sweating" on the previous shift, frost at the joint, and mentioned it verbally to an operator. It didn't make the shift log as an action. If it had been handled on that shift, it would have been a torque job with an isolation, not a nine-hour suspension. So again: known, spoken, not captured.

**Interviewer (C10 probe):** How is that cost tracked, if at all? LDs?

**Priya:** The EPC's daily report records lost hours. Roughly 350 craft had hot work suspended and had to be reassigned or stood down, so they'll call it several thousand craft hours, part of which they'll claim wasn't their fault. Commissioning lost about two days on that system. How it's tracked on our side: delay notices from the EPC go to the owner's commercial team. Nobody converts it into float consumption on the critical path in a way I see. There are LDs in the EPC contract tied to train substantial completion, and they're large. I've heard a number and I won't quote it. But a nine-hour suspension is almost never traced through to LD exposure. It gets absorbed and argued about at the end.

**Interviewer (C11):** When a hazard sits on the line between two employers, e.g. your crew spots it and another company created it, how does it get closed, and who proves it's closed?

**Priya:** The temp power in the classified area is the cleanest example. The hazard was the EPC electrical sub's equipment and the scaffold contractor's lighting, in an area owned by our commissioning team, with gas in. Closing it meant one contractor removing, another re-routing, and our area authority confirming.

Who proves it's closed? The EPC HSE coordinator closes it in their system with a photo. I can't see that system directly. We get a monthly export. So in practice I proved it closed by walking it, and I recorded that in my Power Apps tracker. Two different records, and they didn't agree for about a week, because the EPC closed it when the first spider box came out.

**Interviewer (C11 probe):** Which tools help or don't?

**Priya:** The e-permit system helps with permits and nothing else. It's not built for hazards. The EPC's safety system covers their scope only. Teams is where the conversation happened, with no structure. My tracker has the right structure but only owner staff can use it. Nothing covers the whole interface.

**Interviewer (C11 probe):** What would an owner or lawyer ask to see?

**Priya:** When it was first known and by whom. What permits were active in that area during the time it was open. Who was assigned, when, and how closure was verified, by a person, in the field, with evidence. And that the record wasn't edited afterward. An audit trail. If there's a loss-of-containment event and a crew was working there under a permit, the first question will be "did anyone know about this hazard before, and what was authorized in that area while it was open?" Right now I could answer that, but it would take me a week of reconstructing from Teams, emails, permit logs and my tracker.

**Interviewer (C12):** How are tools for the site's safety or field coordination paid for today? Whose budget, per what unit (worker, seat, project, month), and who has to sign?

**Priya:** I don't hold budget, to be clear. My CM has a tools budget of roughly $250k a year, which is owner's cost. It covers things like P6 licenses for owner staff, the drone progress survey service, some document control add-ons, a few specialty software seats. Most of it is per-seat or per-service. I make recommendations into it, and he usually listens, but he signs.

The EPC's safety tools, their observation module, their HSE software, are the EPC's cost, in their contract price. We don't pay for those directly and we don't control them. The e-permit system was specified in the EPC contract, and the EPC administers it.

Above what the CM's budget can carry, it goes to the Project Director. And anything that touches the site network, runs on devices in the field or stores data in the cloud goes through the owner's IT and OT cybersecurity review. For an LNG facility that review is serious.

**Interviewer (C12 probe):** What was the last safety-related purchase and how long did approval take?

**Priya:** We put live permit-board displays in the permit office and the commissioning trailer, basically screens showing the e-permit status in real time. About $40k all-in with the integration. Four and a half months from request to install, and most of that was the cyber review, because it touched the e-permit system's data.

**Interviewer (C12 probe):** What happens when crews turn over weekly?

**Priya:** At peak the EPC was badging two to three hundred new workers a week. Per-seat licensing for craft from the owner side isn't realistic. Nobody would administer it. When the EPC moved their cards to a login-based module, that's exactly what broke. Owner staff seats are stable, about 150 of us. Craft is 4,000-plus and changing all the time.

---

## Section 3: Concept Presentation & Willingness-to-Pay

**Interviewer (Concept):** I'm going to read a short description of a concept, and then ask for your reaction. "Some teams are testing a tool where any worker can report a hazard by voice, photo or text in their own language, in about the time it takes to send a text. The system suggests a category, severity and responsible owner. A human safety reviewer confirms or edits it before it goes anywhere. The owner sees one queue of open items. The reporter is notified when it's verified closed. It can also answer 'what's the rule here?' with the source cited. It's priced per project, not per user."

**Priya:** Can you read the middle part again? From "the system suggests."

**Interviewer (Concept):** "The system suggests a category, severity and responsible owner. A human safety reviewer confirms or edits it before it goes anywhere."

**Priya:** Okay. Thanks.

**Interviewer (P1):** In your own words, what would this change about your week, if anything? What wouldn't it change?

**Priya:** What it could change is the August problem. If the pipefitter's radio call, "there's a weld going on inside a test barricade in bay 14," became a structured record with a location and a timestamp that reached me before the 14:00 meeting, instead of reaching me as a lunch story on Friday, that is exactly the signal I've been missing. Same with the flange. A commissioning tech saying "flange sweating on subsystem so-and-so" by voice, in ten seconds, and it being captured.

What it wouldn't change, unless it plugs in: my matrix, the e-permit system, the 14:00 meeting, the lookahead. It sounds like it's built around HSE observations. My world is permits, schedule and system state. A hazard report that doesn't know which permits are active at that location, or which systems are live, is just a better photo in a different inbox. I'd still be the one translating it.

**Interviewer (P1 probe):** Can you give me an example of what "plugs in" would mean to you?

**Priya:** A report comes in with a location. It resolves that location to the e-permit location tree and shows me the active and planned permits there. It knows if that location is inside a classified area or an active test exclusion zone. It lets me link the report to a P6 activity in the lookahead. And the output is a row: conflict, location, affected permits, owner of resolution, due date. If I can pull that into my matrix, or better, it replaces the manual overlap check for field-raised items, that changes my week. If it's another dashboard I have to look at, it doesn't.

**Interviewer (P2):** What worries you about it? What would make you, or your crew, refuse to use it?

**Priya:** Several things. I'll go in order of how much they worry me.

First, "what's the rule here with the source cited." That one scares me the most. If a crew asks "can I do hot work here" and it finds a generic hot work procedure, or a superseded revision, and says yes, with a citation, that's how someone gets hurt, and the citation makes it look more trustworthy. The answer to "can I do hot work here" is never in a procedure. It's in the permit, the gas test, the SIMOPS matrix and the area authority. I've seen these tools hallucinate. If it ever hallucinates a permit, or implies authorization, it's over. On this site it would have to refuse permit questions outright, or read the live e-permit status and say clearly where it got it. And the documents it cites have to be the controlled revisions from document control, not whatever PDF someone uploaded.

Second, devices. Half my interface problems are in classified areas. The only phones allowed there are intrinsically safe. If it doesn't run on the IS devices we've been issued, and work with gloves and with compressor noise, then it doesn't exist in the areas that matter most. Crews will use it in the laydown yard and not in the unit.

Third, a second source of truth. If this creates a parallel record of hazards next to permits, and they disagree, which one do people follow? For process safety, two sources of truth is worse than one imperfect one. It has to be clear that it's a signal and the permit system is the authority.

Fourth, the human reviewer. Who is that at 2 a.m.? Night shift is exactly when my conflicts get missed. If the reviewer is a day-shift HSE coordinator, a night-shift report sits there until 7. That's the same gap as today.

Fifth, data integrity. Duplicates, locations that don't resolve, AI-suggested owners that are a company rather than a person. And audit: can a record be edited after the fact, and is that logged?

Sixth, contractual and cyber. The EPC may not want the owner seeing their raw hazard data in real time. That's a commercial conversation, not a technical one. And our cyber review will want to know where the data lives, who can access it, and whether anything touches OT.

**Interviewer (P2 probe):** What would make you, or the crews on your site, refuse to use it?

**Priya:** Me, the hallucinated-permit scenario. One instance and I'd push to shut it off. For crews, if it's seen as the owner watching them, or if it needs a login. The EPC's card module already taught them that. And if they report something and never hear back, they'll stop within a month, same as the cards.

**Interviewer (P3):** Who on your site would use it most, and who would ignore or resist it?

**Priya:** Use it most: mechanical and pipefitting crews, because they're in the racks at the interfaces and they already radio things. Commissioning techs, because they're walking systems constantly. Some EPC HSE coordinators, if it saves them transcribing cards. And me, obviously, as a consumer of the output.

Resist: EPC construction management, if it gives the owner real-time visibility into things they'd rather manage internally. The EPC HSE manager, if it competes with their system, which it would. Early operations for Train 1 will not put anything into a system that isn't part of their PSM and MOC-controlled tools. They have their own shift log and they're right to protect it. And some of the older area superintendents will just not open it, like my matrix email.

**Interviewer (P3 probe):** Why would operations resist in particular?

**Priya:** Because once a unit is operating under PSM, every change and every record has a controlled process. An uncontrolled tool that suggests severity and owners on an operating unit is a compliance question for them. They'd need to see it defined as an input to their process, not a replacement for any part of it.

**Interviewer (P5):** Imagine two ways to pay: (a) a project-level subscription at $24,000 per project-year, sized for a resident core team of about 200 people, all employers included, or (b) traditional per-seat licensing at about $10 per user per month. How would each land with you, and why?

**Priya:** Does the 200 include craft? Or is that owner and contractor staff?

**Interviewer (P5):** It's sized for about 200 resident users. I don't have more detail than that.

**Priya:** Okay. Then my reaction to (a) is that $24,000 is noise on a $6.5B project. It's less than the permit-board screens cost us. My CM could approve that out of the tools budget without thinking hard. But honestly, the price would make me more suspicious, not less. At that price I'd wonder who's doing the e-permit integration, who's supporting the IS devices, who's getting it through our cyber review. And 200 people doesn't match my site. Our owner team is about 150. The people who see the hazards are the 4,000 craft. If it's 200 residents, it covers the reviewers and the supervisors, not the people with the information. So it's cheap for the wrong scope.

(b), per seat: at $10 a month, if you licensed all the craft, 4,000 times $10 times 12 is, what, $480,000 a year, with turnover making the count a moving target. Nobody would pay that and nobody would administer it. If you only licensed owner staff, it's about $18,000 a year, similar to (a), and it has the same scope problem. Per seat just doesn't fit a site where two or three hundred people badge in every week. I'd push against per-seat regardless of price.

**Interviewer (P5 probe):** Why would per-seat be a problem even at a lower total?

**Priya:** Because the moment a license is per person, someone has to decide who gets one. And the answer will be supervisors, because they're stable and cheaper to administer. Then the pipefitter in the rack doesn't have access, and you've rebuilt the current system where the information stops at the foreman.

**Interviewer (P5b):** Another version being considered is $150,000 per project-year, for the full site, all employers, all crews. How does that compare?

**Priya:** That's more consistent with the scope I'd actually need. Full site, all crews, that's the version that addresses my problem. The $24,000 one doesn't.

But $150,000 is sixty percent of my CM's tools budget. That's the issue. It wouldn't come out of our budget alone. It would have to go to the Project Director as an owner's cost, or get pushed into the EPC's HSE scope through a change, and the EPC would price that change with markup. For $150,000 I'd also expect the integration work to be included, e-permit and at least the P6 lookahead linkage, and the IS device support. If those are extra, it's more than $150,000 in reality.

I'd also want to be careful here. I'm not the buyer. I'd tell you what I'd recommend, but my CM and the Project Director decide, and they'd be comparing it to other things that money could do.

**Interviewer (P5b probe):** What would it depend on, whether $150,000 is reasonable?

**Priya:** Whether it actually closes the field-to-permit gap and stops being another inbox. If it catches one August-type event early, that's worth far more than $150,000 in process-safety terms. But I can't take "it might catch an event" to my CM as a business case. I'd need pilot data.

**Interviewer (P6):** At what annual price per project would this be so cheap you'd doubt it? A bargain? Getting expensive but still worth considering? Too expensive, no matter what?

**Priya:** I'll answer for the full-site version, all employers, including the integrations I described. That's the only version I'd recommend.

So cheap I'd doubt it: under about $20,000 a year. At that price I'd assume there's no real support, the integration is on us, and it won't survive a cyber review.

A bargain: around $60,000 a year. That's something my CM could probably carry in the tools budget with some trade-offs, and it's an easy recommendation if the pilot works.

Getting expensive but still worth considering: around $120,000. At that point it's a Project Director conversation and I'd need hard pilot numbers.

Too expensive, no matter what: about $175,000 and up. Not because it couldn't be worth it on a project this size, but because at that level it's competing with real things, and for something unproven on our site it wouldn't get through. For us, at least.

**Interviewer (P6 probe):** Would those numbers change if the integrations weren't included?

**Priya:** Yes, down. Without e-permit integration, it's a better observation card. I'd put bargain at maybe $30,000, and too expensive at around $80,000, because then we'd be paying someone separately to integrate it, or I'd be doing it myself in Power Automate on weekends, which I'm not going to do again.

**Interviewer (P7):** Which budget line would it come from, and what would it need to replace or prove to get funded? What evidence after a 12-week pilot would get you to sign?

**Priya:** Budget line: first choice, the CM's tools budget, if it's under about $75,000. Above that, owner's project cost through the Project Director, possibly under HSE or commissioning support. Getting the EPC to pay isn't realistic mid-contract without a change order.

What it would replace: my Power Apps tracker, probably. Part of the Teams chaos. Maybe the photos of the permit board. It would not replace the e-permit system, P6, the EPC's HSE system, or the 14:00 meeting, and anyone who tells my CM it will replace the permit system will lose the room.

What it has to prove, after twelve weeks, in one area, say the Train 2 rack interface with commissioning:

One, the number of field-raised SIMOPS-relevant items that reached the matrix or the 14:00 meeting that would otherwise have reached me late or not at all. I'd want to compare against a baseline, say the prior twelve weeks from my tracker and permit logs.

Two, time from the field observation to the permit issuer or area authority knowing. Today it's hours to days. I'd want that in minutes for anything touching an active permit or a live system.

Three, zero hallucinated permit or rule answers in an audit of a sample. I'd audit it myself, a couple of hundred questions, including trick ones.

Four, the reviewer acceptance rate on suggested category and owner, and how often the suggested owner was a named person versus just a company.

Five, participation by EPC and subcontractor craft, not just owner staff, and whether it holds up in weeks nine to twelve, not just the first three. The card program looked great for three weeks.

Six, it works on the IS devices in the classified area, with gloves on, near the compressors.

And it has to pass our cyber review before the pilot, not after. If it can't get through that, the rest doesn't matter.

**Interviewer (P7 probe):** Who would have to sign, in practice?

**Priya:** My CM for the pilot, if it's small. The Project Director for a full-year contract. IT and OT cyber has an effective veto. And practically, the EPC construction manager has to agree to let their crews use it, or it's a pilot on 150 owner staff, which proves nothing.

**Interviewer (P9):** Anything I should have asked but didn't? Who else should I talk to?

**Priya:** You didn't ask about night shift, and you should. Most of my misses happen on nights or across shift handover. And ask about management of change. When area classification changes, or a system goes from construction to commissioning to operations, the ownership and the rules change. Anything that routes to an owner has to know which phase an area is in, on that day.

Who else: an EPC permit coordinator, ideally a night-shift one. An area authority on the commissioning side. The EPC HSE manager, who'll tell you why they don't want this. Someone from early operations on an operating train. The owner's OT cybersecurity lead, early. And honestly, a pipefitter, like the one who made the radio call in August. He's the one it's supposed to be for.

**Interviewer (Close):** Thank you for your time.

**Priya:** Sure. If you want the anonymized version of my matrix fields to see what structured output I mean, I can describe them, but I can't send the file.

**Interviewer (Close):** Understood. Thank you.

*[End of transcript]*
