<h1 align="center">
Deep Reinforcement Learning for Continuous Robot Trajectory Control
</h1>

<h3 align="center">
Simon Schwaiger<sup>1</sup>, Mohamed Aburaia<sup>1</sup>, Lucas Muster<sup>1</sup>, Moritz Abdank<sup>1</sup> and Wilfried Wöber<sup>1</sup>
</h3>

<i align="center">

<sup>1</sup> University of Applied Sciences Technikum Wien, Faculty of Industrial Engineering, 1200 Vienna, Austria

<a href="mailto:novotny@technikum-wien.at">schwaige@technikum-wien.at</a>

</i>

<table align="center" style="border-collapse: collapse; max-width: 100pt;">
  <tr>
    <td align="middle" style="border: none;">
      <a href="https://www.researchgate.net/publication/363480631_Deep_Reinforcement_Learning_for_Continuous_Robot_Trajectory_Control" style="color: white; font-size: 14pt;">
        <div style="background-color: #363636; border-radius: 50px; padding: 10px 20px; color: white; width: 80pt;">
            <img src="img/document_icon.png" height="14" style="transform:translate(-10%,-1px);"> Paper
        </div>
      </a>
    </td>
  </tr>
</table>

<h2 align="center"> Abstract</h2>

<i align="center">

Trajectory control is fundamental to any robot application. Probabilistic path planning aims to solve trajectory control without focusing on a specific robot type. Similarly, reinforcement learning has been applied to robot control tasks with the goal of having problems of different nature be solved by the same agent. However, tested reinforcement learning models directly generate actuator control signals from sensor input. Due to the end-to-end nature of proposed implementations, trajectory and closed loop control are performed by the same model. We want to increase modularity in reinforcement learning-based robot control pipelines by solving trajectory and closed loop control separately from each other. Therefore, we formulate a continuous robot trajectory control problem as a reinforcement learning environment and evaluate agent performance for multiple environment configurations. Using this problem formulation, an agent is able to learn robot kinematics in simulation and determine joint trajectories. We deploy multi-goal reinforcement learning in order to allow agents to plan movement from an arbitrary start pose to an arbitrary goal pose without requiring a dedicated training procedure. The problem formulation is evaluated by training recent for continuous control and documenting agent performance. The results show, that continuous trajectory control can be achieved by the presented methods, allowing an agent to learn the kinematics of a six degree of freedom robot.

</i>

***************************************

## Citation

If you use this work in your research, please cite our paper:

```bibtex
Cmoing soon!
```