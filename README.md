# 🌟 **Smart Spoon — AI-Powered Food Analysis & Dietary Recommendation System**

A next-gen food-intelligence system that blends **computer vision**, **flavor analytics**, and **rule-based dietary intelligence** to deliver personalized nutritional suggestions.
Designed for **students, researchers, AI enthusiasts**, and **interview showcases** 🚀

---

## ✨ **Key Highlights**

* 🥗 **AI-Based Food Detection** using color-profile matching
* 🧂 **Dietary Recommendations** tailored to medical conditions
* 📊 **Excel/CSV User Data Insights** (Age, Gender, Medical Conditions)
* 🔍 **Ingredient & Salt/Spice Profiling** for each dish
* 🍽️ **Smart Taste Improvement Suggestions** powered by rule-based analysis
* 📁 Supports **local file upload** for both images & datasets
* 💻 Fully **terminal-based** (no Google Colab dependencies)

---

## 🎯 **Tech Stack**

| Component          | Purpose                           |
| ------------------ | --------------------------------- |
| **Python**         | Core backend logic                |
| **NumPy**          | Pixel-level color vector analysis |
| **Pandas**         | Demographic Excel/CSV analysis    |
| **Pillow (PIL)**   | Image processing                  |
| **I/O Operations** | Terminal-based workflow           |
| **Rule-based AI**  | Food taste recommendation engine  |

---

## 🧠 **How Smart Spoon Works**

Smart Spoon follows a fully automated decision pipeline:

1. **Image Upload**
   User selects any food image.

2. **Color Vector Extraction**
   System reads dominant RGB pixel averages using PIL & NumPy.

3. **Food Matching Engine**
   Colour distance is computed with Euclidean distance
   → Matches with nearest food profile in `FOOD_DATABASE`.

4. **User Profile Detection**
   Age, gender, medical history & food frequency collected.

5. **Dynamic Dietary Recommendation**
   Suggestions vary based on:

   * Food's natural salt profile
   * User’s medical conditions (Hypertension, Kidney issues)
   * Age-based spice tolerance
   * Restaurant visit frequency

6. **Taste Feedback Loop**
   User gives taste feedback → AI returns improvement suggestions.

---

## 🚀 **Installation Guide**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/yourusername/smart-spoon.git
cd smart-spoon
```

### **2️⃣ Install Dependencies**

```bash
pip install numpy pandas pillow
```

### **3️⃣ Run the Application**

```bash
python smart_spoon.py
```

---

## 🧪 **Supported Image Formats**

✔ JPG
✔ JPEG
✔ PNG

---

## 📂 **Uploadable Dataset Format (Optional)**

Your Excel/CSV file **should contain**:

| Column Name          | Description                          |
| -------------------- | ------------------------------------ |
| Age                  | Age of the user                      |
| Gender               | Male/Female/Other                    |
| Medical Condition    | Hypertension / Kidney Disease / None |
| Restaurant Frequency | Daily / Weekly / Monthly / Rarely    |

Example:

```csv
Age,Gender,Medical Condition,Restaurant Frequency
23,Male,None,Weekly
45,Female,Hypertension,Daily
32,Male,None,Monthly
```

---

## 🧰 **List of Dishes Detected**

Smart Spoon currently detects the following based on color clusters:

| Dish      | Salt   | Spice  | Profile      |
| --------- | ------ | ------ | ------------ |
| Biryani   | Medium | High   | Golden-brown |
| Dosa      | Low    | Medium | Light cream  |
| Pizza     | High   | Low    | Red-yellow   |
| Dal Tadka | Medium | Medium | Yellow-gold  |
| Idli      | Low    | Low    | White        |

---

## 🏆 **Program Flow**

```
Start System  
 └── Optional: Upload Excel/CSV  
       └── Generates Insights  
 └── Upload Food Image  
 └── Food Detection  
 └── Show Ingredients  
 └── Personalized Diet Recommendations  
 └── Taste Feedback  
 └── Smart Suggestions  
End  
```

---

## 🖥️ **Run Screenshot (Example Output)**

```
=== SMART SPOON FOOD ANALYSIS SYSTEM ===  

Successfully Loaded: userdata.xlsx  
Average age: 29.8  
Gender Distribution:  
Male: 10  
Female: 8  

Image loaded successfully!  
Detected Food: Biryani  
Ingredients: rice, chicken, spices, yogurt, saffron  
Salt Content: medium  
Spice Level: high  

Dietary Recommendation:  
- Recommended Salt: 1/2 tsp  
- Reduce spicy intake if age > 60  
```

---

## 📌 **Future Enhancements**

* 📸 Neural-network powered food classification
* 🧠 ML-powered taste prediction model
* 🌍 API endpoint for mobile integration
* 🍱 Nutritional value extraction (calories, macros)

---

## 📜 **License**

This project is licensed under the **MIT License**.

---

## 👨‍💻 **Author**

**Somesh Gowda**
AI/ML Enthusiast | Python Developer | Cybersecurity Learner


