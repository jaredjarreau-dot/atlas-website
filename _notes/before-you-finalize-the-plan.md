---
title: "Before You Finalize the Plan: Three Checks for Any AI Redesign"
seo_title: "AI Job Redesign Checklist: Cost, Scale and Risk"
slug: before-you-finalize-the-plan
date: 2026-12-11
summary: "Part 3 of 3: checklists for the all-in cost, scale and urgency, and risk and governance of an AI redesign, plus how to test it before it goes live."
seo_description: "Before an AI job redesign goes live, check the all-in cost, scale and urgency, and risk and governance, then test it. Part 3 of 3."
---

<style>
.series { border-left: 4px solid var(--gold); background: #F7F5F2; padding: 14px 18px; margin: 22px 0 30px; font-size: 15px; line-height: 1.6; }
table { width: 100%; border-collapse: collapse; margin: 18px 0 30px; font-size: 15px; line-height: 1.5; }
th, td { padding: 10px 12px; border-bottom: 1px solid var(--card-border); text-align: left; vertical-align: top; }
th { background: #F7F5F2; color: var(--navy); font-weight: 600; }
td:last-child, th:last-child { text-align: right; white-space: nowrap; }
.check li { margin-bottom: 8px; }
@media (max-width: 600px) { table { font-size: 14px; } th, td { padding: 8px 6px; } }
@media print { header, footer, .cta, nav { display: none !important; } body { background: #fff; } }
</style>

<div class="series"><strong>Find the Balance Point, a three-part series.</strong><br>
Part 1: <a href="/field-notes/should-we-use-ai.html">"Should we use AI?" is an incomplete question</a><br>
Part 2: <a href="/field-notes/find-the-balance-point.html">Find the balance point, one task at a time</a><br>
Part 3: Before you finalize the plan (you're here)</div>

[Part 2](/field-notes/find-the-balance-point.html) gave every task a balance point. A balance point is a draft until it survives three checks: what it really costs, whether the volume and timing justify it, and what happens when it goes wrong. If a task loses one of these, step it back one level for now and revisit it later.

## 1. Economics: what's the all-in cost?

Compare today's cost with the redesigned cost. Count everything: tools, data cleanup, the time to check the work, and getting people ready. Budget for what AI will cost when prices rise, not today's introductory pricing.

<div class="check" markdown="1">

**Checklist**

- **Today's cost.** How many times a year does the task happen, how long does it take, and what does an hour of that person's time cost with benefits?
- **Tools.** Licenses, usage fees and any add-ons. What happens to the price at your volume next year?
- **Setup.** Data cleanup, integrations, writing the instructions, and the hours your people spend on it.
- **Checking the work.** The time a person spends reviewing output at the level you chose. This is the cost most plans leave out.
- **Getting people ready.** Training, and the slower weeks while people learn the new way.
- **The fallback.** What it costs to keep a manual process working for the day the tool is down.
- **Price rise.** Rerun the math with the tool costing 50% more. If the plan only works at today's price, it isn't a plan yet.

</div>

**A worked example (illustrative numbers).** A coordinator books 300 interviews a year at 20 minutes each, and an hour of their time costs $40 with benefits.

| Line | | Amount |
|---|---|---|
| **Today:** 300 interviews × 20 minutes = 100 hours × $40 | | **$4,000 a year** |
| Scheduling tool license | | $1,800 |
| Setup and calendar cleanup: 15 hours × $40 (first year only) | | $600 |
| Checking the work: 3 minutes × 300 = 15 hours × $40 | | $600 |
| Training: 4 hours × 2 people × $40 (first year only) | | $320 |
| **Redesigned, year 1** | | **$3,320** (saves $680) |
| **Redesigned, year 2 on** | | **$2,400** (saves $1,600) |
| **Year 2 if the license rises 50%** | | **$3,300** (saves $700) |

It still pays, but by less than the vendor demo suggests. The real win here may not be the money; it's the 100 hours. Where those hours go is the last question in this post.

## 2. Scale and urgency: how big is the workflow, and how quickly do we need to act?

A task that happens five times a year rarely justifies an agent; one that happens 500 times a week might. If something's broken today, it goes first.

<div class="check" markdown="1">

**Checklist**

- **Volume.** How many times a week or year does it happen? Is that growing?
- **Sameness.** How alike are the cases? High volume with lots of variation needs more people involved, not fewer.
- **Pain today.** Is it late, error-prone or burning someone out? Broken beats boring.
- **Deadline.** Is anything forcing the timing: a new law, a peak season, a person leaving?
- **Dependencies.** Does this task feed others? Fix the upstream one first, or you automate around a bad input.
- **Reversibility.** Can you switch back easily if it doesn't work? Easy-to-reverse changes can go sooner.

</div>

**Putting it in order.** Score each task high or low on volume and on pain today. High on both goes first. High pain, low volume often needs a better process more than it needs AI. Low on both waits.

## 3. Risk and governance: what happens if, or when, it goes wrong?

Are we compliant? Think about pay transparency, ADA accommodation, EEO and privacy. If you can't defend it, step back until a person signs off.

<div class="check" markdown="1">

**Checklist**

- **The failure.** What's the worst realistic mistake, who is affected, and how would you find out? If nobody would notice, that's your answer: step back a level.
- **The owner.** Name the person accountable for the output. "The system" is not an answer. A Canadian tribunal held Air Canada responsible for what its website chatbot told a customer (*Moffatt v. Air Canada*, 2024 BCCRT 149).
- **Pay transparency.** If the task touches job postings or offers, does it keep the pay range in every Virginia posting? Virginia's pay-range requirement took effect July 1, 2026.
- **Disability accommodation.** If a person is screened, scheduled or assessed by a tool, can they ask for an accommodation and reach a human?
- **Fair treatment (EEO).** If the task helps decide who gets hired, promoted or paid what, compare outcomes across groups and keep the records to show it.
- **Privacy.** What employee or candidate data goes into the tool? Where is it stored, how long, and does the vendor train on it?
- **Explainability.** Could you explain a decision to the person it affected, in plain English?
- **Records.** Can you show what the tool did and who checked it, months later?
- **The way back.** Is there a manual backup, and does someone still know how to run it?

</div>

This is a checklist, not legal advice. For anything that touches hiring, pay or accommodation decisions, bring in your employment counsel before go-live.

## Then: test before it goes live

Don't flip the switch on a new balance point. Test it exhaustively first:

1. **Set the bar in advance.** Decide what "good enough" means (accuracy, turnaround, complaints) before you look at results.
2. **Run it alongside the old way.** Do the task both ways for a set number of cases or weeks, and compare every output.
3. **Check the exceptions on purpose.** Feed it the unusual cases, not just the easy ones.
4. **Have the named owner sign off.** In writing, against the bar from step 1.
5. **Go live, keep watching.** Review a sample on a schedule, and keep the manual backup ready.

If it doesn't pass, step the task one level closer to the person and test again.

## One last thing: where does the freed-up time go?

By default, freed-up time doesn't go anywhere useful. Decide where it goes: the backlog, the hard cases, owning the AI's output, customers and colleagues, and learning. Then check the redesigned job against what makes work worth doing: variety, owning a whole piece of work, impact, agency, mastery and connection.

## Next step

For the work that stays with people, map the skills the redesigned role needs with the free [Skills Gap Prompt](/field-notes/skills-gap-prompt.html).

## Where this comes from

The six levels in Part 2 adapt Kevin Feng, David McDonald and Amy Zhang's ["Levels of Autonomy for AI Agents"](https://arxiv.org/abs/2506.12469) (2025). The start question in Part 1 owes a debt to Michael Hammer's 1990 *Harvard Business Review* article, "Reengineering Work: Don't Automate, Obliterate." The No AI level, the questions and these three checks are mine.

Built for the AI Ready RVA HR Cohort workshop, December 11, 2026.
