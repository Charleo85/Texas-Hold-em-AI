# Texas Hold'em AI 🤖
CS Independent Study @UVa

Overview
--------
This is an independent study on the application of current machine learning techniques into Texas Hold’em AI.

Setup
-----
- TensorFlow [documentation](https://www.tensorflow.org/versions/master/api_docs/python/index.html) 
  ``` bash
  # Ubuntu/Linux 64-bit
  $ sudo apt-get install python-pip python-dev
  # Ubuntu/Linux 64-bit, CPU only, Python 3.5
  $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0-cp35-cp35m-linux_x86_64.whl

  # Mac OS X
  $ sudo easy_install pip3
  $ sudo easy_install --upgrade six
  # Mac OS X, CPU only, Python 3.4 or 3.5:
  $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow-0.11.0-py3-none-any.whl
  
  
  $ sudo pip3 install --upgrade $TF_BINARY_URL
  ```
  
  - [Troubleshoot](https://www.tensorflow.org/versions/master/get_started/os_setup.html#common-problems)
  
- Jupyter Notebook  [documentation](http://jupyter.readthedocs.io/en/latest/index.html)
  
  ``` bash
  $ pip3 install --upgrade pip
  $ pip3 install jupyter
  $ jupyter notebook
  ```

[Demo](Demo.ipynb)
------------------

[Timeline](Timeline.md)
-----------------------


Resources
---------
- Machine Learning
    - Framework
		-  Awesome TensorFlow [Link](https://github.com/jtoy/awesome-tensorflow)
		-  TensorFlow Playground [Link](http://playground.tensorflow.org)
		-  Binary Stochastic Neurons in Tensorflow [Link](https://gist.github.com/spitis/34b44190c702ae9e858dd020d2790a17)
    - Relavant Reports
        - *End of Code* by [Wired](http://www.wired.com/2016/05/the-end-of-code/)
        - *Why Randomness is Important for Deep Learning* [Link](http://blog.evjang.com/2016/07/randomness-deep-learning.html)
    - Book
    	- *Neural Networks and Deep Learning* [Link](http://neuralnetworksanddeeplearning.com)
    - Research Paper
	    - *Deep Reinforcement Learning from Self-Play in Imperfect-Information Games* [PDF](http://arxiv.org/pdf/1603.01121v2.pdf)
	    - *Mastering the Game of Go with Deep Neural Networks and Tree Search* [PDF](https://gogameguru.com/i/2016/03/deepmind-mastering-go.pdf)
- Game Theory
	- *prisoner dilemma game* [Link](http://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/index.html)
- Behavior Theory
- Poker Strategy
    - the Poker Bank [link](http://www.thepokerbank.com)
- Related Course
    - [CS221: Artificial Intelligence](http://web.stanford.edu/class/cs221/)
    - [CS6316 Machine Learning](https://www.cs.virginia.edu/yanjun/teach/2016f/index.html)
    - [CS6501 Poker](http://www.cs.virginia.edu/evans/poker/)
    - AI Strategies for Solving Poker Texas Hold'em [Slides](http://www.slideshare.net/GiovanniMurru/ai-strategies-for-solving-poker-texas-holdem)
- Others' work
    - Claudico [Overview](http://reports-archive.adm.cs.cmu.edu/anon/anon/home/ftp/2015/CMU-CS-15-104.pdf)
    - [Slumbot](http://www.slumbot.com)
    - [DeepStack](https://arxiv.org/abs/1701.01724)

Acknowledge
-----------

Thanks Prof. David Evans for the instructions and supports.


Contact Us
----------

- Current Collaborators
    - Charlie Wu [jw7jb@virginia.edu](mailto:jw7jb@virginia.edu)
    - Tong Qiu [tq7bw@virginia.edu](mailto:tq7bw@virginia.edu)
