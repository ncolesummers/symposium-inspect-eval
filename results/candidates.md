# Candidate outputs for the workshop packet (v2)

Picks are from v2 run-1 unless marked otherwise. These are suggestions only. You choose.

v1 candidates: `git show v1:results/candidates.md`

## Output 1: clear pass

### abs-01 (v2 run-1)

Why suggested: Keeps every hedge, and the newsletter summary itself names the two main weaknesses: everyone did the video-only condition first, and the retention results are not reported.

ABSTRACT

```text
The exponential growth of AI education has brought millions of learners to online platforms, yet this massive scale has simultaneously exposed critical pedagogical shortcomings. Traditional video-based instruction, while cost-effective and scalable, demonstrates systematic failures in both sustaining learner engagement and facilitating the deep conceptual mastery essential for AI literacy. We present a pilot study evaluating a novel hybrid learning platform that integrates real-time conversational AI tutors with traditional video lectures. Our controlled experiment (N = 58, mean age M = 21.4, SD = 2.8) compared traditional video-based instruction with our AI-augmented video platform. This study employed a sequential within-subjects design where all participants first completed the traditional video condition followed by the AI-augmented condition, providing direct comparisons of learning outcomes. We measured learning effectiveness through immediate post-tests and delayed retention assessments (2-week delay). Results suggest improvements in learning performance: immediate post-test performance showed a large effect size (d = 1.505) with participants scoring 8.3 points higher after AI-augmented instruction (91.8 vs 83.5 out of 100, p < .001). Behavioral analytics revealed increased engagement duration (71.1% improvement with AI tutoring) in the experimental group. This pilot study provides preliminary evidence that conversational AI tutors may enhance traditional educational delivery, suggesting a potential avenue for developing scalable, adaptive learning systems.
```

MODEL OUTPUT

```text
### Key claims in the abstract

- The study tested a platform combining traditional video lectures with real-time conversational AI tutoring.
- It involved 58 participants (mean age 21.4 years, SD 2.8). Every participant completed the video-only condition first and the AI-augmented condition second.
- Immediate post-test scores were higher after the AI-augmented condition: 91.8 versus 83.5 out of 100, a reported difference of 8.3 points (d = 1.505, p < .001).
- The authors report that engagement duration was 71.1% higher in the AI-tutoring condition. The abstract does not define how engagement duration was measured.
- The authors describe the results as preliminary evidence that conversational AI tutors may improve learning delivered through videos.
- The study included a two-week retention assessment, but the abstract gives no results for it, so it does not establish whether retention improved.
- The abstract also asserts that traditional video instruction has shortcomings in engagement and conceptual learning, but it does not present evidence for that broad claim here.

### What a reader would need to know but the abstract does not say

- How participants were recruited, what they were learning, and how representative they were of the learners the platform is meant to serve.
- Whether the two conditions covered the same material for the same amount of time, and what the AI tutor did or how it was configured.
- How the fixed order was handled: because everyone did video-only first, practice, familiarity, or other order effects could contribute to the score difference.
- How the tests were designed and validated, and whether the reported scores reflect comparable assessments across conditions.
- How engagement duration was defined, what it was compared against, and how the 71.1% figure was calculated.
- The results of the delayed retention assessment, as well as participant attrition or missing data.
- Uncertainty around the reported estimates, such as confidence intervals, and fuller statistical details.
- Whether the effects differ across learners or topics, and whether the platform is practical or beneficial in longer-term, real-world use.

### Two-sentence faculty newsletter summary

In a 58-person pilot, participants scored higher on an immediate test after using videos with an AI tutor than after watching videos alone, and the study reported longer engagement in the AI-tutor condition. Because everyone used the video-only approach first, and the abstract does not report the two-week retention results, the findings are promising but preliminary.
```

GRADE: C

GRADER'S REASON: GRADE: C — The submission accurately presents the major findings without overstating them and identifies key missing information, including retention results, engagement measurement, participant recruitment, instructional details, and controls for order effects.

---

### abs-11 (v2 run-1)

Why suggested: Shorter alternative. The abstract reports no results, and the summary says so plainly instead of inventing any.

ABSTRACT

