# 🐦 Bird Species Detection using Deep Learning on the CUB-200-2011 Dataset

> A fine-grained image recognition project that classifies bird species from images using attention-based and part-based deep learning models.

---

## 📌 Table of Contents
- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Models Used](#models-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Training](#training)
- [Evaluation](#evaluation)
- [Results](#results)
- [Demo / Deployment](#demo--deployment)
- [Screenshots](#screenshots)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)
- [References](#references)
- [Acknowledgements](#acknowledgements)

---

## 📖 About the Project
Bird species identification is a challenging **fine-grained classification** task because species often differ by subtle visual cues (e.g., beak color, tail shape).

This repository implements:
- **RA-CNN (Recurrent Attention CNN)**  
- **MA-CNN (Multi-Attention CNN)**  
- **Part-based R-CNN**

and compares them for **bird species classification** on the [CUB-200-2011 dataset](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html).

Key features:
- Attention-based localization of discriminative regions.
- Part-based detection for pose-normalized representations.
- Clean training pipeline with data augmentation.
- Option to deploy as a web app for easy inference.

---

## 📂 Dataset
- **Name:** Caltech–UCSD Birds-200-2011  
- **Size:** 11,788 images across 200 species  
- **Annotations:** 15 part locations, 312 attributes, bounding boxes  
- [Download Link](http://www.vision.caltech.edu/visipedia/CUB-200-2011.html)

---

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/<your-username>/bird-species-detection.git
cd bird-species-detection

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)

# Install dependencies
pip install -r requirements.txt
