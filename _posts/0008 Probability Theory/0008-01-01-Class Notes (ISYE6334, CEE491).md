---
layout: post
title: Class Notes (ISYE6334, CEE491)
categories: Probability Theory
description: Personal Notes
keywords: CEE491，Risk-Analysis，Probability, Decision
mathjax: true
---

# 1. Basic Probability
> **Types of uncertainties**

- Inherent variability or randomness
- Statistical uncertainty
- Measurement error
- Model error
- Human error

Statistical uncertatinty could be reduced through accumulation of data.

## 1.1 Trial, Sample, Event

**Trials** (experiments or observations):
- probability is concerned with the outcome of trials
- trail refers to an event whose outcome is unknown

**Sample Space** $S$: 
- the collection of all possible outcomes of a trial


**Sample Point** $x$: each indivisual outcome
**Event** $E$: any collection of sample points

General relation: $x\in S$, $E\subseteq S$, $S=\bar{E}\cup E$
Special case: $E=S$: certain event; $E=\empty$: null event

$P(E)$: likelihood of occurrence of event $E$ in its sample space $S$
> **Axioms:**
(1) $P(E)\geq 0$
(2) $P(S)=1$
(3) $P(\bar{E})= 1-P(E)$

## 1.2 Permutation, Combination
**Permutation**: 从 n 个人中挑选 k 个排成一列，有多少种挑选及排列方式

$$n\text{P}k=\frac{n!}{(n-k)!}$$

**Combination**: 从 n 个人中挑选 k 个，有多少种挑选方式

$$n\text{C}k=\frac{n!}{(n-k)!k!}$$


## 1.3 Relationship between Events
**Mutually exclusive**: $EF=\empty$ (不能同时发生)
- $P(E\cup F)=P(E) + P(F)$ if mutually exclusive
- $P(E\cup F)=P(E) + P(F) - P(E,F)$ if not mutually exclusive

**Independent**: $P(E,F)=P(E)P(F)$
- $P(E,F)=P(E)P(F\vert E)$ if dependent
- $P(E\vert F)=P(E)$ in other words

<span style="background-color: yellow; color: black;">Two mutually exlusive events are dependent</span>, 因为如果一个发生我们就知道另一个不会发生 ($P(E,F)=0$)

**Conditional Independent**:
$$p(x,y\vert z)=p(x\vert z)p(y\vert z)$$ 


**Complementary**: $E\bar{F}=\emptyset$

**Collective exhaustive** events: $\bigcup_{i=1}^M  E_i=S$



# 2. Multiple Events
For multiple events: $E_1,E_2,...,E_M$

## 2.1 Associate Properties
(1) $(E_1\cup E_2)\cup E_3 = E_1\cup(E_2 \cup E_3) = E_1\cup E_2\cup E_3$

(2) $(E_1E_2)E_3 = E_1(E_2E_3) = E_1E_2E_3$

## 2.2 De Morgan's Rules
$$\tag{2.1}\overline{\bigcup_{i=1}^M  E_i}=\bigcap_{i=1}^M \overline{E_i}$$

That is $\overline{E_i\cup E_2\cup...\cup E_M}=\overline{E_1}...\overline{E_M}$

$$\tag{2}\overline{\bigcap_{i=1}^M  E_i}=\bigcup_{i=1}^M \overline{E_i}$$

That is $\overline{E_1...E_M}=\overline{E_1}\cup\overline{E_1}\cup\overline{E_M}$

> **Representation through circuits**

Let $E_i$ indicates the failure event of $i$-th component, and $E_{sys}$ indicates the whole system's failure. The parallel and series circuits are shown below:

<center>
    <img src="/images/2021-09/011300.jpg" style="zoom:40%"> <br><div style="color: #999;"></div>
</center><br>

Series connections: $E_{sys} = E_1\cup E_2\cup E_3$, &nbsp;&nbsp;&nbsp;&nbsp;$\overline{E_{sys}}=\bar{E_1}\bar{E_2}\bar{E_3}$

Parallel connections: $E_{sys} = E_1E_2E_3$, &nbsp;&nbsp;&nbsp;&nbsp;$\overline{E_{sys}}=\bar{E_1}\cup\bar{E_2}\cup\bar{E_3}$


# 3. Elements of Probability Theory
## 3.1 Inclusion-Exclusion Rule
For simplest case: $P(E_1\cup E_2)=P(E_1) + P(E_2) - P(E_1E_2)$

For general cases:
$$P(\bigcup_{i=1}^nE_i)=\sum_{i=1}^nP(E_i) - \sum_{i=1}^{n-1}\sum_{j=i+1}^nP(E_iE_j)+...+(-1)^{n-1}P(E_1E_2...E_n)$$

#### Conditional Probability

$$P(E_1\vert E_2)=\begin{cases}
   \frac{P(E_1E_2)}{P(E_2)} & P(E_2)\neq 0\\
   0 & P(E_2)= 0
\end{cases}$$

#### Multiplication Rule
$$P(E_1E_2)=P(E_1\vert E_2)\cdot P(E_2)$$

#### Statistical Independence

Two events are **statistically independant (S.I.)** if the occurrence of one event doesn't change the probability of the other, that is, $P(E_1\vert E_2)=P(E_1)$ and $P(E_2\vert E_1)=P(E_2)$. 

Only when $E_1,E_2$ are S.I., the formulation $P(E_1E_2)=P(E_1)\cdot P(E_2)$ works







$$Pr(A\vert B)=\frac{Pr(A\cap B)}{Pr(B)}$$

$$Pr(A\cup B)=Pr(A) + Pr(B) - Pr(A\cap B)$$


## 1. Total Probability Rule

Let $E_1,E_2,...,E_M$:

(1) $E_iE_i=\empty$ for any $i\neq j$  
(2) $\bigcup_{i=1}^ME_i=S$

then
$P(A)=\sum_{i=1}^MP(A\vert E_i)P(E_i)$


That's because $=\sum_{i=1}^MP(A, E_i)=P(AE_1\cup...\cup AE_M)=P(A(E_1\cup...\cup E_M))=P(AS)=P(A)$


## 2. Bayes's Rule

$$P(E_1\vert E_2)=\frac{P(E_2\vert E_1)}{P(E_2)}\cdot P(E_1)$$

where
- $P(E_1\vert E_2)$ posterior probability
- $P(E_1)$ prior probability
- $P(E_2\vert E_1)$ likelihood
- $P(E_2)$ normalizing factor
- $P(E_2)=P(E_2\vert E_1)P(E_1) + P(E_2\vert\sim E_1)P(\sim E_1)$



