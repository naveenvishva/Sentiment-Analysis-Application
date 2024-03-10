import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QDialog, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from sentiment_model import predict_sentiment

class SentimentAnalysisApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sentiment Analysis")

        self.user_input = QLineEdit()
        self.analyze_button = QPushButton("Analyze")
        self.result_label = QLabel()
        self.view_analysis_button = QPushButton("View Analysis")

        self.user_reviews = []  # List to store user reviews
        self.predicted_sentiments = []  # List to store predicted sentiments

        # Layout setup
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.user_input)
        input_layout.addWidget(self.analyze_button)
        input_layout.addWidget(self.result_label)

        button_layout = QVBoxLayout()
        button_layout.addWidget(self.view_analysis_button)

        layout = QVBoxLayout()
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # Connect button actions
        self.analyze_button.clicked.connect(self.predict_sentiment)
        self.view_analysis_button.clicked.connect(self.show_analysis_dialog)

    def predict_sentiment(self):
        input_text = self.user_input.text()
        if not input_text:
            self.result_label.setText("Please enter a review.")
            return

        sentiment = predict_sentiment(input_text)
        self.result_label.setText(f"Predicted Sentiment: {sentiment}")

        # Store the user's input and predicted sentiment for further analysis
        self.user_reviews.append(input_text)
        self.predicted_sentiments.append(sentiment)

        self.user_input.clear()  # Clear the input field after analysis

    def show_analysis_dialog(self):
        analysis_dialog = QDialog()
        analysis_dialog.setWindowTitle("Sentiment Analysis Results")
        
        analysis_layout = QVBoxLayout()
        
        if self.user_reviews:
            # Count the number of positive and negative sentiments
            positive_count = self.predicted_sentiments.count("Positive")
            negative_count = self.predicted_sentiments.count("Negative")

            # Create a Matplotlib figure for the bar chart
            fig = plt.Figure()
            ax = fig.add_subplot(111)
            ax.bar(["Positive", "Negative"], [positive_count, negative_count])
            ax.set_title("Sentiment Distribution of All Reviews")
            ax.set_xlabel("Sentiment")
            ax.set_ylabel("Count")
            
            canvas = FigureCanvas(fig)
            canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            analysis_layout.addWidget(canvas)

        analysis_dialog.setLayout(analysis_layout)
        analysis_dialog.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SentimentAnalysisApp()
    window.show()
    sys.exit(app.exec_())
