<h1 align="center">
Open Loop Robot Control using Deep Q-Learning
</h1>

<h3 align="center">
Simon Schwaiger<sup>1</sup>, Mohamed Aburaia<sup>1</sup>, Ali Aburaia<sup>1</sup> and Wilfried Wöber<sup>1</sup>
</h3>

<i align="center">

<sup>1</sup> University of Applied Sciences Technikum Wien, Faculty of Industrial Engineering, 1200 Vienna, Austria

<a href="mailto:novotny@technikum-wien.at">schwaige@technikum-wien.at</a>

</i>

<table align="center" style="border-collapse: collapse; max-width: 100pt;">
  <tr>
    <td align="middle" style="border: none;">
      <a href="https://www.researchgate.net/publication/357035371_Explainable_Artificial_Intelligence_For_Robot_Arm_Control" style="color: white; font-size: 14pt;">
        <div style="background-color: #363636; border-radius: 50px; padding: 10px 20px; color: white; width: 80pt;">
            <img src="img/document_icon.png" height="14" style="transform:translate(-10%,-1px);"> Paper
        </div>
      </a>
    </td>
  </tr>
</table>

<h2 align="center"> Abstract</h2>

<i align="center">

In this paper, we investigate reinforcement learning model explainability through a pick and place task. Two robots withthree degrees of freedom learned to solve the pick and place task in simulation as well as reality. To investigate theexplanatory factors implicitly learned by the models, we derive robot parameters, i.e., the length of the robot segments.To overcome the black box nature of reinforcement learning models and provide a physical explanation of the results, therobot dimensions are derived from the learned reinforcement learning model and compared to the real dimensions. Thehypothesis in the presented work is that converged reinforcement learning models must learn the robot parametersimplicitly in order to learn a task. This transforms black box models into white box models, where each model’s decisionscan be interpreted. Our experiments show that robot parameters can be derived from learned models and that the chosenreinforcement learning model implicitly learns physical context. In order to create robust and trustworthy AI systems forintelligent factories, we suggest that a physical interpretation of all black box models must be done.

</i>

***************************************

## Citation

If you use this work in your research, please cite our paper:

```bibtex
@inproceedings{Schwaiger2021Explainable,
    author			= {Schwaiger, Simon and Aburaia, Ali and Aburaia, Mohamed and Wöber, Wilfried},
    title				= {Explainable Artificial Intelligence For Robot Arm Control},
    editor      = {Katalinic, Branko},
    booktitle		= {Proceedings of the 32nd DAAAM International Symposium},
    month				= {27.-30. October},
    address 		= {Vienna, Austria},
    pages				= {0640-0647},
    year        = {2021},
    publisher   = {DAAAM International},
    isbn        = {978-3-200-07799-7}
}
```