---
layout: post
title: A/B Testing - Policy and Ethics for Experiments
categories: Statistics
description: Personal Notes
keywords:
mathjax: true
---


<center>

# A/B Testing - Policy and Ethics for Experiments
</center>


**Four Principles of IRB** (IRB, Institutional review board 是一个通过审查拟议的研究方法来应用研究伦理以确保它们是道德的委员会)

### (1) First Principle: Risk
First, in the study, *what risk is the participant undertaking?* The main threshold is whether the risk exceeds that of “minimal risk”. **Minimal risk** is defined as <u>the probability and magnitude of harm that a participant would encounter in normal daily life</u>. The harm considered encompasses physical, psychological and emotional, social, and economic concerns. If the risk exceeds minimal risk, then informed consent (知情同意) is required.

### (2) Second Principle: Benefits
Next, *what benefits might result from the study?* Even if the risk is minimal, how might the results help? <u>In most online A/B testing, the benefits are around improving the product</u>. In other social sciences, it is about understanding the human condition in ways that might help, for example in education and development. In medicine, the risks are often higher but the benefits are often around improved health outcomes.

It is important to be able to state what the benefit would be from completing the study.

### (3) Third Principle: Alternatives
Third, *what other choices do participants have?* For example, if you are testing out changes to a search engine, participants always have the choice to use another search engine. The main issue is that <u>the fewer alternatives that participants have, the more issue that there is around coercion and whether participants really have a choice in whether to participate or not, and how that balances against the risks and benefits</u>.

In online experiments, the issues to consider are what the other alternative services that a user might have, and what the switching costs might be, in terms of time, money, information, etc.

### (4) Fourth Principle: Data Sensitivity
Finally, *what data is being collected, and what is the expectation of privacy and confidentiality*? This last question is quite nuanced, encompassing numerous questions:
- Do participants understand what data is being collected about them?
- What harm would befall them should that data be made public?
- Would they expect that data to be considered private and confidential?

For example, if participants are being observed in a public setting (e.g., a football stadium), there is really no expectation of privacy. If the study is on existing public data, then there is also no expectation of further confidentiality.

If, however, new data is being gathered, then the questions come down to:
- What data is being gathered? How sensitive is it? Does it include financial and health data?
- Can the data being gathered be tied to the individual, i.e., is it considered personally identifiable?
- How is the data being handled, with what security? What level of confidentiality can participants expect?
- What harm would befall the individual should the data become public, where the harm would encompass health, psychological / emotional, social, and financial concerns?

For example, often times, collected data from observed “public” behavior, surveys, and interviews, if the data were not personally identifiable, would be considered exempt from IRB review.

**To summarize, there are really three main issues with data collection with regards to experiments**:
1. For new data being collected and stored, how sensitive is the data and what are the internal safeguards for handling that data? E.g., what access controls are there, how are breaches to that security caught and managed, etc.?
2. Then, for that data, how will it be used and how will participants’ data be protected? How are participants guaranteed that their data, which was collected for use in the study, will not be used for some other purpose? This becomes more important as the sensitivity of the data increases.
3. Finally, what data may be published more broadly, and does that introduce any additional risk to the participants?

### Summary of Principles
Summary: it is a grey area as to whether many of these Internet studies should be subject to IRB review or not and whether informed consent is required. Neither has been common to date.

Most studies, due to the nature of the online service, are likely minimal risk, and the bigger question is about data collection with regards to identifiability, privacy, and confidentiality / security. That said, arguably, a neutral third party outside of the company should be making these calls rather than someone with a vested interest in the outcome. One growing risk in online studies is that of bias and the potential for discrimination, such as differential pricing and whether that is discriminatory to a particular population for example. Discussing those types of biases is beyond the scope of this course.

Our recommendation is that there should be internal reviews of all proposed studies by experts regarding the questions:
- Are participants facing more than minimal risk?
- Do participants understand what data is being gathered?
- Is that data identifiable?
- How is the data handled?

And if enough flags are raised, that an external review happen.