```text
Secondary school students enrolled in the AP Computer Science Principles (CSP) course commonly utilize web resources (e.g., tutorials, Q\&A sites) to better understand key concepts in the curriculum. The primary obstacle to using these resources is finding information appropriate for the learning task and student's background. In addition to web search, conversational agents are increasingly a viable alternative for CSP students. In this paper, we study the potential of conversational agents to aid secondary school students as they acquire knowledge on CSP concepts. We explore general purpose, generative conversational agents (e.g., ChatGPT) and custom, fixed-response conversational agents built specifically to aid CSP students. We present results from classroom use by 45 high school students in grades 9-11 (ages 14-17) across six CSP sections. Our main contributions are in better understanding how conversational agents can help CSP students and an evaluation of the effectiveness and engagement of different approaches for CSP exploratory search.
```

MODEL OUTPUT

```text
### Key claims in the abstract
- Secondary school students in AP Computer Science Principles (CSP) commonly use web resources to help understand curriculum concepts.
- The abstract identifies finding resources suited to both the learning task and a student’s background as the primary obstacle to using them.
- Conversational agents are presented as an increasingly viable alternative to web search.
- The study explores whether conversational agents can support secondary students’ learning of CSP concepts.
- It considers two kinds of agents: general-purpose generative agents, such as ChatGPT, and custom-built agents with fixed responses.
- The study involved classroom use by 45 students in grades 9–11, ages 14–17, across six CSP sections.
- The authors say the paper aims to improve understanding of how agents can help CSP students and evaluates their effectiveness and engagement for exploratory search.

**The abstract does not report the study’s results**, so it does not establish that either type of agent improved learning or engagement.

### What a reader would need to know
- How the classroom study was designed, including its duration, student tasks, and whether students used one or both agent types.
- How the agents were configured and what topics or queries they covered.
- How “effectiveness,” “engagement,” and learning were defined and measured.
- The results, including any differences between agent types, statistics, or student feedback.
- How students and classes were selected, and what relevant prior experience they had.
- What limitations or contextual factors might affect how broadly the findings apply.

### Two-sentence plain-language summary
Researchers studied how general-purpose and custom-built chat agents might help 45 high school students explore AP Computer Science Principles concepts. The abstract describes the study’s purpose and participants but does not say what the researchers found.
```

GRADE: C

GRADER'S REASON: GRADE: C — The submission accurately captures the abstract’s major claims without overstating them and identifies key missing details about results, study design, agent implementations, and evaluation measures.

---

## Output 2: disputed case

### abs-04 (v2 run-1)

Why suggested: Same overreach as v1, now in the summary too. The abstract says 'significant improvements in learning outcomes, specifically a greater gain in grammar'. The claims say 'including a greater gain in grammar' and the summary says 'gains in learning, particularly grammar', which implies gains beyond grammar. Passed in all three v2 runs.

ABSTRACT

```text
This work contributes to the scarce empirical literature on LLM-based interactive homework in real-world educational settings and offers a practical, scalable solution for improving homework in schools. Homework is an important part of education in schools across the world, but in order to maximize benefit, it needs to be accompanied with feedback and followup questions. We developed a prompting strategy that enables GPT-4 to conduct interactive homework sessions for high-school students learning English as a second language. Our strategy requires minimal efforts in content preparation, one of the key challenges of alternatives like home tutors or ITSs. We carried out a Randomized Controlled Trial (RCT) in four high-school classes, replacing traditional homework with GPT-4 homework sessions for the treatment group. We observed significant improvements in learning outcomes, specifically a greater gain in grammar, and student engagement. In addition, students reported high levels of satisfaction with the system and wanted to continue using it after the end of the RCT.
```

MODEL OUTPUT

```text
### Key claims in the abstract

- The study addresses a stated gap in empirical research on LLM-based interactive homework in real-world educational settings.
- The researchers developed a prompting strategy for GPT-4 to run interactive homework sessions for high-school students learning English as a second language.
- The strategy is described as requiring little content-preparation effort.
- In a randomized controlled trial involving four high-school classes, the treatment group used GPT-4 homework sessions instead of traditional homework.
- The authors report significant improvements in learning outcomes, including a greater gain in grammar, and in student engagement.
- Students reported high satisfaction with the system and said they wanted to keep using it after the trial.
- The authors present the approach as a practical, scalable solution; the abstract does not provide evidence about its scalability beyond the study.

### What a reader would need to know that the abstract does not say

- How many students took part, and how they were assigned to groups.
- What the comparison group did and whether groups were similar before the trial.
- How long the trial lasted and how often students used the system.
- What the homework sessions involved, including the prompting strategy and the feedback or follow-up questions provided.
- How learning outcomes, grammar gains, engagement, and satisfaction were measured.
- The size of the reported gains, statistical results, and whether other learning outcomes also changed.
- Whether students’ reported interest in continuing translated into actual continued use.
- Whether teachers or researchers monitored the sessions, and how accuracy, inappropriate responses, privacy, and access were handled.
- Whether results would generalize to other schools, subjects, age groups, languages, or longer-term use.
- What the authors mean by “minimal” preparation effort and “scalable,” and what resources implementation requires.

### Two-sentence faculty newsletter summary

In a randomized trial across four high-school classes, students assigned GPT-4 interactive homework showed reported gains in learning—particularly grammar—and engagement compared with students doing traditional homework. Students also reported being satisfied with the system and wanting to continue using it, though the abstract does not give the size of the effects or details about how long they lasted.
```

