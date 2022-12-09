<!-- ---
待完善，暂不发布
layout: post
title: ISYE6334 Markov Chains
categories: Supply-Chain
description:
keywords: SCE, Supply-Chain, ISYE6334
mathjax: true
topmost: true
--- -->

# Discrete-Time Markov Chains
vs. Continuous-Time Markov Chains

# 6.1 Definition of DTMC
A DTMC has the following elements:
1. $X_n$ System state at $n$
   e.g. number of heads after $n$ tosses, or inventory level at the end of week $n$
2. $S$ State space: set of possible outcomes(possible values of $x_n$)
3. $\mathbf{P}=[P_{ij}]$ Transition(probability) matrix:
   $$P_{ij}=Pr\Big(X_{n+1}=j\vert X_n=i\Big)$$
4. $\mathbf{a}^{(0)}$ Initial(state) distribution
   $$a^{(0)}_i=Pr(X_0=i)$$

> **Def 1: DTMC** 
> A discrete time stochastic process $X=\{X_n\}$ is a DTMC on state space $S$ with transition matrix $\mathbf{P}$ if 
> $$P_{ij}=Pr\{X_{n+1}=j\vert X_n=i\}=Pr\{X_{n+1}=j\vert X_0=i_0,...,X_n=i\}$$
> 
> In other words, <span style="background-color: yellow; color: black;">future state only depends on the most recent state</span>







