# 🐦 Bird Species Detection Using Deep Learning  
### Fine-Grained Image Classification using Vision Transformer (ViT-B/16)

This project focuses on automated bird species recognition using the **CUB-200-2011 dataset** and **Vision Transformer (ViT-B/16)**. It includes cleaning, augmentation, model training, and a full evaluation pipeline for fine-grained species classification.

---

## 📌 Overview

Bird species identification is a challenging fine-grained classification task due to subtle visual differences between species.  
This project builds a complete pipeline—from dataset preparation to model analysis—achieving:

**➡️ Final Accuracy: 87.12%**

---

## 🚀 Features

- ✔️ Fine-grained classification using **ViT-B/16**  
- ✔️ Comprehensive **data cleaning & augmentation**  
- ✔️ Custom **80:10:10 stratified split**  
- ✔️ Detailed **misclassification analysis**  
- ✔️ Graphs: accuracy, loss, confusion matrix, workflow diagram  

---

## 📁 Dataset (CUB-200-2011)

- **11,788 total images**
- **200 bird species**
- Includes:
  - Bounding boxes  
  - Part annotations  
  - Labels and metadata  

### Dataset Improvements
- Removed **60+ mislabeled/low-quality images**
- Added images for weak classes
- Improved class balance via custom split

---

## 🧠 Model Architecture – ViT-B/16

Key components:
- Image patch extraction (16×16)
- Patch embedding + positional encoding
- Transformer encoder blocks
- [CLS] token for classification
- MLP classifier head

Training Setup:
- Optimizer: **AdamW**
- Scheduler: **Cosine Annealing**
- Mixed precision: **FP16 / AMP**
- Gradient clipping enabled

---

## 🛠 Methodology

### 1️⃣ Dataset Preparation
- Merged metadata (labels, bounding boxes)
- Stratified train/val/test split

### 2️⃣ Data Cleaning
- Outlier detection using PCA + t-SNE
- Manual image verification
- Removed inconsistent bounding boxes

### 3️⃣ Data Augmentation
- RandomResizedCrop  
- Horizontal/vertical flip  
- Minor rotations  
- Color jitter  
- ImageNet normalization  

### 4️⃣ Training Process
- Batch Size: 32  
- Epochs: ~50  
- Early stopping enabled  

### 5️⃣ Evaluation Metrics
- Accuracy  
- Precision / Recall / F1  
- Confusion matrix  
- Per-class accuracy  

---

## 📊 Results

### 🔥 Final Test Accuracy  
**87.12%**

### 📈 Accuracy Progression

| Stage | Accuracy (%) |
|-------|--------------|
| ResNet18 Baseline | 55.00 |
| ViT-B/16 (Minimal Augmentation) | 84.00 |
| Stronger Augmentation | 86.00 |
| Custom Stratified Split | 88.00 |
| Added External Images | 89.40 |
| After Cleaning Mislabeled Images | 87.12 |
| Cleaning + 50:50 Split | 87.15 |

---

## 🧩 Misclassification Analysis

- **70.2%** of errors occur **within the same bird family**
- Highest confusion among:
  - Warblers  
  - Sparrows  
  - Thrushes  
- Difficult cases involve:
  - Poor lighting  
  - Occlusions  
  - Juvenile/non-breeding plumage  

---

## 🖼 Visual Outputs (Included in Report)

- ViT-B/16 architecture diagram  
- Accuracy vs epoch curve  
- Loss curves  
- Confusion matrix  
- Misclassified image samples  
- Workflow flowchart  

---

## 🔮 Future Enhancements

### Dataset
- Add verified images from iNaturalist / GBIF
- Expert validation of ambiguous species

### Model
- Try ViT-L/16 or Swin-L transformer  
- Hierarchical classification (family → species)  
- Part-based attention (head, wings, tail)  
- Bird pose estimation integration  

---

**Megh Patel** (AU2544020)

**Konark Karia** (AU2544011)

**School of Engineering & Applied Science**

**Ahmedabad University**
