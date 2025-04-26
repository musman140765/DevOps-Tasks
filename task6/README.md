# Monitoring and Alerting Setup with Prometheus, Node Exporter, and Grafana

## Overview

This task6 solution showing the steps to set up a **Monitoring Stack** using **Prometheus**, **Node Exporter**, and **Grafana** as system services on an Ubuntu VM. The stack will track **CPU** and **memory** usage, with Grafana used for visualization of metrics scraped by Prometheus from Node Exporter.

## Prerequisites

- Ubuntu VM (or similar Linux-based system)
- Sudo privileges

## Tools Used

### 🔹 Prometheus
Prometheus is an open-source monitoring system that collects metrics from configured targets at specified intervals, evaluates rule expressions, displays results, and can trigger alerts if conditions are met, target VM results.

![image](https://github.com/user-attachments/assets/da83db52-b6aa-4717-8491-ccb51301d23b)


### 🔹 Node Exporter
Node Exporter is a Prometheus exporter for hardware and OS metrics exposed by *nix systems such as CPU, memory, disk, and network usage, target VM results.

![image](https://github.com/user-attachments/assets/bcec1774-fd43-4dda-b5a7-f22886d48adc)


### 🔹 Grafana
Grafana is a data visualization and monitoring platform. It connects to Prometheus (and other data sources) and allows users to build dashboards and graphs for real-time metric analysis, grafana hosted VM.

![image](https://github.com/user-attachments/assets/5ed38138-dff3-4105-b57b-f7250bc9d508)

