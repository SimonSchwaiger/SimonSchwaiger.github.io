# Professional Work

---

## UGV-CBRN Robot

A search and rescue robot for exploring disaster vicinities, radiation mapping and sampling of potentially hazardous substances. The robot was developed as part of the FFG-funded research project UGV-ABC Probe with my research focus being the implementation of Lidar-based autonomous navigation as well as 3D vision and an assisted teleoperation system. The robot's hardware and software architectures are described in the publication <b><a href="https://simonschwaiger.github.io/2024-ugv-cbrn.html" target=”_blank”>UGV-CBRN: An Unmanned Ground Vehicle for Chemical, Biological, Radiological, and Nuclear Disaster Response (Link)</a></b>.

<center><img src="./img/projects/sieglindeNoBackground.png" alt="ROS ML Container Demo" style="max-width: 20%" /></center>

---

## ODIN Robot

**O**bjective-**D**riven **I**ntelligent **N**avigator is an autonomous outdoor robot for logistics duties around the UAS Technikum campus and in agricultural use cases. My main role on this robot was the conversion of the original teleoperated chassis to full Lidar-based autonomy, including reverse-engingeering the electronics, changing the main control board and converting the controller to use the robot operating system (ROS). The robot is further described in our publication <b><a href="https://simonschwaiger.github.io/2024-ei-towards-full-autonomy.html" target=”_blank”>Towards full Autonomy in Mobile Robot Navigation and Manipulation (Link)</a></b>.

<center><img src="./img/projects/ODIN_white_background.png" alt="ROS ML Container Demo" style="max-width: 25%" /></center>

---

## Application-Driven Mobile Robotics Courses

Apart from teaching existing courses, I have designed five courses on data-driven robotics, leveraging commonly used open-source robotics tools. The content ranges from introductory courses on sensor- and planning-based robot control to master lectures on geometric and semantic environment analysis. Details regarding my courses are provided in the <b><a href="https://simonschwaiger.github.io/teaching.html" target=”_blank”>Teaching Experience section (link)</a></b>

<center><img src="./img/projects/moro_mpc_demo.gif" alt="ROS ML Container Demo" style="max-width: 70%" /></center>

---

<h2><a href="https://github.com/TW-Robotics/AIAV" target=”_blank”>AIAV Website and Blogposts</a></h2>

The AIAV (AI Anwenden und Verstehen) research project aims to explain fundamental and state of the art concepts from the domain of artifical intelligence (AI) to small and medium-sized businesses. Apart from presenting fundamental theory surrounding AI, our website also presents blog posts about practical AI use cases and a list of institutions in Austria working on AI. Over the course of the project, I have implemented multiple use cases and written blog posts about them. Furthermore, I was heavily involved in website design and administration and have coordinated contributions in our main repository.

* <b><a href="https://www.aiav.technikum-wien.at/post/wanderung-in-richtung-des-geringsten-fehlers-wie-programme-lernen" target=”_blank”>Link to Blogpost on AIAV Website (in German)</a></b>
* <b><a href="https://github.com/TW-Robotics/AIAV" target=”_blank”>Link to Main Use Case Repository</a></b>


</div>
<div class="w3-card-4 w3-margin w3-white" style="padding: 15pt;">

# Personal Projects

---

<h2><a href="https://github.com/SimonSchwaiger/ros-ml-container" target=”_blank”>ROS Machine Learning Container</a></h2>

Docker-based ROS development environment combining scientific computing frameworks such as PyTorch and Scikit-Learn with ROS (2), making the workspace somewhat portable. Additionally, graphics acceleration methods can be set based on your GPU's vendor. It bridges the gap between modern Python, web tools and robotics applications.

This workspace was originally created for my master thesis, but is now used by students and lecturers at UAS Technikum Wien's robotics group and serves as the basis of my homelab's machine learning instances. Common configurations are pre-built using GitHub workflows and hosted in the GitHub container registry.
<center><img src="./img/projects/mlContainerDemo.png" alt="ROS ML Container Demo" style="max-width: 70%" /></center>

---

<h2><a href="https://github.com/SimonSchwaiger/tinysim-2d" target=”_blank”>Tinysim</a></h2>

A lightweight time-discrete mobile robot simulator for ROS 2. It can reconstruct simulation scenes from recorded sensor data (3D or 2D maps) and simulate various laser scanners and depth sensors using Open3D as the underlying engine.
<center><img src="./img/projects/tinysimDemo.gif" alt="Simulator Demo" style="max-width: 70%" /></center>

---

<h2><a href="https://github.com/SimonSchwaiger/SimonSchwaiger.github.io" target=”_blank”>Academic Website Template</a></h2>

This website's template is written in CSS and HTML accompanied by a simple Python-based build script. The website is built and styled from content written in Markdown, allowing me to quickly add and edit content. The site is built using GitHub workflows and deployed on GitHub pages.

---

<h2><a href="https://github.com/SimonSchwaiger/home-lab" target=”_blank”>Homelab</a></h2>

Automatically deployed, self-hosted services including machine learning instances and cloud storage using Docker, Ansible and Nextcloud. The machine learning instances are based on my ROS Machine Learning Container.
