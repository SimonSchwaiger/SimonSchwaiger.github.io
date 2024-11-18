<h1 align="center">
Open Loop Robot Control using Deep Q-Learning
</h1>

<h3 align="center">
Simon Schwaiger<sup>1</sup>, Ali Aburaia<sup>1</sup>, Mohamed Aburaia<sup>1</sup> and Wilfried Wöber<sup>1</sup>
</h3>

<i align="center">

<sup>1</sup> University of Applied Sciences Technikum Wien, Faculty of Industrial Engineering, 1200 Vienna, Austria

<a href="mailto:novotny@technikum-wien.at">schwaige@technikum-wien.at</a>

</i>

<table align="center" style="border-collapse: collapse; max-width: 100pt;">
  <tr>
    <td align="middle" style="border: none;">
      <a href="https://www.researchgate.net/publication/363480276_Open_Loop_Robot_Control_using_Deep_Q-Learning" style="color: white; font-size: 14pt;">
        <div style="background-color: #363636; border-radius: 50px; padding: 10px 20px; color: white; width: 80pt;">
            <img src="img/document_icon.png" height="14" style="transform:translate(-10%,-1px);"> Paper
        </div>
      </a>
    </td>
  </tr>
</table>

<h2 align="center"> Abstract</h2>

<i align="center">

Motion planning is essential for any robot application. Since motion planning algorithms require explicit knowledge about the configuration, constraints and physical parameters of the robot, motion planning algorithms are often specific to a certain robot configuration or robotics task. While reinforcement learning can be used to have a robot learn to achieve a task, these implementations are typically done as end-to-end solutions, where a model is trained on a real robot, taking raw sensor data as the input and outputting joint torque. For this type of system, however, training typically has to be performed on the real robot. We implement and evaluate a system that trains a neuronal network to determine robot trajectory in simulation instead of the real robot. We create a modular system for robot arm control, where joints are controlled by an open loop controller, while kinematics and trajectory planning are done using a reinforcement learning model. The model is trained in simulation using multi-goal reinforcement learning, allowing one neuronal network to plan a path to multiple arbitrary goal points. We train models using training optimisations such as reward shaping and hindsight experience replay. The results show that motion planning can be performed by the presented approach, allowing an autonomously trained neuronal network to determine robot movement and adapt to changing goals and a changing environment.

</i>

***************************************

## Citation

If you use this work in your research, please cite our paper:

```bibtex
@inproceedings{Schwaiger2021Open,
    author			= {Schwaiger, Simon and Aburaia, Ali and Aburaia, Mohamed and Wöber, Wilfried},
    title				= {Open Loop Robot Control using Deep {Q}-Learning},
    editor      = {Kubinger, Wilfried and Brandstötter, Mathias and Schöffmann, Christian and Vincze, Markus},
    booktitle		= {Proceedings of the Austrian Robotics Workshop 2021},
    month				= {10.-11. June},
    address  		= {Vienna, Austria},
    pages				= {12-17},
    year        = {2021},
    isbn        = {978-3-200-07799-7}
}
```