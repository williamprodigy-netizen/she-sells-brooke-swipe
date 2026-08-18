#!/usr/bin/env python3
"""Build the She Sells (Brooke) swipe site.

IMPORTANT: this is the AUSTRALIAN business, a separate company from Shelby Sapp's
She Sells Remote. Two different brands sharing a name and an ICP and nothing else.
Never merge the two — check the Facebook Page id when in doubt.

Run: python3 build_site.py
"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/SHE_SELLS_BROOKE_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/*.mp4"))):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     "The post-quiz VSL, fronted by Brooke."))
    return rows


CONFIG = {
    "SITE": "She Sells (Brooke) — Australia",
    "CREATOR": "She Sells — fronted by Brooke",
    "ADS_KEY": "she_sells_brooke",
    "FUNNEL_IDS": [],
    "CAPTURED": "1–2 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/SHE_SELLS_BROOKE_Swipe",
    "BLURB": "<b>NOT Shelby Sapp.</b> A separate Australian business running a quiz &rarr; "
             "VSL &rarr; application funnel at the same buyer we sell to: career women who "
             "want out of the 9&ndash;5. <b>143 active ads.</b>",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("transcripts.html", "VSL transcript"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("Country", "Australia"),
        ("FB Page", "130931930113119"),
        ("Active ads", "143"),
        ("VSL", "4m 27s"),
        ("Front", "Quiz opt-in"),
        ("Platform", "GoHighLevel"),
        ("Price", "not observed"),
        ("Registered", "yes"),
    ],

    "OFFER": [
        ("Product", "She Sells &mdash; remote/high-ticket sales career for women"),
        ("Presenter", "<b>Brooke</b>, a former teacher &mdash; the on-camera face is not "
                      "necessarily the business owner"),
        ("Promise", "Quit the 9&ndash;5, double income, work as little as 20 hours a week"),
        ("Positioning", "&ldquo;It&rsquo;s not just a program, it&rsquo;s a movement&rdquo;"),
        ("Path", "Quiz opt-in (first, last, email, phone) &rarr; 4:27 VSL &rarr; apply"),
        ("Also runs", "In-person events &mdash; a Perth live event ad scores 98 (&ldquo;Winning&rdquo;)"),
        ("Price", "<b>Not observed.</b> Nothing priced in the captured funnel"),
    ],

    "FINDINGS": [
        ("Not a Shelby Sapp duplicate &mdash; verified",
         "Same name, same ICP, and it nearly got filed as a duplicate on first pass. It is a "
         "<b>different company</b>: Shelby is <i>She Sells Remote</i> "
         "(shesellsremote.com, US); this is <i>She Sells</i> (shesells.online, Australia), "
         "Facebook Page <code>130931930113119</code>, running in-person events in Perth. "
         "<b>The Page id is the check.</b>"),
        ("The lead is emotional cost, not money",
         "The page opens on being stuck on a hamster wheel, guilty about not being present "
         "for family, chronically exhausted, stressed by bills &mdash; and only then "
         "introduces the offer. Income appears later. Worth comparing with how early we put a "
         "number in our own copy."),
        ("Teacher-to-freedom is the origin story",
         "Brooke frames herself as a former teacher on an average salary with someone else "
         "controlling her time. For a UK/AU/US audience of career women, teacher is among the "
         "most recognisable versions of &ldquo;respectable but trapped&rdquo;."),
        ("The MLM objection is named in the ad, not the funnel",
         "Their ad copy says outright <i>&ldquo;no MLM nonsense to sign up to&rdquo;</i> and "
         "&ldquo;no degree needed&rdquo;. They spend paid impressions killing the objection "
         "<b>before</b> the click, rather than handling it on the page."),
        ("Quiz first, VSL second, application third",
         "The quiz is a low-friction opt-in that also qualifies. Our funnel asks for the "
         "commitment earlier. A quiz collects the same contact details while feeling like the "
         "prospect is learning something about themselves."),
    ],

    "FUNNEL": [
        ("Quiz opt-in", "shesells.online/take-quiz463039",
         "First, last, email, phone on GoHighLevel. Registered."),
        ("VSL", "shesells.online/launch-your-salescareer434568",
         "4:27 Wistia VSL fronted by Brooke, then <b>CLICK HERE TO APPLY</b>."),
        ("In-person events", "shesells.online/perth-live-and-in-person-2026",
         "Live events in Perth, sold through a separate winning ad."),
    ],

    "TRANSCRIPT_GROUPS": [
        ("The VSL", sorted(glob.glob(os.path.join(PKG, "Transcript/*.md")))),
    ],

    "SLIDE_PAGES": [],
    "VIDEOS": video_library(),

    "ANALYSIS": """
<div class="warn"><b>Do not merge this with Shelby Sapp.</b> Two different companies share the
name &ldquo;She Sells&rdquo;. Shelby Sapp runs <i>She Sells Remote</i> in the US &mdash; the
$7,000 closer mentorship that is the textbook example in this swipe file. This is an
<b>Australian</b> business fronted by Brooke. Different country, different offer, different
Facebook Page, different funnel. Any analysis or copy bank that blends them is wrong.</div>

<h2 class="sec">Why they matter to us</h2>
<p>This is the closest ICP overlap in the entire file: career-driven women who want out of a
job, sold a remote sales skill and a promise of time freedom. They are running <b>143 active
ads</b> against that audience, so they are a live competitor for the same attention, not a
curiosity.</p>

<h2 class="sec">The copy order is the lesson</h2>
<div class="tablewrap"><table>
<tr><th>Their order</th><th>What it does</th></tr>
<tr><td>1. The feeling</td><td>Exhausted, guilty, stuck, stressed about bills</td></tr>
<tr><td>2. The recognition</td><td>&ldquo;Most women are never shown a way out&rdquo;</td></tr>
<tr><td>3. The person</td><td>Brooke, a teacher who left</td></tr>
<tr><td>4. The mechanism</td><td>A sales skill that can be learned</td></tr>
<tr><td>5. The number</td><td>Income, last</td></tr>
</table></div>
<p style="margin-top:12px">The money arrives after the identity has been sold. Our copy tends
to lead with the outcome figure, which asks the reader to believe a number before they believe
the story.</p>

<h2 class="sec">Worth taking</h2>
<div class="grid g2">
<div class="card"><h3>Kill the objection in the ad</h3><p>&ldquo;No MLM nonsense, no degree
needed&rdquo; runs in paid, before the click. Cheaper than handling it on the page, and it
filters who arrives.</p></div>
<div class="card"><h3>Try a quiz as the opt-in</h3><p>Same fields, less felt commitment, and
it qualifies while it collects. A quiz feels like self-discovery rather than a form.</p></div>
<div class="card"><h3>Sell the identity before the income</h3><p>Five beats before a number
appears. Ours is faster to the money and may be asking for belief too early.</p></div>
<div class="card"><h3>In-person events as a channel</h3><p>Their Perth live-event ad is one of
their best performers. Live events are a channel we have not touched at all.</p></div>
</div>

<h2 class="sec">Read carefully</h2>
<p><b>Who actually owns this business is unconfirmed.</b> Brooke fronts the VSL and describes
herself as a former teacher, but that does not establish that she owns the company. The
Facebook Page carries the brand name, not a person's.</p>
<p><b>No price is claimed</b> because none appears in the captured funnel. Figures spoken in
the VSL are described as outcomes, not as the cost of the program, and should not be repeated
as pricing.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
