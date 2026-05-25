import html, pathlib
pairs = [
 ("pair-1","Elaborate · Business · Choppy → cumulative",
  "The founder walked in. She was late. She was underslept. She was carrying three coffees.",
  'The founder walked in late and underslept, <span class="hl">three coffees balanced in two hands, her laptop bag slipping off one shoulder,</span> already apologizing to no one in particular.',
  "<b>The move:</b> four clipped sentences become one base clause with free modifiers trailing off it. The fix for choppy prose is a longer, well-built sentence, not a shorter one."),
 ("pair-2","Short · Marketing · Antithesis, not a triad",
  "Our platform is fast, it's secure, and it's also affordable.",
  '<span class="hl">Powerful enough for the experts who demand it, simple enough for the rest of us</span> who would rather not think about it.',
  "<b>The move:</b> the reflex is three flat claims. A weighted pair set in contrast carries more and sounds less like a checklist. Prefer the pair to the triad."),
 ("pair-3","Elaborate · Business · Left-branching for suspense",
  "We cut our price. We did it after losing three deals in one quarter to a competitor who undercut us.",
  '<span class="hl">After losing three deals in a single quarter to a rival who undercut us on every line,</span> we cut our price.',
  "<b>The move:</b> the circumstances build first; the decision lands at the end as the almost inevitable conclusion. The shape delivers the logic."),
 ("pair-4","Elaborate · Marketing · Cumulative with an absolute",
  "Our app tracks your habits. It sends you reminders. It shows your progress. It keeps you motivated over time.",
  'The app tracks your habits and nudges you when you slip, <span class="hl">a quiet mirror held up each morning, its streak counter ticking,</span> until the habit no longer needs the app at all.',
  "<b>The move:</b> one base clause carries an appositive (“a quiet mirror”) and a nominative absolute (“its streak counter ticking”), then lands the payoff. Four flat sentences could not build this arc."),
 ("pair-5","Short · Marketing · Syntactic symbolism (increase)",
  "The approval process kept getting more complicated and slower over time until it barely worked.",
  '<span class="hl">Step by step, approval by approval, sign-off stacked on sign-off,</span> the process grew until it could no longer move.',
  "<b>The move:</b> the accreting parallel phrases enact the pile-up they describe. The sentence gets heavier as the process does. Symbolism here is increase, not acceleration."),
 ("pair-6","Elaborate → short · Business · Short by contrast",
  "After a long process that involved many stakeholders and several rounds of review, the proposal was ultimately rejected by the committee.",
  'Months of review, a dozen stakeholders, three rounds of edits, two redesigns. <span class="hl">The committee killed it.</span>',
  "<b>The move:</b> the short sentence is loud only because the long one precedes it. Its power is the contrast, not the brevity. The opening list runs to four items to break the three-beat habit."),
]
def eyebrow(s):
    return s.replace(" · ", ' <span class="dim">·</span> ')
tpl = '''<!DOCTYPE html><html><head><meta charset="utf-8"><link rel="stylesheet" href="card.css"></head>
<body><div class="card">
<div class="eyebrow">{eb}</div>
<div class="grid">
<div class="col before"><div class="tag b">Before · default</div><div class="txt">{before}</div></div>
<div class="arrow">&#8594;</div>
<div class="col after"><div class="tag a">After · crafted</div><div class="txt">{after}</div></div>
</div>
<div class="move">{move}</div>
</div></body></html>'''
for pid, eb, before, after, move in pairs:
    out = tpl.format(eb=eyebrow(eb), before=html.escape(before), after=after, move=move)
    pathlib.Path(f"/tmp/sscards/{pid}.html").write_text(out)
print("generated", len(pairs), "cards")
