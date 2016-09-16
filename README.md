# Texas Hold'em AI 🤖
CS Independent Study @UVa

Overview
--------
This is an independent study on the application of current machine learning techniques into Texas Hold’em AI.

Possible Topic(s)
-----------------
**Topic: Pre-flop Decisions.**

When we play the poker game as human, the pre-flop situation emotionally and strategically determines how we play the whole round of game. As the beginning stage of the machine prediction, more accurate and simplified calculation at this stage might be helpful to foresee or narrow the result of the entire game.

Rules require strategy of different complexity:

- Kuhn poker
- Leduc Hold’em
- No-limit Hold’em
- Limit Hold'em / Cash game

Three important stages to consider:

- When cards are dealed
    - David Sklansky’s table
    - Expected Hand Strength (EHS)
- When it’s your turn to bet
    - Limp / Raise / Fold decision
    - Stake/blind ratio and Jam/Fold strategy
- When everyone finishes his/her actions
    - Possible range of everyone’s hand


**September 8th update**

**Focusing on first time bet decisions**

- Rational Neural Network
    - logic based on probability & nash equilibrium
    - data derived from rigorous calculation ([EHS](https://en.wikipedia.org/wiki/Poker_Effective_Hand_Strength_(EHS)_algorithm))
    - regression between hand strengths and bet sizes

- Artful Neural Network
    - logic based on professional strategies
    - from real world data
    - deep learning (???)

- Input
	- previous opponent bet size
	- pocket hand strength

- Output
	- randomness(could be a normal ditribution)
	- opoenent hand strength
	- bet size
	- consistent strategies	 in rest of game

**September 15th update**

**Randomness in Training**

1. Probabilistic trend prediction
    - Based on results from rational neural network
    - For each input, output a probabilistic distribution of bet sizes
    - Example: distribution of 27 (Fig. 1) vs. distribution of AA (Fig. 2)

2. Empirical data training
    - Regression on probabilistic trend distribution described above
    - Use artful neural network to add noise to the curve
    - Example: distribution of AA before regression (Fig. 2) vs. distribution of AA after regression (Fig. 3)

3. Randomness in betting consistency
    - Use randomness to "explore" around the distribution curve
    - Indeterministic betting strategies without predictable patterns
    - Example: how randomness "explores" around distribution curve of AA (Fig. 4)


Milestones
----------
1. Learn different machine learning techniques and decide the specify aspect our research project will focus on.

2. Look for the proper dataset to train the netrual network and compare the results of different training methodology.

3. Integrate the project API into current AI bot and finish the research paper

Datasets
--------
- Standardization
    - pot size
    - player level
- Remove possible error
    - unreasonable plays
- Additional information
    - player waiting time
    - ...

Resources
---------
- Machine Learning
    - Framework
    - Relavant Reports
        - *End of Code* by [Wired](http://www.wired.com/2016/05/the-end-of-code/)
        - *Why Randomness is Important for Deep Learning* [Link](http://blog.evjang.com/2016/07/randomness-deep-learning.html)
    - Research Paper
	    - *Deep Reinforcement Learning from Self-Play in Imperfect-Information Games* [PDF](http://arxiv.org/pdf/1603.01121v2.pdf)
	    - *Mastering the Game of Go with Deep Neural Networks and Tree Search* [PDF](https://gogameguru.com/i/2016/03/deepmind-mastering-go.pdf)
- Game Theory
- Behavior Theory
- Poker Strategy
    - the Poker Bank [link](http://www.thepokerbank.com)
- Related Course
    - [CS6501 Poker](http://www.cs.virginia.edu/evans/poker/)
    - AI Strategies for Solving Poker Texas Hold'em [Slides](http://www.slideshare.net/GiovanniMurru/ai-strategies-for-solving-poker-texas-holdem)
- Research Paper
    - [Claudico Overview](http://reports-archive.adm.cs.cmu.edu/anon/anon/home/ftp/2015/CMU-CS-15-104.pdf)


Setup
-----



Update Timeline
---------------

- Sep. 3rd Project Setup
    - github init



Acknowledge
-----------

Thanks Prof. David Evans for the instructions and supports.

Contact Us
----------

- Current Collaborators
    - Charlie Wu [jw7jb@virginia.edu](mailto:jw7jb@virginia.edu)
    - Tong Qiu [tq7bw@virginia.edu](mailto:tq7bw@virginia.edu)
