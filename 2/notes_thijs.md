# Notes for chaper 2

Combinatie van tekstfragmenten van het boek en eigen samenvattingen.  

- An _agent_ is anything that can be viewed as perceiving it's _environment_ through _sensors_ and acting upon that environment through _actuators_.
- _rational agent_: an agent that does the right and optimal thing, based on a _performance measure_
  - Definition of a _rational agent_: For each possible percept sequence, a rational agent should select an action that is expected to maximize its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge the agent has.
- _omniscience agent_: An omniscient agent knows the actual outcome of its actions and can act accordingly; but omniscience is impossible in reality.
- _simple reflex agent_: Act solely upon the current perception based on an condition-action-rule.
- _model-based reflex agent_: Agent with internal state, makes a model of the world based on the perceived part of the environment.
- _goal-based agent_: act to achieve their goals
- _utility-based agents_ try to maximize their own expected "happiness"
- _percept_: the agent's perceptual inputs at any given instant.
- _percept sequence_: the complete history of everything the agent has ever perceived.
- De door de agent gekozen actie kan alleen gebaseerd worden op de huidige percept óf op de (of een deel van) percept sequence. De agent kan geen acties baseren op dingen die de agent nog niet heeft perceived.
- _agent function_: maps any given percept sequence to an action, abstract mathematical description, possibly unachievable in real world scenarios.
- _agent program_: concrete implementation of the agent function, the task of the AI expert/student
- _Task environment_ is beschreven door _PEAS_: Performance measure, environment, actuators, sensors: zie `./2/Notes.ipynb`. In designing an agent, the first step must always be to specify the task environment as fully as possible.
- _competitive multiagent environment_: environment waarbij agents hun eigen belang nagaan.
- _cooperative multiagent environment_: to maximise the performance measure of all agents.
- De moeilijkste environment is een combinatie van: partially observable, multiagent, stochastic, sequential, dynamic, continous en unknown: zie `./2/Notes.ipynb`.
