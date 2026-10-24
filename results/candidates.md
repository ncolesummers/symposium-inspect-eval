# Candidate outputs for the workshop packet (from run-1)

These are suggestions only. You choose.

## Output 1: clear pass

### abs-01

Why suggested: Keeps every hedge, notes that the 2-week retention results are missing, and names the main weakness: everyone did the video-only condition first.

ABSTRACT

```text
The exponential growth of AI education has brought millions of learners to online platforms, yet this massive scale has simultaneously exposed critical pedagogical shortcomings. Traditional video-based instruction, while cost-effective and scalable, demonstrates systematic failures in both sustaining learner engagement and facilitating the deep conceptual mastery essential for AI literacy. We present a pilot study evaluating a novel hybrid learning platform that integrates real-time conversational AI tutors with traditional video lectures. Our controlled experiment (N = 58, mean age M = 21.4, SD = 2.8) compared traditional video-based instruction with our AI-augmented video platform. This study employed a sequential within-subjects design where all participants first completed the traditional video condition followed by the AI-augmented condition, providing direct comparisons of learning outcomes. We measured learning effectiveness through immediate post-tests and delayed retention assessments (2-week delay). Results suggest improvements in learning performance: immediate post-test performance showed a large effect size (d = 1.505) with participants scoring 8.3 points higher after AI-augmented instruction (91.8 vs 83.5 out of 100, p < .001). Behavioral analytics revealed increased engagement duration (71.1% improvement with AI tutoring) in the experimental group. This pilot study provides preliminary evidence that conversational AI tutors may enhance traditional educational delivery, suggesting a potential avenue for developing scalable, adaptive learning systems.
```

MODEL OUTPUT

```text
### Key claims in the abstract

- The study evaluated a pilot platform combining video lectures with real-time conversational AI tutoring, comparing it with video-only instruction.
- Fifty-eight participants (mean age 21.4 years, SD 2.8) completed both conditions: video-only first, then AI-augmented instruction.
- On the immediate post-test, the AI-augmented condition was associated with a reported average score of 91.8, compared with 83.5 after video-only instruction—a difference of 8.3 points. The abstract reports *p* < .001 and an effect size of *d* = 1.505.
- The abstract reports that engagement duration was 71.1% higher in the AI-tutoring condition. It does not state whether this difference was statistically significant.
- The authors characterize the findings as preliminary evidence that conversational AI tutors may improve learning with video instruction. The abstract says delayed retention was assessed, but does not report its results.

### What the abstract does not say

- **Who participated:** how they were recruited, their prior AI knowledge or educational background, or whether they represent the broader population of online learners.
- **What was taught:** the course content, its length and difficulty, and whether the material was representative of AI education generally.
- **How the AI tutor worked:** what it could do, how learners interacted with it, and whether the tutor or instructional content was standardized.
- **How outcomes were measured:** what the tests and engagement measure assessed, whether the tests were validated, and how “engagement duration” was defined.
- **What happened on the delayed assessment:** the retention scores, comparison between conditions, and whether any difference persisted after two weeks.
- **Whether the reported differences were statistically reliable beyond the immediate test:** confidence intervals and other details of the statistical analyses are not provided; the abstract also does not report a significance test for engagement.
- **How many participants completed each assessment** or whether there was missing data or attrition.
- **Whether other learning conditions were controlled**, such as time spent studying, opportunities to review material, or access to assistance.
- **Whether the AI tutor caused the differences:** all participants completed video-only instruction first and AI-augmented instruction second. Without a counterbalanced order or separate comparison group, the results cannot rule out effects of practice, order, or time.
- **How broadly the findings apply:** a small pilot study alone does not establish that the platform will have similar effects in other learner populations or settings.
```

GRADE: C

GRADER'S REASON: C — The submission accurately presents the major findings without overstating them and identifies the missing methodological details, delayed retention results, order-effect controls, and limits to generalizability.

---

### abs-12

Why suggested: Shorter alternative for a slide. Adds no numbers to an abstract that has none, and asks what 'most' means.

ABSTRACT

