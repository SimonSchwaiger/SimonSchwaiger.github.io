<h1 align="center">
From Words to Poses: Enhancing Novel Object Pose Estimation with Vision Language Models
</h1>

<h3 align="center">
Tessa Pulli<sup>1</sup>, Stefan Thalhammer<sup>2</sup>, Simon Schwaiger<sup>2</sup> and Markus Vincze<sup>1</sup>
</h3>

<i align="center">

<sup>1</sup> Vision for Robotics Laboratory, Automation and Control Institute, TU Wien, Austria

<sup>2</sup> University of Applied Sciences Technikum Wien, Faculty of Industrial Engineering, 1200 Vienna, Austria

<a href="mailto:pulli@acin.tuwien.ac.at">pulli@acin.tuwien.ac.at</a>

</i>

<table align="center" style="border-collapse: collapse; max-width: 300pt;">
  <tr>
    <td align="middle" style="border: none;">
      <a href="https://arxiv.org/pdf/2409.05413" style="color: white; font-size: 14pt;">
        <div style="background-color: #363636; border-radius: 50px; padding: 10px 20px; color: white; width: 80pt;">
            <img src="img/document_icon.png" height="14" style="transform:translate(-10%,-1px);"> Paper
        </div>
      </a>
    </td>
    <td align="middle" style="border: none;">
      <a href="" style="color: white; font-size: 14pt;">
        <div style="background-color: #363636; border-radius: 50px; padding: 10px 20px; color: white; width: 80pt;">
            <img src="img/logo_github.png" height="14" style="transform:translate(-10%,-1px);"> Code
        </div>
      </a>
    </td>
    <td align="middle" style="border: none;">
      <a href="https://arxiv.org/abs/2409.05413" style="color: white; font-size: 14pt;">
        <div style="background-color: #363636; border-radius: 50px; padding: 10px 20px; color: white; width: 80pt;">
            <img src="img/logo_arxiv.png" height="14" style="transform:translate(-10%,-1px);"> arXiv
        </div>
      </a>
    </td>
  </tr>
</table>

<h2 align="center"> Abstract</h2>

<i align="center">

Robots are increasingly envisioned to interact in real-world scenarios, where they must continuously adapt to new situations. To detect and grasp novel objects, zero-shot
pose estimators determine poses without prior knowledge. Recently, vision language models (VLMs) have shown considerable advances in robotics applications by establishing an understanding between language input and image input. In our work, we take advantage of VLMs zero-shot capabilities and translate this ability to 6D object pose estimation. We propose a novel framework for promptable zero-shot 6D object pose estimation using language embeddings. The idea is to derive a coarse location of an object based on the relevancy map of a language-embedded NeRF reconstruction and to compute the pose estimate with a point cloud registration method. Additionally, we provide an analysis of LERF’s suitability for open-set object pose estimation. We examine hyperparameters, such as activation thresholds for relevancy maps and investigate the zero-shot capabilities on an instance- and category-level. Furthermore, we plan to conduct robotic grasping experiments in a real-world setting.

</i>

***************************************

## Citation

If you use this work in your research, please cite our paper:

```bibtex
@misc{Pulli2024FromWords,
    title               = {From Words to Poses: Enhancing Novel Object Pose Estimation with Vision Language Models. \textit{arXiv preprint arXiv:2409.05413}}, 
    author              = {Tessa Pulli and Stefan Thalhammer and Simon Schwaiger and Markus Vincze},
    year                = {2024},
    url                 = {https://arxiv.org/abs/2409.05413}
}
```