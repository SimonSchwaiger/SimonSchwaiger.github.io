import re
import mistune

## STATIC PAGES (MAIN, CV, Teaching)
configStatic = {
    "src": [
        "./mainpage.md",
        "./teaching_experience.md",
        "./cv.md",
        "./portfolio.md"
    ],

    "highlight": [
        None,
        "./teaching.html",
        "./cv.html",
        "./portfolio.html"

    ],

    "outfile": [
        "../index.html",
        "../teaching.html",
        "../cv.html",
        "../portfolio.html"
    ]
}

## DYNAMIC PUBLICATION PAGE
configPublications = {
    "src": [
        "2025-otas.md",
        "2025-drone-robotics-courses.md",
        "2024-ugv-cbrn.md",
        "2024-ei-towards-full-autonomy.md",
        "2024-icra40-from-words-to-poses.md",
        "2023-arw-applicability-of-docker.md",
        "2022-arw-deep-rl-continuous-control.md",
        "2021-daam-explainable-ai-for-robot-arm-control.md",
        "2021-arw-open-loop-robot-control-using-dqn.md",
        "2020-ei-evaluation-of-navigation-methodologies-for-mobile-robots.md",
    ],

    "title": [
        "OTAS: Open-vocabulary Token Alignment for Outdoor Segmentation*",
        "Drones in Electronics Engineering and AI-Driven Robotics Courses: Hands-on Lab Concepts",
        "UGV-CBRN: An Unmanned Ground Vehicle for Chemical, Biological, Radiological, and Nuclear Disaster Response*",
        "Towards full Autonomy in Mobile Robot Navigation and Manipulation",
        "From Words to Poses: Enhancing Novel Object Pose Estimation with Vision Language Models",
        "On the Applicability of Docker Containers and systemd Services for Search and Rescue Applications",
        "Deep Reinforcement Learning for Continuous Robot Trajectory Control",
        "Explainable Artificial Intelligence For Robot Arm Control",
        "Open Loop Robot Control using Deep Q-Learning",
        "Evaluierung von Navigationsmethoden für mobile Roboter, Evaluation of navigation methodologies for mobile robots",
    ],

    "author": [
        "Simon Schwaiger, Stefan Thalhammer, Wilfried Wöber, Gerald Steinbauer-Wagner",
        "Florian Wimmer, Simon Schwaiger, Christian Fibich",
        "Simon Schwaiger&ast;, Lucas Muster&ast;, Georg Novotny, Michael Schebek, Wilfried Wöber, Stefan Thalhammer, Christoph Böhm",
        "Simon Schwaiger&ast;, Lucas Muster&ast;, Alessandro Scherl, Paolo Trivisonne, Wilfried Wöber, Stefan Thalhammer",
        "Tessa Pulli, Stefan Thalhammer, Simon Schwaiger, Markus Vincze",
        "Georg Novotny, Simon Schwaiger, Lucas Muster, Mohamed Aburaia, Wilfried Wöber",
        "Simon Schwaiger, Mohamed Aburaia, Lucas Muster, Moritz Abdank, Wilfried Wöber",
        "Simon Schwaiger, Mohamed Aburaia, Ali Aburaia, Wilfried Wöber",
        "Simon Schwaiger, Ali Aburaia, Mohamed Aburaia, Wilfried Wöber",
        "Wilfried Wöber, Johannes Rauer, Maximilian Papa, Ali Aburaia, Simon Schwaiger, Georg Novotny, Mohamed Aburaia, Wilfried Kubinger",
    ],

    "published": [
        "ArXiv, 2025",
        "Proceedings of the 2025 IEEE Global Engineering Education Conference (EDUCON)",
        "ArXiv, 2024",
        "e+i Elektrotechnik und Informationstechnik, 2024",
        "Proceedings of IEEE ICRA@40, 2024",
        "Proceedings of the Austrian Robotics Workshop 2023",
        "Proceedings of the Austrian Robotics Workshop 2022",
        "Proceedings of the 32nd International DAAAM Symposium 2021",
        "Proceedings of the Austrian Robotics Workshop 2021",
        "e+i Elektrotechnik und Informationstechnik, 2020",
    ],

    "description": [
        "Open-language 2D segmentation and 3D reconstruction for in the wild outdoor robots.",
        "Real-world deployment of drone hardware and software in electronics engineering and robotics courses.",
        "Integration and field test of disaster response mobile robot in cooperation with the Austrian Armed Forces.",
        "Showcase of data-driven robotics research at UAS Technikum to increase autonomy of robots in real world scenarios.",
        "Advancing zero-shot 6D object pose estimation by leveraging geometric and semantic reconstruction with neural radiance fields.",
        "Use of containerization (Docker), service management (systemd), and monitoring tools to enhance the maintenance and deployment of robotics systems in search and rescue operations.",
        "Continuous trajectory planning for 7DOF robots using various reinforcement learning algorithmns.",
        "Explainability examination of models performing discrete trajectory planning for 3DOF robots using policy iteration.",
        "Discrete trajectory planning for 3DOF robots using multi-goal reinforcement learning.",
        "Presentation of current research in the Technikum Digital Factory.",
    ],

    "thumbnail": [ ## Just add empty paths if you want to ommit a thumbnail
        "./img/pub_thumbnail_2025-otas.gif",
        "./img/pub_thumbnail_2025-educon-drones-education.png",
        "./img/pub_thumbnail_2024-ugv-cbrn.gif",
        "./img/pub_thumbnail_2024-ei-towards-full-autonomy.png",
        "./img/pub_thumbnail_2024-icra40-from-words-to-poses.png",
        "./img/pub_thumbnail_arw-applicability-of-docker.png",
        "",  
        "",
        "",
        "",
    ]
}

