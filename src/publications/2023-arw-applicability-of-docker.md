<h1 align="center">
On the Applicability of Docker Containers and systemd Services for Search and Rescue Applications
</h1>

<h3 align="center">
Georg Novotny<sup>1</sup>, Simon Schwaiger<sup>1</sup>, Lucas Muster<sup>1</sup>, Mohamed Aburaia<sup>1</sup> and Wilfried Wöber<sup>1</sup>
</h3>

<i align="center">

<sup>1</sup> University of Applied Sciences Technikum Wien, Faculty of Industrial Engineering, 1200 Vienna, Austria

<a href="mailto:novotny@technikum-wien.at">novotny@technikum-wien.at</a>

</i>

<table align="center" style="border-collapse: collapse; max-width: 300pt;">
  <tr>
    <td align="middle" style="border: none;">
      <a href="https://www.joanneum.at/fileadmin/ROBOTICS/ARW_Proceedings/2023_ARW_Proceedings.pdf" style="color: white; font-size: 14pt;">
        <div style="background-color: #363636; border-radius: 50px; padding: 10px 20px; color: white; width: 80pt;">
            <img src="img/document_icon.png" height="14" style="transform:translate(-10%,-1px);"> Paper
        </div>
      </a>
    </td>
    <td align="middle" style="border: none;">
      <a href="https://github.com/TW-Robotics/search-and-rescue-robot-2024" style="color: white; font-size: 14pt;">
        <div style="background-color: #363636; border-radius: 50px; padding: 10px 20px; color: white; width: 80pt;">
            <img src="img/logo_github.png" height="14" style="transform:translate(-10%,-1px);"> Code
        </div>
      </a>
    </td>
    <td align="middle" style="border: none;">
      <a href="https://www.researchgate.net/publication/370299803_On_the_Applicability_of_Docker_Containers_and_systemd_Services_for_Search_and_Rescue_Applications" style="color: white; font-size: 14pt;">
        <div style="background-color: #363636; border-radius: 50px; padding: 10px 20px; color: white; width: 80pt;">
            <img src="img/logo_arxiv.png" height="14" style="transform:translate(-10%,-1px);"> ArXiv
        </div>
      </a>
    </td>
  </tr>
</table>

<h2 align="center"> Abstract</h2>

<i align="center">

The use of robotics in search and rescue operations has grown in recent years, as these systems have the potentialto greatly improve the efficiency and effectiveness of rescueefforts. However, developing and maintaining robotics systemsfor search and rescue applications can be challenging. Thesesystems often operate in harsh and unpredictable environments,which demands high autonomy and intelligent behavior of therobots. Such robots are developed based on a vast amountof (open source) software solutions, which force robotic engi-neers to focus on systems engineering instead of applicationimplementation. One way to address robot maintenance isto use containerization and service management technologies,such as Docker containers and systemd services, to managethe software and resources on the robotics platform. Dockercontainers allow applications and their dependencies to bepackaged in a portable, isolated environment, while systemdprovides a reliable and flexible way to manage system processes.In addition, monitoring tools can be used to track systemresources and alert human supervisors to potential issues, whiledeployment tools can streamline the process of deploying andmaintaining the robotics platform.This paper tackles the identification and presentation ofuseful tools for robotic system maintenance focusing on searchand rescue robots. We aim to provide a guideline for the roboticsystem maintenance process, and explore the applicability ofDocker containers, systemd services, and other tools for searchand rescue robotics applications. We discuss the benefits andpotential challenges of using these technologies, and provideexamples for application. Through our analysis, we aim toprovide insight into the potential of containerization, servicemanagement, monitoring, and deployment technologies to en-hance the capabilities of search and rescue robotics systems.We hope that our study will simplify the development andmaintenance procedure for robotic system development.

</i>

***************************************

## Citation

If you use this work in your research, please cite our paper:

```bibtex
@inproceedings{Novotny2023,
  author    = {Georg Novotny and Simon Schwaiger and Lucas Muster and Mohamed Aburaia and Wilfried W{\"o}ber},
  editor    = {Andreas Müller and Manfred Nader and Hubert Gattringer},
  isbn      = {978-3-200-08957-0},
  journal   = {Proceedings of the Austrian Robotics Workshop},
  month     = {4},
  pages     = {19-24},
  publisher = {Johannes Kepler University},
  title     = {On the Applicability of Docker Containers and systemd Services for Search and Rescue Applications},
  url       = {https://www.joanneum.at/fileadmin/ROBOTICS/ARW_Proceedings/2023_ARW_Proceedings.pdf},
  year      = {2023}
}
```