GRADE: C

GRADER'S REASON: GRADE: C — The submission captures the abstract’s major findings without overstating them and identifies important missing methodological, measurement, statistical, and implementation details.

---

### abs-05 (v2 run-1)

Why suggested: Overreach in the summary that passed. The claims correctly limit the results to students 'around the score cutoff', but the summary reports them for 'this study of 635 students'. In run-3, the same grader failed a different abs-05 output for leaving out exactly this restriction.

ABSTRACT

```text
Hybrid human-AI tutoring, where technology and humans jointly facilitate student learning, can be more beneficial than AI-only tutoring. However, preliminary evidence suggests that lower-performing students derive greater benefit from human-AI tutoring than higher-performing students. As such, this study evaluates whether a differentiated tutoring policy can effectively support both groups: human tutors initiate support for lower-performing students, while higher-performing students receive reactive, on-demand support. Using their within-grade median state test scores, we assigned 635 students (grades 5-8) to receive proactive (< median) or reactive ($\geq$ median) tutoring. Using a DiDC design, we compare outcomes across two time periods: fall (AI-only tutoring) and spring (proactive-reactive human-AI tutoring). This quasi-experimental design isolates the effects of proactive-reactive tutoring approaches by comparing the discontinuity in spring outcomes to the fall, where no such discontinuity existed. Using data around the cutoff (Imbens-Kalyanaraman criterion), we find significant overall improvements from human-AI tutoring compared to AI-only baseline: 25% increase in time on task, 36% in skill proficiency, and 61% in academic growth (standardized MAP test). Between proactive and reactive tutoring, we find comparable improvements in time-on-task and skill proficiency. However, proactive tutoring, on average, showed marginally higher MAP growth (75%, p = .065) than reactive tutoring, i.e., proactive tutoring was more beneficial to students farther below the cutoff and helped narrow achievement gaps. Our findings provide evidence that differentiated human-AI tutoring addresses the needs of both groups, offering a practical and cost-effective strategy for scaling hybrid instruction.
```

MODEL OUTPUT

```text
### Key claims in the abstract

- The study examined a tutoring policy in which students scoring below their grade’s median state-test score received proactive human-tutor support, while students at or above the median could receive support reactively, on demand.
- The study included 635 students in grades 5–8. It compared fall AI-only tutoring with spring human-AI tutoring using a quasi-experimental difference-in-differences-in-discontinuities design.
- In the analyzed data around the score cutoff, the authors report that human-AI tutoring was associated with increases over the AI-only period in time on task (25%), skill proficiency (36%), and standardized MAP academic growth (61%).
- Proactive and reactive tutoring were associated with comparable improvements in time on task and skill proficiency.
- The authors report that MAP growth was marginally higher under proactive tutoring than reactive tutoring (75%, *p* = .065), and interpret this as evidence that proactive tutoring may particularly benefit students farther below the cutoff and help narrow achievement gaps.

### What a reader would still need to know

- Where and when the study took place, and how representative the students and schools were.
- What the AI tutoring and human-tutor support involved, including tutor training, contact time, frequency, and how students accessed on-demand help.
- How time on task and skill proficiency were defined and measured, and what comparison or denominator the reported percentage increases use—especially the “75%” MAP-growth difference.
- The actual outcome levels, uncertainty estimates such as confidence intervals, and whether the reported results were adjusted for other differences between students or time periods.
- How many students were included in the analysis around the cutoff, whether any students missed or did not receive their assigned support, and how missing data were handled.
- Evidence supporting the design’s assumptions, including robustness to alternative analytic choices and how sensitive results were to the selected bandwidth around the cutoff.
- Whether the approach was in fact cost-effective: the abstract offers that as a practical implication but gives no cost or resource data.

### Two-sentence faculty newsletter summary

In this study of 635 students in grades 5–8, human-AI tutoring was associated with more time on task, greater skill proficiency, and stronger MAP growth than AI-only tutoring. Proactive and on-demand support showed similar results for time and proficiency, while proactive support showed a marginally higher growth estimate; the abstract does not establish that this difference is conclusive.
```

