# 📧 Spam Detection App

A machine learning web application that detects whether a message is **Spam** or **Not Spam** using Naive Bayes classification.

🔗 **Live Demo**: [spamdetection-2nngorcy6cbl7pui5jdnlp.streamlit.app](https://spamdetection-2nngorcy6cbl7pui5jdnlp.streamlit.app)

---

## 🚀 Features

- Detects spam messages in real-time
- Simple and clean UI built with Streamlit
- Trained on the SMS Spam Collection Dataset
- 98% model accuracy

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Streamlit | Web application framework |
| Scikit-learn | Machine learning model |
| Pandas | Data manipulation |
| CountVectorizer | Text feature extraction |
| Multinomial Naive Bayes | Classification algorithm |

---

## 📁 Project Structure

```
Spam_Detection/
├── app.py            # Main Streamlit application
├── spam.csv          # Dataset
├── requirements.txt  # Dependencies
└── README.md         # Project documentation
```

---

## ⚙️ How It Works

1. The SMS Spam Collection dataset is loaded and cleaned
2. Messages are converted to numerical features using **CountVectorizer**
3. A **Multinomial Naive Bayes** model is trained on the data
4. User inputs a message → model predicts **Spam** or **Not Spam**

---

## 🧪 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 98% |
| Algorithm | Multinomial Naive Bayes |
| Vectorizer | CountVectorizer (stop words removed) |
| Test Size | 20% |

---

## 📦 Installation & Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/ShaileshY7/Spam_Detection.git
cd Spam_Detection
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the app**
```bash
streamlit run app.py
```

4. Open your browser at `http://localhost:8501`

---

## 📊 Dataset

- **Name**: SMS Spam Collection Dataset
- **Source**: [Kaggle](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- **Size**: 5,572 messages
- **Classes**: Spam / Ham (Not Spam)

---

## 🖼️ Screenshots

### Home Page
> Enter any message and click **Validate** to check if it's spam or not.

---

## 📝 Example Test Messages

**Spam:**
- `Congratulations! You've won a $1000 gift card. Click here to claim now!`
- `FREE entry! Text WIN to 80086 and get a chance to win £500 weekly prize.`

**Not Spam:**
- `Hey, are we still meeting for lunch tomorrow?`
- `I'll be late to the office today, stuck in traffic.`

---

## 🙋‍♂️ Author

**ShaileshY7**  
GitHub: [@ShaileshY7](https://github.com/ShaileshY7)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