```text
This paper provides an educational case study regarding our experience in deploying ChatGPT Large Language Models (LLMs) in the Spring 2025 and Fall 2023 offerings of ECE 4320: Power System Analysis and Control at Georgia Tech. As part of course assessments, students were tasked with identifying, explaining, and correcting errors in the ChatGPT outputs corresponding to power factor correction problems. While most students successfully identified the errors in the outputs from the GPT-4 version of ChatGPT used in Fall 2023, students found the errors from the ChatGPT o1 version much more difficult to identify in Spring 2025. As shown in this case study, the role of LLMs in pedagogy, assessment, and learning in power engineering classrooms is an important topic deserving further investigation.
```

MODEL OUTPUT

```text
## Key claims in the abstract

- The paper is an educational case study of the authors’ experience using ChatGPT LLMs in two offerings of Georgia Tech’s ECE 4320: Power System Analysis and Control: Fall 2023 and Spring 2025.
- In course assessments, students were asked to identify, explain, and correct errors in ChatGPT responses to power factor correction problems.
- In Fall 2023, most students successfully identified errors in responses from the GPT-4 version of ChatGPT.
- In Spring 2025, students found errors in responses from ChatGPT o1 much more difficult to identify.
- The authors argue that the role of LLMs in pedagogy, assessment, and learning in power engineering classrooms deserves further investigation.

## What the abstract does not say

- How many students took part, or what “most” means in numbers.
- How the authors measured whether students identified errors successfully or found them difficult.
- What the errors were, and how many or what kinds of problems and ChatGPT responses were assessed.
- The exact prompts, model versions or settings, and procedures used to generate the responses.
- Whether the two offerings used comparable assessments, instruction, grading, or student populations.
- Whether the observed difference was tested statistically or could be attributed to the model rather than other differences between the offerings.
- Whether the activity affected students’ learning, performance, or attitudes toward LLMs.
- How representative the findings are beyond these course offerings.
```

GRADE: C

GRADER'S REASON: C — The submission accurately captures the abstract’s major claims without overstating them and identifies missing methodological details, quantitative results, comparability information, and learning outcomes.

---

## Output 2: disputed case

### abs-04

Why suggested: Possible overreach that passed. The abstract says 'significant improvements in learning outcomes, specifically a greater gain in grammar'. The output says 'including a greater gain in grammar', which implies other learning gains the abstract does not claim.

ABSTRACT

```text
This work contributes to the scarce empirical literature on LLM-based interactive homework in real-world educational settings and offers a practical, scalable solution for improving homework in schools. Homework is an important part of education in schools across the world, but in order to maximize benefit, it needs to be accompanied with feedback and followup questions. We developed a prompting strategy that enables GPT-4 to conduct interactive homework sessions for high-school students learning English as a second language. Our strategy requires minimal efforts in content preparation, one of the key challenges of alternatives like home tutors or ITSs. We carried out a Randomized Controlled Trial (RCT) in four high-school classes, replacing traditional homework with GPT-4 homework sessions for the treatment group. We observed significant improvements in learning outcomes, specifically a greater gain in grammar, and student engagement. In addition, students reported high levels of satisfaction with the system and wanted to continue using it after the end of the RCT.
```

MODEL OUTPUT

```text
### Key claims in the abstract

- The study addresses what the authors describe as a scarce empirical literature on LLM-based interactive homework in real-world educational settings.
- The authors developed a prompting strategy for GPT-4 to run interactive homework sessions for high-school students learning English as a second language.
- The strategy is described as requiring little content preparation; the abstract does not quantify that effort.
- The authors conducted a randomized controlled trial in four high-school classes, with the treatment group doing GPT-4 homework sessions instead of traditional homework.
- The authors report significant improvements in learning outcomes and student engagement, including a greater gain in grammar. The abstract does not specify the comparisons or measures behind these findings.
- Students reportedly expressed high satisfaction with the system and a desire to keep using it after the trial.
- The authors present the approach as practical and scalable, though the abstract does not provide evidence about its scalability.

### What a reader would need to know

- How many students took part, how they were assigned, and whether assignment was randomized at the student or class level.
- The students’ ages, proficiency levels, schools, and relevant background characteristics.
- How long the trial lasted and how often students used the system.
- What the control group did, and whether the two groups had comparable homework time, content, and teacher support.
- What the GPT-4 sessions involved, including the prompting strategy, feedback, follow-up questions, and safeguards.
- How learning outcomes and engagement were measured, and whether those measures were validated.
- The size of the reported effects, their statistical uncertainty, and which outcomes were statistically significant.
- Whether the analysis accounted for students being grouped in classes, and how missing data or noncompliance were handled.
- How satisfaction and willingness to continue were collected, and how many students responded.
- Whether the findings persisted over time or generalized beyond these classes and this subject.
- What “minimal” content preparation involved in practice, and what costs, technical requirements, or teacher workload the approach entails.
```

