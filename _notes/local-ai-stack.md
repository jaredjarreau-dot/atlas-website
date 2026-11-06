---
title: "The Case for Keeping Client Data Local"
slug: local-ai-stack
date: 2026-05-26
summary: "How an HR consultant rebuilt his workflow around data security, local models, and hardware he already owned — and why keeping client data off the cloud is a professional obligation."
---

I am not a software engineer. My background is in HR and compensation consulting — the work of designing pay structures, building skills frameworks, and advising organizations on their most sensitive workforce decisions. It is, almost by definition, work that touches the most confidential data a company holds.

About a year ago I started experimenting seriously with AI tools. I was not an early adopter — I watched the first wave from the sidelines, skeptical of the hype. What changed was simpler than a philosophical shift: I figured out how to use these tools without compromising the data I am responsible for protecting. That realization opened a door I have not stopped walking through since.

AI is now woven into the vast majority of my workflow. What I want to share here is not a pitch for any particular tool. It is the framework I landed on after a year of trial, error, and some genuine rethinking about what responsible AI use actually looks like in practice.

## How It Started: A Practical Problem

The first version of my AI workflow was straightforward and wrong. I was running client work — compensation models, benchmarking analyses, workforce strategy documents — through cloud tools because they were fast, capable, and right there. The productivity gains were real. So was the friction: I kept hitting token limits mid-analysis on my Pro subscription, losing thread on complex work at exactly the wrong moment.

The token ceiling was annoying. What it forced me to do was more important: slow down and think about the architecture.

Every query I sent was a round trip to a data center I do not control, processed by infrastructure maintained by companies whose business model is shaped by the data that flows through them. For personal productivity tasks, that is a reasonable tradeoff most people make without thinking twice. For client compensation data — salary bands, individual pay decisions, organizational restructuring scenarios — it is a choice that deserves a lot more deliberation than I was giving it.

That realization was the genesis of what I now think of as a hybrid, sovereignty-first approach to AI.

## The Stack

I want to be specific here, because the accessibility of this setup is part of the point.

**Claude Code** serves as my dedicated AI companion for complex synthesis and reasoning — the work where cloud compute is genuinely warranted and the material I am sharing is appropriate to share. Strategic thinking, writing, novel problem-solving, research synthesis. This is where the ceiling of frontier models matters and where I use them deliberately.

**Ollama** running **Qwen 2.5 Coder 32B** and **Llama 3** handles everything routine, repetitive, and sensitive. Ollama is a free, open-source tool that runs large language models directly on your machine — no internet connection, no cloud endpoint, no external data transmission. Client data processed through this stack never leaves the device. It cannot become training data for someone else's model. All free to download and run.

**Notion** serves as the central intelligence hub. A library of custom Python scripts writes back to it continuously — feeding a live Control Room with hourly AI-generated briefings, auto-prepared research for booked client calls, weekly financial summaries, and a full log of project activity. Notion is where the automation outputs land and where I actually operate day to day. It functions as both the interface and the long-term memory of the whole system.

The **Python scripts** themselves handle the autonomous daily work: email triage, calendar management, financial data sync, meeting prep, weekly briefing synthesis. Most of this runs on a local schedule overnight or while I am in meetings. I now understand roughly a quarter to half of what is happening inside each one and can make basic edits — but the heavy lifting is done by Qwen, locally, on the machine.

All of this runs on a **used M1 MacBook I bought for around $800** a few months ago. That detail matters. You do not need a new machine. You do not need an enterprise software budget. The M1 chip handles a 32-billion parameter model efficiently enough for real daily work. The barrier to this setup is one afternoon and a willingness to think clearly about your workflow — not thousands of dollars in new hardware.

## The Bigger Concern

My most recent thinking on this was shaped by something I did not expect: the younger generation's pushback on AI.

I hear them. I share more of those concerns than I initially admitted to myself, particularly around the environmental cost of the infrastructure being built to support the current AI moment. The data center buildout underway in 2026 is extraordinary — billions in capital expenditure, enormous energy consumption, significant water usage for cooling, strain on electrical grids in communities that did not sign up for it.

A meaningful share of that capacity is serving workloads that a four-year-old laptop can handle locally without breaking a sweat.

I am not arguing against AI. I use it constantly and it has made me meaningfully more capable. I am arguing for using it with the same intentionality I try to bring to everything else. Cloud compute when it is genuinely warranted. Local compute when it is not. Deliberate routing rather than reflexive convenience. That discipline is, I think, both a better professional practice and a better collective habit.

## What I Would Want Other Practitioners to Take Away

If you work in HR, consulting, law, finance, or any field where client confidentiality is foundational: the data you handle did not consent to becoming training data. Your professional obligations predate the AI era and still apply within it. The tools to protect that data while using AI effectively are free, accessible, and work on hardware most of us already own.

The setup I have described took time to build and required learning I did not have a year ago. It was worth every hour. The work feels more secure, the automation runs more reliably than a strained Pro subscription ever did, and I operate with full confidence that client data is exactly where it belongs.

I am genuinely curious how others in professional services are approaching this — the data sovereignty question especially. I would genuinely like to hear how you are navigating it — drop a note or book a conversation below.