with open("./mainStructure.html", "r") as file:
    page_code = file.readlines()

page_code = "".join(page_code)
start_match = re.search("<!-- START GENERATED HTML HERE -->", page_code)
end_match = re.search("<!-- END GENERATED HTML HERE -->", page_code)

## STATIC PAGES (MAIN, CV, Teaching)
def buildStaticFile(page_code, start_match, end_match, src, highlight, outfile, content=None):
    if content == None: ## This is very hacky but works for now
        with open(src, "r") as file:
            content = file.readlines()

    content = mistune.html("".join(content))

    page = "".join([
        page_code[:start_match.end()],
        content,
        page_code[end_match.start():]
    ])

    if highlight != None:
        button_section = '<a href="{}">\n\s*<button class="'.format(highlight)
        highlight_match = re.search(button_section, page)
        page = "".join([
            page[:highlight_match.end()],
            "button-highlight ",
            page[highlight_match.end():]
        ])

    with open(outfile, "w") as file:
        file.write(page)

for (s, h, o) in zip(configStatic["src"], configStatic["highlight"], configStatic["outfile"]):
    buildStaticFile(page_code, start_match, end_match, s, h, o)

## DYNAMIC PUBLICATION PAGE
def buildPublicationEntry(page_code, start_match, end_match, src, title, author, published, description, thumbnail):
    src_no_extension = re.sub(r'\.md$', '', src)
    outfile = "../" + src_no_extension + ".html"
    subpage_link = "./" + src_no_extension + ".html"
    src = "./publications/" + src
    buildStaticFile(page_code, start_match, end_match, src, "./publications.html", outfile)
    # Format summary entry and return. #TODO: Stack thumbnail and text on top of each other on mobile version
    return "".join([
        '<table style="border-collapse: collapse;">\n<td style="border: none; max-width: 330px;">',
        '<a href="' + subpage_link + '"><img src="' + thumbnail + '" style="width: 100%;"></a></td>\n<td style="border: none; max-width: 800px;">\n\n',
        "### [", title, "](" + subpage_link + ")\n\n*",
        author, "*\n\n",
        "Published in **", published, "**\n\n",
        description, "\n\n---\n\n",
        "</td>\n</tr>\n</table>\n"
    ])

publication_summary = ["# Publications\n\n"]

for (s, t, a, p, d, th) in zip(configPublications["src"], configPublications["title"], configPublications["author"], configPublications["published"], configPublications["description"], configPublications["thumbnail"]):
    publication_summary.append(
        buildPublicationEntry(page_code, start_match, end_match, s, t, a, p, d, th))

content = "".join(publication_summary)#[:-5] #Only needed if thumbnails and table for each entry are omitted
buildStaticFile(page_code, start_match, end_match, "", "./publications.html", "../publications.html", content=content)
