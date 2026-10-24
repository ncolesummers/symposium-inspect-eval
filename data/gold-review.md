# Gold target review

Draft targets were written by `gpt-6.1-sol` using the prompt in `data/build.py`. Every target needs a human check before the runs.

**How to review:** edit the text inside each `target` block below, add notes if you like, and tick the box. Tell me when you're done and I'll copy your edits into `data/abstracts.jsonl` and commit them. (You can edit `abstracts.jsonl` directly instead if you prefer.)

**Things worth deciding once for all 12:**
- **Format is inconsistent.** Some drafts number their items and some don't. The grader only sees the text, so this mostly matters for the slides.
- **The "Not stated" lists are long** (5 to 8 items). The rubric says "Missing information is named", so a long gold list may push the grader to fail answers that name only the main gaps. You may want to cut each list down to the gaps that matter most.
- **Some "key claims" are background, not findings** (marked below). Because the rubric checks that "major findings are present", a background claim in the gold may confuse the grader.
- **The abstracts are verbatim from arXiv**, LaTeX included (abs-05 `($\geq$ median)`, abs-10 `$(n=70)$`).

## abs-01: Beyond Passive Viewing: A Pilot Study of a Hybrid Learning Platform Augmenting Video Lectures with Conversational AI

- [ ] Reviewed
- Source: [2604.15334v1](https://arxiv.org/abs/2604.15334v1) · 208 words

*Reviewer flag:* The abstract says participants were tested within-subjects (everyone did both conditions in a fixed order), then reports engagement "in the experimental group". The draft drops that phrase. The draft also correctly notes that the abstract gives no results for the 2-week retention test.

**Abstract**

> The exponential growth of AI education has brought millions of learners to online platforms, yet this massive scale has simultaneously exposed critical pedagogical shortcomings. Traditional video-based instruction, while cost-effective and scalable, demonstrates systematic failures in both sustaining learner engagement and facilitating the deep conceptual mastery essential for AI literacy. We present a pilot study evaluating a novel hybrid learning platform that integrates real-time conversational AI tutors with traditional video lectures. Our controlled experiment (N = 58, mean age M = 21.4, SD = 2.8) compared traditional video-based instruction with our AI-augmented video platform. This study employed a sequential within-subjects design where all participants first completed the traditional video condition followed by the AI-augmented condition, providing direct comparisons of learning outcomes. We measured learning effectiveness through immediate post-tests and delayed retention assessments (2-week delay). Results suggest improvements in learning performance: immediate post-test performance showed a large effect size (d = 1.505) with participants scoring 8.3 points higher after AI-augmented instruction (91.8 vs 83.5 out of 100, p < .001). Behavioral analytics revealed increased engagement duration (71.1% improvement with AI tutoring) in the experimental group. This pilot study provides preliminary evidence that conversational AI tutors may enhance traditional educational delivery, suggesting a potential avenue for developing scalable, adaptive learning systems.

**Draft target**

```target
Key claims:
Results from a pilot study suggest improved immediate learning performance with AI-augmented video instruction: participants scored 8.3 points higher than after traditional video instruction (91.8 vs. 83.5 out of 100; d = 1.505, p < .001).
Behavioral analytics showed a 71.1% increase in engagement duration with AI tutoring.
The pilot study provides preliminary evidence that conversational AI tutors may enhance traditional educational delivery, suggesting a potential avenue for scalable, adaptive learning systems.

Not stated in the abstract:
Participants’ recruitment method, educational backgrounds, and prior AI knowledge.
The instructional topics, video content, conversational AI system, and duration of each condition.
Results of the delayed retention assessments conducted after two weeks.
How engagement duration was defined and measured, and whether its increase was statistically significant.
How order, practice, or carryover effects were addressed, given that all 58 participants completed traditional instruction before AI-augmented instruction.
Whether the findings generalize to other populations, subjects, or longer-term learning outcomes.
```

---

## abs-02: aiPlato: A Novel AI Tutoring and Step-wise Feedback System for Physics Homework

- [ ] Reviewed
- Source: [2601.09965v1](https://arxiv.org/abs/2601.09965v1) · 206 words

**Abstract**

> This exploratory study examines the classroom deployment of aiPlato, an AI-enabled homework platform, in a large introductory physics course at the University of Texas at Arlington. Designed to support open-ended problem solving, aiPlato provides step-wise feedback and iterative guidance through tools such as "Evaluate My Work" and "AI Tutor Chat", while preserving opportunities for productive struggle. Over four optional extra-credit assignments, the platform captured detailed student interaction data, which were analyzed alongside course performance and end-of-semester survey responses. We examine how students engaged with different feedback tools, whether engagement patterns were associated with performance on the cumulative final exam, and how students perceived the platform's usability and learning value. Students who engaged more frequently with aiPlato tended to achieve higher final exam scores, with a mean difference corresponding to a standardized effect size of approximately 0.81 between high and low engagement groups after controlling for prior academic performance. Usage patterns and survey responses indicate that students primarily relied on iterative, formative feedback rather than solution-revealing assistance. As a quasi-experimental pilot study, these findings do not establish causality and may reflect self-selection effects. Nonetheless, the results demonstrate the feasibility of integrating AI-mediated, step-wise feedback into authentic physics homework and motivate future controlled studies of AI-assisted tutoring systems.

**Draft target**

```target
Key claims:
1. In this exploratory, quasi-experimental pilot study, students who engaged more frequently with aiPlato tended to achieve higher cumulative final exam scores. After controlling for prior academic performance, the mean difference between high- and low-engagement groups corresponded to a standardized effect size of approximately 0.81.
2. Usage patterns and survey responses indicate that students primarily relied on iterative, formative feedback rather than solution-revealing assistance.
3. The findings do not establish causality and may reflect self-selection effects.
4. The results demonstrate the feasibility of integrating AI-mediated, step-wise feedback into authentic physics homework and motivate future controlled studies.

Not stated in the abstract:
1. The number of students enrolled, using aiPlato, included in the analyses, or responding to the survey.
2. Whether there was a separate comparison or control condition and, if so, what it involved.
3. The study’s calendar duration and the timing or spacing of the four optional extra-credit assignments.
4. How high and low engagement were defined, how prior academic performance was measured, and which statistical methods were used to control for it.
5. The raw final exam scores, uncertainty around the effect-size estimate, and statistical significance.
6. The survey questions, response rate, and detailed usability or perceived learning-value results.
```

---

## abs-03: An Experience Report on a Pedagogically Controlled, Curriculum-Constrained AI Tutor for SE Education

- [ ] Reviewed
- Source: [2512.11882v1](https://arxiv.org/abs/2512.11882v1) · 209 words

**Abstract**

> The integration of artificial intelligence (AI) into education continues to evoke both promise and skepticism. While past waves of technological optimism often fell short, recent advances in large language models (LLMs) have revived the vision of scalable, individualized tutoring. This paper presents the design and pilot evaluation of RockStartIT Tutor, an AI-powered assistant developed for a digital programming and computational thinking course within the RockStartIT initiative. Powered by GPT-4 via OpenAI's Assistant API, the tutor employs a novel prompting strategy and a modular, semantically tagged knowledge base to deliver context-aware, personalized, and curriculum-constrained support for secondary school students. We evaluated the system using the Technology Acceptance Model (TAM) with 13 students and teachers. Learners appreciated the low-stakes environment for asking questions and receiving scaffolded guidance. Educators emphasized the system's potential to reduce cognitive load during independent tasks and complement classroom teaching. Key challenges include prototype limitations, a small sample size, and the need for long-term studies with the target age group. Our findings highlight a pragmatic approach to AI integration that requires no model training, using structure and prompts to shape behavior. We position AI tutors not as teacher replacements but as enabling tools that extend feedback access, foster inquiry, and support what schools do best: help students learn.

**Draft target**

```target
Key claims:
The paper presents the design and pilot evaluation of RockStartIT Tutor, a GPT-4-powered assistant for a digital programming and computational thinking course, evaluated using the Technology Acceptance Model with 13 students and teachers.
The tutor uses a novel prompting strategy and a modular, semantically tagged knowledge base to provide context-aware, personalized, curriculum-constrained support for secondary school students without model training.
Learners appreciated the low-stakes environment for asking questions and receiving scaffolded guidance; educators emphasized the system’s potential to reduce cognitive load during independent tasks and complement classroom teaching.
The pilot findings are limited by prototype limitations and a small sample size, and long-term studies with the target age group are needed.

Not stated in the abstract:
The breakdown of the 13 participants into students and teachers, their ages, and how they were recruited.
The duration of the pilot and the frequency or length of tutor use.
Whether there was a control or comparison condition.
The specific TAM measures, data collection procedures, analysis methods, and quantitative results.
Whether the tutor improved learning outcomes or measurably reduced cognitive load.
The details of the prompting strategy, knowledge base, and prototype limitations.
```

---

## abs-04: GPT-4 as a Homework Tutor can Improve Student Engagement and Learning Outcomes

- [ ] Reviewed
- Source: [2409.15981v1](https://arxiv.org/abs/2409.15981v1) · 159 words

**Abstract**

> This work contributes to the scarce empirical literature on LLM-based interactive homework in real-world educational settings and offers a practical, scalable solution for improving homework in schools. Homework is an important part of education in schools across the world, but in order to maximize benefit, it needs to be accompanied with feedback and followup questions. We developed a prompting strategy that enables GPT-4 to conduct interactive homework sessions for high-school students learning English as a second language. Our strategy requires minimal efforts in content preparation, one of the key challenges of alternatives like home tutors or ITSs. We carried out a Randomized Controlled Trial (RCT) in four high-school classes, replacing traditional homework with GPT-4 homework sessions for the treatment group. We observed significant improvements in learning outcomes, specifically a greater gain in grammar, and student engagement. In addition, students reported high levels of satisfaction with the system and wanted to continue using it after the end of the RCT.

**Draft target**

```target
Key claims:
The authors developed a prompting strategy that enables GPT-4 to conduct interactive homework sessions for high-school students learning English as a second language, requiring minimal effort in content preparation.
In an RCT conducted in four high-school classes, traditional homework was replaced with GPT-4 homework sessions for the treatment group.
The authors observed significant improvements in learning outcomes, specifically a greater gain in grammar, and in student engagement.
Students reported high satisfaction with the system and wanted to continue using it after the RCT ended.

Not stated in the abstract:
The number of students, their ages, baseline English proficiency, and geographic or school context.
The trial duration, frequency and length of homework sessions, and whether outcomes persisted after the trial.
The unit and method of randomization, group sizes, and details of the control condition.
How grammar gains, engagement, and satisfaction were measured.
The effect sizes, uncertainty estimates, and statistical tests.
The details of the prompting strategy and the amount of preparation effort required.
```

---

## abs-05: Improving Hybrid Human-AI Tutoring by Differentiating Human Tutor Roles Based on Student Needs

- [ ] Reviewed
- Source: [2605.11155v1](https://arxiv.org/abs/2605.11155v1) · 239 words

*Reviewer flag:* Claim 1 ("lower-performing students derive greater benefit") is prior evidence the abstract cites as motivation, not this study's finding. The abstract's own concluding claim ("provide evidence that differentiated human-AI tutoring addresses the needs of both groups") is missing. The "Not stated" list has 8 items, the longest of all 12.

**Abstract**

> Hybrid human-AI tutoring, where technology and humans jointly facilitate student learning, can be more beneficial than AI-only tutoring. However, preliminary evidence suggests that lower-performing students derive greater benefit from human-AI tutoring than higher-performing students. As such, this study evaluates whether a differentiated tutoring policy can effectively support both groups: human tutors initiate support for lower-performing students, while higher-performing students receive reactive, on-demand support. Using their within-grade median state test scores, we assigned 635 students (grades 5-8) to receive proactive (< median) or reactive ($\geq$ median) tutoring. Using a DiDC design, we compare outcomes across two time periods: fall (AI-only tutoring) and spring (proactive-reactive human-AI tutoring). This quasi-experimental design isolates the effects of proactive-reactive tutoring approaches by comparing the discontinuity in spring outcomes to the fall, where no such discontinuity existed. Using data around the cutoff (Imbens-Kalyanaraman criterion), we find significant overall improvements from human-AI tutoring compared to AI-only baseline: 25% increase in time on task, 36% in skill proficiency, and 61% in academic growth (standardized MAP test). Between proactive and reactive tutoring, we find comparable improvements in time-on-task and skill proficiency. However, proactive tutoring, on average, showed marginally higher MAP growth (75%, p = .065) than reactive tutoring, i.e., proactive tutoring was more beneficial to students farther below the cutoff and helped narrow achievement gaps. Our findings provide evidence that differentiated human-AI tutoring addresses the needs of both groups, offering a practical and cost-effective strategy for scaling hybrid instruction.

**Draft target**

```target
Key claims:
Preliminary evidence suggests that lower-performing students derive greater benefit from human-AI tutoring than higher-performing students.
Using data around the assignment cutoff, the study finds significant overall improvements from human-AI tutoring compared with the AI-only baseline: 25% in time on task, 36% in skill proficiency, and 61% in academic growth measured by the standardized MAP test.
Proactive and reactive tutoring showed comparable improvements in time on task and skill proficiency.
Proactive tutoring, on average, showed marginally higher MAP growth (75%, p = .065) than reactive tutoring; the abstract reports that proactive tutoring was more beneficial to students farther below the cutoff and helped narrow achievement gaps.

Not stated in the abstract:
The number of students included in the cutoff-based analysis and the numbers receiving proactive versus reactive tutoring.
The schools, geographic setting, and student demographics beyond grades 5–8 and performance-based assignment.
The exact duration, frequency, and amount of tutoring in fall and spring.
The AI system used, human tutors’ qualifications, and the specific procedures for proactive and reactive support.
The cutoff bandwidth selected by the Imbens-Kalyanaraman criterion, detailed model specifications, and checks of the quasi-experimental assumptions.
Confidence intervals, exact p-values for the overall improvements, and how the reported percentage gains were calculated.
Attrition, missing-data handling, and whether effects persisted beyond spring.
Cost data or a cost-effectiveness analysis supporting the description of the strategy as cost-effective.
```

---

## abs-06: NotebookLM as a Socratic physics tutor: Design and preliminary observations of a RAG-based tool

- [ ] Reviewed
- Source: [2504.09720v3](https://arxiv.org/abs/2504.09720v3) · 169 words

*Reviewer flag:* This study observed teachers, not students. Check that the claims don't imply anything about student outcomes.

**Abstract**

> This study explores NotebookLM, a Google Gemini - powered AI platform that integrates Retrieval-Augmented Generation (RAG) as a Socratic tutor for physics education. In this implementation, NotebookLM was configured to support students in solving conceptually oriented physics problems through a guided, questioning-based dialogue. When deployed as a collaborative tutor, the system restricts student interaction to a chat-only interface, promoting controlled and guided engagement. By grounding its responses in teacher-provided source documents, the AI tutor helps mitigate one of the major shortcomings of standard Large Language Models - hallucinations - thereby ensuring more traceable and reliable answers. This work details the methodological design of the tutor, including the iterative development of a pedagogical "Training Manual", and presents preliminary qualitative observations from demonstrations with pre-service and in-service teachers. These observations highlight both the promising potential of the tool and key pedagogical challenges, such as managing user motivation. While limitations remain, this work offers a promising and replicable model for educators seeking to implement grounded AI tutors in their own teaching contexts.

**Draft target**

```target
Key claims:
1. NotebookLM was configured as a Socratic tutor to support students in solving conceptually oriented physics problems through guided, questioning-based dialogue, with interaction restricted to a chat-only interface when deployed as a collaborative tutor.
2. Grounding the tutor’s responses in teacher-provided source documents helps mitigate hallucinations and supports more traceable and reliable answers.
3. Preliminary qualitative observations from demonstrations with pre-service and in-service teachers highlight both the tool’s promising potential and pedagogical challenges, such as managing user motivation.
4. While limitations remain, the work offers a promising and replicable model for educators seeking to implement grounded AI tutors in their own teaching contexts.

Not stated in the abstract:
1. The number of demonstration participants, their characteristics beyond teacher status, or how they were recruited.
2. The demonstrations’ duration, setting, specific physics topics, or tasks.
3. Whether there was a control or comparison condition.
4. Whether students used the tutor directly or whether student learning outcomes were measured.
5. How qualitative observations were collected or analyzed.
6. Whether hallucination reduction, answer reliability, or traceability was empirically measured.
7. The contents of the teacher-provided documents and pedagogical Training Manual, or the detailed implementation procedures needed for replication.
8. The full range of limitations and pedagogical challenges, or how motivation-related challenges were addressed.
```

---

## abs-07: Critical Thinking with Generative AI: A Constraint-First Design Pilot of a Thinking-Partner Intervention

- [ ] Reviewed
- Source: [2609.38029v1](https://arxiv.org/abs/2609.38029v1) · 228 words

**Abstract**

> Generative AI (GenAI) tools entered higher education classrooms faster than the field was able to study their effects on learning. One concern is that GenAI may displace the critical thinking and AI literacy that students will need after graduation. This paper reports a Design-Based Research pilot of a GenAI-assisted critical thinking framework, in which ChatGPT was used as a thinking partner in an undergraduate research methods and statistics course during Spring 2025 (N = 14). The mixed-methods design combined pre- and post-intervention measures of statistical learning (AASCDM), AI literacy (MAILS), and critical thinking (WGCTA) with instructor field notes, student artifacts, and student-AI interaction logs. Pre-post tests showed gains on every AASCDM dimension and on eight of nine MAILS dimensions, while WGCTA percentiles did not change. Qualitative analysis identified four themes: the ways students positioned the LLM (as answer generator, validator, or co-thinker); the depth of student engagement (procedural vs. conceptual); occasional humanizing of the tool; and the role of curriculum design in shaping each of the prior three. Read together, the findings indicate that one semester of GenAI-assisted instruction can move domain learning and self-reported AI literacy but does not move standardized critical thinking, and that the modal student-LLM relationship is one of validation instead of dialogue. We end with design principles for the next iteration of the framework and implications for research on adaptive and personalized learning.

**Draft target**

```target
Key claims:
In a Design-Based Research pilot in an undergraduate research methods and statistics course during Spring 2025 (N = 14), pre-post tests showed gains on every AASCDM statistical-learning dimension and eight of nine MAILS AI-literacy dimensions.
WGCTA percentiles did not change. Read together, the pilot findings indicate that one semester of GenAI-assisted instruction can move domain learning and self-reported AI literacy but does not move standardized critical thinking.
Qualitative analysis identified four themes: students’ positioning of the LLM, procedural versus conceptual engagement, occasional humanizing of the tool, and curriculum design’s role in shaping these.
The findings indicate that the modal student-LLM relationship is validation rather than dialogue.

Not stated in the abstract:
Whether there was a control or comparison condition.
The magnitude, variability, or statistical significance of the pre-post changes.
Students’ demographics, recruitment, or prior experience with GenAI, statistics, and research methods.
The framework’s specific activities and the frequency or amount of ChatGPT use.
Details of the qualitative coding and how the modal relationship was determined.
Whether any changes persisted beyond the semester or generalized to other courses or populations.
```

---

## abs-08: ChatGPT-5 in Secondary Education: A Mixed-Methods Analysis of Student Attitudes, AI Anxiety, and Hallucination-Aware Use

- [ ] Reviewed
- Source: [2512.04109v1](https://arxiv.org/abs/2512.04109v1) · 221 words

**Abstract**

> This mixed-methods study examined secondary students' interactions with the generative AI chatbot ChatGPT-5 in a formal classroom setting, focusing on attitudes, anxiety, and responses to hallucinated outputs. Participants were 109 16-year-old students from three Greek high schools who used ChatGPT-5 during an eight-hour intervention in the course "Technology." Students engaged in information seeking, CV generation, document and video summarization, image generation, quiz creation, and age-appropriate explanations, including tasks deliberately designed to elicit hallucinations. Quantitative data were collected with the Student Attitudes Toward Artificial Intelligence scale (SATAI) and the Artificial Intelligence Anxiety Scale (AIAS); qualitative data came from semi-structured interviews with 36 students. SATAI results showed moderately positive attitudes toward AI, with stronger cognitive evaluations than behavioral intentions, whereas AIAS scores indicated moderate learning-related anxiety and higher concern about AI-driven job replacement. Gender differences in AI anxiety were small and non-significant, while female students reported more positive cognitive attitudes than males. AI attitudes and AI anxiety were essentially uncorrelated. Thematic analysis identified four pedagogical affordances (knowledge expansion, immediate feedback, familiar interface, perceived skill development) and three constraints (uncertainty about accuracy, anxiety about AI feedback, privacy concerns). After encountering hallucinations, many students reported restricting AI use to domains where they already possessed knowledge and could verify answers, a strategy termed "epistemic safeguarding." The study discusses implications for critical AI literacy in secondary education.

**Draft target**

```target
Key claims:
Students showed moderately positive attitudes toward AI, with stronger cognitive evaluations than behavioral intentions, alongside moderate learning-related anxiety and higher concern about AI-driven job replacement.
Gender differences in AI anxiety were small and non-significant, while female students reported more positive cognitive attitudes than males. AI attitudes and AI anxiety were essentially uncorrelated.
Thematic analysis identified four pedagogical affordances (knowledge expansion, immediate feedback, familiar interface, perceived skill development) and three constraints (uncertainty about accuracy, anxiety about AI feedback, privacy concerns).
After encountering hallucinations, many students reported restricting AI use to domains where they already possessed knowledge and could verify answers, a strategy termed “epistemic safeguarding.”

Not stated in the abstract:
How students and schools were selected, or participants’ prior experience with AI.
Whether there was a control condition or pre-intervention measurement.
Exact scale scores, effect sizes, or statistical results beyond the qualitative descriptions provided.
How hallucinations were elicited, how often they occurred, or how students’ ability to identify them was assessed.
Whether reported epistemic safeguarding translated into observed behavior or persisted after the intervention.
Whether the intervention improved learning outcomes or critical AI literacy.
```

---

## abs-09: Can AI support student engagement in classroom activities in higher education?

- [ ] Reviewed
- Source: [2506.18941v1](https://arxiv.org/abs/2506.18941v1) · 221 words

*Reviewer flag:* Only 2 key claims, because the abstract states very little. This is a good test of whether the workflow invents results.

**Abstract**

> Lucrative career prospects and creative opportunities often attract students to enroll in computer science majors and pursue advanced studies in the field. Consequently, there has been a significant surge in enrollment in computer science courses, resulting in large class sizes that can range from hundreds to even thousands of students. A common challenge in such large classrooms is the lack of engagement between students and both the instructor and the learning material. However, with advancements in technology and improvements in large language models (LLMs), there is a considerable opportunity to utilize LLM-based AI models, such as conversational artificial intelligence (CAI), to enhance student engagement with learning content in large classes. To explore the potential of CAI to support engagement, especially with learning content, we designed an activity in a software Engineering course (with a large class size) where students used CAI for an in-class activity. We conducted a within-subject investigation in a large classroom at a US university where we compared student engagement during an in-class activity that used CAI tool vs. one without CAI tool. The CAI tool we used was ChatGPT due to its widespread popularity and familiarity. Our results indicate that CAI (ChatGPT) has the potential to support engagement with learning content during in-class activities, especially in large class sizes. We further discuss the implications of our findings.

**Draft target**

```target
Key claims:
The researchers conducted a within-subject investigation in a large software engineering class at a US university, comparing student engagement during an in-class activity using ChatGPT with engagement during one without a CAI tool.
The results indicate that CAI (ChatGPT) has the potential to support engagement with learning content during in-class activities, especially in large classes.

Not stated in the abstract:
The sample size, exact class size, and student demographics or level of study.
The content and duration of the activities and whether they were otherwise comparable.
How engagement was defined and measured.
The order of the activities and whether order effects were addressed.
The numerical results, effect sizes, or statistical significance.
The ChatGPT version, prompts, and guidance provided to students.
Whether any engagement effects persisted or translated into learning gains.
```

---

## abs-10: An Empirical Study to Understand How Students Use ChatGPT for Writing Essays

- [ ] Reviewed
- Source: [2501.10551v5](https://arxiv.org/abs/2501.10551v5) · 213 words

*Reviewer flag:* Claim 1 is the abstract's motivation ("impact ... will depend on how students use them"), not a finding.

**Abstract**

> As large language models (LLMs) advance and become widespread, students increasingly turn to systems like ChatGPT for assistance with writing tasks. Educators are concerned with students' usage of ChatGPT beyond cheating; using ChatGPT may reduce their critical engagement with writing, hindering students' learning processes. The negative or positive impact of using LLM-powered tools for writing will depend on how students use them; however, how students use ChatGPT remains largely unknown, resulting in a limited understanding of its impact on learning. To better understand how students use these tools, we conducted an online study $(n=70)$ where students were given an essay-writing task using a custom platform we developed to capture the queries they made to ChatGPT. To characterize their ChatGPT usage, we categorized each of the queries students made to ChatGPT. We then analyzed the relationship between ChatGPT usage and a variety of other metrics, including students' self-perception, attitudes towards AI, and the resulting essay itself. We found that factors such as gender, race, and perceived self-efficacy can help predict different AI usage patterns. Additionally, we found that different usage patterns were associated with varying levels of enjoyment and perceived ownership over the essay. The results of this study contribute to discussions about how writing education should incorporate generative AI-powered tools in the classroom.

**Draft target**

```target
Key claims:
The impact of LLM-powered writing tools on learning will depend on how students use them; how students use ChatGPT remains largely unknown.
In an online study of 70 students completing an essay-writing task, factors such as gender, race, and perceived self-efficacy were found to help predict different AI usage patterns.
Different ChatGPT usage patterns were associated with varying levels of enjoyment and perceived ownership over the essay.

Not stated in the abstract:
Students’ ages, educational levels, recruitment methods, or demographic breakdown.
Whether there was a control condition or random assignment.
The study duration and details of the essay-writing task.
The categories used to characterize ChatGPT queries.
How self-efficacy, enjoyment, perceived ownership, attitudes towards AI, and essay characteristics were measured.
The direction, magnitude, or statistical significance of the reported relationships.
Whether ChatGPT use caused changes in learning, critical engagement, enjoyment, ownership, or essay quality.
```

---

## abs-11: Investigating Conversational Agents to Support Secondary School Students Learning CSP

- [ ] Reviewed
- Source: [2604.16213v1](https://arxiv.org/abs/2604.16213v1) · 152 words

*Reviewer flag:* Claim 1 is background about CSP students using web resources. The abstract reports no actual results, so the gold's real content is the "Not stated" list.

**Abstract**

> Secondary school students enrolled in the AP Computer Science Principles (CSP) course commonly utilize web resources (e.g., tutorials, Q\&A sites) to better understand key concepts in the curriculum. The primary obstacle to using these resources is finding information appropriate for the learning task and student's background. In addition to web search, conversational agents are increasingly a viable alternative for CSP students. In this paper, we study the potential of conversational agents to aid secondary school students as they acquire knowledge on CSP concepts. We explore general purpose, generative conversational agents (e.g., ChatGPT) and custom, fixed-response conversational agents built specifically to aid CSP students. We present results from classroom use by 45 high school students in grades 9-11 (ages 14-17) across six CSP sections. Our main contributions are in better understanding how conversational agents can help CSP students and an evaluation of the effectiveness and engagement of different approaches for CSP exploratory search.

**Draft target**

```target
Key claims:
Secondary school students enrolled in AP Computer Science Principles (CSP) commonly use web resources to better understand curriculum concepts; the primary obstacle is finding information appropriate to the learning task and the student’s background.
The study explores the potential of general-purpose, generative conversational agents and custom, fixed-response conversational agents to help secondary school students acquire knowledge of CSP concepts.
The paper presents results from classroom use by 45 high school students in grades 9–11, ages 14–17, across six CSP sections, including an evaluation of effectiveness and engagement for different CSP exploratory search approaches.

Not stated in the abstract:
The specific effectiveness or engagement results, including whether either agent approach performed better.
Whether conversational agents improved learning compared with web search or another control condition.
The study duration and frequency of agent use.
How students were recruited or assigned to different approaches.
The specific learning tasks, agent implementations, and measures used to assess effectiveness and engagement.
```

---

## abs-12: VArsity: Can Large Language Models Keep Power Engineering Students in Phase?

- [ ] Reviewed
- Source: [2507.20995v1](https://arxiv.org/abs/2507.20995v1) · 123 words

*Reviewer flag:* The abstract gives no numbers ("most students", "much more difficult"). This tests whether the workflow adds quantities.

**Abstract**

> This paper provides an educational case study regarding our experience in deploying ChatGPT Large Language Models (LLMs) in the Spring 2025 and Fall 2023 offerings of ECE 4320: Power System Analysis and Control at Georgia Tech. As part of course assessments, students were tasked with identifying, explaining, and correcting errors in the ChatGPT outputs corresponding to power factor correction problems. While most students successfully identified the errors in the outputs from the GPT-4 version of ChatGPT used in Fall 2023, students found the errors from the ChatGPT o1 version much more difficult to identify in Spring 2025. As shown in this case study, the role of LLMs in pedagogy, assessment, and learning in power engineering classrooms is an important topic deserving further investigation.

**Draft target**

```target
Key claims:
1. The paper presents an educational case study of deploying ChatGPT in the Fall 2023 and Spring 2025 offerings of ECE 4320: Power System Analysis and Control at Georgia Tech.
2. As part of course assessments, students were tasked with identifying, explaining, and correcting errors in ChatGPT outputs for power factor correction problems.
3. Most students successfully identified errors in GPT-4 outputs in Fall 2023, while students found errors in ChatGPT o1 outputs much more difficult to identify in Spring 2025.
4. The case study identifies the role of LLMs in power engineering pedagogy, assessment, and learning as an important topic deserving further investigation.

Not stated in the abstract:
1. The number of students in either course offering or their backgrounds and prior experience with LLMs.
2. The specific problems, prompts, outputs, and errors used in the assessments.
3. Quantitative error-identification results or how success and difficulty were measured.
4. Whether the assessments and instructional conditions were comparable across offerings, or whether there was a control condition.
5. The duration of the activities and their effects on student learning or retention.
```

---
