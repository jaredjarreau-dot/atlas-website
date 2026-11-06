---
title: "The Skills Gap Prompt: Redesigning a Role Without Leaving People Behind"
slug: skills-gap-prompt
date: 2026-12-11
summary: "A free, copy-and-paste AI prompt that compares a current job description with the redesigned role, shows the skills gap, and suggests how to develop the people in the role today."
---

This prompt compares a current job description with the redesigned version of the role. It identifies the skills and proficiency levels the new role needs, shows the gap, and suggests ways to develop the people in the role today. Paste it into any AI chat tool and replace the [brackets] with your own content.

<style>
.sg-prompt { position: relative; margin: 28px 0 36px; border: 1px solid var(--card-border); border-left: 4px solid var(--gold); border-radius: 6px; background: #F7F5F2; }
.sg-prompt pre { margin: 0; padding: 56px 24px 24px; white-space: pre-wrap; word-wrap: break-word; font-family: 'SFMono-Regular', Menlo, Consolas, monospace; font-size: 14px; line-height: 1.6; color: var(--text); }
.sg-copy { position: absolute; top: 12px; right: 12px; padding: 8px 18px; border: none; border-radius: 4px; background: var(--navy); color: var(--white); font: 600 14px 'Helvetica Neue', Helvetica, Arial, sans-serif; cursor: pointer; }
.sg-copy:hover, .sg-copy:focus-visible { background: var(--gold); outline: none; }
@media (max-width: 600px) { .sg-prompt pre { padding: 56px 16px 16px; font-size: 13px; } }
</style>

<div class="sg-prompt">
<button type="button" class="sg-copy" data-target="sg-prompt-text" aria-label="Copy the prompt to your clipboard">Copy prompt</button>
<pre id="sg-prompt-text">You are an experienced compensation and job-architecture professional. I'm redesigning a job and need to understand how the skills change, and how to help the people in the role today develop the skills to be successful.

CURRENT JOB DESCRIPTION
[paste the current job description]

REDESIGNED ROLE
- Outputs this role delivers: [3-4 outputs]
- Tasks that stay with a person: [list]
- Tasks moving to AI, automation, contractors or another role: [list]

Use this proficiency scale throughout:
- Basic: does the task with guidance or a checklist
- Working: does it independently in routine situations
- Advanced: handles complex or unusual cases and coaches others
- Expert: sets the standard others follow; rare below senior or specialist roles

Please do the following.

1. Skills for the redesigned role. Name the closest O*NET occupation, with its SOC code. List the 6-8 most important skills for the tasks that stay with a person, using O*NET names where they fit. At least half must be specific to this job's work (knowledge areas, technical skills or tools), and no more than two can be general skills like communication or critical thinking. Calibrate levels to the role: for most non-manager roles, most skills should be Basic or Working. Table columns: Skill | Task it supports | Importance (1-5) | Level needed | What that level looks like here (one sentence) | Confidence (High, Medium or Low).
Include an AI skill only where a task uses an AI tool, and say what the person must be able to do with it.

2. The gap. Using the same skill names and scale, rate the level the current job description requires. In one table show: Skill | Current level | Needed level | Change (New, Higher, Same, Lower or No longer needed). Include skills from the current job that drop out.

3. Development plan for the people in the role today. For each New or Higher skill: Skill | Approach (on-the-job practice, mentoring or shadowing, a short course, a certification, or a project assignment) | Time to reach the needed level | Priority (High, Medium or Low). Then add one line that starts "Carry-over skills:" naming the skills marked Lower or No longer needed that could be used in another role.

Rules:
- Don't add degrees, years of experience or certifications unless a task truly or legally requires one. If you do, explain why.
- Use neutral, inclusive language.
- Keep the whole answer under 700 words. Tables only, plus one short sentence before each table.
- If you're not sure of an O*NET name or SOC code, say so in the Confidence column.
- End with exactly this line: "This compares two jobs, not people. Confirm each person's actual skills with them and their manager before acting on it."</pre>
</div>

<script>
document.querySelectorAll('.sg-copy').forEach(function (btn) {
  btn.addEventListener('click', function () {
    var text = document.getElementById(btn.dataset.target).innerText;
    var done = function () {
      btn.textContent = 'Copied!';
      setTimeout(function () { btn.textContent = 'Copy prompt'; }, 2000);
    };
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(done);
    } else {
      var ta = document.createElement('textarea');
      ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
      document.body.appendChild(ta); ta.select();
      try { document.execCommand('copy'); done(); } finally { document.body.removeChild(ta); }
    }
  });
});
</script>

## Review and edit before using

This prompt gives you a first draft, not an answer. Before you use the result:

1. **Check the occupation.** Look up the O*NET code it gives you at [onetonline.org](https://www.onetonline.org/). In testing, the AI tools sometimes picked the wrong occupation or code.
2. **Check the proficiency levels.** Are they realistic for this role, or inflated? AI tends to rate too many skills Advanced.
3. **Check what it says is "no longer needed."** AI sometimes drops work that didn't actually move, like opening the office or researching a briefing.
4. **Add what's missing.** The knowledge only someone who has done the job would know rarely shows up in a first draft.
5. **Cut what the work doesn't need.** Keep a degree, years of experience or a certification only if a task truly requires it.
6. **Confirm with people.** The prompt compares jobs, not people. Validate each person's actual skills with them and their manager before you build a development plan around them.
7. **Keep it confidential.** NEVER paste employee names, pay or other personal data online or into a public AI tool.

*Built for the AI Ready RVA HR Cohort workshop, December 11, 2026.*
