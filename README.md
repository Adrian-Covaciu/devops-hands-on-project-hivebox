[![Dynamic DevOps Roadmap](https://img.shields.io/badge/Dynamic_DevOps_Roadmap-559e11?style=for-the-badge&logo=Vercel&logoColor=white)](https://devopsroadmap.io/getting-started/)
[![Community](https://img.shields.io/badge/Join_Community-%23FF6719?style=for-the-badge&logo=substack&logoColor=white)](https://newsletter.devopsroadmap.io/subscribe)
[![Telegram Group](https://img.shields.io/badge/Telegram_Group-%232ca5e0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/DevOpsHive/985)
[![Fork on GitHub](https://img.shields.io/badge/Fork_On_GitHub-%2336465D?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)

# HiveBox - DevOps End-to-End Hands-On Project

<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox" style="display: block; padding: .5em 0; text-align: center;">
    <img alt="HiveBox - DevOps End-to-End Hands-On Project" border="0" width="90%" src="https://devopsroadmap.io/img/projects/hivebox-devops-end-to-end-project.png" />
  </a>
</p>

> [!CAUTION]
> **[Fork](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork)** this repo, and create PRs in your fork, **NOT** in this repo!

> [!TIP]
> If you are looking for the full roadmap, including this project, go back to the [getting started](https://devopsroadmap.io/getting-started) page.

This repository is the starting point for [HiveBox](https://devopsroadmap.io/projects/hivebox/), the end-to-end hands-on project.

You can fork this repository and start implementing the [HiveBox](https://devopsroadmap.io/projects/hivebox/) project. HiveBox project follows the same Dynamic MVP-style mindset used in the [roadmap](https://devopsroadmap.io/).

The project aims to cover the whole Software Development Life Cycle (SDLC). That means each phase will cover all aspects of DevOps, such as planning, coding, containers, testing, continuous integration, continuous delivery, infrastructure, etc.

Happy DevOpsing ♾️

## Before you start

Here is a pre-start checklist:

- ⭐ <a target="_blank" href="https://github.com/DevOpsHiveHQ/dynamic-devops-roadmap">Star the **roadmap** repo</a> on GitHub for better visibility.
- ✉️ <a target="_blank" href="https://newsletter.devopsroadmap.io/subscribe">Join the community</a> for the project community activities, which include mentorship, job posting, online meetings, workshops, career tips and tricks, and more.
- 🌐 <a target="_blank" href="https://t.me/DevOpsHive/985">Join the Telegram group</a> for interactive communication.

## Preparation

- [Create GitHub account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) (if you don't have one), then [fork this repository](https://github.com/DevOpsHiveHQ/devops-hands-on-project-hivebox/fork) and start from there.
- [Create GitHub project board](https://docs.github.com/en/issues/planning-and-tracking-with-projects/creating-projects/creating-a-project) for this repository (use `Kanban` template).
- Each phase should be presented as a pull request against the `main` branch. Don’t push directly to the main branch!
- Document as you go. Always assume that someone else will read your project at any phase.
- You can get senseBox IDs by checking the [openSenseMap](https://opensensemap.org/) website. Use 3 senseBox IDs close to each other (you can use the following [5eba5fbad46fb8001b799786](https://opensensemap.org/explore/5eba5fbad46fb8001b799786), [5c21ff8f919bf8001adf2488](https://opensensemap.org/explore/5c21ff8f919bf8001adf2488), and [5ade1acf223bd80019a1011c](https://opensensemap.org/explore/5ade1acf223bd80019a1011c)). Just copy the IDs, you will need them in the next steps.

<br/>
<p align="center">
  <a href="https://devopsroadmap.io/projects/hivebox/" imageanchor="1">
    <img src="https://img.shields.io/badge/Get_Started_Now-559e11?style=for-the-badge&logo=Vercel&logoColor=white" />
  </a><br/>
</p>

---

## Implementation

### Tests and Lints to complete a PR

This repository uses pylint and hadolint to check and pass the pipeline. It also performs an analysis using SonarCloud.

### Build and Run the Application

<ol>
  <li>
    <strong>Build the Docker Image</strong><br/>
    <p>Run the following command to build the image:</p>
    <pre><code>docker build -t pyapp:latest .</code></pre>
  </li>

  <li>
    <strong>Run the Docker Container</strong><br/>
    <p>Execute the following command to run the container and display the application version:</p>
    <pre><code>docker run pyapp:latest</code></pre>
  </li>
</ol>

### Use the application (localhost and default values example)

<ol>
  <li>
    <strong>Install pre-requisites</strong><br/>
    <pre><code>
      python3 -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
    </code></pre>
  </li>

  <li>
    <strong>Start the application</strong><br/>
    <pre><code>python3 application/main.py</code></pre>
  </li>

  <li>
    <strong>Call version endpoint</strong><br/>
    <pre><code>curl "localhost:5000/version"</code></pre>
  </li>

  <li>
    <strong>Call temperature endpoint with query arguments</strong><br/>
    <pre><code>curl "localhost:5000/temperature?box_ids=580f30787ac61b0010983265,57aa3052f52f21100029a5a9,5879ecfd0eb1a0000f36a145"</code></pre>
  </li>

</ol>

### Deploy in minikube

<ol>
  <li>
  <strong>Install and run minikube</strong><br/>
    <p>Go to minikube documentation for setup instructions https://minikube.sigs.k8s.io/docs/</p>
  </li>

  <li>
    <strong>Enable ingress and change the service type</strong><br/>
    <p>Enable the ingress addon and fix the default NodePort service type to be LoadBalancer</p>
    <pre><code>
    minikube addons enable ingress
    kubectl patch svc ingress-nginx-controller -n ingress-nginx \
      -p '{"spec": {"type": "LoadBalancer"}}'
    </code></pre>
  </li>

  <li>
    <strong>Start the tunnel</strong><br/>
    <p>This simulates a cloud LoadBalancer locally:</p>
    <pre><code>minikube tunnel</code></pre>
  </li>

  <li>
    <strong>Apply Kubernetes manifests</strong><br/>
    <p>Deploy your app and ingress resources:</p>
    <pre><code>kubectl apply -f manifests/</code></pre>
  </li>

  <li>
    <strong>Update your hosts file</strong><br/>
    <p>Point your custom domain to the LoadBalancer External-IP:</p>
    <pre><code>
    sudo vi /etc/hosts
    127.0.0.1 pyapp.local
    </code></pre>
  </li>

  <li>
    <strong>Test the app</strong><br/>
    <p>Access it via Ingress like a real domain:</p>
    <pre><code>
    curl http://pyapp.local/version
    curl http://pyapp.local/temperature
    </code></pre>
  </li>
</ol>