GRADE: C

GRADER'S REASON: C — The submission includes all major findings without overstating the abstract’s claims and identifies missing methodological, measurement, statistical, and implementation details.

---

### abs-07

Why suggested: Understatement that passed. The abstract says the findings 'indicate' GenAI 'can move' learning; the output says they are 'suggesting' it was 'associated with movement'. Rubric line 1 only forbids stating claims more strongly, so the grader cannot penalize misrepresenting the authors in the cautious direction.

ABSTRACT

```text
Generative AI (GenAI) tools entered higher education classrooms faster than the field was able to study their effects on learning. One concern is that GenAI may displace the critical thinking and AI literacy that students will need after graduation. This paper reports a Design-Based Research pilot of a GenAI-assisted critical thinking framework, in which ChatGPT was used as a thinking partner in an undergraduate research methods and statistics course during Spring 2025 (N = 14). The mixed-methods design combined pre- and post-intervention measures of statistical learning (AASCDM), AI literacy (MAILS), and critical thinking (WGCTA) with instructor field notes, student artifacts, and student-AI interaction logs. Pre-post tests showed gains on every AASCDM dimension and on eight of nine MAILS dimensions, while WGCTA percentiles did not change. Qualitative analysis identified four themes: the ways students positioned the LLM (as answer generator, validator, or co-thinker); the depth of student engagement (procedural vs. conceptual); occasional humanizing of the tool; and the role of curriculum design in shaping each of the prior three. Read together, the findings indicate that one semester of GenAI-assisted instruction can move domain learning and self-reported AI literacy but does not move standardized critical thinking, and that the modal student-LLM relationship is one of validation instead of dialogue. We end with design principles for the next iteration of the framework and implications for research on adaptive and personalized learning.
```

MODEL OUTPUT

```text
## Key claims in the abstract

- The paper reports a Design-Based Research pilot using ChatGPT as a thinking partner in an undergraduate research methods and statistics course in Spring 2025, with 14 students.
- Pre- to post-intervention measures showed gains on every AASCDM dimension and on eight of the nine MAILS dimensions.
- WGCTA percentiles did not change from pre- to post-intervention.
- Qualitative analysis identified four themes: how students positioned the LLM (as answer generator, validator, or co-thinker); whether their engagement was procedural or conceptual; occasional humanizing of the tool; and the influence of curriculum design on the other three themes.
- The authors interpret the findings as suggesting that, in this course and pilot, GenAI-assisted instruction was associated with movement in domain learning and self-reported AI literacy, but not in standardized critical thinking.
- The authors also report that validation, rather than dialogue, was the modal student–LLM relationship.
- The paper concludes with design principles for a next iteration of the framework and implications for research on adaptive and personalized learning.

## What the abstract does not say

- How students were recruited or what their backgrounds and prior experience with GenAI were.
- Whether there was a comparison or control group, or how the study accounts for changes that might have occurred without the intervention.
- What the intervention involved in practice: its duration and frequency, specific activities, guidance given to students, or how ChatGPT use was managed.
- The size and statistical significance of the reported gains, including uncertainty or variation among students.
- How each measure was administered and scored, and whether the measures were appropriate for this sample and context.
- What “gains” on the AASCDM and MAILS mean in practical terms, or which MAILS dimension did not show a gain.
- How the qualitative analysis was conducted, including who coded the data and how the themes were checked.
- How many students showed each interaction pattern, or how “modal” was determined.
- Whether the results persisted beyond the semester or related to students’ later performance.
- How broadly the findings might apply beyond this small pilot in one course.
```

GRADE: C

GRADER'S REASON: C — The submission includes the abstract’s major findings without overstating them and names the key missing methodological, statistical, participant, and generalizability information.

---

## Output 3: clear fail

No candidate: the grader gave C to every sample in all three runs.
