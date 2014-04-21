# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# This HTML version of is provided for convenience, but it is not the best
# format for the book. In particular, some of the symbols are not rendered
# correctly.
# 
# You might prefer to read the [PDF
# version](http://thinkstats.com/thinkstats.pdf), or you can buy a hardcopy
# [here](http://www.lulu.com/product/paperback/think-stats/12443331).
# 
# 0pt
# 
# Think Stats: Probability and Statistics for Programmers
# 
# Allen B. Downey
# 
# Version 1.6.0
# 
#   
#   
# 
# Copyright 2011 Allen B. Downey
# 
#   
#   
# 
# Permission is granted to copy, distribute, and/or modify this document under
# the terms of the Creative Commons Attribution-NonCommercial 3.0 Unported
# License, which is available at `http://creativecommons.org/licenses/by-
# nc/3.0/`.
# 
#   * [Preface](thinkstats001.html)
#     * [Why I wrote this book](thinkstats001.html#toc1)
#     * [How I wrote this book](thinkstats001.html#toc2)
#     * [Contributor List](thinkstats001.html#toc3)
#   * [Statistical thinking for programmers](thinkstats002.html)
#     * [Do first babies arrive late?](thinkstats002.html#toc4)
#     * [A statistical approach](thinkstats002.html#toc5)
#     * [The National Survey of Family Growth](thinkstats002.html#toc6)
#     * [Tables and records](thinkstats002.html#toc7)
#     * [Significance](thinkstats002.html#toc8)
#     * [Glossary](thinkstats002.html#toc9)
#   * [Descriptive statistics](thinkstats003.html)
#     * [Means and averages](thinkstats003.html#toc10)
#     * [Variance](thinkstats003.html#toc11)
#     * [Distributions](thinkstats003.html#toc12)
#     * [Representing histograms](thinkstats003.html#toc13)
#     * [Plotting histograms](thinkstats003.html#toc14)
#     * [Representing PMFs](thinkstats003.html#toc15)
#     * [Plotting PMFs](thinkstats003.html#toc16)
#     * [Outliers](thinkstats003.html#toc17)
#     * [Other visualizations](thinkstats003.html#toc18)
#     * [Relative risk](thinkstats003.html#toc19)
#     * [Conditional probability](thinkstats003.html#toc20)
#     * [Reporting results](thinkstats003.html#toc21)
#     * [Glossary](thinkstats003.html#toc22)
#   * [Cumulative distribution functions](thinkstats004.html)
#     * [The class size paradox](thinkstats004.html#toc23)
#     * [The limits of PMFs](thinkstats004.html#toc24)
#     * [Percentiles](thinkstats004.html#toc25)
#     * [Cumulative distribution functions](thinkstats004.html#toc26)
#     * [Representing CDFs](thinkstats004.html#toc27)
#     * [Back to the survey data](thinkstats004.html#toc28)
#     * [Conditional distributions](thinkstats004.html#toc29)
#     * [Random numbers](thinkstats004.html#toc30)
#     * [Summary statistics revisited](thinkstats004.html#toc31)
#     * [Glossary](thinkstats004.html#toc32)
#   * [Continuous distributions](thinkstats005.html)
#     * [The exponential distribution](thinkstats005.html#toc33)
#     * [The Pareto distribution](thinkstats005.html#toc34)
#     * [The normal distribution](thinkstats005.html#toc35)
#     * [Normal probability plot](thinkstats005.html#toc36)
#     * [The lognormal distribution](thinkstats005.html#toc37)
#     * [Why model?](thinkstats005.html#toc38)
#     * [Generating random numbers](thinkstats005.html#toc39)
#     * [Glossary](thinkstats005.html#toc40)
#   * [Probability](thinkstats006.html)
#     * [Rules of probability](thinkstats006.html#toc41)
#     * [Monty Hall](thinkstats006.html#toc42)
#     * [Poincaré](thinkstats006.html#toc43)
#     * [Another rule of probability](thinkstats006.html#toc44)
#     * [Binomial distribution](thinkstats006.html#toc45)
#     * [Streaks and hot spots](thinkstats006.html#toc46)
#     * [Bayes’s theorem](thinkstats006.html#toc47)
#     * [Glossary](thinkstats006.html#toc48)
#   * [Operations on distributions](thinkstats007.html)
#     * [Skewness](thinkstats007.html#toc49)
#     * [Random Variables](thinkstats007.html#toc50)
#     * [PDFs](thinkstats007.html#toc51)
#     * [Convolution](thinkstats007.html#toc52)
#     * [Why normal?](thinkstats007.html#toc53)
#     * [Central limit theorem](thinkstats007.html#toc54)
#     * [The distribution framework](thinkstats007.html#toc55)
#     * [Glossary](thinkstats007.html#toc56)
#   * [Hypothesis testing](thinkstats008.html)
#     * [Testing a difference in means](thinkstats008.html#toc57)
#     * [Choosing a threshold](thinkstats008.html#toc58)
#     * [Defining the effect](thinkstats008.html#toc59)
#     * [Interpreting the result](thinkstats008.html#toc60)
#     * [Cross-validation](thinkstats008.html#toc61)
#     * [Reporting Bayesian probabilities](thinkstats008.html#toc62)
#     * [Chi-square test](thinkstats008.html#toc63)
#     * [Efficient resampling](thinkstats008.html#toc64)
#     * [Power](thinkstats008.html#toc65)
#     * [Glossary](thinkstats008.html#toc66)
#   * [Estimation](thinkstats009.html)
#     * [The estimation game](thinkstats009.html#toc67)
#     * [Guess the variance](thinkstats009.html#toc68)
#     * [Understanding errors](thinkstats009.html#toc69)
#     * [Exponential distributions](thinkstats009.html#toc70)
#     * [Confidence intervals](thinkstats009.html#toc71)
#     * [Bayesian estimation](thinkstats009.html#toc72)
#     * [Implementing Bayesian estimation](thinkstats009.html#toc73)
#     * [Censored data](thinkstats009.html#toc74)
#     * [The locomotive problem](thinkstats009.html#toc75)
#     * [Glossary](thinkstats009.html#toc76)
#   * [Correlation](thinkstats010.html)
#     * [Standard scores](thinkstats010.html#toc77)
#     * [Covariance](thinkstats010.html#toc78)
#     * [Correlation](thinkstats010.html#toc79)
#     * [Making scatterplots in pyplot](thinkstats010.html#toc80)
#     * [Spearman’s rank correlation](thinkstats010.html#toc81)
#     * [Least squares fit](thinkstats010.html#toc82)
#     * [Goodness of fit](thinkstats010.html#toc83)
#     * [Correlation and Causation](thinkstats010.html#toc84)
#     * [Glossary](thinkstats010.html#toc85)
#   * [Index](thinkstats011.html)

# <codecell>