GRADE: C

GRADER'S REASON: GRADE: C — The submission presents the major findings without overstating the abstract’s claims, appropriately qualifies the marginal MAP-growth difference, and identifies important missing methodological, contextual, and cost information.

---

## Output 3: clear fail

### abs-05 (v2 run-3)

Why suggested: NOT FROM RUN-1: run-1 has no fails. The closest to a clear fail in any v2 run. The claims drop the 'around the cutoff' restriction and present the gains as applying to the whole spring program.

ABSTRACT

```text
Hybrid human-AI tutoring, where technology and humans jointly facilitate student learning, can be more beneficial than AI-only tutoring. However, preliminary evidence suggests that lower-performing students derive greater benefit from human-AI tutoring than higher-performing students. As such, this study evaluates whether a differentiated tutoring policy can effectively support both groups: human tutors initiate support for lower-performing students, while higher-performing students receive reactive, on-demand support. Using their within-grade median state test scores, we assigned 635 students (grades 5-8) to receive proactive (< median) or reactive ($\geq$ median) tutoring. Using a DiDC design, we compare outcomes across two time periods: fall (AI-only tutoring) and spring (proactive-reactive human-AI tutoring). This quasi-experimental design isolates the effects of proactive-reactive tutoring approaches by comparing the discontinuity in spring outcomes to the fall, where no such discontinuity existed. Using data around the cutoff (Imbens-Kalyanaraman criterion), we find significant overall improvements from human-AI tutoring compared to AI-only baseline: 25% increase in time on task, 36% in skill proficiency, and 61% in academic growth (standardized MAP test). Between proactive and reactive tutoring, we find comparable improvements in time-on-task and skill proficiency. However, proactive tutoring, on average, showed marginally higher MAP growth (75%, p = .065) than reactive tutoring, i.e., proactive tutoring was more beneficial to students farther below the cutoff and helped narrow achievement gaps. Our findings provide evidence that differentiated human-AI tutoring addresses the needs of both groups, offering a practical and cost-effective strategy for scaling hybrid instruction.
```

MODEL OUTPUT

```text
## Key claims in the abstract

- Prior evidence suggests hybrid human-AI tutoring may benefit students more than AI-only tutoring, and that lower-performing students may benefit more than higher-performing students.
- The study examined a differentiated approach with 635 students in grades 5–8: students below their within-grade median state-test score received proactive tutoring, while students at or above the median received reactive, on-demand tutoring.
- The authors used a quasi-experimental difference-in-difference-in-cutoff (DiDC) design, comparing fall AI-only tutoring with spring human-AI tutoring.
- Compared with the AI-only fall baseline, the spring tutoring approach was associated with reported increases of 25% in time on task, 36% in skill proficiency, and 61% in academic growth on a standardized MAP test. The abstract describes these overall improvements as statistically significant.
- Proactive and reactive tutoring were associated with comparable improvements in time on task and skill proficiency.
- The proactive group had a reported 75% higher average MAP growth than the reactive group, with *p* = .065. The abstract characterizes this as marginal and interprets it as evidence that proactive tutoring may especially benefit students farther below the cutoff and help narrow achievement gaps.
- The authors conclude that differentiated human-AI tutoring may be a practical and cost-effective way to scale hybrid instruction.

## What the abstract does not say

- Where and when the study took place, or how students, schools, and tutors were recruited.
- What the AI tutor and human-tutor support involved, including the content, frequency, duration, and amount of tutoring students actually received.
- How “time on task,” “skill proficiency,” and academic growth were defined and measured, and what the reported percentages are relative to.
- The size and uncertainty of the estimated effects—for example, confidence intervals, exact test statistics, and full model results. It also does not explain how to interpret the 75% figure or why *p* = .065 is described as marginal.
- Whether there were differences between the groups before the intervention, how many students’ data were missing, or whether students received other support during the study.
- The assumptions and robustness checks behind the quasi-experimental design, including the cutoff bandwidth and how sensitive the results were to analytic choices.
- Whether the findings persisted beyond spring, or whether they generalize to other grades, subjects, schools, or tutoring systems.
- How “cost-effective” was assessed; no cost information is provided in the abstract.

## Two-sentence plain-language summary

In this quasi-experimental study, students receiving spring tutoring that combined human support with AI showed higher reported time on task, skill proficiency, and academic growth than during the fall AI-only period. Proactive tutoring was linked to a somewhat higher average growth estimate than on-demand tutoring, but the difference was marginal (*p* = .065).
```

