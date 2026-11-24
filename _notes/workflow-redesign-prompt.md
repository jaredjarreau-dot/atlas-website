---
title: "The Workflow Redesign Prompt: A Fresh Route From Inputs to Output"
seo_title: "Workflow Redesign Prompt for AI Job Redesign"
slug: workflow-redesign-prompt
date: 2026-12-11
summary: "A free, copy-and-paste AI prompt: give it a workflow's inputs and output, and it proposes a simpler route, flags tasks to cut, and suggests how much AI each task should get."
seo_description: "A free AI prompt that proposes a simpler workflow from its inputs and output, flags tasks to cut, and suggests how much AI each task should get."
---

This prompt gives an AI tool a workflow's inputs and its output, without today's route, and asks for a fresh way to get there. It flags tasks that don't add value, and suggests how much AI each remaining task should get, using the six levels from the [Find the Balance Point](/field-notes/find-the-balance-point.html) decision tree. Paste it into any AI chat tool and replace the [brackets] with your own content.

<style>
.sg-prompt { position: relative; margin: 28px 0 36px; border: 1px solid var(--card-border); border-left: 4px solid var(--gold); border-radius: 6px; background: #F7F5F2; }
.sg-prompt pre { margin: 0; padding: 56px 24px 24px; white-space: pre-wrap; word-wrap: break-word; font-family: 'SFMono-Regular', Menlo, Consolas, monospace; font-size: 14px; line-height: 1.6; color: var(--text); }
.sg-copy { position: absolute; top: 12px; right: 12px; padding: 8px 18px; border: none; border-radius: 4px; background: var(--navy); color: var(--white); font: 600 14px 'Helvetica Neue', Helvetica, Arial, sans-serif; cursor: pointer; }
.sg-copy:hover, .sg-copy:focus-visible { background: var(--gold); outline: none; }
@media (max-width: 600px) { .sg-prompt pre { padding: 56px 16px 16px; font-size: 13px; } }
</style>

<div class="sg-prompt">
<button type="button" class="sg-copy" data-target="sg-prompt-text" aria-label="Copy the prompt to your clipboard">Copy prompt</button>
<pre id="sg-prompt-text">You are an experienced work-design consultant. I'm redesigning one workflow and want a fresh way to get from the inputs to the output. Don't copy how we do it today.

WORKFLOW
- The output it must deliver: [the output, and what "good" looks like]
- The inputs it starts from: [the information, systems and people involved]
- How we do it today (optional, for comparison only): [the current steps]
- Constraints: [rules, compliance, budget, the tools we have]

YOUR TASK
1. Ignoring today's route, design the simplest workflow that turns these inputs into this output.
2. List the tasks in your workflow. For each, say whether it adds value to the output. Mark any task you would cut or combine, and why.
3. For each remaining task, suggest how much AI it should get, using these six levels, from the most AI to none:
   - Observer: AI runs it on its own; a person monitors
   - Approver: AI does it; a person handles the exceptions
   - Consultant: AI leads and checks in at key moments
   - Collaborator: a person and AI plan and do it together
   - Operator: a person directs; AI acts only when asked
   - Practitioner: no AI; a person does it
   Give one line of reasoning for each, starting from Observer and stopping at the first level that keeps the work good and safe.
4. Name the risks: where a mistake could go uncaught, what data the AI would need (and whether it's good enough), and what a person must still own.
5. If I gave you today's steps, compare: what's simpler, what's faster, and what's riskier.

Keep it to one page. If something important is missing, ask me before you answer.
- End with exactly this line: "This is a starting point. The people who do the work today should review it before anything changes."</pre>
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

This prompt gives you a brainstorm, not a decision. You're still accountable for the process, and you judge whether the solution works.

1. **Check the output first.** If the AI changed what the workflow delivers, start over. The output is the point.
2. **Question every cut.** Some tasks exist for a reason the AI can't see: a regulation, a customer promise, an audit trail.
3. **Walk the levels yourself.** Use the AI's suggested level as a starting point, then run each task through the decision tree with the people who do the work.
4. **Check the data.** An AI-heavy workflow is only as good as its inputs. If the data isn't ready, that task steps back a level for now.
5. **Run the three checks.** Before you finalize, test the plan for the all-in cost, scale and urgency, and risk and governance. See [Before You Finalize the Plan](/field-notes/before-you-finalize-the-plan.html).
6. **Test before it goes live.** Run the new workflow alongside the old one and check every output first.
7. **Keep it confidential.** NEVER paste employee names, pay, client data or other personal information into a public AI tool.

## What comes next

Once the workflow is redesigned, map the skills the new role needs with the free [Skills Gap Prompt](/field-notes/skills-gap-prompt.html).

*Built for the AI Ready RVA HR Cohort workshop, December 11, 2026.*
