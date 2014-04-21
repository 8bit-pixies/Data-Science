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
# # Chapter 0  Preface
# 
# ## Why I wrote this book
# 
# _Think Stats: Probability and Statistics for Programmers_ is a textbook for a
# new kind of introductory prob-stat class. It emphasizes the use of statistics
# to explore large datasets. It takes a computational approach, which has
# several advantages:
# 
# * Students write programs as a way of developing and testing their understanding. For example, they write functions to compute a least squares fit, residuals, and the coefficient of determination. Writing and testing this code requires them to understand the concepts and implicitly corrects misunderstandings.
# * Students run experiments to test statistical behavior. For example, they explore the Central Limit Theorem (CLT) by generating samples from several distributions. When they see that the sum of values from a Pareto distribution doesn’t converge to normal, they remember the assumptions the CLT is based on.
# * Some ideas that are hard to grasp mathematically are easy to understand by simulation. For example, we approximate p-values by running Monte Carlo simulations, which reinforces the meaning of the p-value.
# * Using discrete distributions and computation makes it possible to present topics like Bayesian estimation that are not usually covered in an introductory class. For example, one exercise asks students to compute the posterior distribution for the “German tank problem,” which is difficult analytically but surprisingly easy computationally.
# * Because students work in a general-purpose programming language (Python), they are able to import data from almost any source. They are not limited to data that has been cleaned and formatted for a particular statistics tool.
# 
# The book lends itself to a project-based approach. In my class, students work
# on a semester-long project that requires them to pose a statistical question,
# find a dataset that can address it, and apply each of the techniques they
# learn to their own data.
# 
# To demonstrate the kind of analysis I want students to do, the book presents a
# case study that runs through all of the chapters. It uses data from two
# sources:
# 
# * The National Survey of Family Growth (NSFG), conducted by the U.S. Centers for Disease Control and Prevention (CDC) to gather “information on family life, marriage and divorce, pregnancy, infertility, use of contraception, and men’s and women’s health.” (See http://cdc.gov/nchs/nsfg.htm.)
# * The Behavioral Risk Factor Surveillance System (BRFSS), conducted by the National Center for Chronic Disease Prevention and Health Promotion to “track health conditions and risk behaviors in the United States.” (See http://cdc.gov/BRFSS/.)
# 
# Other examples use data from the IRS, the U.S. Census, and the Boston
# Marathon.
# 
# ## How I wrote this book
# 
# When people write a new textbook, they usually start by reading a stack of old
# textbooks. As a result, most books contain the same material in pretty much
# the same order. Often there are phrases, and errors, that propagate from one
# book to the next; Stephen Jay Gould pointed out an example in his essay, “The
# Case of the Creeping Fox Terrier1.”(A breed of dog that is about half the size
# of a [Hyrocotherium](http://wikipedia.org/wiki/Hyracotherium).
# 
# I did not do that. In fact, I used almost no printed material while I was
# writing this book, for several reasons:
# 
# * My goal was to explore a new approach to this material, so I didn’t want much exposure to existing approaches.
# * Since I am making this book available under a free license, I wanted to make sure that no part of it was encumbered by copyright restrictions.
# * Many readers of my books don’t have access to libraries of printed material, so I tried to make references to resources that are freely available on the Internet.
# * Proponents of old media think that the exclusive use of electronic resources is lazy and unreliable. They might be right about the first part, but I think they are wrong about the second, so I wanted to test my theory.
# 
# The resource I used more than any other is Wikipedia, the bugbear of
# librarians everywhere. In general, the articles I read on statistical topics
# were very good (although I made a few small changes along the way). I include
# references to Wikipedia pages throughout the book and I encourage you to
# follow those links; in many cases, the Wikipedia page picks up where my
# description leaves off. The vocabulary and notation in this book are generally
# consistent with Wikipedia, unless I had a good reason to deviate.
# 
# Other resources I found useful were Wolfram MathWorld and (of course) Google.
# I also used two books, David MacKay’s _Information Theory, Inference, and
# Learning Algorithms_, which is the book that got me hooked on Bayesian
# statistics, and Press et al.’s _Numerical Recipes in C_. But both books are
# available online, so I don’t feel too bad.
# 
# **Allen B. Downey**   
# Needham MA    
# Allen B. Downey is a Professor of Computer Science at the Franklin W. Olin
# College of Engineering.  
# 
# ## Contributor List
# 
# If you have a suggestion or correction, please send email to
# `downey@allendowney.com`. If I make a change based on your feedback, I will
# add you to the contributor list (unless you ask to be omitted).
# 
# If you include at least part of the sentence the error appears in, that makes
# it easy for me to search. Page and section numbers are fine, too, but not
# quite as easy to work with. Thanks!
# 
# * Lisa Downey and June Downey read an early draft and made many corrections and suggestions.
# * Steven Zhang found several errors.
# * Andy Pethan and Molly Farison helped debug some of the solutions, and Molly spotted several typos.
# * Andrew Heine found an error in my error function.
# * Dr. Nikolas Akerblom knows how big a Hyracotherium is.
# * Alex Morrow clarified one of the code examples.
# * Jonathan Street caught an error in the nick of time.
# * Gábor Lipták found a typo in the book and the relay race solution.
# * Many thanks to Kevin Smith and Tim Arnold for their work on plasTeX, which I used to convert this book to DocBook.
# * George Caplan sent several suggestions for improving clarity.
# * Julian Ceipek found an error and a number of typos.
# * Stijn Debrouwere, Leo Marihart III, Jonathan Hammler, and Kent Johnson found errors in the first print edition.
# * Dan Kearney found a typo.
# * Jeff Pickhardt found a broken link and a typo.
# * Jörg Beyer found typos in the book and made many corrections in the docstrings of the accompanying code.
# * Tommie Gannert sent a patch file with a number of corrections.
# * Alexander Gryzlov suggested a clarification in an exercise.
# * Martin Veillette reported an error in one of the formulas for Pearson’s correlation.
# * Christoph Lendenmann submitted several errata.
# * Haitao Ma noticed a typo and and sent me a note.
# 
# ----
# 
# # IPython Editor's Note
# 
# One the back of learning more about data analytics I stumbled across this book. 
# I have modified it and distributed it as ipython notebooks. Unfortunately through such a conversion, some information may have been lost. I have tried my best to remain faithful to the original text, but
# if you have found any questionable material feel free to raise a pull request.
# 
# **Chapman Siu**

# <codecell>