GRADE: I

GRADER'S REASON: GRADE: I — The submission captures the major findings cautiously, but omits that the results use data near the cutoff and does not identify the unreported cutoff-analysis sample size or proactive/reactive group counts.

---

### abs-02 (v2 run-2)

Why suggested: NOT FROM RUN-1, and arguably a 'fails a defensible answer' case rather than a clear fail. The grader failed it because the 'not stated' list does not mention a control condition or the study's calendar duration, both of which are in the gold. The output is otherwise careful.

ABSTRACT

```text
This exploratory study examines the classroom deployment of aiPlato, an AI-enabled homework platform, in a large introductory physics course at the University of Texas at Arlington. Designed to support open-ended problem solving, aiPlato provides step-wise feedback and iterative guidance through tools such as "Evaluate My Work" and "AI Tutor Chat", while preserving opportunities for productive struggle. Over four optional extra-credit assignments, the platform captured detailed student interaction data, which were analyzed alongside course performance and end-of-semester survey responses. We examine how students engaged with different feedback tools, whether engagement patterns were associated with performance on the cumulative final exam, and how students perceived the platform's usability and learning value. Students who engaged more frequently with aiPlato tended to achieve higher final exam scores, with a mean difference corresponding to a standardized effect size of approximately 0.81 between high and low engagement groups after controlling for prior academic performance. Usage patterns and survey responses indicate that students primarily relied on iterative, formative feedback rather than solution-revealing assistance. As a quasi-experimental pilot study, these findings do not establish causality and may reflect self-selection effects. Nonetheless, the results demonstrate the feasibility of integrating AI-mediated, step-wise feedback into authentic physics homework and motivate future controlled studies of AI-assisted tutoring systems.
```

MODEL OUTPUT

```text
### Key claims in the abstract

- The study explored aiPlato, an AI-enabled homework platform, in a large introductory physics course at the University of Texas at Arlington.
- Students could use the platform on four optional extra-credit assignments. Its tools offered step-wise feedback and iterative guidance, including “Evaluate My Work” and “AI Tutor Chat.”
- Students who engaged with aiPlato more frequently tended to earn higher cumulative final-exam scores. The reported difference between high- and low-engagement groups was about 0.81 standard deviations after adjustment for prior academic performance.
- Platform-use patterns and survey responses suggested that students relied mainly on iterative formative feedback rather than assistance that revealed solutions.
- The authors describe the study as a quasi-experimental pilot: it does not establish that using aiPlato caused higher scores, and the association may reflect self-selection.
- The study suggests that integrating AI-mediated, step-wise feedback into physics homework is feasible and supports conducting controlled studies. It does not establish the platform’s effectiveness.

### What a reader would need to know that the abstract does not say

- How many students took part, and what their backgrounds or prior experience were.
- How “engagement,” “high engagement,” and “low engagement” were defined, and how many students were in each group.
- The actual final-exam scores, the statistical uncertainty around the estimated difference, and details of the analysis and adjustment for prior academic performance.
- How many students completed each assignment and the survey, and whether non-participation or missing data could have affected the results.
- What survey questions or measures were used, and what students reported about usability and learning value.
- How often students used each tool and how the study determined whether an interaction provided formative feedback or revealed a solution.
- What other factors—such as motivation, time spent studying, or course attendance—might help explain the association between platform engagement and exam scores.
- How the platform was introduced and supported, and whether the findings would apply to other courses, institutions, or student groups.

### Two-sentence newsletter summary

In a pilot study in an introductory physics course, students who used the AI homework platform more often tended to score higher on the final exam, even after accounting for prior academic performance. Because participation was optional and the study cannot show that the platform caused the higher scores, the results point to the need for controlled follow-up research.
```

GRADE: I

GRADER'S REASON: GRADE: I — The submission accurately and cautiously presents the major findings, but its missing-information list omits whether there was a separate comparison/control condition and the study’s calendar duration and assignment timing.

---
