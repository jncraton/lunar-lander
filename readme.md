Lunar Lander
============

A lunar landing simulation lab

![Lander animation](https://gymnasium.farama.org/_images/lunar_lander.gif)

Learning Objectives
-------------------

After completing this lab, students will be able to:

- Design a simple agent
- Examine agent percepts to produce actions

Installation
------------

- Clone this repository
- `pip3 install --upgrade -r requirements.txt`

Running
-------

`python3 lander.py`

The agent will run once with visual output followed by a number of runs to compute an average reward.

Task
----

Improve the `agent` function so that a higher average reward is earned. It should be possible to average a reward over 50 with a simple reflex-based agent.

Resources
---------

- Documentation for the [Lunar Lander](https://gymnasium.farama.org/environments/box2d/lunar_lander/) environment

Installation issues
-------------------

If you encounter issues during installation, the following command may be helpful:

```sh
pip install --upgrade pip wheel setuptools
```
