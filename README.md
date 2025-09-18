# 🐦 Bird Species Detection using Deep Learning on the CUB-200-2011 Dataset

> A fine-grained image recognition project that classifies bird species from images using attention-based and part-based deep learning models.

---

## 📌 Table of Contents
- [About the Project](#about-the-project)
- [Dataset](#dataset)

---

## 📖 About the Project
Bird species identification is a challenging **fine-grained classification** task because species often differ by subtle visual cues (e.g., beak color, tail shape).

This repository implements and compares three approaches:
- **RA-CNN (Recurrent Attention CNN)**  
- **MA-CNN (Multi-Attention CNN)**  
- **Part-based R-CNN**

All experiments use the [CUB-200-2011 dataset](https://www.kaggle.com/datasets/wenewone/cub2002011). The project contains data preprocessing, model implementations, training scripts, evaluation scripts, and a lightweight demo for inference.

Key features:
- Attention-based localization of discriminative regions.
- Part-based detection for pose-normalized representations.
- Clean training pipeline with data augmentation.
- Option to deploy as a web demo (Streamlit/Flask).

Get the project documentation and step by step implementation : [Project Documentation](https://colab.research.google.com/drive/1Ff72-yVkSh6Bnm-HwVrTf9IDdOpcvWBd?usp=sharing)

---

## 📂 Dataset
- **Name:** Caltech–UCSD Birds-200-2011  
- **Size:** 11,788 images across 200 species  
- **Annotations:** 15 part locations, 312 attributes, bounding boxes  
- **Download:** [CUB-200-2011 dataset](https://www.kaggle.com/datasets/wenewone/cub2002011)

---